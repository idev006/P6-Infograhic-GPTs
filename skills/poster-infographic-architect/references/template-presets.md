# Template Presets v0.3

Presets are starting architectures, not rigid final designs. Any explicit user parameter overrides the preset.

## P01 — Hero Campaign Poster
Type: poster
Header/Hero/Child/Footer: 1/1/2/1
Use: strong campaign message, one dominant visual
Layout: central hero
Density: LOW

## P02 — Corporate Announcement
Type: poster
Slots: 2/1/3/1
Use: official announcement, organization branding
Layout: structured editorial
Density: MEDIUM

## P03 — Event Poster
Type: poster
Slots: 2/1/3/2
Use: event title, date, venue, CTA
Layout: hero + supporting blocks
Density: MEDIUM

## P04 — Public Safety Poster
Type: poster
Slots: 2/1/4/1
Use: warning, awareness, prevention
Layout: hero + modular warnings
Density: MEDIUM

## P05 — Product / Service Poster
Type: poster
Slots: 1/1/3/2
Use: product/service promotion
Layout: hero product + benefits
Density: MEDIUM

## P06 — Minimal Premium Poster
Type: poster
Slots: 1/1/1/1
Use: premium visual communication
Layout: large whitespace, dominant hero
Density: LOW

## P07 — 3-Key-Point Infographic
Type: infographic
Slots: 1/1/3/1
Use: simple educational infographic
Layout: hero + 3 equal modules
Density: MEDIUM

## P08 — 4-Step Process
Type: infographic
Slots: 1/1/4/1
Use: process, workflow, how-to
Layout: sequential child modules
Density: MEDIUM

## P09 — 5-Fact Infographic
Type: infographic
Slots: 2/1/5/1
Use: facts, tips, checklist
Layout: modular grid
Density: MEDIUM

## P10 — 6-Module Infographic
Type: infographic
Slots: 2/1/6/1
Use: broad educational content
Layout: 2x3 or adaptive modular grid
Density: HIGH

## P11 — Data Snapshot
Type: infographic
Slots: 2/2/4/2
Use: key statistics + charts
Layout: data-led
Density: HIGH

## P12 — Comparison Infographic
Type: infographic
Slots: 1/2/4/1
Use: A vs B, before/after, options
Layout: split hero + comparison modules
Density: MEDIUM

## P13 — Timeline Infographic
Type: infographic
Slots: 1/1/6/1
Use: chronology, milestones
Layout: vertical/diagonal timeline
Density: HIGH

## P14 — Problem → Solution
Type: infographic
Slots: 1/2/4/1
Use: issue, evidence, solution, CTA
Layout: split hero + modular solution blocks
Density: MEDIUM

## P15 — Executive One-page
Type: one_page_report
Slots: 3/2/4/2
Use: executive brief, management summary
Layout: editorial grid
Density: HIGH

## P16 — KPI One-page
Type: one_page_report
Slots: 2/2/6/2
Use: KPI dashboard-style report
Layout: data-led modular grid
Density: HIGH

## P17 — Project Status One-page
Type: one_page_report
Slots: 2/1/6/2
Use: progress, status, risks, next steps
Layout: structured report grid
Density: HIGH

## P18 — Strategic One-page
Type: one_page_report
Slots: 2/2/5/2
Use: context, priorities, actions
Layout: editorial strategy map
Density: HIGH

## P19 — Technical One-page
Type: one_page_report
Slots: 2/1/8/2
Use: technical summary, system overview
Layout: dense modular grid
Density: VERY_HIGH

## P20 — Visual Story One-page
Type: one_page_report
Slots: 1/1/5/1
Use: narrative summary with strong visual continuity
Layout: hero-led editorial story
Density: MEDIUM

## Preset behavior

- parameter: preset_id = P01..P20 | AUTO | CUSTOM
- preset values are defaults only
- explicit slot counts override preset slot counts
- explicit canvas/orientation override preset layout assumptions
- explicit asset bindings override preset placement
- preservation constraints always remain active
- AUTO may select a preset based on template type, density, content pattern, and viewing context
