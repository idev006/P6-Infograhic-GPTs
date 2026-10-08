# QA Scoring v0.1

## Purpose

Review the compiled design and prompt before returning it to the user.

## Blocking failures

Any blocking failure requires revision before output.

Blocking conditions:
- unauthorized person identity change
- logo/emblem distortion or redesign
- QR regeneration when exact QR is required
- signature alteration
- official insignia alteration
- product identity redesign
- contradiction with explicit user instruction
- missing must_include item
- violation of must_preserve
- fabricated data presented as user data
- impossible section mapping caused by ignored constraints
- prompt contains mutually contradictory preservation rules

## Scored dimensions

Score each 0–10:

1. Objective Alignment
2. Audience Fit
3. Message Clarity
4. Information Hierarchy
5. Section Logic
6. Composition Coherence
7. Visual Hierarchy
8. Typography Readability
9. Color / Contrast Logic
10. Asset Mapping Accuracy
11. Preservation Compliance
12. Brand Integrity
13. Prompt Clarity
14. Generation Feasibility
15. Overall Professional Quality

## Acceptance thresholds

- Any blocking failure → FAIL
- Preservation Compliance < 9 → FAIL
- Brand Integrity < 8 when brand assets exist → FAIL
- Prompt Clarity < 8 → REVISE
- Overall Professional Quality < 8 → REVISE
- Average score >= 8 with no blocking failures → PASS

## Feedback loop routing

If Objective Alignment fails → L1
If Information Hierarchy fails → L3
If Section Logic fails → L4
If Asset Mapping fails → L5/L10
If Preservation fails → L5.5
If Art Direction fails → L6/L7
If Composition fails → L8
If Typography/Color fails → L9
If Prompt Clarity fails → L11

## Final QA checklist

Before output confirm:
- all user constraints represented
- canvas/orientation correct
- all supplied assets accounted for or intentionally unused
- protected assets have explicit preservation instructions
- hierarchy is clear
- section roles are coherent
- text is readable for viewing context
- no unnecessary decorative complexity
- final prompt is self-contained
