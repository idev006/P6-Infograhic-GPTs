# P6-Infograhic-GPTs

> Product name: **Visual Template Architect**

A ChatGPT Plugin for creating reusable layout templates for:
- Infographics
- Posters
- One-page reports

The plugin designs the template structure before content is populated.

## Canonical template architecture

```text
CANVAS
├── BACKGROUND LAYER
├── HEADER
│   └── Header Slots [0..N]
├── CONTENT BOX
│   ├── HERO SECTION
│   │   └── Hero Slots [0..N]
│   └── CHILD CONTENT SECTION
│       └── Child Slots [0..N]
└── FOOTER
    └── Footer Slots [0..N]
```

The user may explicitly define the number of slots in:
- Header
- Hero
- Child Content
- Footer

Background is a page-level layer and is not counted as a slot.

## Default

- Canvas: A4
- Orientation: Portrait
- Size: 210 × 297 mm
- Slot counts: AUTO unless explicitly set

## Core principles

1. Template-first, not final-content-first.
2. Header / Content Box / Footer form the main foreground structure.
3. Hero and Child are children of Content Box.
4. Explicit slot counts are authoritative.
5. Preserve before transform for supplied assets.
6. Layout adapts to slot count, canvas, and information density.
7. QA must verify exact requested slot counts.

## Plugin workflow

User requirements
→ Template type
→ Canvas
→ Slot counts
→ Background
→ Header
→ Content Box
→ Hero
→ Child modules
→ Footer
→ Grid / Visual System
→ Asset mapping
→ Template Prompt Compiler
→ QA
→ Reusable Template Specification / Prompt

## Repository

idev006/P6-Infograhic-GPTs
