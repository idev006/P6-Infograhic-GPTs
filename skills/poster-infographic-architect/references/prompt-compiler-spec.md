# Prompt Compiler Specification v0.1

## Purpose

Compile design decisions into one production-ready prompt for a downstream image-generation model.

## Required output order

1. ROLE
2. PROJECT OBJECTIVE
3. OUTPUT CANVAS
4. COMMUNICATION STRATEGY
5. CREATIVE CONCEPT
6. REFERENCE ASSET MAP
7. PRESERVATION CONSTRAINTS
8. SECTION ARCHITECTURE
9. COMPOSITION & VISUAL FLOW
10. VISUAL HIERARCHY
11. SUBJECT / SCENE
12. TYPOGRAPHY SYSTEM
13. CONTENT TO RENDER
14. COLOR SYSTEM
15. GRAPHIC / DATA ELEMENTS
16. LIGHTING / ATMOSPHERE
17. BRANDING RULES
18. TECHNICAL QUALITY
19. NEGATIVE CONSTRAINTS
20. FINAL QA INSTRUCTIONS

## Compilation rules

- Use explicit, concrete language.
- Avoid contradictory adjectives.
- Do not repeat the same constraint in multiple conflicting ways.
- Put identity/asset preservation before stylistic transformation language.
- Separate exact text from descriptive art direction.
- Do not invent facts, statistics, logos, or institutional details.
- If text accuracy is critical, instruct exact wording and readable typography.
- If a downstream model is unreliable for QR/logo/signature fidelity, reserve placement for later compositing.

## Reference asset block template

```text
REFERENCE ASSET [ID]
Role:
Target:
Priority:
Preservation policy:
Preserve:
Allowed transformations:
Forbidden transformations:
Fidelity:
```

## Canvas block template

```text
Canvas:
Orientation:
Dimensions:
Aspect ratio:
Output medium:
Viewing context:
```

## Section block template

```text
HEADER:
Purpose:
Content:
Assets:

HERO:
Purpose:
Content:
Assets:

CONTENT:
Modules:
Assets:

FOOTER:
Content:
Assets:

BACKGROUND:
Treatment:

OVERLAY:
Treatment:
```

## Negative constraints

Include only relevant negatives such as:
- no clutter
- no malformed typography
- no logo distortion
- no unauthorized face changes
- no random icons
- no duplicated elements
- no unreadable text
- no inconsistent perspective

## Model adaptation

When target_image_model is known:
- adapt syntax and level of detail to that model
- preserve semantic requirements
- never weaken asset preservation constraints solely for model style

When unknown:
- use model-neutral professional prompt language.
