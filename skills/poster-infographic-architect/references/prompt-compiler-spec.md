# Template Prompt Compiler Specification v0.6

## Required output order

1. ROLE
2. TEMPLATE TYPE + PRESET
3. CANVAS
4. REFERENCE IMAGE ROLE MAP
5. REGION SOURCE MAP
6. EDITORIAL SHELL STYLE
7. BACKGROUND DESIGN
8. HEADER DESIGN
9. HERO SECTION
10. BALANCED MASONRY CONTENT
11. PANEL FRAME SYSTEM
12. FOOTER DESIGN
13. GRID / SPACING / GUTTER
14. OPTICAL BALANCE
15. TYPOGRAPHY
16. COLOR
17. MOTIF / GRAPHIC LANGUAGE
18. ASSET BINDINGS
19. PRESERVATION
20. NEGATIVE CONSTRAINTS
21. FINAL QA

## Mandatory declarations

State:
- hero_section
- hero_slot_count
- child_layout_type
- image_panel_count
- panel_frame_mode
- editorial_shell_style
- Header/Background/Footer design modes
- region reference-image mappings

## Panel map

For each Masonry panel:
- panel_id M01..MNN
- relative size
- aspect behavior
- masonry position/relationship
- frame style
- content mode
- asset binding if any
- editable state

## Panel-frame language

When panel_frame_mode = THEMED_FRAME:
- explicitly describe how frame design derives from the shell
- keep panel interior empty
- use decorative treatment that does not overpower future photographs

When panel_frame_mode = PLAIN_GUIDE:
- specify a thin placement outline only

## Reference handling

Do not insert a reference image solely because it influenced:
- palette
- motif
- texture
- composition
- shape
- atmosphere
- silhouette

Only explicit bind_to_slot / fixed-region placement permits literal insertion.

## Negative constraints

Include:
- no generic blank header/footer
- no arbitrary unrelated background
- no Pinterest-style chaotic masonry
- no awkward dead gaps
- no missing requested panels
- no automatic insertion of references
- no distorted locked assets
- no panel decoration overpowering future photos
- no fabricated factual copy
