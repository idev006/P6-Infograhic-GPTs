import json
from pathlib import Path
import tempfile
import unittest
from PIL import Image, ImageFont
from render_publication import render, wrap, blocks, date_label, LayoutOverflow, THAI

FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

class RendererTests(unittest.TestCase):
    def test_wrap_preserves_text(self):
        font=ImageFont.truetype(FONT,40)
        text='abc def 01234 abcdefghijk'
        lines=wrap(text,font,100)
        self.assertEqual(''.join(lines),text)
        self.assertTrue(all(font.getlength(line)<=100 for line in lines))
    def test_phone_input_value_preserved(self):
        self.assertIn(('footer','012-345-6789',True),blocks({'title':'A','phone':'012-345-6789'}))
    def test_date(self):
        self.assertEqual(date_label('2026-10-21'),'21 ต.ค.69')
        self.assertEqual(date_label('October'),'October')
        self.assertEqual(date_label('๒๐๒๖-๑๐-๒๑'),'21 ต.ค.69')
    def test_dimensions_and_geometry(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'synthetic.png'
            qc=render({'title':'Synthetic Schedule','digits':'arabic','sections':[{'heading':'Day 1','body':'09:00 Opening\n10:00 Discussion'}],'phone':'012-345-6789'},FONT,out)
            with Image.open(out) as img:
                self.assertEqual(img.size,(2480,3508))
            self.assertTrue(out.with_suffix('.qc.json').exists())
            for line in qc['text_bounds']:
                x1,y1,x2,y2=line['bounds']
                self.assertTrue(0<=x1<=x2<=2480 and 0<=y1<=y2<=3508)
    def test_canonical_schedule_fields(self):
        content=blocks({'title':'Schedule','agency':'Agency','days':[{'date':'2026-10-21','status':'meetings','operator':{'name':'Op','phone':'0123'},'meetings':[{'time':'09:00','end_time':'10:00','title':'Review','notes':'Note','owner':'Owner','chair':'Chair','room':'Room'}]}]})
        values=[t for _,t,_ in content]
        self.assertIn('Agency',values)
        self.assertIn('09.00–10.00 น.',values)
        self.assertIn('Note',values)
        self.assertIn(('body','0123',True),content)

    def test_numeral_policy_and_status(self):
        thai_font=Path(__file__).resolve().parent.parent/'assets'/'Sarabun-Regular.ttf'
        if not thai_font.exists():
            self.skipTest('Thai integration font not available')
        with tempfile.TemporaryDirectory() as tmp:
            for mode,phone in [('thai','๐๑๒-๓๔๕'),('arabic','012-345')]:
                qc=render({'title':'Test ๑2','digits':mode,'phone':'01๒-๓45'},thai_font,Path(tmp)/(mode+'.png'))
                self.assertIn({'role':'footer','text':phone},qc['rendered_text'])
        values=[t for _,t,_ in blocks({'title':'T','days':[{'status':'no_room'},{'status':'no_room_av'}]})]
        self.assertIn('ไม่มีการใช้ห้องประชุม',values)
        self.assertIn('ไม่มีการใช้ห้องประชุมและระบบโสตทัศนูปกรณ์',values)

    def test_role_labels_and_missing_values(self):
        values=[t for _,t,_ in blocks({'title':'T','days':[{'operator':{'name':'Operator'},'meetings':[{'time':'09:00','title':'Meeting','owner':'Team','chair':'Leader','room':'A'},{'time':'10:00','title':'Missing'}]}]})]
        for expected in ('ผู้ปฏิบัติหน้าที่: Operator','เจ้าของเรื่อง: Team','ประธาน: Leader','ห้องประชุม: A','เจ้าของเรื่อง: —','ประธาน: —','ห้องประชุม: —'):
            self.assertIn(expected,values)

    def test_overflow_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(LayoutOverflow):
                render({'title':'Too much','digits':'arabic','sections':[{'body':'abcdef '*30000}]},FONT,Path(tmp)/'bad.png')
    def test_missing_thai_font_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError,'glyphs'):
                render({'title':'ทดสอบ'},FONT,Path(tmp)/'bad.png')
    def test_phone_requires_string(self):
        with self.assertRaises(ValueError):
            blocks({'title':'Test','phone':12345})

if __name__=='__main__': unittest.main()
