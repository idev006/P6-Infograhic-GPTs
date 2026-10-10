# Template Prompt Compiler Specification v0.7

## Required output order

1. USER MODE RESOLUTION
2. ROLE
3. TEMPLATE TYPE + PRESET
4. CANVAS
5. REFERENCE IMAGE ROLE MAP
6. REGION SOURCE MAP
7. EDITORIAL SHELL STYLE
8. BACKGROUND DESIGN
9. HEADER DESIGN
10. HERO SECTION
11. CONTENT LAYOUT
12. PANEL / COMPARISON FRAME SYSTEM
13. FOOTER DESIGN
14. GRID / SPACING / GUTTER
15. OPTICAL BALANCE
16. TYPOGRAPHY
17. COLOR
18. MOTIF / GRAPHIC LANGUAGE
19. ASSET BINDINGS
20. PRESERVATION
21. NEGATIVE CONSTRAINTS
22. FINAL QA

## User-mode rule

EASY:
- avoid unnecessary jargon
- present only essential decisions
- internally normalize all inferred settings

ADVANCED:
- include normalized parameters and maps when useful

AUTO:
- choose EASY behavior unless explicit technical settings suggest otherwise

## Mandatory declarations

State internally:
- user_mode
- hero_section
- hero_slot_count
- content_layout_type
- panel_frame_mode
- editorial_shell_style
- region mappings

If BALANCED_MASONRY:
- image_panel_count
- M01..MNN map

If BEFORE_AFTER:
- comparison_pair_count
- orientation
- Before position
- After position
- pair IDs and frame synchronization

## Before / After prompt language

Explicitly require:
- Before on left / After on right by default
- matched or optically equivalent image areas
- clear central separation or transition cue
- synchronized frame family
- empty image apertures
- no fabricated transformation claims

## Negative constraints

Include as relevant:
- no generic blank header/footer
- no unrelated background
- no chaotic masonry
- no visually unequal Before/After sides unless requested
- no reversed Before/After placement unless requested
- no missing panels/pairs
- no automatic reference insertion
- no distorted locked assets
- no fabricated factual copy
