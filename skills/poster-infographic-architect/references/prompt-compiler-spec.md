# Template Prompt Compiler Specification v0.2

## Purpose

Compile decisions into a reusable template-generation prompt/specification for infographic, poster, or one-page report layouts.

## Required output order

1. ROLE
2. TEMPLATE TYPE
3. CANVAS & ORIENTATION
4. BACKGROUND LAYER
5. PAGE GRID & MARGINS
6. HEADER REGION
7. CONTENT BOX
8. HERO SECTION
9. CHILD CONTENT SECTION
10. FOOTER REGION
11. SLOT TABLE / SLOT MAP
12. VISUAL HIERARCHY
13. TYPOGRAPHY SYSTEM
14. COLOR SYSTEM
15. GRAPHIC LANGUAGE
16. REFERENCE ASSET BINDINGS
17. PRESERVATION CONSTRAINTS
18. EDITABILITY RULES
19. NEGATIVE CONSTRAINTS
20. FINAL TEMPLATE QA

## Mandatory slot declaration

Always state:
- header_slot_count
- hero_slot_count
- child_slot_count
- footer_slot_count

For every slot include:
- slot_id
- parent section
- slot index
- semantic role
- allowed content type
- relative size
- alignment
- priority
- asset binding if any
- editable/fixed/locked state

## Slot naming

Use stable IDs:
- H01, H02 ... for Header
- R01, R02 ... for Hero
- C01, C02 ... for Child
- F01, F02 ... for Footer

## Template language

Describe placeholders, not invented final content, unless the user supplied exact content.

Prefer:
"Reserve H01 for organization logo"

Do not invent:
"A police logo reading ..."

## Output formats

template_spec:
structured specification

template_prompt:
production-ready prompt for generating a blank or lightly labeled visual template

both:
return specification first, then compiled template prompt

## Negative constraints

Include relevant rules such as:
- no unintended extra slots
- no merged slots unless specified
- no missing requested slots
- no background competing with content
- no unreadable placeholder labels
- no distorted locked assets
- no accidental final-copy fabrication
