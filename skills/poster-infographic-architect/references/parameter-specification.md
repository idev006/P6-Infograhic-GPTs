# Parameter Specification v0.10

## G00 — Interaction
- user_mode: AUTO | EASY | ADVANCED
- design_cognition: REQUIRED
- art_direction_mode: AUTO | GUIDED | USER_DEFINED

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

## G02 — Template & Canvas
- preset_id: AUTO | CUSTOM | P01..P30
- template_type: AUTO | infographic | poster | one_page_report | newsletter | institutional_journal | magazine
- canvas_size: A4 default
- orientation: portrait default
- page_count: AUTO | integer >= 1
- width / height / unit / resolution

## G03 — Presentation Viability
- presentation_viability: REQUIRED
- minimum_photo_usability: HIGH | MEDIUM | LOW
- default: HIGH
- orientation_adaptation: AUTO
- page_count_adaptation: AUTO
- hero_compaction: AUTO
- density_guard: ENABLED
- real_photo_simulation: REQUIRED

## G04 — Art Direction
- creative_concept
- visual_hierarchy_plan
- editorial_shell_style
- typography_character
- color_strategy
- motif_strategy
- visual_density
- balance_strategy
- negative_space_strategy

## G05 — Editorial Shell
- background_mode: AUTO_DESIGNED
- header_mode: AUTO_DESIGNED
- footer_mode: AUTO_DESIGNED
- header_instruction
- footer_instruction
- background_instruction

## G06 — Region Source Mapping
- header_reference_images
- footer_reference_images
- background_reference_images
- style_reference_images
- hero_reference_images
- content_reference_images
- logo_image
- locked_assets

## G07 — Exact Asset Pipeline
For identity-critical assets:
- asset_render_policy: ORIGINAL_ASSET_ONLY | GENERATIVE_ALLOWED
- default for logo/emblem/QR/signature/official insignia: ORIGINAL_ASSET_ONLY
- asset_generation: FORBIDDEN by default
- asset_redraw: FORBIDDEN by default
- asset_style_transfer: FORBIDDEN by default
- asset_compositing: REQUIRED_WHEN_USED
- protected_clear_space: AUTO

## G08 — Logo Harmony
- logo_integration_mode: PRESERVE_AND_HARMONIZE
- logo_policy: LOCKED_100
- logo_placement_mode: DIGNIFIED_EDITORIAL
- shell_harmony_from_logo: ENABLED

## G09 — Hero
- hero_section: ENABLED | DISABLED
- default: ENABLED
- hero_slot_count: AUTO | integer >= 0
- hero_size_mode: AUTO | FULL | COMPACT
- viability may select COMPACT unless explicit user constraint forbids it

## G10 — Content Layout
- content_layout_type:
  AUTO | BALANCED_MASONRY | PAIRED_BALANCED_MASONRY | EDITORIAL_COLLAGE | BEFORE_AFTER | GRID | EDITORIAL_GRID | CUSTOM

Defaults:
- general multi-image → BALANCED_MASONRY
- multi-pair Before/After → PAIRED_BALANCED_MASONRY
- magazine/journal narrative → EDITORIAL_COLLAGE when advantageous

### Panel count
- image_panel_count: AUTO | integer >= 0
- comparison_pair_count: AUTO | integer >= 1
- panel_content_mode: IMAGE_ONLY | IMAGE_WITH_CAPTION

### Collage rules
- equal_size_grid_fallback: FORBIDDEN unless explicitly requested
- panel_size_variation: CONTROLLED
- gutter_consistency: REQUIRED
- optical_balance: REQUIRED
- minimum_aperture_viability: REQUIRED

### Before / After
- comparison_orientation: LEFT_RIGHT | TOP_BOTTOM | AUTO
- before_position: LEFT by default
- after_position: RIGHT by default
- comparison_pairing: EXPLICIT
- comparison_frame_sync: MATCHED

## G11 — Panel Frame
- panel_frame_mode: THEMED_FRAME | PLAIN_GUIDE
- default: THEMED_FRAME
- frame_family: AUTO
- frame_repetition: CONTROLLED
- form_field_appearance: FORBIDDEN
- decorative_overload: FORBIDDEN

## G12 — Assets & Preservation
Preservation levels:
LOCKED, STRICT, GUIDED, FLEXIBLE, INSPIRATION_ONLY

## G13 — Output
- output_format: template_prompt | template_spec | both
- critique_visibility: HIDDEN | SUMMARY | FULL

## Override precedence
1. Explicit user instruction
2. Identity / exact-asset integrity
3. Presentation viability
4. Explicit advanced parameter
5. Explicit region mapping
6. Before/After semantics
7. Hero requirements
8. Explicit counts
9. Frame mode
10. Preset
11. Art-direction inference
12. Defaults
