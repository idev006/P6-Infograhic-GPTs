# Template Presets v0.7

Global defaults:
- user_mode = AUTO
- Background = AUTO-DESIGNED
- Header = AUTO-DESIGNED
- Footer = AUTO-DESIGNED
- Hero = ENABLED
- Default content layout = BALANCED_MASONRY
- Panel frame = THEMED_FRAME
- References guide design without automatic placement
- Locked assets preserve identity exactly

Format: Hero / suggested content.

## Poster
- P01 Hero Campaign — 1 / 2 panels
- P02 Corporate Announcement — 1 / 3 panels
- P03 Event Poster — 1 / 3 panels
- P04 Public Safety — 1 / 4 panels
- P05 Product / Service — 1 / 3 panels
- P06 Minimal Premium — 1 / 1 panel
- P07 Photo-led — 1 / 2 panels
- P08 Quote / Message — 1 / 2 panels
- P09 Recruitment — 1 / 4 panels
- P10 Festival / Celebration — 1 / 3 panels

## Infographic
- P11 3-Key-Point — 1 / 3 panels
- P12 4-Step Process — 1 / 4 panels
- P13 5-Fact — 1 / 5 panels
- P14 6-Module — 1 / 6 panels
- P15 Data Snapshot — 2 / 4 panels
- P16 Comparison — 2 / 4 panels
- P17 Timeline — 1 / 6 panels
- P18 Problem → Solution — 2 / 4 panels
- P19 Checklist — 1 / 7 panels
- P20 Map / Location — 1 / 5 panels

## One-page / Editorial
- P21 Executive One-page — 2 / 4 panels
- P22 KPI One-page — 2 / 6 panels
- P23 Project Status — 1 / 6 panels
- P24 Strategic One-page — 2 / 5 panels
- P25 Technical One-page — 1 / 8 panels
- P26 Visual Story — 1 / 5 panels
- P27 Before / After — 1 / 1 comparison pair by default
- P28 Meeting / Activity Summary — 1 / 6 panels
- P29 Policy / Guideline — 1 / 7 panels
- P30 Dashboard Summary — 3 / 6 panels

## P27 Before / After behavior

Default:
- content_layout_type = BEFORE_AFTER
- comparison_pair_count = 1
- comparison_orientation = LEFT_RIGHT
- before_position = LEFT
- after_position = RIGHT
- comparison_frame_sync = MATCHED
- panel_frame_mode = THEMED_FRAME

Explicit pair count or orientation overrides these defaults.

## Behavior

- natural-language user requests are normalized automatically
- explicit image_panel_count overrides suggested Masonry count
- explicit comparison_pair_count overrides P27 default
- explicit Hero disable overrides preset Hero
- explicit frame mode overrides THEMED_FRAME
- explicit region source mapping overrides inference
