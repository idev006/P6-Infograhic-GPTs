# Parameter Specification v0.6

## G00 — Preset

- preset_id: AUTO | CUSTOM | P01..P30
- template_type: AUTO | infographic | poster | one_page_report | newsletter | institutional_journal

## G01 — Canvas

- canvas_size: A4 default
- orientation: portrait default
- width/height/unit
- output_medium
- resolution

## G02 — Editorial Shell

Defaults:
- background_mode: AUTO_DESIGNED
- header_mode: AUTO_DESIGNED
- footer_mode: AUTO_DESIGNED
- editorial_shell_style: AUTO

editorial_shell_style:
- AUTO
- INSTITUTIONAL
- SCHOOL_NEWSLETTER
- NEWS_MAGAZINE
- GOVERNMENT_FORMAL
- MODERN_EDITORIAL
- CORPORATE
- CEREMONIAL

Optional overrides:
- header_instruction
- footer_instruction
- background_instruction
- visual_motif_instruction

## G03 — Region Source Mapping

- header_reference_images: array
- footer_reference_images: array
- background_reference_images: array
- style_reference_images: array
- hero_reference_images: array
- content_reference_images: array
- logo_image
- locked_assets: array

Per-image usage_mode:
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

Explicit mapping overrides inference.

## G04 — Hero

- hero_section: ENABLED | DISABLED
- default: ENABLED
- hero_slot_count: AUTO | integer >= 0
- default: 1 unless preset/instruction indicates otherwise

## G05 — Masonry Content

- child_layout_type: balanced_masonry | grid | editorial_grid | custom
- default: balanced_masonry
- image_panel_count: AUTO | integer >= 0
- panel_content_mode: IMAGE_ONLY | IMAGE_WITH_CAPTION
- default: IMAGE_ONLY
- masonry_balance: OPTICAL
- gutter: AUTO
- size_variation: CONTROLLED

Stable panel IDs:
- M01..MNN

When image_panel_count is explicit, panel count must match exactly.

## G06 — Panel Frame

- panel_frame_mode: THEMED_FRAME | PLAIN_GUIDE
- default: THEMED_FRAME
- panel_frame_style: AUTO
- panel_corner_style: AUTO
- panel_border_weight: AUTO
- panel_inset: AUTO
- panel_shadow: AUTO
- panel_motif: AUTO

THEMED_FRAME:
Design a decorative photo frame aligned with the template theme.

PLAIN_GUIDE:
Remove decorative framing and retain only a thin placement outline.

In all modes:
- panel remains empty
- no reference photo is inserted automatically

## G07 — Art Direction

- style
- mood
- tone
- visual_language
- creative_intensity
- visual_complexity
- brand_personality
- typography_style
- color_palette

## G08 — Assets

- images: array[0..20]
- logo
- QR
- signature
- charts
- diagrams
- brand_assets

Preservation:
- LOCKED
- STRICT
- GUIDED
- FLEXIBLE
- INSPIRATION_ONLY

Default:
- logo/emblem/QR/signature = LOCKED

## G09 — Output

- output_format: template_prompt | template_spec | both
- must_include
- must_preserve
- must_avoid
- forbidden_elements

## Override precedence

1. Explicit user instruction
2. Explicit region-image mapping
3. Hero enable/disable instruction
4. Explicit image_panel_count
5. Explicit panel_frame_mode
6. Explicit asset binding
7. Preservation policy
8. Preset
9. Plugin inference
10. Defaults
