# Template QA Scoring v0.5

## Blocking failures

Revise before output if:
- Background is missing when not explicitly disabled
- Header is missing when not explicitly disabled
- Footer is missing when not explicitly disabled
- Background/Header/Footer are represented only as generic empty boxes instead of designed regions
- Hero slot count differs from explicit request
- Child slot count differs from explicit request
- Hero or Child lies outside Content Box
- reference images are inserted without explicit binding
- user-bound asset is mapped incorrectly
- unauthorized identity or brand alteration
- must_include or must_preserve is violated
- factual content is fabricated
- preservation or structural rules contradict one another

## Scored dimensions 0–10

1. Template Type Fit
2. Canvas Fit
3. Background Design Quality
4. Header Design Quality
5. Footer Design Quality
6. Region Hierarchy
7. Hero Slot Accuracy
8. Child Slot Accuracy
9. Grid Coherence
10. Hero Dominance
11. Child Modularity
12. Typography Scalability
13. Reference Use Quality
14. Preservation Compliance
15. Reusability
16. Template Prompt Clarity
17. Overall Professional Quality

## Acceptance

- any blocking failure → FAIL
- explicit Hero/Child count accuracy must be 10/10
- Background/Header/Footer Design Quality each < 8 → REVISE
- Preservation Compliance < 9 → FAIL
- Reusability < 8 → REVISE
- Overall Professional Quality < 8 → REVISE
- otherwise PASS

## Visual-form warning

If the result resembles a blank form because every region/slot uses identical outlined rectangles, REVISE the visual treatment before output.

## Final checklist

Confirm:
- Background visually spans/supports the page
- Header is visibly designed
- Footer is visibly designed
- Content Box contains Hero + Child
- Hero/Child slots match requested counts
- empty slots remain reusable
- reference images are influence-only unless explicitly bound
- prompt/spec is self-contained
