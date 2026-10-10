# Parameter Specification v0.7

## G00 — Interaction Mode

- user_mode: AUTO | EASY | ADVANCED
- default: AUTO

AUTO behavior:
- natural language → EASY behavior
- explicit technical parameters → ADVANCED handling for those values
- mixed input is supported

EASY mode:
- infer technical values
- minimize questions
- accept plain-language controls

ADVANCED mode:
- expose and honor detailed parameters

## G01 — Preset & Template

- preset_id: AUTO | CUSTOM | P01..P30
- template_type: AUTO | infographic | poster | one_page_report | newsletter | institutional_journal

## G02 — Canvas

- canvas_size: A4 default
- orientation: portrait default
- width
- height
- unit
- output_medium
- resolution

## G03 — Editorial Shell

Defaults:
- background_mode: AUTO_DESIGNED
- header_mode: AUTO_DESIGNED
- footer_mode: AUTO_DESIGNED
- editorial_shell_style: AUTO

editorial_shell_style:
AUTO, INSTITUTIONAL, SCHOOL_NEWSLETTER, NEWS_MAGAZINE, GOVERNMENT_FORMAL, MODERN_EDITORIAL, CORPORATE, CEREMONIAL

Optional:
- header_instruction
- footer_instruction
- background_instruction
- visual_motif_instruction

## G04 — Region Source Mapping

- header_reference_images
- footer_reference_images
- background_reference_images
- style_reference_images
- hero_reference_images
- content_reference_images
- logo_image
- locked_assets

usage_mode:
palette_source, motif_source, texture_source, composition_source, shape_source, atmosphere_source, silhouette_source, reference_only, locked_asset, bind_to_slot, prohibited

## G05 — Hero

- hero_section: ENABLED | DISABLED
- default: ENABLED
- hero_slot_count: AUTO | integer >= 0
- default: 1 unless preset/instruction indicates otherwise

Natural-language aliases:
- "ไม่เอาฮีโร่" / "ไม่มีภาพหลัก" → DISABLED
- "มีภาพหลัก 1 ภาพ" → ENABLED + 1

## G06 — Content Layout

- content_layout_type: AUTO | BALANCED_MASONRY | BEFORE_AFTER | GRID | EDITORIAL_GRID | CUSTOM
- default resolution: BALANCED_MASONRY unless user requests comparison

### Balanced Masonry
- image_panel_count: AUTO | integer >= 0
- panel_content_mode: IMAGE_ONLY | IMAGE_WITH_CAPTION
- masonry_balance: OPTICAL
- gutter: AUTO
- size_variation: CONTROLLED

### Before / After
- comparison_pair_count: integer >= 1 | AUTO
- comparison_orientation: LEFT_RIGHT | TOP_BOTTOM
- default: LEFT_RIGHT
- before_position: LEFT | TOP | RIGHT | BOTTOM
- default: LEFT
- after_position: RIGHT | BOTTOM | LEFT | TOP
- default: RIGHT
- before_label: AUTO | string | NONE
- after_label: AUTO | string | NONE
- comparison_divider: AUTO | ENABLED | DISABLED
- comparison_balance: OPTICAL_EQUIVALENCE
- comparison_frame_sync: MATCHED

Natural-language triggers:
- before and after
- before/after
- ก่อนและหลัง
- ก่อน-หลัง
- เปรียบเทียบซ้ายขวา
- เทียบก่อนทำกับหลังทำ

## G07 — Panel Frame

- panel_frame_mode: THEMED_FRAME | PLAIN_GUIDE
- default: THEMED_FRAME
- panel_frame_style: AUTO
- panel_corner_style: AUTO
- panel_border_weight: AUTO
- panel_inset: AUTO
- panel_shadow: AUTO
- panel_motif: AUTO

Natural-language aliases:
- "ไม่เอากรอบ" / "ไม่ต้องทำกรอบรูป" → PLAIN_GUIDE
- unspecified → THEMED_FRAME

All image panels remain empty unless explicitly bound.

## G08 — Art Direction

- style
- mood
- tone
- visual_language
- creative_intensity
- visual_complexity
- brand_personality
- typography_style
- color_palette

## G09 — Assets

- images: array[0..20]
- logo
- QR
- signature
- charts
- diagrams
- brand_assets

Preservation:
LOCKED, STRICT, GUIDED, FLEXIBLE, INSPIRATION_ONLY

Default logo/emblem/QR/signature = LOCKED.

## G10 — Output

- output_format: template_prompt | template_spec | both
- must_include
- must_preserve
- must_avoid
- forbidden_elements

## Override precedence

1. Explicit user instruction
2. Explicit advanced parameter
3. Explicit region-image mapping
4. Before/After request
5. Hero enable/disable
6. Explicit panel/pair count
7. Explicit panel_frame_mode
8. Explicit asset binding
9. Preservation policy
10. Preset
11. Plugin inference
12. Defaults
