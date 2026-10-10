---
name: poster-infographic-architect
description: Use when a user wants a reusable editorial-style infographic, poster, newsletter, magazine, journal, one-page report, or before-after comparison template driven by expert design cognition, professional viability checks, exact locked-asset handling, editorial shell design, and adaptive collage layouts.
---

# Visual Template Architect — Design Cognition Blackbox

## Mission

Treat every user request as a design brief and solve it like a senior multidisciplinary design team.

The plugin must:
- understand the brief and references
- protect identity-critical assets
- form a concept and art direction
- choose a presentation strategy that remains usable with real photos
- design a coherent shell
- build image panels using adaptive editorial collage rather than mechanical grids
- critique and refine before output

## Mandatory blackbox pipeline

1. Intent & Brief Intelligence
2. Audience & Context Intelligence
3. Content Semantics & Hierarchy
4. Reference Image Intelligence
5. Exact Asset / Identity Protection
6. Creative Concept Formation
7. Art Direction
8. Presentation Viability Check
9. Editorial Shell Design
10. Content Architecture
11. Image Aperture Intelligence
12. Adaptive Collage / Comparison Layout
13. Typography / Color / Rhythm
14. Real-photo Placement Simulation
15. Professional Critique
16. Refinement Loop
17. Final Prompt / Template Specification

Never jump directly from requested image count to equal-size boxes.

## Core principles

**Meaning before form. Concept before decoration. System before styling. Usability before density. Refinement before delivery.**

## Exact Asset Pipeline

Identity-critical assets such as:
- logo
- emblem
- official insignia
- QR
- signature

default to:

```text
render_policy = ORIGINAL_ASSET_ONLY
generation = FORBIDDEN
redraw = FORBIDDEN
style_transfer = FORBIDDEN
```

The system may analyze the asset to harmonize the shell, but it must not ask a generative model to recreate the asset.

When the downstream workflow cannot directly composite the original asset, reserve an exact protected placement zone and instruct post-compositing of the supplied original.

## Presentation Viability

Before committing to a layout, test whether the requested image count, canvas, Hero size, shell size, and panel geometry allow real photos to remain useful.

If not viable, adapt one or more:
- Hero height
- Hero presence
- orientation
- page count
- shell proportions
- content layout
- panel proportions
- comparison strategy

Do not satisfy count at the expense of usability.

## Adaptive Collage System

Supported image architectures:

- BALANCED_MASONRY
- PAIRED_BALANCED_MASONRY
- EDITORIAL_COLLAGE
- GRID only when explicitly requested or semantically superior

### BALANCED_MASONRY
Default for general multi-image content.
Use controlled varied panel sizes/aspect ratios and optical balance.

### PAIRED_BALANCED_MASONRY
Default for multi-pair Before/After work.
Preserve clear Before↔After relationships while avoiding repetitive equal-height rows.

### EDITORIAL_COLLAGE
Use for magazine/journal storytelling when freer image rhythm improves narrative and hierarchy.

### Anti-grid rule
When BALANCED_MASONRY, PAIRED_BALANCED_MASONRY, or EDITORIAL_COLLAGE is active:

**Do not produce an equal-size repetitive grid unless the user explicitly asks for a grid.**

## Image Aperture Intelligence

Every image placeholder must be useful for realistic photo insertion.

Evaluate:
- minimum visible area
- plausible crop
- common photo ratios
- subject readability
- comparison legibility
- caption allowance if present

Avoid thin banner-like apertures for ordinary activity photos unless explicitly intended.

## Real-photo Placement Simulation

Before QA, mentally simulate common real photos placed into each aperture.

If a normal 4:3, 3:2, portrait, or landscape image would become unreadable, over-cropped, or visually trivial, revise the layout.

## Hero

Hero remains enabled by default, but viability may require compacting it.

Do not silently remove Hero if the user explicitly requires it; instead adapt page/orientation or surface a concise tradeoff.

## Panel frames

THEMED_FRAME remains default.

The frame must behave like an editorial photo container, not a double-line rectangular form field.

Possible treatments:
- partial accent edge
- clipped corner
- subtle mat
- theme-shaped mask
- restrained shadow/depth
- asymmetrical editorial border
- frameless crop with accent anchor

PLAIN_GUIDE remains available when decoration is disabled.

## Before / After

For multiple pairs:
- default = PAIRED_BALANCED_MASONRY
- Before remains perceptually associated with its corresponding After
- avoid five identical stacked rows when a better collage/paired composition exists
- preserve comparison clarity over decorative novelty

## Supporting references

Use:
- references/presentation-viability-engine.md
- references/exact-asset-pipeline.md
- references/adaptive-collage-engine.md
- references/design-cognition-blackbox.md
- references/design-intelligence-art-direction.md
- references/logo-harmony-engine.md
- references/user-mode-spec.md
- references/before-after-engine.md
- references/parameter-specification.md
- references/template-architecture.md
- references/template-presets.md
- references/section-layout-engine.md
- references/editorial-shell-engine.md
- references/region-source-mapping.md
- references/balanced-masonry-engine.md
- references/image-asset-taxonomy.md
- references/design-foundations.md
- references/asset-preservation-policy.md
- references/prompt-compiler-spec.md
- references/qa-scoring.md
