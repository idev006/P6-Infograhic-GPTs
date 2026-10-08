# Template Presets v0.4

Presets are starting architectures, not rigid final designs. Explicit user parameters always override preset values.

Global preset rules:
- Header, Footer, and Background are created by default unless explicitly disabled.
- Background is a page-level layer, never a counted slot.
- Slots remain EMPTY by default.
- Input images may guide slot geometry and layout without being inserted.
- Assets are bound to slots only when explicitly requested or defined as fixed/locked brand assets.

## Poster Presets

### P01 — Hero Campaign Poster
Type: poster
Slots H/R/C/F: 1/1/2/1
Use: strong campaign message, one dominant visual
Layout: central hero
Density: LOW

### P02 — Corporate Announcement
Type: poster
Slots H/R/C/F: 2/1/3/1
Use: official announcement, organization branding
Layout: structured editorial
Density: MEDIUM

### P03 — Event Poster
Type: poster
Slots H/R/C/F: 2/1/3/2
Use: event title, date, venue, CTA
Layout: hero + supporting blocks
Density: MEDIUM

### P04 — Public Safety Poster
Type: poster
Slots H/R/C/F: 2/1/4/1
Use: warning, awareness, prevention
Layout: hero + modular warnings
Density: MEDIUM

### P05 — Product / Service Poster
Type: poster
Slots H/R/C/F: 1/1/3/2
Use: product/service promotion
Layout: hero product + benefits
Density: MEDIUM

### P06 — Minimal Premium Poster
Type: poster
Slots H/R/C/F: 1/1/1/1
Use: premium visual communication
Layout: large whitespace, dominant hero
Density: LOW

### P07 — Photo-led Poster
Type: poster
Slots H/R/C/F: 2/1/2/1
Use: portrait, activity, destination, or campaign photo
Layout: large image-shaped hero placeholder
Density: LOW

### P08 — Quote / Message Poster
Type: poster
Slots H/R/C/F: 1/1/2/1
Use: quotation, leadership message, key statement
Layout: typography-led hero
Density: LOW

### P09 — Recruitment Poster
Type: poster
Slots H/R/C/F: 2/1/4/2
Use: recruitment, application, qualification, contact
Layout: hero + requirements grid
Density: MEDIUM

### P10 — Festival / Celebration Poster
Type: poster
Slots H/R/C/F: 2/1/3/1
Use: celebration, greeting, cultural event
Layout: decorative hero with modular details
Density: MEDIUM

## Infographic Presets

### P11 — 3-Key-Point Infographic
Type: infographic
Slots H/R/C/F: 1/1/3/1
Use: simple educational infographic
Layout: hero + 3 equal modules
Density: MEDIUM

### P12 — 4-Step Process
Type: infographic
Slots H/R/C/F: 1/1/4/1
Use: process, workflow, how-to
Layout: sequential modules
Density: MEDIUM

### P13 — 5-Fact Infographic
Type: infographic
Slots H/R/C/F: 2/1/5/1
Use: facts, tips, checklist
Layout: modular grid
Density: MEDIUM

### P14 — 6-Module Infographic
Type: infographic
Slots H/R/C/F: 2/1/6/1
Use: broad educational content
Layout: 2x3 or adaptive grid
Density: HIGH

### P15 — Data Snapshot
Type: infographic
Slots H/R/C/F: 2/2/4/2
Use: key statistics + charts
Layout: data-led
Density: HIGH

### P16 — Comparison Infographic
Type: infographic
Slots H/R/C/F: 1/2/4/1
Use: A vs B, before/after, options
Layout: split hero + comparison modules
Density: MEDIUM

### P17 — Timeline Infographic
Type: infographic
Slots H/R/C/F: 1/1/6/1
Use: chronology, milestones
Layout: vertical/diagonal timeline
Density: HIGH

### P18 — Problem → Solution
Type: infographic
Slots H/R/C/F: 1/2/4/1
Use: issue, evidence, solution, CTA
Layout: split hero + solution modules
Density: MEDIUM

### P19 — Checklist Infographic
Type: infographic
Slots H/R/C/F: 1/1/7/1
Use: checklist, do/don't, readiness list
Layout: repeated compact child cards
Density: HIGH

### P20 — Map / Location Infographic
Type: infographic
Slots H/R/C/F: 2/1/5/1
Use: area overview, route, location facts
Layout: large map-shaped hero + supporting modules
Density: MEDIUM

## One-page Report Presets

### P21 — Executive One-page
Type: one_page_report
Slots H/R/C/F: 3/2/4/2
Use: executive brief, management summary
Layout: editorial grid
Density: HIGH

### P22 — KPI One-page
Type: one_page_report
Slots H/R/C/F: 2/2/6/2
Use: KPI dashboard-style report
Layout: data-led modular grid
Density: HIGH

### P23 — Project Status One-page
Type: one_page_report
Slots H/R/C/F: 2/1/6/2
Use: progress, status, risks, next steps
Layout: structured report grid
Density: HIGH

### P24 — Strategic One-page
Type: one_page_report
Slots H/R/C/F: 2/2/5/2
Use: context, priorities, actions
Layout: editorial strategy map
Density: HIGH

### P25 — Technical One-page
Type: one_page_report
Slots H/R/C/F: 2/1/8/2
Use: technical summary, system overview
Layout: dense modular grid
Density: VERY_HIGH

### P26 — Visual Story One-page
Type: one_page_report
Slots H/R/C/F: 1/1/5/1
Use: narrative summary with strong visual continuity
Layout: hero-led editorial story
Density: MEDIUM

### P27 — Before / After One-page
Type: one_page_report
Slots H/R/C/F: 2/2/4/2
Use: transformation, improvement, comparison
Layout: paired hero + evidence modules
Density: MEDIUM

### P28 — Meeting / Activity Summary
Type: one_page_report
Slots H/R/C/F: 2/1/6/2
Use: meeting summary, activity report, field report
Layout: photo-friendly hero + modular summary
Density: HIGH

### P29 — Policy / Guideline One-page
Type: one_page_report
Slots H/R/C/F: 2/1/7/2
Use: rules, policy, guidelines, procedures
Layout: hierarchy-led modular report
Density: HIGH

### P30 — Dashboard Summary One-page
Type: one_page_report
Slots H/R/C/F: 2/3/6/2
Use: metrics, status indicators, executive dashboard
Layout: KPI hero row + modular detail grid
Density: VERY_HIGH

## Preset behavior

- preset_id = AUTO | CUSTOM | P01..P30
- presets define starting slot counts, layout intent, and density
- explicit slot counts override preset slot counts
- explicit slot definitions override preset slot roles
- explicit canvas/orientation override preset assumptions
- input images may influence shape/aspect of EMPTY slots
- reference images are not inserted by default
- explicit asset bindings override empty-slot behavior
- preservation constraints always remain active
- AUTO may select a preset from template type, content pattern, density, viewing context, and supplied references
