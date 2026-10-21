"""Validate canonical schedule JSON; does not certify image pixels or OCR.

ISO dates are Gregorian; Thai digits are accepted in dates and times. Missing
owner/chair/operator values are valid and must never be filled by inference.
"""
import argparse
import datetime
import json
import re
import sys

DIGITS = str.maketrans('๐๑๒๓๔๕๖๗๘๙', '0123456789')
STATUSES = {'meetings', 'no_meetings', 'no_room', 'no_room_av', 'unknown'}

def normal(value):
    return str(value).translate(DIGITS)

def validate(data):
    errors, ids, dates = [], set(), set()
    if not isinstance(data, dict):
        return ['schedule: expected object']
    for field in ('title', 'agency'):
        if field in data and not isinstance(data[field], str):
            errors.append(f'{field}: expected string')
    if 'amendments' in data and not isinstance(data['amendments'], list):
        errors.append('amendments: expected array')
    days = data.get('days')
    if not isinstance(days, list) or not days:
        return errors + ['days: expected nonempty array']
    for i, day in enumerate(days):
        path = f'day {i}'
        if not isinstance(day, dict):
            errors.append(f'{path}: expected object')
            continue
        key = day.get('date')
        normalized = normal(key) if isinstance(key, str) else ''
        try:
            if not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', normalized):
                raise ValueError
            datetime.date.fromisoformat(normalized)
        except ValueError:
            errors.append(f'{path}: invalid ISO date')
        if normalized:
            if normalized in dates:
                errors.append(f'{path}: duplicate date')
            dates.add(normalized)
        status = day.get('status')
        if not isinstance(status, str) or status not in STATUSES:
            errors.append(f'{path}: invalid status')
        if 'label' in day and not isinstance(day['label'], str):
            errors.append(f'{path}: label must be string')
        if 'operator' in day and day['operator'] is not None:
            operator = day['operator']
            if not isinstance(operator, dict):
                errors.append(f'{path}: operator must be object or null')
            else:
                for field in ('name', 'role', 'phone'):
                    if field in operator and not isinstance(operator[field], str):
                        errors.append(f'{path}: operator.{field} must be string')
        rows = day.get('meetings')
        if not isinstance(rows, list):
            errors.append(f'{path}: meetings must be array')
            continue
        if status in {'no_meetings', 'no_room', 'no_room_av'} and rows:
            errors.append(f'{path}: status conflicts with meeting rows')
        if status == 'meetings' and not rows:
            errors.append(f'{path}: meetings status requires rows; use unknown for missing data')
        for j, row in enumerate(rows):
            where = f'{path} row {j}'
            if not isinstance(row, dict):
                errors.append(f'{where}: expected object')
                continue
            rid = row.get('id')
            if not isinstance(rid, str) or not rid.strip():
                errors.append(f'{where}: ID must be nonempty string')
            elif rid in ids:
                errors.append(f'{where}: duplicate ID')
            else:
                ids.add(rid)
            times = {}
            for field in ('time', 'end_time'):
                if field == 'end_time' and field not in row:
                    continue
                value = row.get(field)
                value = normal(value) if isinstance(value, str) else ''
                if not re.fullmatch(r'(?:[01][0-9]|2[0-3]):[0-5][0-9]', value):
                    errors.append(f'{where}: invalid {field}')
                else:
                    times[field] = value
            if len(times) == 2 and times['end_time'] < times['time']:
                errors.append(f'{where}: end_time precedes time on same day')
            if not isinstance(row.get('title'), str) or not row['title'].strip():
                errors.append(f'{where}: title must be nonempty string')
            for field in ('owner', 'chair', 'room', 'notes'):
                if field in row and not isinstance(row[field], str):
                    errors.append(f'{where}: {field} must be string (use — when unspecified)')
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('schedule', help='UTF-8 canonical schedule JSON')
    args = parser.parse_args()
    try:
        with open(args.schedule, encoding='utf-8') as handle:
            data = json.load(handle)
        errors = validate(data)
    except (OSError, ValueError, UnicodeError) as exc:
        errors = [f'input: {exc}']
    print(json.dumps({'valid': not errors, 'errors': errors}, ensure_ascii=False, indent=2))
    return int(bool(errors))

if __name__ == '__main__':
    sys.exit(main())
