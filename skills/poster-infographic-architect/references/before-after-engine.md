# Before / After Comparison Engine v0.7

## Purpose

Create a clear, aesthetically balanced transformation comparison that lets the viewer compare the state before and after an activity, improvement, renovation, treatment, cleanup, process, or other change.

## Trigger

Activate when the user explicitly requests:
- Before / After
- before-and-after
- ก่อน / หลัง
- ก่อนและหลัง
- ก่อน-หลัง
- เปรียบเทียบก่อนทำกับหลังทำ
- เปรียบเทียบซ้ายขวา
- equivalent transformation-comparison intent

## Default layout

```text
BEFORE | AFTER
 LEFT  | RIGHT
```

Internal defaults:
- content_layout_type = BEFORE_AFTER
- comparison_orientation = LEFT_RIGHT
- before_position = LEFT
- after_position = RIGHT
- comparison_pair_count = 1 unless otherwise specified
- comparison_balance = OPTICAL_EQUIVALENCE
- comparison_frame_sync = MATCHED
- panel_frame_mode = THEMED_FRAME unless overridden

## Composition

For each pair:
- Before and After image apertures should use equal or perceptually equivalent area.
- Prefer matched aspect ratios.
- Use equal margins and synchronized frame treatment.
- Use a central divider, transition line, arrow, label bridge, or whitespace channel when it improves recognition.
- Do not add visual decoration that makes one side appear intentionally superior except where the user requests an expressive transformation treatment.

## Labels

Default labels may be:
- BEFORE / AFTER for English
- ก่อน / หลัง for Thai

If the user supplies exact labels, use them.

If the user asks for no labels:
- before_label = NONE
- after_label = NONE

Labels are navigational, not factual claims.

## Multiple pairs

Stable IDs:
- BA01-B = Before pair 1
- BA01-A = After pair 1
- BA02-B / BA02-A
- etc.

Recommended A4 portrait behavior:
- 1 pair: large left/right pair
- 2 pairs: two stacked left/right comparison rows
- 3 pairs: compact paired modules if still legible
- 4+ pairs: adapt density carefully; prefer repeated paired rows or paired masonry

Do not break visual pairing.

## Hero relationship

Hero remains enabled by default.

When a Hero is present:
- Hero stays above or otherwise dominant
- comparison occupies the remaining content area
- Hero may introduce the activity, not duplicate the Before/After pair

If the user wants the comparison itself to be the Hero, this is allowed by explicit instruction.

## Frame relationship

THEMED_FRAME:
- use the same frame family on both sides
- may use subtle BEFORE/AFTER accents while preserving equal visual weight

PLAIN_GUIDE:
- use matched thin outlines only

## Asset behavior

If actual Before/After photos are supplied only as references for template design, do not insert them unless explicit binding is requested.

If the user explicitly requests those images to populate the comparison, bind them to the corresponding Before/After panels.

## QA

Revise if:
- left/right roles are ambiguous
- default ordering is reversed
- panel areas are noticeably unequal without instruction
- frame treatment differs enough to bias the comparison
- visual pairing is broken
- labels collide with image apertures
- multiple pairs cannot be matched instantly
