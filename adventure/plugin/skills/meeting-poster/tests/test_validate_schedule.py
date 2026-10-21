import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from validate_schedule import validate, normal

class ScheduleTests(unittest.TestCase):
    def setUp(self):
        self.data = {'days': [{'date': '2026-10-19', 'status': 'meetings',
                    'meetings': [{'id': 'm1', 'time': '09:00', 'title': 'ประชุม'}]}]}
    def row(self):
        return self.data['days'][0]['meetings'][0]
    def test_minimum_and_missing_officials(self):
        self.assertEqual(validate(self.data), [])
    def test_simultaneous_rows_and_distinct_operators(self):
        day = self.data['days'][0]
        day['operator'] = {'name': 'ก', 'phone': '๐๑๒'}
        day['meetings'].append(dict(self.row(), id='m2'))
        other = copy.deepcopy(day)
        other.update(date='2026-10-20', operator={'name': 'ข'})
        other['meetings'] = [dict(self.row(), id='m3')]
        self.data['days'].append(other)
        self.assertEqual(validate(self.data), [])
    def test_thai_digits(self):
        self.data['days'][0]['date'] = '๒๐๒๖-๑๐-๑๙'
        self.row().update(time='๐๙:๐๐', end_time='๑๐:๓๐')
        self.assertEqual(validate(self.data), [])
        self.assertEqual(normal('พิษณุ ๑'), 'พิษณุ 1')
    def test_invalid_dates(self):
        for date in ('2026-02-29', '2026-13-01', '20261019', '2026-W43-1', None, [], True):
            with self.subTest(date=date):
                self.data['days'][0]['date'] = date
                self.assertTrue(validate(self.data))
    def test_time_bounds_types_and_ranges(self):
        for time in ('33:00', '24:00', '12:60', '9:00', '09.00', 900, None, [], '٠٩:٠٠'):
            with self.subTest(time=time):
                self.row()['time'] = time
                self.assertTrue(validate(self.data))
        self.row().update(time='10:00', end_time='09:59')
        self.assertTrue(validate(self.data))
        self.row()['end_time'] = '10:00'
        self.assertEqual(validate(self.data), [])
    def test_ids(self):
        for rid in (None, '', ' ', 1, True, [], {}):
            with self.subTest(rid=rid):
                self.row()['id'] = rid
                self.assertTrue(validate(self.data))
        self.row()['id'] = 'm1'
        self.data['days'][0]['meetings'].append(dict(self.row()))
        self.assertTrue(validate(self.data))
    def test_conflicting_statuses(self):
        for status in ('no_meetings', 'no_room', 'no_room_av'):
            with self.subTest(status=status):
                self.data['days'][0]['status'] = status
                self.assertTrue(validate(self.data))
        self.data['days'][0]['meetings'] = []
        self.assertEqual(validate(self.data), [])
    def test_unknown_does_not_imply_no_meetings(self):
        self.data['days'][0].update(status='unknown', meetings=[])
        self.assertEqual(validate(self.data), [])
    def test_duplicate_normalized_dates(self):
        other = copy.deepcopy(self.data['days'][0])
        other.update(date='๒๐๒๖-๑๐-๑๙', status='unknown', meetings=[])
        self.data['days'].append(other)
        self.assertTrue(validate(self.data))
    def test_bad_schema_does_not_crash(self):
        cases = [None, [], 'x', {}, {'days': None}, {'days': {}}, {'days': [None]},
                 {'days': [{'date': [], 'status': [], 'meetings': {}}]}]
        for data in cases:
            with self.subTest(data=data):
                self.assertTrue(validate(data))
        for field, value in [('title', 3), ('owner', []), ('chair', {}), ('room', False), ('notes', None)]:
            data = copy.deepcopy(self.data)
            data['days'][0]['meetings'][0][field] = value
            self.assertTrue(validate(data))
        self.data['days'][0]['operator'] = {'phone': 123}
        self.assertTrue(validate(self.data))
    def test_cli_invalid_json(self):
        with tempfile.TemporaryDirectory() as temp:
            file = Path(temp) / 'bad.json'
            file.write_text('{', encoding='utf-8')
            result = subprocess.run([sys.executable, str(Path(__file__).resolve().parent.parent/'scripts'/'validate_schedule.py'), str(file)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertFalse(json.loads(result.stdout)['valid'])
            self.assertNotIn('Traceback', result.stderr)

if __name__ == '__main__':
    unittest.main()
