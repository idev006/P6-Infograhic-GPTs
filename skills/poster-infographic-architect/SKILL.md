---
name: poster-infographic-architect
description: Use when a user wants to create a reusable infographic, poster, or one-page report template with system-designed background, header, and footer plus configurable hero and child-content slots.
---

# Infographic / Poster / One-page Template Architect

## Mission

Create a reusable visual template. The system designs the **Background, Header, and Footer automatically**. The reusable slot system is focused primarily on the **Hero Section** and **Child Content Section** inside the Content Box.

The primary output is a template specification and/or production-ready template-generation prompt.

## Canonical template structure

```text
CANVAS
├── BACKGROUND LAYER        ← SYSTEM-DESIGNED
├── HEADER REGION           ← SYSTEM-DESIGNED
├── CONTENT BOX
│   ├── HERO SECTION        ← SLOT-BASED
│   │   └── Hero Slots [0..N]
│   └── CHILD CONTENT       ← SLOT-BASED
│       └── Child Slots [0..N]
└── FOOTER REGION           ← SYSTEM-DESIGNED
```

## Core policy

**Region design and slot content are different things.**

- Background must be visually designed, not left as an empty box.
- Header must be visually designed as a real header region.
- Footer must be visually designed as a real footer region.
- Hero and Child Content use reusable empty slots by default.
- Reference images may influence layout, proportions, slot geometry, style, mood, tone, and visual language without being inserted into slots.
- Do not turn every region or slot into identical outlined rectangles. Select an appropriate visual treatment from editorial blocks, cards, masks, open whitespace, bands, panels, asymmetric zones, or other professional layout devices.

## Header behavior

Header is system-managed by default. The engine decides its layout, visual treatment, internal grouping, typography hierarchy, and space allocation.

It may support:
- logo / organization identity
- title
- subtitle
- category
- date / metadata

Do not invent factual header text. If exact text is unavailable, design the header structurally with appropriate placeholder treatment.

## Footer behavior

Footer is system-managed by default. The engine decides its layout, visual treatment, internal grouping, and proportion.

It may support:
- source
- note / disclaimer
- CTA
- contact
- website / social
- QR
- secondary branding

Do not invent factual footer text. If exact text is unavailable, design the footer structurally with appropriate placeholder treatment.

## Background behavior

Background is always a page-level visual system unless explicitly disabled.

It may use:
- solid / tonal field
- gradient
- abstract geometry
- restrained pattern
- texture
- atmospheric illustration
- reference-derived color/mood

Background must visually connect Header, Content Box, and Footer and maintain figure-ground readability.

## User-configurable primary slot counts

The primary user-facing slot controls are:
- hero_slot_count
- child_slot_count

If omitted, infer from preset, template type, content pattern, reference images, and information density.

Header/Footer internal groups are system-managed by default. Advanced explicit instructions may override them, but the user should not need to specify their counts.

## Defaults

When unspecified:
- Template type: AUTO among infographic, poster, one_page_report
- Preset: AUTO from 30 built-in presets
- Canvas: A4
- Size: 210 × 297 mm
- Orientation: Portrait
- Background: AUTO-DESIGNED
- Header: AUTO-DESIGNED
- Footer: AUTO-DESIGNED
- Hero slots: AUTO
- Child slots: AUTO
- Reference image binding: REFERENCE_ONLY / PLACEHOLDER_GUIDE
- Asset policy: Preserve-first

## Priority

1. Explicit user instructions
2. Explicit Hero/Child slot counts and roles
3. Explicit asset binding
4. User-supplied preservation constraints
5. Project requirements
6. Preset
7. Skill references
8. Intelligent inference
9. Defaults

## Workflow

1. Normalize request and identify template type.
2. Resolve preset_id (AUTO, P01–P30, or CUSTOM).
3. Resolve canvas and orientation.
4. Analyze reference images and classify roles.
5. Design the full-page Background.
6. Design the Header region.
7. Build Content Box.
8. Resolve Hero slot count and geometry.
9. Resolve Child slot count and geometry.
10. Design the Footer region.
11. Map reference influence to layout without inserting assets unless explicitly bound.
12. Define typography, colors, spacing, hierarchy, and visual language.
13. Apply preservation rules.
14. Compile template specification/prompt.
15. Run QA and revise before output.

## Slot rules

Hero/Child slots remain EMPTY by default.

Each slot defines:
- slot_id
- parent_section
- slot_index
- semantic_role
- content_type
- relative_size / aspect behavior
- alignment
- priority
- asset_binding or NONE
- editable state

Stable IDs:
- R01..RNN = Hero
- C01..CNN = Child Content

## Preserve-first asset policy

Defaults:
- Person / face → LOCKED identity
- Logo / emblem / QR / signature → LOCKED
- Product / uniform / identifiable object → STRICT
- Background reference → GUIDED
- Style reference → INSPIRATION_ONLY

A supplied logo should guide Header planning but is not inserted unless the user requests binding. If bound, preserve its geometry, colors, text, and aspect ratio.

## Output

Return a production-ready template specification/prompt defining:
- canvas
- selected preset
- full Background treatment
- Header design
- Content Box proportions
- Hero slot count and geometry
- Child slot count and geometry
- Footer design
- grid / margins / spacing
- typography system
- color system
- reference influence map
- asset bindings, if any
- preservation constraints
- negative constraints
- final QA instructions

## Supporting references

Use:
- references/parameter-specification.md
- references/template-architecture.md
- references/template-presets.md
- references/image-asset-taxonomy.md
- references/section-layout-engine.md
- references/design-foundations.md
- references/asset-preservation-policy.md
- references/prompt-compiler-spec.md
- references/qa-scoring.md
