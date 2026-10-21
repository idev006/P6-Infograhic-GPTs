# Adventure release 0.3.0

## Completed scope
Production workflow for meeting posters and general publications; police-context editorial role; approved P01/P02; robust canonical schedule validator; numeral/date formatter; basic deterministic Thai typography fallback; bundled licensed Sarabun; regression tests; versioned GitHub source and plugin release.

## Verification executed
- 11 schedule validation tests PASS: malformed schema, invalid dates/times, same-time rows, duplicate IDs/dates, absent officials, status conflicts, reversed ranges and invalid JSON CLI.
- 15 renderer/independent contract tests PASS: exact role labels, Thai-digit date handling, full numeral policy including phones, statuses, placeholders, grapheme wrapping, bounds, missing font, overflow rejection and string-only phones.
- Synthetic Thai schedule rendered with Sarabun/RAQM, fully decoded PNG2480x3508, approximately300dpi; full-page visual inspection: readable Thai, no observed clipping in this fixture.
- Structural JSON/YAML/archive checks before upload; plugin source readback after release.

## Limits and excluded claims
The fallback is basic text layout, NOT a full photo-collage or table-grid renderer. P01/P02 artistic compositions still use supported host graphics tools and require per-output QC. No new OCR model/server is deployed. Ambiguous source fields require clarification. Real-world blurred OCR, complex multi-panel print and image-model portrait fidelity are not certified by these tests. No universal world-class, pixel-identical face, CMYK/PDF-X or native4K/8K guarantee.

## Release readiness
Ready as a versioned skills-based plugin with tested optional typography utilities. Every final client deliverable must still pass source and visual QC. A completed release does not mean every future rendering is correct. Use current user inputs; no production photos/contact records bundled.

## Reproduce
Set PYTHONPATH to skills/adventure-publication/scripts; run python -m unittest discover -s skills/adventure-publication/tests. Repeat with meeting-poster/scripts and tests. Pillow RAQM, fontTools, regex(optional) and a Latin test font required. For a schedule validate JSON first, then follow renderer reference. Font binary is bundled in plugin; GitHub text-source snapshot stores Sarabun-Regular.ttf.base64 with OFL.txt, decode using standard base64 before running Thai tests.
