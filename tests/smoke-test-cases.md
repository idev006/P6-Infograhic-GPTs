# Smoke Test Cases — Visual Prompt Architect v0.1

Use these after private installation.

## T01 — Minimal poster, no image
Input:
"ทำโปสเตอร์ A4 เรื่องป้องกันมิจฉาชีพออนไลน์สำหรับประชาชนทั่วไป"

Expected:
- defaults to A4 portrait
- infers communication strategy
- creates section architecture
- returns production-ready master prompt
- does not force unnecessary questions

## T02 — Person reference
Input:
Attach one portrait and request a professional campaign poster.

Expected:
- classifies image as PERSON_FACE_REFERENCE
- identity policy = LOCKED
- prompt explicitly protects facial identity, age, skin tone, hairstyle
- may adapt pose/lighting/background only within policy

## T03 — Logo + person + background
Expected:
- person → LOCKED identity
- logo → LOCKED functional/brand asset
- background → GUIDED
- assets mapped to appropriate sections
- no arbitrary blending

## T04 — Exact QR
Expected:
- QR → LOCKED
- prompt does not request QR regeneration
- recommends reserved placement / later compositing when exact fidelity matters

## T05 — Style reference conflict
Person reference + highly stylized reference.

Expected:
- identity preservation outranks style intensity
- style reference = INSPIRATION_ONLY
- no look-alike replacement

## T06 — High-density infographic
Input:
A4 portrait, 8 facts, 2 statistics, source and CTA.

Expected:
- content section uses modules
- editorial/modular grid
- disciplined hierarchy
- footer includes source/CTA
- reduced decorative complexity

## T07 — Explicit landscape override
Input:
"A4 landscape"

Expected:
- landscape overrides portrait default
- layout recomposed rather than merely rotated

## T08 — User-defined image placement
Input:
"ภาพ 1 เป็น Hero, ภาพ 2 เป็น Background"

Expected:
- exact mapping preserved
- AUTO does not override placement

## T09 — Brand lock
Input:
Logo supplied with "ห้ามแก้โลโก้"

Expected:
- LOCKED policy
- no recolor/redraw/distortion
- QA treats violation as blocking failure

## T10 — Prompt QA
Expected:
- no contradictory instructions
- no fabricated data
- all assets accounted for
- preservation compliance >= 9
- overall QA pass before output
