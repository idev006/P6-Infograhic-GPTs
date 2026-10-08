# Template QA Scoring v0.2

## Blocking failures

Any of these require revision:
- header slot count differs from explicit request
- hero slot count differs from explicit request
- child slot count differs from explicit request
- footer slot count differs from explicit request
- Hero or Child placed outside Content Box
- Background treated as a normal content slot
- user-bound asset mapped to the wrong slot
- unauthorized identity or brand alteration
- missing must_include item
- violation of must_preserve
- invented factual content represented as user content
- mutually contradictory slot or preservation rules

## Scored dimensions 0–10

1. Template Type Fit
2. Canvas Fit
3. Region Hierarchy
4. Slot Count Accuracy
5. Slot Role Clarity
6. Grid Coherence
7. Hero Dominance
8. Child Modularity
9. Footer Proportion
10. Background Support
11. Typography Scalability
12. Asset Mapping Accuracy
13. Preservation Compliance
14. Editability / Reusability
15. Template Prompt Clarity
16. Overall Professional Quality

## Acceptance

- any blocking failure → FAIL
- Slot Count Accuracy < 10 when user gave counts → FAIL
- Preservation Compliance < 9 → FAIL
- Template Prompt Clarity < 8 → REVISE
- Editability / Reusability < 8 → REVISE
- Overall Professional Quality < 8 → REVISE
- otherwise PASS

## Feedback routing

Structure/count failure → Template Architecture / Layout Engine
Asset failure → Asset Intelligence / Preservation
Visual hierarchy failure → Design Foundations / Layout
Prompt failure → Template Prompt Compiler

## Final checklist

Confirm:
- exact slot counts
- correct parent-child hierarchy
- Header / Content Box / Footer visible as intended
- Hero and Child both inside Content Box
- Background is page-level
- every slot has an ID and role
- user assets are either bound or intentionally unassigned
- template remains reusable and editable
- prompt/spec is self-contained
