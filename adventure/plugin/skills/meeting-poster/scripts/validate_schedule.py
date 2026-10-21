"""Validate canonical schedule JSON; does not certify image pixels or OCR."""
import json,re,sys,datetime
DIGITS=str.maketrans('๐๑๒๓๔๕๖๗๘๙','0123456789')
def normal(s):return str(s).translate(DIGITS)
def validate(data):
 errors=[];ids=set();dates=set()
 for i,d in enumerate(data.get('days',[])):
  key=d.get('date','')
  try:datetime.date.fromisoformat(key)
  except (ValueError,TypeError):errors.append(f'day {i}: invalid ISO date')
  if key in dates:errors.append(f'day {i}: duplicate date')
  dates.add(key)
  rows=d.get('meetings',[])
  if d.get('status') in ('no_meetings','no_room','no_room_av') and rows:errors.append(f'{key}: status conflicts with meeting rows')
  for j,r in enumerate(rows):
   rid=r.get('id')
   if not rid or rid in ids:errors.append(f'{key} row {j}: missing/duplicate ID')
   ids.add(rid)
   for field in ('time','end_time'):
    if field not in r and field=='end_time':continue
    t=normal(r.get(field,''))
    if not re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d',t):errors.append(f'{key} row {j}: invalid {field} {t}')
   if not str(r.get('title','')).strip():errors.append(f'{key} row {j}: missing title')
 return errors
if __name__=='__main__':
 data=json.load(open(sys.argv[1],encoding='utf-8'));errors=validate(data)
 print(json.dumps({'valid':not errors,'errors':errors,'days':len(data.get('days',[])),'rows':sum(len(d.get('meetings',[])) for d in data.get('days',[]))},ensure_ascii=False,indent=2))
 sys.exit(bool(errors))
