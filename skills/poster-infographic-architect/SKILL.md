---
name: poster-infographic-architect
description: Use when a user wants to create a reusable layout template for an infographic, poster, or one-page report, with configurable header, hero, child-content, footer, background, and optional reference assets.
---

# Infographic / Poster / One-page Template Architect

## Mission

Create a reusable visual template first. The template defines structure, slot counts, slot roles, hierarchy, layout logic, and asset placement rules before any final content is populated.

The plugin's primary output is a **template specification / template-generation prompt**, not a finished poster narrative.

## Canonical template structure

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

Optional overlay/decorative layers may support the template but never replace these structural regions.

## User-configurable slot counts

The user may explicitly set:
- header_slot_count
- hero_slot_count
- child_slot_count
- footer_slot_count

If a count is omitted, infer an appropriate value from project type and information density.

A slot is a reusable placeholder. It may later hold text, image, logo, chart, statistic, QR, icon, or another supported element. Slots remain EMPTY by default; reference images may guide slot shape and layout without being inserted.

## Defaults

When unspecified:
- Template type: AUTO among infographic, poster, one_page_report
- Preset: AUTO from 30 built-in presets
- Canvas: A4
- Size: 210 × 297 mm
- Orientation: Portrait
- Background: AUTO
- Header slots: AUTO
- Hero slots: AUTO
- Child slots: AUTO
- Footer slots: AUTO
- Style / mood / tone: AUTO
- Asset policy: Preserve-first

## Priority

1. Explicit user instructions
2. Explicit slot counts and slot roles
3. User-supplied assets and preservation constraints
4. Project requirements
5. Skill references
6. Intelligent inference
7. Defaults

## Workflow

1. Normalize the request, identify template type, and resolve preset_id (AUTO, P01–P30, or CUSTOM).
2. Resolve canvas and orientation.
3. Resolve slot counts for Header, Hero, Child, and Footer.
4. Build Background Layer.
5. Build Header grid and slot geometry.
6. Build Content Box.
7. Inside Content Box, build Hero Section first, then Child Content Section.
8. Build Footer grid and slot geometry.
9. Assign semantic roles to slots.
10. Map user-supplied assets to eligible slots.
11. Define art direction, grid, spacing, typography hierarchy, color roles, and visual flow.
12. Apply preservation rules.
13. Compile the template-generation prompt/specification.
14. Run template QA and revise before output.

## Slot rules

Each slot should define:
- slot_id
- parent_section
- slot_index
- semantic_role
- content_type
- relative_size
- alignment
- priority
- asset_binding or AUTO
- editable/fixed state

Explicit slot count must be honored unless physically impossible for the requested canvas. If impossible, preserve the count and simplify slot size/content density before proposing a count change.

## Structural rules

- Header, Content Box, Footer are foreground structural regions.
- Background is a page-level layer behind all foreground regions.
- Hero and Child are children of Content Box.
- Hero slots receive stronger visual hierarchy than Child slots by default.
- Child slots should be visually modular and repeatable.
- Footer slots should remain compact and secondary unless explicitly promoted.
- Slot geometry may vary by orientation and information density.
- Template structure is semantic; exact coordinates are decided by the layout engine.

## Preserve-first asset policy

User-provided assets are not permission to redesign identity or brand features.

Defaults:
- Person / face → LOCKED identity
- Logo / emblem / QR / signature → LOCKED
- Product / uniform / identifiable object → STRICT
- Background reference → GUIDED
- Style reference → INSPIRATION_ONLY

## Output

Return a production-ready **template prompt/specification** that clearly defines:
- canvas
- background treatment
- region proportions
- slot counts
- slot IDs and roles
- section hierarchy
- grid / spacing rules
- visual system
- asset bindings
- preservation constraints
- negative constraints
- final QA instructions

## Supporting references

Use these operational references:
- references/parameter-specification.md
- references/template-architecture.md
- references/template-presets.md
- references/image-asset-taxonomy.md
- references/section-layout-engine.md
- references/design-foundations.md
- references/asset-preservation-policy.md
- references/prompt-compiler-spec.md
- references/qa-scoring.md
