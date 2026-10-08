# Template Presets v0.5

All presets share these defaults:
- Background = AUTO-DESIGNED
- Header = AUTO-DESIGNED
- Footer = AUTO-DESIGNED
- Reference images guide design but do not populate slots automatically
- Hero and Child are the reusable slot-based areas

Format below: Hero/Child slots.

## Poster

- P01 Hero Campaign Poster — 1/2 — central hero, LOW density
- P02 Corporate Announcement — 1/3 — structured editorial, MEDIUM
- P03 Event Poster — 1/3 — event-focused hero + details, MEDIUM
- P04 Public Safety Poster — 1/4 — warning/prevention modules, MEDIUM
- P05 Product / Service Poster — 1/3 — hero product + benefits, MEDIUM
- P06 Minimal Premium Poster — 1/1 — whitespace-led, LOW
- P07 Photo-led Poster — 1/2 — large image-shaped hero placeholder, LOW
- P08 Quote / Message Poster — 1/2 — typography-led hero, LOW
- P09 Recruitment Poster — 1/4 — hero + requirements, MEDIUM
- P10 Festival / Celebration Poster — 1/3 — decorative hero + details, MEDIUM

## Infographic

- P11 3-Key-Point Infographic — 1/3 — equal supporting modules, MEDIUM
- P12 4-Step Process — 1/4 — sequential flow, MEDIUM
- P13 5-Fact Infographic — 1/5 — modular facts, MEDIUM
- P14 6-Module Infographic — 1/6 — adaptive grid, HIGH
- P15 Data Snapshot — 2/4 — data-led, HIGH
- P16 Comparison Infographic — 2/4 — A/B comparison, MEDIUM
- P17 Timeline Infographic — 1/6 — timeline flow, HIGH
- P18 Problem → Solution — 2/4 — issue/solution split, MEDIUM
- P19 Checklist Infographic — 1/7 — repeated compact modules, HIGH
- P20 Map / Location Infographic — 1/5 — map-shaped hero + facts, MEDIUM

## One-page Report

- P21 Executive One-page — 2/4 — editorial executive brief, HIGH
- P22 KPI One-page — 2/6 — KPI/data grid, HIGH
- P23 Project Status One-page — 1/6 — status/risk/next steps, HIGH
- P24 Strategic One-page — 2/5 — strategy map, HIGH
- P25 Technical One-page — 1/8 — dense technical summary, VERY_HIGH
- P26 Visual Story One-page — 1/5 — narrative editorial, MEDIUM
- P27 Before / After One-page — 2/4 — paired comparison, MEDIUM
- P28 Meeting / Activity Summary — 1/6 — activity/photo summary, HIGH
- P29 Policy / Guideline One-page — 1/7 — hierarchy-led guidance, HIGH
- P30 Dashboard Summary One-page — 3/6 — KPI hero row + detail grid, VERY_HIGH

## Preset behavior

- preset_id = AUTO | CUSTOM | P01..P30
- preset controls Hero/Child starting architecture, layout intent, and density
- Background/Header/Footer remain system-designed
- explicit Hero/Child counts override preset values
- explicit canvas/orientation overrides preset assumptions
- input images may influence empty slot shape/aspect
- asset binding requires explicit instruction
- preservation constraints always apply
