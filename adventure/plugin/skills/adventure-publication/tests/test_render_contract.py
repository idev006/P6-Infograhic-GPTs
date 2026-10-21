"""Independent release checks. Expected failures document current renderer gaps."""
import sys
from pathlib import Path
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'scripts'))
from render_publication import blocks, date_label, render
FONT=Path(__file__).resolve().parent.parent/'assets'/'Sarabun-Regular.ttf'

class RenderContractTests(unittest.TestCase):
    def test_all_status_meanings_retained(self):
        values=[t for _,t,_ in blocks({'title':'T','days':[{'status':s} for s in ('no_meetings','no_room','no_room_av','unknown')]})]
        for text in ('ไม่มีการประชุม','ไม่มีการใช้ห้องประชุม','ไม่มีการใช้ห้องประชุมและระบบโสตทัศนูปกรณ์','รอข้อมูล'):
            self.assertIn(text,values)
    def test_arabic_and_thai_digits_in_entire_canonical_render(self):
        data={'title':'ประชุม 12','agency':'ภาค ๖','days':[{'date':'2026-10-21','status':'meetings','operator':{'name':'นาย 1','phone':'01๒'},'meetings':[{'id':'m1','time':'09:00','title':'งาน 2','chair':'พิษณุ ๑','room':'ห้อง 3'}]}]}
        with tempfile.TemporaryDirectory() as temp:
            for mode, forbidden in [('thai','0123456789'),('arabic','๐๑๒๓๔๕๖๗๘๙')]:
                qc=render(dict(data,digits=mode),FONT,Path(temp)/(mode+'.png'))
                self.assertFalse(set(forbidden)&set(''.join(t['text'] for t in qc['rendered_text'])))
    def test_validated_thai_digit_date_has_canonical_label(self):
        self.assertEqual(date_label('๒๐๒๖-๑๐-๒๑'),'21 ต.ค.69')
    def test_roles_are_distinguishable(self):
        values=[t for _,t,_ in blocks({'title':'T','days':[{'date':'2026-10-21','meetings':[{'time':'09:00','title':'ประชุม','owner':'ก','chair':'ข','room':'ค'}]}]})]
        self.assertTrue(any('ประธาน' in text and 'ข' in text for text in values))
        self.assertTrue(any('เจ้าของเรื่อง' in text and 'ก' in text for text in values))
    def test_missing_officials_display_placeholder(self):
        values=[t for _,t,_ in blocks({'title':'T','days':[{'meetings':[{'time':'09:00','title':'ประชุม'}]}]})]
        self.assertTrue(any('—' in text for text in values))

if __name__=='__main__': unittest.main()
