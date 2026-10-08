# Section & Layout Engine v0.1

## Goal

Translate information architecture into a spatial design without treating sections as fixed coordinates.

## Semantic sections

### Header
Typical content:
- brand
- category
- campaign label
- institutional identifier

### Hero
Typical content:
- headline
- primary visual
- primary message
- key statistic

### Content
Typical content:
- facts
- steps
- comparisons
- charts
- recommendations
- supporting visuals

### Footer
Typical content:
- CTA
- QR
- contact
- source
- disclaimer
- secondary brand mark

### Background Layer
Provides:
- context
- depth
- atmosphere
- continuity

### Overlay Layer
Provides:
- gradients
- translucent panels
- lines
- textures
- HUD elements
- decorative accents

## Section enablement logic

Header:
- ENABLE when brand/institution/category needs clear identification.
- DISABLE or MERGE into Hero for minimal campaign graphics.

Hero:
- ENABLE for almost all posters and many infographics.
- MERGE with Header for compact formats.

Content:
- ENABLE when more than one supporting point is needed.
- May contain 1..N modules.

Footer:
- ENABLE when CTA, source, contact, QR, legal text, or attribution exists.

Background:
- AUTO by default.
- May be plain color, image, gradient, texture, or environmental scene.

Overlay:
- AUTO.
- Use only when it improves hierarchy or visual cohesion.

## Layout selection heuristics

### Central Hero
Use when:
- one dominant subject
- low/medium information density
- strong campaign message

### Split Layout
Use when:
- subject and content need equal presence
- before/after, comparison, or portrait + facts

### Editorial Grid
Use when:
- medium/high information density
- one-page report
- multiple content modules

### Modular Grid
Use when:
- 3+ peer-level facts, steps, or categories

### Z Pattern
Use when:
- strong headline + visual + CTA
- campaign/social poster

### F Pattern
Use when:
- text-heavy informational layout

### Data-led
Use when:
- chart/statistic is the main communication object

### Full Bleed
Use when:
- atmosphere and image impact dominate
- limited text

## Grid heuristics

Portrait A4:
- prefer 4, 6, or 8-column underlying grid
- maintain outer margins and consistent gutters
- use larger top/bottom breathing room for premium editorial layouts

Landscape:
- prefer 6, 8, or 12-column logic
- allow side-by-side hero/content regions

Square/social:
- prioritize central hierarchy and mobile legibility

## Visual flow

Choose based on content:
- top_down for formal documents
- z_pattern for campaign graphics
- f_pattern for reading-heavy layouts
- diagonal for dynamic campaign work
- central for hero-first visuals

## Whitespace

LOW density:
- generous whitespace
- few modules
- strong focal point

MEDIUM:
- balanced spacing

HIGH:
- tighter modular system
- strong grouping
- reduced decorative complexity

VERY_HIGH:
- one-page report logic
- grid discipline
- minimal nonfunctional decoration

## Composition constraints

- Never place protected assets where required cropping violates preservation policy.
- Do not use decorative overlays that reduce logo/QR readability.
- Headline and hero must not compete at identical visual weight.
- Maintain figure-ground separation.
- Maintain readable contrast and text-safe areas.
