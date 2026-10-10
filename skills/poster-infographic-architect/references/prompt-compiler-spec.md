# Template Prompt Compiler Specification v0.10

## Required output order

1. USER MODE
2. DESIGN BRIEF INTERPRETATION
3. COMMUNICATION GOAL
4. CREATIVE CONCEPT
5. ART DIRECTION
6. PRESENTATION VIABILITY DECISION
7. TEMPLATE TYPE + PRESET
8. CANVAS / ORIENTATION / PAGE COUNT
9. REFERENCE IMAGE ROLE MAP
10. EXACT ASSET PLAN
11. REGION SOURCE MAP
12. LOGO / BRAND HARMONY PLAN
13. EDITORIAL SHELL
14. HEADER
15. HERO
16. CONTENT LAYOUT
17. IMAGE APERTURE MAP
18. PANEL / COLLAGE / COMPARISON FRAME SYSTEM
19. FOOTER
20. GRID / SPACING / NEGATIVE SPACE
21. HIERARCHY / FLOW / BALANCE / RHYTHM
22. TYPOGRAPHY
23. COLOR
24. MOTIF / GRAPHIC LANGUAGE
25. ASSET BINDINGS / COMPOSITING
26. PRESERVATION
27. NEGATIVE CONSTRAINTS
28. FINAL QA

## Exact-asset instruction

For logo/emblem/QR/signature/official insignia:

- DO NOT GENERATE OR REDRAW THE ASSET
- use supplied original asset only
- composite original proportionally
- preserve every internal detail
- if compositing is unavailable, leave a protected placement zone

## Collage instruction

When BALANCED_MASONRY / PAIRED_BALANCED_MASONRY / EDITORIAL_COLLAGE is active, explicitly state:

- do not use equal-size repetitive grid
- do not use repeated thin horizontal rectangles
- use varied but controlled image apertures
- preserve real-photo usability
- maintain optical balance and coherent pairing
- avoid form-like panel appearance

## Viability instruction

The prompt must state that image apertures must remain practical after insertion of normal 4:3, 3:2, portrait, or landscape activity photos.

If not viable, adapt canvas/orientation/Hero/page count before finalizing.

## EASY mode

Hide technical detail but compile all rules internally.
