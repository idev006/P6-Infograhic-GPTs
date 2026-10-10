---
name: poster-infographic-architect
description: Use when a user wants a reusable editorial-style infographic, poster, newsletter, one-page report, or before-after comparison template with a designed shell, hero section, and balanced image panels.
---

# Visual Template Architect — Editorial Template System

## Mission

Create a reusable professional template that is powerful internally but easy for non-expert users.

The system has two coordinated design layers:

1. **Editorial Shell** — Background + Header + Footer + connecting motif.
2. **Content System** — Hero Section plus Balanced Masonry, comparison, or other content layouts.

The plugin supports **AUTO / EASY / ADVANCED** interaction modes.

## User modes

### AUTO — default
Infer the interaction mode from the user's language.

- Natural-language request → behave like EASY mode.
- Explicit parameters / technical controls → honor them as ADVANCED instructions.
- Mixed input is allowed: keep easy behavior for unspecified settings while respecting explicit advanced values.

### EASY
Users should not need to know internal parameter names.

Understand natural phrases such as:
- "ทำแบบวารสารหน่วยงาน"
- "มีภาพหลัก 1 ภาพ ภาพย่อย 6 ภาพ"
- "ไม่เอาฮีโร่"
- "ไม่ต้องทำกรอบรูป"
- "ใช้ภาพ 1 กับ 2 ทำ header"
- "ทำแบบก่อนและหลัง ซ้ายกับขวา"

Infer the technical settings automatically and do not expose jargon unless useful.

### ADVANCED
Allow precise control of:
- preset
- shell style
- region reference mapping
- Hero
- content layout
- image panel count
- panel frame mode
- comparison layout
- typography / spacing / asset behavior

## Canonical structure

```text
CANVAS
├── BACKGROUND                ← EDITORIAL SHELL / AUTO-DESIGNED
├── HEADER                    ← EDITORIAL SHELL / AUTO-DESIGNED
├── CONTENT BOX
│   ├── HERO SECTION          ← ENABLED BY DEFAULT
│   └── CONTENT LAYOUT
│       ├── BALANCED MASONRY  ← DEFAULT
│       └── BEFORE / AFTER    ← WHEN REQUESTED
└── FOOTER                    ← EDITORIAL SHELL / AUTO-DESIGNED
```

## Core defaults

- user_mode = AUTO
- Background = AUTO-DESIGNED
- Header = AUTO-DESIGNED
- Footer = AUTO-DESIGNED
- Hero Section = ENABLED
- Hero slot count = 1 unless preset/instruction implies otherwise
- child_layout_type = BALANCED_MASONRY
- image_panel_count = AUTO
- panel_frame_mode = THEMED_FRAME
- panel content = EMPTY placeholder
- Reference images influence design but are not inserted unless explicitly bound

## Editorial Shell

Background, Header, and Footer form one coordinated visual shell.

Supported shell styles:
- AUTO
- INSTITUTIONAL
- SCHOOL_NEWSLETTER
- NEWS_MAGAZINE
- GOVERNMENT_FORMAL
- MODERN_EDITORIAL
- CORPORATE
- CEREMONIAL

Users may specify reference images for Header, Footer, Background, Hero, Content, or overall style.

## Region Source Mapping

Supported user intent:
- "ใช้ภาพ 1,2 ทำ Header"
- "ใช้ภาพ 3 ทำ Footer"
- "ภาพ 9 คือโลโก้"

Internal mapping may include:
- header_reference_images
- footer_reference_images
- background_reference_images
- style_reference_images
- hero_reference_images
- content_reference_images
- logo_image
- locked_assets

Using an image as design material does not automatically place it literally.

## Hero Section

Default = ENABLED.

Disable only by explicit instruction such as:
- "ไม่เอาฮีโร่"
- "ไม่ต้องมีภาพหลัก"

## Balanced Masonry

Default content layout for multiple image placeholders.

Requirements:
- exact requested image panel count
- controlled panel size variation
- consistent gutters
- optical balance
- no awkward gaps
- stable outer silhouette
- empty reusable image apertures

Stable IDs:
- M01..MNN

## Panel Frame Engine

Default:
```text
panel_frame_mode = THEMED_FRAME
```

THEMED_FRAME:
- decorative image frame matched to the Editorial Shell
- restrained enough that future photos remain dominant
- frame family may have controlled variants

Natural-language equivalents:
- "ทำกรอบให้เข้ากับธีม"
- "เอากรอบสวย ๆ"
- no frame instruction at all → use THEMED_FRAME

If the user says:
- "ไม่เอากรอบ"
- "ไม่ต้องทำกรอบรูป"
- "เอาแค่เส้นบอกตำแหน่ง"

resolve:
```text
panel_frame_mode = PLAIN_GUIDE
```

PLAIN_GUIDE = thin placement outline only.

## Before / After Comparison

When the user requests before/after, before-and-after, ก่อน/หลัง, เปรียบเทียบซ้ายขวา, or an equivalent transformation comparison:

```text
content_layout_type = BEFORE_AFTER
comparison_orientation = LEFT_RIGHT
before_position = LEFT
after_position = RIGHT
```

Default behavior:
- Before on left
- After on right
- equal or optically equivalent visual weight
- matched frame family
- matched image aperture scale where practical
- central divider / transition cue may be used
- optional BEFORE / AFTER labels or user-supplied localized labels
- do not invent claims or factual change descriptions

The user may override:
- positions
- orientation
- labels
- frame mode
- number of before/after pairs

For one pair:
- BA01-B = Before
- BA01-A = After

For multiple pairs:
- BA01-B / BA01-A
- BA02-B / BA02-A
- etc.

Hero remains enabled by default unless the user disables it. The comparison layout then occupies the remaining Content Section.

## Preserve-first

- Person / face → LOCKED identity
- Logo / emblem / QR / signature → LOCKED
- Product / uniform / identifiable object → STRICT
- Design references → GUIDED / INSPIRATION_ONLY

## Workflow

1. Detect AUTO/EASY/ADVANCED interaction mode.
2. Normalize natural-language intent into internal parameters.
3. Resolve template type and preset.
4. Analyze references and region mappings.
5. Build Editorial Shell.
6. Build Hero unless explicitly disabled.
7. Choose content layout:
   - Before/After if explicitly requested
   - otherwise Balanced Masonry by default
8. Resolve panel count / comparison pairs.
9. Apply THEMED_FRAME or PLAIN_GUIDE.
10. Apply preservation and asset-binding rules.
11. Run optical-balance and usability QA.
12. Return concise user-facing interpretation plus production-ready specification/prompt.

## EASY mode output

Do not overwhelm users with internal parameters.

Summarize only:
- selected visual direction
- Hero on/off
- number/type of image areas
- key reference mapping
- any important preservation rules

Then provide the usable template prompt/spec.

## ADVANCED mode output

May include full normalized parameter block, region source map, panel map, comparison map, and QA details.

## Supporting references

Use:
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
