# Parameter Specification v0.2

This file is the SSOT for template input behavior.

## Global rules
- Every parameter is OPTIONAL unless required by meaning.
- Missing values resolve to AUTO unless an explicit default is defined.
- Explicit user values override inference and defaults.
- Explicit slot counts must be honored whenever physically feasible.
- Preservation rules are never relaxed by omission.
- Do not ask for values that can be safely inferred.

## G00 — Preset Selection
- preset_id: AUTO | CUSTOM | P01..P30
- preset_name: derived or user label

Preset values are defaults only. Explicit user values override preset values. Reference images may influence EMPTY slot geometry but are not bound unless explicitly requested.

## G01 — Project & Communication
- template_type: AUTO | infographic | poster | one_page_report
- objective: string/enum
- topic: string
- target_audience: string
- communication_goal: string
- primary_message: string
- language: string/enum
- brand: string/object
- platform: string/enum
- viewing_context: string/enum

## G02 — Canvas & Output
- canvas_size: default A4
- width: default 210
- height: default 297
- unit: default mm
- aspect_ratio: derived
- orientation: default portrait
- output_medium: AUTO
- resolution: AUTO
- print_or_digital: AUTO

Supported presets:
A3, A4, A5, Letter, Legal, 1:1, 4:5, 3:4, 9:16, 16:9, custom.

## G03 — Template Structure & Slot Counts

### Page regions
- background_layer: AUTO
- header_region: ENABLED
- content_box: ENABLED
- footer_region: ENABLED

### Content Box children
- hero_section: ENABLED
- child_content_section: ENABLED

### User-configurable counts
- header_slot_count: integer >= 0 | AUTO
- hero_slot_count: integer >= 0 | AUTO
- child_slot_count: integer >= 0 | AUTO
- footer_slot_count: integer >= 0 | AUTO

### Optional slot definitions
- header_slots: array | AUTO
- hero_slots: array | AUTO
- child_slots: array | AUTO
- footer_slots: array | AUTO

Per-slot object:
- slot_id
- slot_index
- semantic_role
- content_type
- relative_size
- alignment
- priority
- asset_binding
- editable_state
- notes

content_type examples:
TEXT, TITLE, SUBTITLE, METADATA, NOTE, DISCLAIMER, CONTACT, IMAGE, LOGO, STATISTIC, CHART, ICON, QR, SOURCE, CTA, MIXED, AUTO

Header/Footer slots MAY use text-oriented content types. Empty-slot behavior still applies unless exact text is supplied or explicitly bound.

editable_state:
EDITABLE, FIXED, LOCKED

## G04 — Content Planning
- headline
- subheadline
- body_content
- key_message
- key_statistics
- content_blocks
- CTA
- source
- information_density: LOW | MEDIUM | HIGH | VERY_HIGH
- content_priority: PRIMARY | SECONDARY | SUPPORTING | OPTIONAL

Content values inform slot roles but do not change explicit slot counts.

## G05 — Art Direction
- style
- mood
- tone
- visual_language
- realism
- creative_intensity
- visual_complexity
- brand_personality

## G06 — Composition & Layout
- layout_type
- grid_system
- visual_flow
- focal_point
- balance
- alignment
- whitespace
- spatial_density
- section_ratio
- header_ratio
- content_box_ratio
- hero_ratio
- child_ratio
- footer_ratio
- reading_direction
- gutter
- outer_margin

## G07 — Visual System
- color_palette
- primary_color
- secondary_color
- accent_color
- typography_style
- headline_style
- body_style
- icon_style
- illustration_style
- chart_style
- graphic_elements

## G08 — Images & Assets
- images: array[0..12]
- logo
- QR
- signature
- chart
- diagram
- product_assets
- brand_assets

Per-asset:
- asset_id
- semantic_role
- visual_role
- target_section
- target_slot_id
- priority
- preservation_policy
- identity_preservation
- reference_fidelity
- protected_features
- allowed_transformations
- crop_permission
- modification_permission
- recolor_permission
- redraw_permission
- background_removal
- usage_instruction

Preservation:
LOCKED, STRICT, GUIDED, FLEXIBLE, INSPIRATION_ONLY

## G09 — Constraints & Output Control
- must_include
- must_preserve
- must_avoid
- forbidden_elements
- brand_constraints
- text_constraints
- image_constraints
- identity_constraints
- asset_integrity_constraints
- prompt_language
- prompt_detail_level
- target_image_model
- output_format: template_prompt | template_spec | both

## AUTO slot inference

When counts are AUTO:
- Poster: Header 1–2, Hero 1, Child 1–4, Footer 1–2
- Infographic: Header 1–2, Hero 1–2, Child 3–8, Footer 1–2
- One-page report: Header 1–3, Hero 1–2, Child 4–10, Footer 1–3

These are heuristics, not hard limits.

## Override precedence
1. Explicit user instruction
2. Explicit slot counts
3. Explicit slot definitions
4. Explicit asset binding
5. Preservation policy
6. Plugin specification
7. Intelligent inference
8. Defaults
