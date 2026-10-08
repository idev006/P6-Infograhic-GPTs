# Canonical Template Architecture v0.5

## Structural invariant

```text
CANVAS
├── BACKGROUND_LAYER           [SYSTEM_DESIGNED]
├── HEADER_REGION              [SYSTEM_DESIGNED]
├── CONTENT_BOX
│   ├── HERO_SECTION           [SLOT_BASED]
│   │   └── HERO_SLOT[0..N]
│   └── CHILD_CONTENT_SECTION  [SLOT_BASED]
│       └── CHILD_SLOT[0..N]
└── FOOTER_REGION              [SYSTEM_DESIGNED]
```

## Key distinction

Region design is not slot content.

Background, Header, and Footer must have intentional visual design even when the user has not supplied final copy. Empty-slot policy applies primarily to Hero and Child Content payloads.

## Background

Background is global and uncounted. It must be designed as part of the visual system, not merely as an outer border.

It may include tonal fields, gradients, abstract geometry, subtle patterns, textures, atmospheric imagery, or other restrained decorative systems.

## Header

Header is a system-designed region. The engine determines composition and may reserve appropriate places for logo, title, subtitle, organization, category, or metadata.

If exact text/assets are absent, do not invent them. Use structural placeholder treatment where needed.

## Footer

Footer is a system-designed region. The engine determines composition and may reserve appropriate places for source, note, CTA, contact, QR, website, or secondary branding.

If exact text/assets are absent, do not invent them.

## Content Box

Content Box owns the reusable slot-based areas:
- Hero Section
- Child Content Section

Stable IDs:
- R01..RNN for Hero
- C01..CNN for Child

## User control

Primary controls:
```text
hero_slot_count = integer >= 0 | AUTO
child_slot_count = integer >= 0 | AUTO
```

Header/Footer are AUTO-DESIGNED by default. Advanced explicit user instructions may override their internal structure without making header/footer slot counts required inputs.

## Reference images

Default image behavior:
- REFERENCE_ONLY or PLACEHOLDER_GUIDE
- may influence layout, aspect ratio, visual style, and region treatment
- do not populate Hero/Child slots automatically
- fixed/locked assets are inserted only when explicitly bound

## Reusability

A strong template:
- has a designed Background, Header, and Footer
- reserves flexible Hero/Child content capacity
- does not resemble a plain form made from repeated empty rectangles
- supports replacement of content without redesigning the whole page
