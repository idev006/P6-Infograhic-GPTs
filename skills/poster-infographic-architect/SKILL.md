---
name: poster-infographic-architect
description: Use when a user wants a reusable editorial-style infographic, poster, newsletter, or one-page report template with a designed shell, hero section, and balanced masonry image panels.
---

# Visual Template Architect — Editorial Template System

## Mission

Create a reusable professional template with two coordinated layers:

1. **Editorial Shell** — Background + Header + Footer + connecting motif, designed as one visual system.
2. **Content System** — Hero Section plus Balanced Masonry image panels for reusable content placement.

The template should feel like a polished school newsletter, institutional journal, news bulletin, magazine page, or professional one-page report rather than a blank form.

## Canonical structure

```text
CANVAS
├── BACKGROUND                ← EDITORIAL SHELL / AUTO-DESIGNED
├── HEADER                    ← EDITORIAL SHELL / AUTO-DESIGNED
├── CONTENT BOX
│   ├── HERO SECTION          ← ENABLED BY DEFAULT
│   │   └── Hero Slot(s)
│   └── MASONRY CONTENT       ← BALANCED MASONRY
│       ├── M01 [EMPTY IMAGE PANEL]
│       ├── M02 [EMPTY IMAGE PANEL]
│       └── ... M0N
└── FOOTER                    ← EDITORIAL SHELL / AUTO-DESIGNED
```

## Core defaults

- Background = AUTO-DESIGNED
- Header = AUTO-DESIGNED
- Footer = AUTO-DESIGNED
- Hero Section = ENABLED
- Hero slot count = 1 unless preset/instruction implies otherwise
- Child layout = BALANCED_MASONRY
- Image panel count = AUTO unless user specifies a number
- Panel frame mode = THEMED_FRAME
- Panel content = EMPTY placeholder
- Reference images influence design but are not inserted unless explicitly bound

## Editorial Shell policy

Background, Header, and Footer form one coordinated shell.

The shell engine must:
- select an editorial shell style
- choose compatible Header/Footer archetypes
- establish a shared color system, motif, typography language, and decorative vocabulary
- use user-designated reference images for specific regions when supplied
- preserve locked assets such as logos exactly
- avoid generic empty boxes for Header/Footer

Supported shell styles include:
- INSTITUTIONAL
- SCHOOL_NEWSLETTER
- NEWS_MAGAZINE
- GOVERNMENT_FORMAL
- MODERN_EDITORIAL
- CORPORATE
- CEREMONIAL
- AUTO

## Region Source Mapping

Users may identify images for specific design regions:

- header_reference_images
- footer_reference_images
- background_reference_images
- style_reference_images
- hero_reference_images
- content_reference_images
- logo_image
- locked_assets

If the user provides mappings, honor them before inference.

If not provided, infer appropriate roles from the available references.

Per-image design usage may be:
- palette_source
- motif_source
- texture_source
- composition_source
- shape_source
- atmosphere_source
- silhouette_source
- reference_only
- locked_asset
- bind_to_slot
- prohibited

Using an image as design material does not mean placing it literally. Extract or reinterpret permitted visual qualities unless the user explicitly requests compositing or binding.

## Header Designer

Header should resemble an editorial masthead or institutional publication header, not a blank rectangle.

Possible archetypes:
- Institutional Masthead
- School Newsletter
- Government Formal
- News Bulletin
- Magazine Masthead
- Editorial Ribbon
- Split Identity
- Hero-integrated Header
- Corporate Editorial
- Ceremonial Header

Header may reserve space for:
- logo
- organization
- title
- subtitle
- issue/date/category metadata

Never invent factual text.

## Footer Designer

Footer should visually close the page and connect back to the Header/Background.

Possible archetypes:
- Editorial Info Bar
- Institutional Signature
- News Footer
- Source Bar
- Contact Footer
- QR / CTA Footer
- Ribbon Closure
- Minimal Accent Footer

Never invent factual source/contact information.

## Hero Section

Hero Section is ENABLED by default.

Disable only when the user explicitly requests no Hero.

Parameters:
- hero_section = ENABLED | DISABLED
- hero_slot_count = AUTO | integer

Hero normally carries the strongest visual weight and precedes the Masonry Content.

## Balanced Masonry Engine

The Content Section defaults to **balanced_masonry**.

It must create exactly the requested number of empty image panels when the user supplies image_panel_count.

Masonry quality goals:
- optical balance rather than rigid mathematical symmetry
- consistent gutters
- controlled variation in panel size/aspect
- stable overall silhouette
- rhythmic large/medium/small progression
- no awkward dead gaps
- no visually heavy side
- coherent editorial flow
- Hero remains dominant when enabled

Stable IDs:
- M01..MNN = Masonry image panels

## Panel Frame Engine

Each Masonry panel is a reusable image placeholder.

Default:
```text
panel_frame_mode = THEMED_FRAME
```

THEMED_FRAME means:
- create a decorative image frame appropriate to the template theme
- frame shape, corner treatment, border language, inset, shadow, ornament, accent, and motif must harmonize with the Editorial Shell
- decoration must remain restrained enough that inserted photos will still dominate
- frame styles may vary subtly across the masonry while remaining one family
- frame geometry must clearly indicate the exact image-placement area

User may disable decorative frames:

```text
panel_frame_mode = PLAIN_GUIDE
```

PLAIN_GUIDE means:
- no decorative frame
- show only a thin neutral or theme-coordinated outline
- preserve panel bounds clearly so the user knows where to place the image
- do not add heavy cards, ornaments, shadows, or visual clutter

The panel must remain EMPTY in both modes.

Optional:
- panel_content_mode = IMAGE_ONLY | IMAGE_WITH_CAPTION
Default = IMAGE_ONLY

## Optical Balance

Apply optical balance to:
- Header composition
- Hero-to-content proportion
- Masonry panel distribution
- Footer closure
- overall page weight

Mathematical symmetry is optional; perceptual balance is required.

## Preserve-first policy

- Person / face → LOCKED identity
- Logo / emblem / QR / signature → LOCKED
- Product / uniform / identifiable object → STRICT
- Design reference → GUIDED or INSPIRATION_ONLY

Locked assets must never be blended, redrawn, distorted, recolored, or turned into textures unless the user explicitly authorizes a permissible transformation.

## Workflow

1. Normalize brief.
2. Resolve template type and preset.
3. Analyze all reference images.
4. Apply user Region Source Mapping.
5. Choose Editorial Shell style.
6. Select compatible Header/Footer/Background treatments.
7. Build shared motif and typography/color system.
8. Build Hero Section (enabled by default).
9. Resolve image_panel_count.
10. Build Balanced Masonry layout.
11. Apply THEMED_FRAME or PLAIN_GUIDE to panels.
12. Apply preservation rules and explicit asset bindings.
13. Run Optical Balance QA.
14. Compile Template Specification + Production-ready Template Prompt.

## Output

Return:
1. Design Interpretation
2. Region Source Map
3. Editorial Shell Specification
4. Hero Specification
5. Balanced Masonry Panel Map
6. Panel Frame Specification
7. Typography + Color + Motif System
8. Asset Preservation / Binding Rules
9. Production-ready Template Prompt
10. QA result

## Supporting references

Use:
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
