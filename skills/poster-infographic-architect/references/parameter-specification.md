# Parameter Specification v0.5

## Global rules

- Missing values resolve to AUTO unless explicit defaults exist.
- Explicit user instructions override presets and inference.
- Header, Footer, and Background are system-designed by default.
- Hero and Child are the primary slot-based regions.
- Reference images do not populate slots automatically.
- Preservation rules are never relaxed by omission.

## G00 — Preset Selection

- preset_id: AUTO | CUSTOM | P01..P30
- preset_name: derived or user label

Preset values are starting points only.

## G01 — Project & Communication

- template_type: AUTO | infographic | poster | one_page_report
- objective
- topic
- target_audience
- communication_goal
- primary_message
- language
- brand
- platform
- viewing_context

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

## G03 — Region & Slot Architecture

System-managed defaults:
- background_mode: AUTO_DESIGNED
- header_mode: AUTO_DESIGNED
- footer_mode: AUTO_DESIGNED
- content_box: ENABLED

Primary user-facing slot controls:
- hero_slot_count: integer >= 0 | AUTO
- child_slot_count: integer >= 0 | AUTO

Advanced optional overrides:
- header_instruction: string/object | AUTO
- footer_instruction: string/object | AUTO
- background_instruction: string/object | AUTO

Do not require Header/Footer slot counts.

## G04 — Slot Definition

Optional:
- hero_slots: array | AUTO
- child_slots: array | AUTO

Per slot:
- slot_id
- slot_index
- semantic_role
- content_type
- relative_size
- aspect_behavior
- alignment
- priority
- asset_binding
- editable_state
- notes

Content types:
TEXT, TITLE, IMAGE, STATISTIC, CHART, ICON, QR, MIXED, AUTO

Stable IDs:
- Hero: R01..RNN
- Child: C01..CNN

## G05 — Content Planning

- headline
- subheadline
- body_content
- key_message
- key_statistics
- content_blocks
- CTA
- source
- information_density: LOW | MEDIUM | HIGH | VERY_HIGH

Exact supplied Header/Footer text may be used. Missing factual text must not be invented.

## G06 — Art Direction

- style
- mood
- tone
- visual_language
- realism
- creative_intensity
- visual_complexity
- brand_personality

## G07 — Composition & Layout

- layout_type
- grid_system
- visual_flow
- focal_point
- balance
- alignment
- whitespace
- spatial_density
- header_ratio
- content_box_ratio
- hero_ratio
- child_ratio
- footer_ratio
- reading_direction
- gutter
- outer_margin

## G08 — Images & Assets

- images: array[0..12]
- logo
- QR
- signature
- chart
- diagram
- product_assets
- brand_assets

Per asset:
- asset_id
- semantic_role
- reference_mode
- target_section
- target_slot_id
- priority
- preservation_policy
- protected_features
- allowed_transformations
- usage_instruction

reference_mode:
- REFERENCE_ONLY
- PLACEHOLDER_GUIDE
- BIND_TO_SLOT
- FIXED_REGION_ASSET

Default for ordinary reference images:
PLACEHOLDER_GUIDE

Default for logo:
REFERENCE_ONLY + LOCKED, unless user explicitly requests binding.

## G09 — Constraints & Output

- must_include
- must_preserve
- must_avoid
- forbidden_elements
- brand_constraints
- text_constraints
- image_constraints
- identity_constraints
- prompt_language
- prompt_detail_level
- target_image_model
- output_format: template_prompt | template_spec | both

## AUTO inference

Poster:
- Hero 1
- Child 1–4

Infographic:
- Hero 1–2
- Child 3–8

One-page report:
- Hero 1–3
- Child 4–10

Header/Footer/Background remain system-managed regardless of these counts.

## Override precedence

1. Explicit user instruction
2. Explicit Hero/Child slot counts
3. Explicit slot definitions
4. Explicit asset binding
5. Preservation policy
6. Preset
7. Plugin specification
8. Intelligent inference
9. Defaults
