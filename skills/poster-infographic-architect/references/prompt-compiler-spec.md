# Template Prompt Compiler Specification v0.8

## Required output order

1. USER MODE RESOLUTION
2. COMMUNICATION OBJECTIVE
3. CREATIVE CONCEPT
4. ART DIRECTION
5. TEMPLATE TYPE + PRESET
6. CANVAS
7. REFERENCE IMAGE ROLE MAP
8. REGION SOURCE MAP
9. LOGO / BRAND HARMONY PLAN
10. EDITORIAL SHELL STYLE
11. BACKGROUND DESIGN
12. HEADER DESIGN
13. HERO SECTION
14. CONTENT LAYOUT
15. PANEL / COMPARISON FRAME SYSTEM
16. FOOTER DESIGN
17. GRID / SPACING / NEGATIVE SPACE
18. VISUAL HIERARCHY / OPTICAL BALANCE / RHYTHM
19. TYPOGRAPHY
20. COLOR
21. MOTIF / GRAPHIC LANGUAGE
22. ASSET BINDINGS
23. PRESERVATION
24. NEGATIVE CONSTRAINTS
25. FINAL DESIGN QA

## Compiler principle

The final prompt must communicate a coherent art direction, not a checklist of unrelated decorations.

Every major visual instruction should support at least one:
- communication objective
- hierarchy
- identity
- navigation
- emotional tone
- editorial coherence

## EASY mode

Do not expose internal complexity.
Compile the full intelligence internally, but present only essential user-facing interpretation plus the production prompt/spec.

## ADVANCED mode

May expose:
- concept statement
- art-direction plan
- reference role map
- logo harmony plan
- content map
- QA summary

## Logo / Brand Harmony section

When a logo is present, explicitly state:

- use the original logo unchanged
- preserve original geometry, colors, aspect ratio, internal text/symbols
- no redraw, recolor, warp, crop, texture treatment, or stylistic reinterpretation
- maintain protected clear space
- select placement and surrounding contrast deliberately
- adapt shell color/motif/typography/geometry around the logo
- logo should feel integrated, not pasted on
- if exact rendering is unreliable, reserve placement for compositing the original asset

Principle:
"Preserve the logo. Harmonize the environment."

## Content layouts

If BALANCED_MASONRY:
- declare exact panel count
- define optical rhythm
- define frame family

If BEFORE_AFTER:
- Before left / After right by default
- matched comparison weight
- synchronized frame family
- clear comparison cue

## Negative constraints

Include as relevant:
- no arbitrary decoration
- no generic empty header/footer
- no unrelated background
- no chaotic masonry
- no weak hierarchy
- no inconsistent visual languages
- no pasted-on logo appearance
- no logo alteration
- no automatic reference insertion
- no fabricated factual copy
