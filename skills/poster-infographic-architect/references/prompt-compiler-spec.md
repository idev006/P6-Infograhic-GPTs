# Template Prompt Compiler Specification v0.5

## Required output order

1. ROLE
2. TEMPLATE TYPE + PRESET
3. CANVAS & ORIENTATION
4. REFERENCE IMAGE INFLUENCE MAP
5. BACKGROUND DESIGN
6. HEADER DESIGN
7. PAGE GRID & MARGINS
8. CONTENT BOX
9. HERO SECTION + SLOT MAP
10. CHILD CONTENT SECTION + SLOT MAP
11. FOOTER DESIGN
12. VISUAL HIERARCHY
13. TYPOGRAPHY SYSTEM
14. COLOR SYSTEM
15. GRAPHIC LANGUAGE
16. ASSET BINDINGS
17. PRESERVATION CONSTRAINTS
18. EDITABILITY RULES
19. NEGATIVE CONSTRAINTS
20. FINAL TEMPLATE QA

## Mandatory declarations

Always state:
- hero_slot_count
- child_slot_count
- Header = AUTO-DESIGNED or explicit override
- Footer = AUTO-DESIGNED or explicit override
- Background = AUTO-DESIGNED or explicit override

For every Hero/Child slot:
- slot_id
- parent section
- semantic role
- allowed content type
- relative size/aspect behavior
- alignment
- priority
- asset binding if any
- editable state

## Region design requirement

The prompt must explicitly instruct the downstream model to render Header, Footer, and Background as finished visual regions—not empty placeholder boxes.

Header/Footer may reserve typographic or asset locations, but their containers, hierarchy, decoration, spacing, and visual treatment must be designed.

## Template language

Do not invent factual copy.

Use structural descriptions such as:
- "design a refined header with reserved title and logo positions"
- "design a compact footer system for source/contact/QR if later supplied"

## Reference handling

Default:
- analyze references
- use them to inform layout, colors, atmosphere, aspect ratios, and visual language
- do not place them into slots

Only BIND_TO_SLOT or FIXED_REGION_ASSET permits insertion.

## Negative constraints

Include as relevant:
- no generic blank header/footer boxes
- no background reduced to an unrelated border treatment
- no form-like repeated rectangles unless intentionally chosen
- no unintended image insertion
- no missing requested Hero/Child slots
- no distorted locked assets
- no fabricated final copy
