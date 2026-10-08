# Section & Layout Engine v0.5

## Page model

```text
PAGE
├── BACKGROUND LAYER     ← AUTO-DESIGNED
├── HEADER REGION        ← AUTO-DESIGNED
├── CONTENT BOX
│   ├── HERO SECTION     ← reusable slots
│   └── CHILD SECTION    ← reusable slots
└── FOOTER REGION        ← AUTO-DESIGNED
```

## System-managed regions

### Background
Must be intentionally designed across the canvas. Avoid reducing it to decorative edges only unless the chosen art direction explicitly calls for that.

### Header
System chooses:
- height/proportion
- visual treatment
- alignment
- internal grouping
- typography hierarchy
- optional logo/title/subtitle/metadata placement

### Footer
System chooses:
- height/proportion
- visual treatment
- alignment
- internal grouping
- source/CTA/contact/QR/brand support areas as appropriate

Header/Footer may contain text or assets, but factual content is never invented.

## Slot-based Content Box

### Hero Section
User-facing parameter:
- hero_slot_count

Hero patterns:
- 1 → single dominant visual/message placeholder
- 2 → split/paired hero
- 3+ → comparison, KPI row, or multi-hero system when appropriate

### Child Content Section
User-facing parameter:
- child_slot_count

Suggested geometry:
- 1 → full-width/open module
- 2 → split or stacked
- 3 → 3-column / 1+2
- 4 → 2×2 or asymmetric editorial
- 5–6 → adaptive modular grid
- 7+ → dense report/infographic grid

## Visual treatment rule

Do not automatically draw a border around every slot.

Select among:
- open whitespace
- soft cards
- editorial blocks
- image masks
- tinted panels
- asymmetric zones
- dividers
- bands
- restrained outlined cards only when stylistically appropriate

## Region ratios

Typical A4 portrait starting range:
- Header: 8–15%
- Content Box: 72–84%
- Footer: 6–12%

Within Content Box:
- Hero: 25–55%
- Child: remaining area

These ranges adapt to reference images, preset, density, and user constraints.

## Grid logic

A4 portrait:
- 4, 6, or 8-column grid

Landscape:
- 6, 8, or 12-column grid

High Child counts:
- favor modular grids
- reduce ornament
- strengthen grouping

## Quality rules

- Background, Header, Content Box, and Footer must feel like one designed system.
- Header/Footer must look designed even if final text is absent.
- Hero should normally dominate Child.
- Empty content placeholders must not make the result look like a data-entry form.
- Reference images may influence geometry without being inserted.
- Protected assets obey preservation policy.
