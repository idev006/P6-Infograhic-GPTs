# Adventure — Publication Plugin Programme

## Scope and authority
User-authorized extension of P6 Meeting Poster to posters, infographics and other print outputs. This directory is the GitHub project record for P6 Meeting Poster; existing Visual Template Architect project content at repository root remains unchanged. Plugin identity: plugins_6ad6118937c0819199c1f8325e347413. Current release: 0.3.0 (PRIVATE).

## Team
Product/project lead, art director, OCR/data specialist, layout engineer, portrait compositor, AI/plugin engineer, independent QA, UX, release/security, Thai police-context specialist. These are AI workflow responsibilities, not recruited human staff. Independent design and QA specialist passes informed this release.

## Architecture
Inputs → source/asset classification → canonical copy+amendments → publication routing → art direction → host production tools → independent evidence-based QA → actual artifact.
Meeting schedules retain meeting-poster skill, date formatter and validator. General publications use adventure-publication. Supporting visuals0–5; A4 portrait default; Thai numerals default with explicit Arabic override. P01 Golden Dawn and P02 Leadership Power retained.

## Milestones and actual status
- Completed: role charter, editorial/police context rules, routing, quality gates, saved presets, plugin package update.
- Completed: JSON/YAML/frontmatter/archive structural validation. Earlier formatting/invalid-time checks passed in0.1 series.
- Not yet verified: full end-to-end clean/blurred/dense publication benchmark under fresh host sessions; image identity and exact typography remain per-output checks.
- Delivered in 0.3.0: deterministic text-only A4 PNG renderer with RAQM Thai shaping, bundled OFL Sarabun font, digit/date formatting, font coverage checks and fail-on-overflow. This fallback does not implement photographic collage, a full table compositor, CMYK or PDF/X.
- Verified: 26 automated tests passed (15 renderer/contract + 11 schedule validator). A synthetic Thai PNG was decoded, checked at 2480×3508 / 300 dpi and visually inspected. QC sidecars record strings/geometry; they do not certify source correctness.

## Quality target
Professional international quality is an aspiration, not a certification. Zero critical data errors; no fabricated ranks/names/contact details. Visual scores alone never override a critical failure. See production contract.

## Change control
Store generic project docs, source and synthetic fixtures here. Do not upload real photos, personal phone numbers or operational schedules to this public repository. Update existing plugin identity, preserve scope/private visibility; version releases and read back saved files. No unrelated plugin or template workflow changed.

## Acceptance/roadmap
Next benchmark: clean typed schedule, ambiguous image source, dense bilingual infographic; record PASS/FAIL/NOT CHECKED with actual artifacts. Baseline is pending, not passed. Keep source and generated visual separate and use supported host tools. Capability unavailable must produce honest limitation, never fabricated success.

## Release evidence and reproduction
See [0.3.0 release evidence](plugin/RELEASE-0.3.0.md) and [renderer instructions](plugin/skills/adventure-publication/references/renderer.md). The plugin archive includes the actual TTF; this text-only GitHub mirror stores Sarabun-Regular.ttf.base64. Decode it to Sarabun-Regular.ttf in the same assets directory before reproducing Thai rendering tests. Preserve OFL.txt. All fixtures are synthetic.

## Delivery status
The 0.3.0 development scope is complete and published to the existing plugin identity. Advanced visual production uses host-supported graphics capabilities and per-output QA. A fresh-session OCR/photo-fidelity benchmark and broader international-quality certification have not been completed; no such claim is made.
