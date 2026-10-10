# User Mode Router v0.7

## Goal

Make the plugin usable by people with little or no design knowledge while preserving full professional control for advanced users.

## Modes

### AUTO — default

AUTO inspects the form of the request.

If the user writes normal conversational language, use EASY behavior.

If the user supplies explicit parameter names, structured settings, exact mappings, or technical controls, honor those values as ADVANCED controls.

Mixed requests are valid. Do not force the user to choose a mode first.

### EASY

EASY is designed for non-experts.

The user may say only what they naturally know, for example:
- what they are making
- how many photos they want
- whether there should be a main image
- whether they want frames
- which references should influence Header/Footer
- what general visual feeling they want

The engine must infer:
- template type
- preset
- shell style
- Header/Footer archetypes
- background system
- typography hierarchy
- masonry geometry
- frame treatment
- optical balance

Do not ask for an internal parameter when a safe inference is possible.

Ask only when ambiguity materially changes the outcome or creates preservation risk.

### ADVANCED

ADVANCED supports direct parameter control.

Users may specify:
- preset_id
- editorial_shell_style
- header_reference_images
- footer_reference_images
- background_reference_images
- hero_section
- hero_slot_count
- content_layout_type
- image_panel_count
- comparison_pair_count
- panel_frame_mode
- panel_content_mode
- asset bindings
- preservation policies
- grid/spacing/typography/color instructions

## Natural-language normalization examples

"ทำแบบวารสารของหน่วยงาน"
→ editorial_shell_style = INSTITUTIONAL or NEWS_MAGAZINE based on context

"วารสารโรงเรียน"
→ editorial_shell_style = SCHOOL_NEWSLETTER

"มีภาพหลักหนึ่งภาพ"
→ hero_section = ENABLED
→ hero_slot_count = 1

"ไม่เอาภาพหลัก"
→ hero_section = DISABLED

"มีภาพกิจกรรม 6 รูป"
→ image_panel_count = 6

"ไม่ต้องทำกรอบรูป"
→ panel_frame_mode = PLAIN_GUIDE

"ใช้รูป 1 กับ 2 ทำหัว"
→ header_reference_images = [1,2]

"รูป 9 คือโลโก้"
→ logo_image = 9
→ preservation = LOCKED

"ทำก่อนหลังให้เทียบกัน"
→ content_layout_type = BEFORE_AFTER
→ orientation = LEFT_RIGHT
→ Before = LEFT
→ After = RIGHT

## EASY output discipline

Do not dump full internal parameter blocks by default.

Show:
1. concise interpretation
2. key choices the user cares about
3. final template prompt/spec

Expose full parameters only if the user asks.

## ADVANCED output discipline

May show:
- normalized parameters
- region mapping
- panel map
- comparison map
- shell archetypes
- QA results

## Error prevention

Never assume a user has to understand design terminology.

Prefer understanding intent over requiring syntax.
