# Parameter Specification v0.8

## G00 — Interaction

- user_mode: AUTO | EASY | ADVANCED
- default: AUTO
- design_intelligence: REQUIRED
- art_direction_mode: AUTO | GUIDED | USER_DEFINED
- default: AUTO

## G01 — Project Understanding

- objective
- target_audience
- desired_outcome
- communication_goal
- primary_message
- formality
- emotional_tone
- context
- language
- must_include
- must_preserve
- must_avoid

Missing values are inferred when safe.

## G02 — Preset & Template

- preset_id: AUTO | CUSTOM | P01..P30
- template_type: AUTO | infographic | poster | one_page_report | newsletter | institutional_journal | magazine

## G03 — Canvas

- canvas_size: A4 default
- orientation: portrait default
- width
- height
- unit
- output_medium
- resolution

## G04 — Creative Concept & Art Direction

- creative_concept: AUTO | string
- visual_hierarchy_plan: AUTO | object
- editorial_shell_style: AUTO | INSTITUTIONAL | SCHOOL_NEWSLETTER | NEWS_MAGAZINE | GOVERNMENT_FORMAL | MODERN_EDITORIAL | CORPORATE | CEREMONIAL
- typography_character: AUTO
- color_strategy: AUTO
- motif_strategy: AUTO
- visual_density: AUTO | LOW | MEDIUM | HIGH | VERY_HIGH
- balance_strategy: OPTICAL | SYMMETRIC | ASYMMETRIC | AUTO
- negative_space_strategy: AUTO

## G05 — Editorial Shell

- background_mode: AUTO_DESIGNED
- header_mode: AUTO_DESIGNED
- footer_mode: AUTO_DESIGNED
- header_instruction
- footer_instruction
- background_instruction
- visual_motif_instruction

## G06 — Region Source Mapping

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

## G07 — Logo Harmony

- logo_integration_mode: PRESERVE_AND_HARMONIZE | PLACE_ONLY | USER_DEFINED
- default: PRESERVE_AND_HARMONIZE
- logo_policy: LOCKED_100
- logo_placement_mode: DIGNIFIED_EDITORIAL
- logo_clear_space: AUTO_PROTECTED
- logo_contrast_field: AUTO
- brand_integration_level: HIGH | MEDIUM | LOW
- default: HIGH
- shell_harmony_from_logo: ENABLED | DISABLED
- default: ENABLED

LOCKED_100 forbids redraw, recolor, crop, warp, stretch, compression, simplification, internal edits, texture use, or collage dissolution.

Shell harmony adapts environment around the logo, not the logo itself.

## G08 — Hero

- hero_section: ENABLED | DISABLED
- default: ENABLED
- hero_slot_count: AUTO | integer >= 0
- default: 1

## G09 — Content Layout

- content_layout_type: AUTO | BALANCED_MASONRY | BEFORE_AFTER | GRID | EDITORIAL_GRID | CUSTOM
- default: BALANCED_MASONRY unless comparison is requested

### Masonry
- image_panel_count: AUTO | integer >= 0
- panel_content_mode: IMAGE_ONLY | IMAGE_WITH_CAPTION
- masonry_balance: OPTICAL
- gutter: AUTO
- size_variation: CONTROLLED

### Before / After
- comparison_pair_count: AUTO | integer >= 1
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

## G10 — Panel Frame

- panel_frame_mode: THEMED_FRAME | PLAIN_GUIDE
- default: THEMED_FRAME
- panel_frame_style: AUTO
- panel_corner_style: AUTO
- panel_border_weight: AUTO
- panel_inset: AUTO
- panel_shadow: AUTO
- panel_motif: AUTO

## G11 — Assets & Preservation

- images: array[0..20]
- logo
- QR
- signature
- charts
- diagrams
- brand_assets

Preservation:
LOCKED, STRICT, GUIDED, FLEXIBLE, INSPIRATION_ONLY

Logo/emblem/QR/signature/official insignia default = LOCKED.

## G12 — Output

- output_format: template_prompt | template_spec | both
- critique_visibility: HIDDEN | SUMMARY | FULL
- default: SUMMARY in ADVANCED, HIDDEN in EASY

## Override precedence

1. Explicit user instruction
2. Explicit advanced parameter
3. Preservation / identity integrity
4. Explicit region-image mapping
5. Logo Harmony policy
6. Before/After request
7. Hero instruction
8. Explicit panel/pair count
9. Explicit frame mode
10. Explicit asset binding
11. Preset
12. Art Direction inference
13. Plugin defaults
