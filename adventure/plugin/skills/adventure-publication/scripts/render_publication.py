#!/usr/bin/env python3
"""Deterministic text-only A4 publication renderer. No network or generated facts.

JSON: {title, subtitle?, sections?: [{heading?, body}], days?:
[{date?, day?, rows:[{time?, title?, detail?, speaker?, location?}]}],
footer?, phone?, palette?: 'P01'|'P02', digits?: 'thai'|'arabic'}.
Date strings YYYY-MM-DD become abbreviated Thai dates with Buddhist years.
Other date strings are preserved. Phone digit values are preserved; glyphs follow the selected numeral policy.
This basic typography fallback creates new images; it is not an image editor or full collage engine.
Requires a font containing every requested non-whitespace glyph, and Pillow RAQM.
Validate source JSON upstream with validate_schedule.py before rendering; this
renderer does not replace semantic schedule validation.
"""
import argparse
import datetime
import json
from pathlib import Path
import unicodedata
from PIL import Image, ImageDraw, ImageFont, features

W, H = 2480, 3508
PALETTES = {
    'P01': {'bg':'#FBF8EF','ink':'#142840','gold':'#A47B32','panel':'#F1E9D7'},
    'P02': {'bg':'#10253C','ink':'#FFF9EB','gold':'#D7B267','panel':'#1D3850'},
}
THAI = str.maketrans('0123456789','๐๑๒๓๔๕๖๗๘๙')
ARABIC = str.maketrans('๐๑๒๓๔๕๖๗๘๙','0123456789')
MONTHS = ['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.']

class LayoutOverflow(ValueError):
    pass

def clusters(text):
    try:
        import regex
        return regex.findall(r'\X', text)
    except ImportError:
        result=[]
        for ch in text:
            if result and (unicodedata.combining(ch) or unicodedata.category(ch).startswith('M')):
                result[-1] += ch
            else:
                result.append(ch)
        return result

def wrap(text, font, width):
    """Wrap without removing any source character (explicit blank lines retained)."""
    lines=[]
    for para in text.split('\n'):
        line=''
        for cluster in clusters(para):
            if font.getlength(cluster) > width:
                raise LayoutOverflow('A single grapheme exceeds available width')
            if line and font.getlength(line + cluster) > width:
                lines.append(line)
                line=''
            line += cluster
        lines.append(line)
    return lines

def date_label(value):
    try:
        d=datetime.date.fromisoformat(value.translate(ARABIC))
        return f'{d.day} {MONTHS[d.month-1]}{(d.year+543)%100:02d}'
    except (ValueError, TypeError):
        return str(value)

def string(value):
    if not isinstance(value, str):
        raise ValueError('All publication text, including phone, must be JSON strings')
    return value

def blocks(data):
    result=[]
    def add(role, value, exact=False):
        if value is not None and value != '':
            result.append((role,string(value),exact))
    add('title', data.get('title'))
    if not data.get('title'):
        raise ValueError('A nonempty title is required')
    add('subtitle',data.get('subtitle'))
    add('subtitle',data.get('agency'))
    for section in data.get('sections',[]):
        add('heading',section.get('heading'))
        add('body',section.get('body'))
    for day in data.get('days',[]):
        label=day.get('label') or ' • '.join(string(x) for x in [day.get('day'),date_label(day['date']) if day.get('date') else None] if x)
        add('heading',label)
        status_labels={'no_meetings':'ไม่มีการประชุม','no_room':'ไม่มีการใช้ห้องประชุม','no_room_av':'ไม่มีการใช้ห้องประชุมและระบบโสตทัศนูปกรณ์','unknown':'รอข้อมูล'}
        add('body',status_labels.get(day.get('status')))
        operator=day.get('operator')
        if isinstance(operator,dict):
            for key in ('name','role','phone'):
                add('body',('ผู้ปฏิบัติหน้าที่: '+string(operator[key])) if key=='name' and operator.get(key) else operator.get(key),key=='phone')
        for row in day.get('meetings',day.get('rows',[])):
            if isinstance(row,str):
                add('body',row)
            else:
                time=row.get('time')
                if time:
                    time=string(time).replace(':','.')
                    if row.get('end_time'):
                        time+='–'+string(row['end_time']).replace(':','.')
                    add('body',time+' น.')
                for key in ('title','detail','speaker','location'):
                    add('body',row.get(key))
                for key,label in (('owner','เจ้าของเรื่อง'),('chair','ประธาน'),('room','ห้องประชุม')):
                    value=row.get(key)
                    add('body',label+': '+(string(value) if value else '—'))
                add('body',row.get('notes'))
                result.append(('space','',False))
    operator=data.get('operator')
    if isinstance(operator,dict):
        for key in ('name','role','phone'):
            add('footer',('ผู้ปฏิบัติหน้าที่: '+string(operator[key])) if key=='name' and operator.get(key) else operator.get(key),key=='phone')
    elif operator:
        add('footer',operator)
    add('footer',data.get('footer'))
    add('footer',data.get('phone'),True)
    return result

