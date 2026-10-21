# Deterministic typography fallback

Scope: create a NEW text-only PNG, A4 2480×3508 at300dpi. Supports general sections or canonical schedule; it is not an image editor or full collage/table renderer. Palette P01/P02 is only a palette in this script, not the artistic preset composition. Do not silently substitute it for an explicitly requested photographic design.

Dependencies: Python3, Pillow with RAQM, fontTools; regex recommended for grapheme segmentation. Bundled Sarabun-Regular.ttf is licensed under included OFL.txt. Do not install dependencies or fetch fonts without following host policy. If unavailable, use supported host capabilities and disclose limitations.

For a schedule validate canonical JSON first with meeting-poster/scripts/validate_schedule.py INPUT.json. Stop on errors. For all publications keep numeric/contact values as strings. Then run:

python scripts/render_publication.py --input INPUT.json --font assets/Sarabun-Regular.ttf --out OUTPUT.png

Paths above are relative to this skill. Input requires title; optional agency, subtitle, sections:[{heading,body}], days (canonical meetings schema), footer, phone, palette:P01/P02, digits:thai/arabic. Thai default converts all visible digits including phones without changing values. Date internal ISO Gregorian becomes abbreviated Buddhist display. Never infer missing official fields; — displayed.

Inspect OUTPUT.png. Sidecar OUTPUT.qc.json records text strings and geometry/font coverage only. It is NOT source verification or a visual fidelity certificate. Fail rather than truncate on overflow; do not claim every dense weekly schedule will fit. Source ambiguity requires user clarification; renderer does not perform OCR.

Tests: add scripts directory to PYTHONPATH and run unittest discover on tests. DejaVu is used for Latin-only test cases when available; Thai integration uses bundled Sarabun. Validate decoder, dimensions and visual page separately. No CMYK/PDF-X/bleed guarantees are implemented.
