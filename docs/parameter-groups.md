# Parameter Groups

The parameter system is grouped for usability, documentation, UI design, and future schema implementation.

Users are not required to fill every parameter. Unspecified values default to AUTO unless a specific default is defined.

## G01 — Project & Communication

Defines what the work is and why it exists.

- project_type
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

Defines the physical or digital output space.

- canvas_size
- width
- height
- unit
- aspect_ratio
- orientation
- output_medium
- resolution
- print_or_digital

Default:
- A4
- 210 × 297 mm
- Portrait

Supported examples:
- A3 / A4 / A5
- Letter / Legal
- 1:1 / 4:5 / 3:4 / 9:16 / 16:9
- Custom width × height

## G03 — Content & Information

Defines text, facts, data, and message hierarchy.

- headline
- subheadline
- body_content
- key_message
- key_statistics
- content_blocks
- CTA
- source
- information_density
- content_priority

Internal hierarchy:
- Primary
- Secondary
- Supporting
- Optional

## G04 — Section Architecture

Defines semantic regions of the design.

Foreground:
- header_section
- hero_section
- content_section
- footer_section

Layers:
- background_layer
- overlay_layer

Nested:
- content_modules[]

Suggested states:
- AUTO
- ENABLED
- DISABLED
- MERGED

## G05 — Art Direction

Defines how the work should look and feel.

- style
- mood
- tone
- visual_language
- realism
- creative_intensity
- visual_complexity
- brand_personality

Important distinction:
- Style = visual appearance
- Mood = emotional feeling
- Tone = communication voice

## G06 — Composition & Layout

Defines spatial organization.

- layout_type
- grid_system
- visual_flow
- focal_point
- balance
- alignment
- whitespace
- spatial_density
- section_ratio
- reading_direction

Orientation and visual flow are separate:
- physical orientation: Portrait / Landscape / Square
- visual flow: top-down, Z-pattern, diagonal, central, editorial, etc.

## G07 — Visual System

Defines the design language shared across the whole artifact.

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

Supports 0–12 reference images plus structured assets.

- images[0..12]
- logo
- QR
- chart
- diagram
- brand_assets

Each image may contain:
- image_id
- semantic_role
- visual_role
- target_section
- priority
- reference_fidelity
- crop_permission
- modification_permission
- background_removal
- usage_instruction

Suggested priority:
- LOCKED
- CRITICAL
- HIGH
- MEDIUM
- LOW

## G09 — Constraints & Output Control

Defines hard requirements and final prompt behavior.

- must_include
- must_preserve
- must_avoid
- forbidden_elements
- brand_constraints
- text_constraints
- image_constraints
- prompt_language
- prompt_detail_level
- target_image_model
- output_format

## Interaction modes

### Basic
Expose approximately 8–12 parameters.

### Guided
Expose approximately 20–30 parameters.

### Pro
Expose the full schema.

The blackbox should fill omitted parameters intelligently rather than forcing the user to complete a long form.