def verify_glyphs(font_path, texts):
    try:
        from fontTools.ttLib import TTFont
    except ImportError as exc:
        raise RuntimeError('fontTools is required for font coverage verification') from exc
    font=TTFont(font_path)
    cmap=font.getBestCmap() or {}
    missing=sorted({ord(c) for text in texts for c in text if not c.isspace() and ord(c) not in cmap})
    font.close()
    if missing:
        raise ValueError('Font lacks required glyphs: '+', '.join(f'U+{c:04X}' for c in missing))

def render(data, font_path, out):
    if not features.check_feature('raqm'):
        raise RuntimeError('Pillow must be built with RAQM support')
    palette=PALETTES[data.get('palette','P01')]
    digit_mode=data.get('digits','thai')
    if digit_mode not in ('thai','arabic'):
        raise ValueError('digits must be thai or arabic')
    content=[(r,t.translate(THAI if digit_mode=='thai' else ARABIC),exact) for r,t,exact in blocks(data)]
    verify_glyphs(font_path,[t for _,t,_ in content])
    margin=180
    inner=W-2*margin
    chosen=None
    for body_size in range(58,35,-1):
        sizes={'title':round(body_size*1.8),'subtitle':round(body_size*1.1),'heading':round(body_size*1.17),'body':body_size,'footer':round(body_size*.88)}
        fonts={k:ImageFont.truetype(str(font_path),v,layout_engine=ImageFont.Layout.RAQM) for k,v in sizes.items()}
        y=200
        layout=[]
        for role,text,exact in content:
            if role=='space':
                y+=body_size*.22
                continue
            font=fonts[role]
            ascent,descent=font.getmetrics()
            line_height=ascent+descent+round(body_size*.18)
            y+=body_size*(.5 if role=='heading' else .12)
            # Avoid expensive shaping of clearly impossible oversized fields.
            if len(text) > 30000:
                raise LayoutOverflow('Text field exceeds single-page capacity')
            for line in wrap(text,font,inner-48):
                layout.append({'role':role,'text':line,'x':margin+24,'y':round(y),'line_height':line_height})
                y+=line_height
            y+=body_size*(.5 if role in ('title','subtitle') else .18)
        if y<=H-180:
            chosen=(body_size,fonts,layout,y)
            break
    if chosen is None:
        raise LayoutOverflow('Content does not fit A4 at the minimum body font size of 36 px; shorten content or use multiple pages')
    body_size,fonts,layout,bottom=chosen
    img=Image.new('RGB',(W,H),palette['bg'])
    draw=ImageDraw.Draw(img)
    draw.rectangle((margin,120,W-margin,134),fill=palette['gold'])
    actual=[]
    for item in layout:
        role=item['role']; x=item['x']; y=item['y']; font=fonts[role]
        if role=='heading':
            draw.rectangle((margin,y-8,W-margin,y+item['line_height']-2),fill=palette['panel'])
        color=palette['gold'] if role in ('title','heading') else palette['ink']
        draw.text((x,y),item['text'],font=font,fill=color,anchor='lt')
        bounds=list(draw.textbbox((x,y),item['text'],font=font,anchor='lt'))
        if bounds[0]<0 or bounds[1]<0 or bounds[2]>W or bounds[3]>H:
            raise LayoutOverflow('Rendered glyph bounds exceed page')
        actual.append({'role':role,'bounds':bounds})
    draw.rectangle((margin,H-125,W-margin,H-119),fill=palette['gold'])
    out=Path(out); out.parent.mkdir(parents=True,exist_ok=True)
    img.save(out,dpi=(300,300))
    qc={'dimensions_px':[W,H],'dpi':300,'body_font_px':body_size,'palette':data.get('palette','P01'),'digits':digit_mode,'layout_bottom':round(bottom),'page_bounds':[0,0,W,H],'text_bounds':actual,'rendered_text':[{'role':r,'text':t} for r,t,_ in content if r!='space'],'renderer_scope':'Basic typography fallback; new image creation, no image editing or full collage.','all_text_bounds_within_page':True,'font':str(font_path),'verification_scope':'Geometry and font coverage only; no text identity or source accuracy claim.'}
    out.with_suffix('.qc.json').write_text(json.dumps(qc,ensure_ascii=False,indent=2),encoding='utf-8')
    return qc

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',required=True,type=Path)
    parser.add_argument('--font',required=True,type=Path)
    parser.add_argument('--out',required=True,type=Path)
    args=parser.parse_args()
    render(json.loads(args.input.read_text(encoding='utf-8')),args.font,args.out)

if __name__=='__main__':
    main()
