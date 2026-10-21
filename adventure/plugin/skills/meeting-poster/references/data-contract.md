# Canonical schedule
Use JSON: {"title":"...","agency":"...","days":[{"date":"2026-10-19","label":"จันทร์ ๑๙ ต.ค.๖๙","status":"meetings","operator":{"name":"...","phone":"..."},"meetings":[{"id":"m1","time":"13:00","title":"...","owner":"—","chair":"—","room":"...","notes":"..."}]}],"amendments":[]}.
ISO dates use Gregorian years internally; convert Buddhist years by subtracting543 when parsing. Visible dates use Buddhist years and Thai numerals. Times internally HH:MM, visible ๑๓.๐๐ น. Accept time ranges as time/end_time. Store literal source and provenance outside visible labels when useful. status can be meetings/no_meetings/no_room/no_room_av/unknown. Empty rows do not automatically mean no_meetings. Do not infer missing operators. Never merge two meetings merely because date/time match. Stable IDs distinguish same-time meetings. Amendments target ID or unambiguous date+title+time; preserve other fields.

Regression scenarios:
- User says33.00→13.00: resulting time13:00; invalid33:00 must fail validator.
- Add Monday15.00 drill at ภ.๖: append one row, missing owner/chair remain —, repeated request doesn't duplicate.
- Wednesday two09.00 rows remain separate; CANVA chair user correction พิษณุ๑ overridesรอข้อมูล.
- New source changes room or time: don't retain older generated poster value.
- Weekly→Monday request: include every Monday row and no other days; don't lose latest15.00 addition.
- Different daily operators remain associated with corresponding dates.

## Visible date and numeral defaults
Use D MMM YY in every per-day date cell: ๑ พ.ย.๖๙, ๓๑ ต.ค.๖๙. No leading zero; Buddhist year last two digits. Thai month abbreviations: ม.ค., ก.พ., มี.ค., เม.ย., พ.ค., มิ.ย., ก.ค., ส.ค., ก.ย., ต.ค., พ.ย., ธ.ค. Explicit user request for Arabic numerals overrides digit default only (1 พ.ย.69); retain Thai month abbreviations unless separately requested. Apply numeral policy to all visible fields, preserving values, Latin names and abbreviations. ISO/internal numbers need not use Thai digits.


