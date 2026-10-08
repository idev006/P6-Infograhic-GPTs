# Parameter Specification v0.1

This file is the SSOT for input parameter behavior.

## Global rules

- Every parameter is OPTIONAL unless marked otherwise.
- Missing values resolve to AUTO unless an explicit default is defined.
- Explicit user values always override AUTO and defaults.
- Invalid values should be normalized when intent is clear; otherwise fall back to AUTO.
- Preservation rules are never relaxed by omission.
- The engine should not ask for a value that can be safely inferred.

## G01 — Project & Communication

| Parameter | Type | Default | Notes |
|---|---|---|---|
| project_type | enum | AUTO | poster, infographic, one_page, campaign_graphic, social_graphic |
| objective | string/enum | AUTO | educate, inform, persuade, warn, sell, report, recruit, inspire |
| topic | string | required-by-meaning | Core subject |
| target_audience | string | AUTO | May include age, role, domain |
| communication_goal | string | AUTO | Desired communication effect |
| primary_message | string | AUTO | Single strongest message |
| language | enum/string | AUTO | Thai, English, bilingual, other |
| brand | string/object | AUTO | Organization or brand |
| platform | enum/string | AUTO | print, Facebook, LINE, web, presentation, other |
| viewing_context | enum | AUTO | distance, handheld, mobile, desktop, screen, social_feed |

## G02 — Canvas & Output

| Parameter | Type | Default |
|---|---|---|
| canvas_size | enum/string | A4 |
| width | number | 210 |
| height | number | 297 |
| unit | enum | mm |
| aspect_ratio | string | derived |
| orientation | enum | portrait |
| output_medium | enum | AUTO |
| resolution | string/number | AUTO |
| print_or_digital | enum | AUTO |

Supported presets include A3, A4, A5, Letter, Legal, 1:1, 4:5, 3:4, 9:16, 16:9, custom.

Dependency rules:
- preset canvas_size may derive width/height/aspect_ratio.
- explicit width/height overrides preset dimensions.
- explicit orientation overrides preset orientation while preserving size family.

## G03 — Content & Information

| Parameter | Type | Default |
|---|---|---|
| headline | string | AUTO |
| subheadline | string | AUTO |
| body_content | string/array | AUTO |
| key_message | string | AUTO |
| key_statistics | array | AUTO |
| content_blocks | array | AUTO |
| CTA | string | AUTO |
| source | string/array | AUTO |
| information_density | enum | AUTO |
| content_priority | object/array | AUTO |

information_density enum:
LOW, MEDIUM, HIGH, VERY_HIGH

content_priority:
PRIMARY, SECONDARY, SUPPORTING, OPTIONAL

## G04 — Section Architecture

| Parameter | Type | Default |
|---|---|---|
| header_section | section_state | AUTO |
| hero_section | section_state | AUTO |
| content_section | section_state | AUTO |
| footer_section | section_state | AUTO |
| background_layer | section_state | AUTO |
| overlay_layer | section_state | AUTO |
| content_modules | array | AUTO |

section_state:
AUTO, ENABLED, DISABLED, MERGED

Rules:
- sections describe semantic function, not fixed coordinates.
- content_modules may be reordered during information architecture.
- locked user placement cannot be moved automatically.

## G05 — Art Direction

| Parameter | Type | Default |
|---|---|---|
| style | string/enum | AUTO |
| mood | string/array | AUTO |
| tone | string/array | AUTO |
| visual_language | string | AUTO |
| realism | number/enum | AUTO |
| creative_intensity | number/enum | AUTO |
| visual_complexity | number/enum | AUTO |
| brand_personality | string/array | AUTO |

Suggested qualitative levels:
LOW, MEDIUM, HIGH or 0–100 when explicitly provided.

## G06 — Composition & Layout

| Parameter | Type | Default |
|---|---|---|
| layout_type | enum/string | AUTO |
| grid_system | string/object | AUTO |
| visual_flow | enum/string | AUTO |
| focal_point | string | AUTO |
| balance | enum | AUTO |
| alignment | string | AUTO |
| whitespace | enum/number | AUTO |
| spatial_density | enum | AUTO |
| section_ratio | object | AUTO |
| reading_direction | enum/string | AUTO |

Suggested layout_type:
editorial_grid, central_hero, split, z_pattern, f_pattern, diagonal, modular, data_led, full_bleed

balance:
symmetrical, asymmetrical, radial, dynamic

## G07 — Visual System

| Parameter | Type | Default |
|---|---|---|
| color_palette | array/string | AUTO |
| primary_color | string | AUTO |
| secondary_color | string | AUTO |
| accent_color | string | AUTO |
| typography_style | string | AUTO |
| headline_style | string | AUTO |
| body_style | string | AUTO |
| icon_style | string | AUTO |
| illustration_style | string | AUTO |
| chart_style | string | AUTO |
| graphic_elements | array | AUTO |

Rules:
- color choices must maintain readable contrast.
- typography must support the requested language.
- Thai typography must preserve marks, spacing, and legibility.

## G08 — Images & Assets

| Parameter | Type | Default |
|---|---|---|
| images | array[0..12] | [] |
| logo | asset | AUTO |
| QR | asset | AUTO |
| signature | asset | AUTO |
| chart | asset/array | AUTO |
| diagram | asset/array | AUTO |
| product_assets | array | AUTO |
| brand_assets | array | AUTO |

Per-asset object:
- asset_id: string
- semantic_role: enum/string
- visual_role: enum/string
- target_section: enum/string/AUTO
- priority: enum
- preservation_policy: enum
- identity_preservation: boolean/AUTO
- reference_fidelity: enum/0-100
- protected_features: array
- allowed_transformations: array
- crop_permission: enum/boolean
- modification_permission: enum/boolean
- recolor_permission: enum/boolean
- redraw_permission: enum/boolean
- background_removal: enum/boolean
- usage_instruction: string

preservation_policy:
LOCKED, STRICT, GUIDED, FLEXIBLE, INSPIRATION_ONLY

priority:
LOCKED, CRITICAL, HIGH, MEDIUM, LOW

Default policy by role:
- person/face → LOCKED identity
- logo/emblem/QR/signature → LOCKED
- product/uniform/identifiable_object → STRICT
- background/environment → GUIDED
- style/mood_reference → INSPIRATION_ONLY

## G09 — Constraints & Output Control

| Parameter | Type | Default |
|---|---|---|
| must_include | array | [] |
| must_preserve | array | [] |
| must_avoid | array | [] |
| forbidden_elements | array | [] |
| brand_constraints | array/object | AUTO |
| text_constraints | array/object | AUTO |
| image_constraints | array/object | AUTO |
| identity_constraints | array/object | AUTO |
| asset_integrity_constraints | array/object | AUTO |
| prompt_language | enum/string | AUTO |
| prompt_detail_level | enum | detailed |
| target_image_model | string | AUTO |
| output_format | enum/string | master_prompt |

prompt_detail_level:
concise, detailed, production

## Override precedence

1. Explicit user instruction
2. Explicit per-asset instruction
3. User-supplied project constraint
4. Preservation policy
5. Plugin specification
6. Intelligent inference
7. Defaults

## Interaction modes

Basic:
Expose only the essential 8–12 inputs.

Guided:
Expose approximately 20–30 inputs.

Pro:
Expose all parameters.

The internal schema is always the same regardless of interaction mode.
