# Section & Layout Engine v0.2

## Canonical page model

```text
PAGE
├── BACKGROUND LAYER
├── HEADER REGION
│   └── header_slot[1..N]
├── CONTENT BOX
│   ├── HERO SECTION
│   │   └── hero_slot[1..N]
│   └── CHILD CONTENT SECTION
│       └── child_slot[1..N]
└── FOOTER REGION
    └── footer_slot[1..N]
```

Background is a layer, not a counted content slot.

## Slot-count behavior

The user may set:
- header_slot_count
- hero_slot_count
- child_slot_count
- footer_slot_count

Counts may be zero.

Explicit counts are authoritative. The engine may change geometry, grid density, typography scale, and whitespace to accommodate them before suggesting any count change.

## Header Region

Purpose:
- identity
- title family
- headline or report title
- subtitle
- campaign label
- organization
- date/category/metadata

Typical slot patterns:
- 1 slot: unified text/title or brand block
- 2 slots: logo + title, or title + subtitle
- 3 slots: logo + title + metadata/subtitle
- 4+ slots: mixed text/asset grid; only when requested

## Content Box

The main bounded working area between Header and Footer.

It contains exactly two semantic child regions:
1. Hero Section
2. Child Content Section

### Hero Section

Purpose:
- strongest visual
- main headline/message
- key statistic
- central subject

Hero slot patterns:
- 1: single dominant hero
- 2: visual + message/stat
- 3+: multi-hero/comparison layout when explicitly needed

Hero has higher visual weight than Child by default.

### Child Content Section

Purpose:
- modular facts
- steps
- features
- comparisons
- charts
- recommendations
- supporting visuals

Child slots should be repeatable modules.

Suggested geometry:
- 1: full-width module
- 2: 2-column or stacked
- 3: 3-column or 1+2
- 4: 2×2
- 5–6: modular grid
- 7+: dense infographic/report grid with reduced decoration

## Footer Region

Purpose:
- source
- note/disclaimer
- CTA
- contact information
- website/social handle
- QR
- secondary branding

Footer remains visually secondary unless explicitly promoted.

## Background Layer

May be:
- solid color
- gradient
- image
- environment
- texture
- subtle illustration

It must support figure-ground separation and not compete with the foreground.

## Region ratios

AUTO chooses ratios from template type, orientation, and slot counts.

Typical A4 portrait starting ranges:
- Header: 8–15%
- Content Box: 72–84%
- Footer: 6–12%

Within Content Box:
- Hero: 30–55%
- Child: remaining 45–70%

These are starting ranges, not fixed rules.

## Grid logic

A4 portrait:
- 4, 6, or 8-column grid

Landscape:
- 6, 8, or 12-column grid

High child-slot counts:
- favor modular grid
- reduce decorative overlays
- increase grouping clarity

## Layout quality rules

- Header, Hero, Child, Footer must remain visually distinguishable.
- Hero must have stronger hierarchy than Child unless explicitly overridden.
- Child modules must align consistently.
- Footer must not consume disproportionate space.
- Background must not reduce readability.
- Protected assets may only be cropped/repositioned within preservation rules.
- Explicit slot counts must match the final template specification.
