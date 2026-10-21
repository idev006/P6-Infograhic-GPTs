"""Format display labels; internal ISO dates remain Gregorian."""
import datetime
THAI=str.maketrans('0123456789','๐๑๒๓๔๕๖๗๘๙')
ARABIC=str.maketrans('๐๑๒๓๔๕๖๗๘๙','0123456789')
MONTHS=('ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.')
def digits(value,style='thai'):
 if style not in ('thai','arabic'):raise ValueError('style must be thai or arabic')
 text=str(value).translate(ARABIC)
 return text.translate(THAI) if style=='thai' else text

def table_date(iso_date,style='thai'):
 d=datetime.date.fromisoformat(iso_date)
 label=f'{d.day} {MONTHS[d.month-1]}{(d.year+543)%100:02d}'
 return digits(label,style)


