# Presentation Viability Engine v0.10

## Purpose

Prevent structurally valid but practically unusable templates.

The engine evaluates whether the requested number of images, comparison pairs, Hero area, shell proportions, canvas and orientation can produce image apertures that remain meaningful in real presentation use.

## Required questions

Before layout:
- How much usable content area remains after Header/Footer?
- If Hero stays full-size, are supporting photos still legible?
- Are common 4:3, 3:2, portrait or landscape photos likely to crop acceptably?
- Can a senior viewer understand the image at normal print/screen size?
- Does comparison content remain visually comparable?
- Is a single page still the right format?

## Adaptation options

When viability is weak:
1. compact Hero
2. reduce decorative shell height
3. change orientation
4. change page count
5. change content architecture
6. reduce caption footprint
7. use paired/editorial collage
8. surface a concise tradeoff if user constraints prevent a strong solution

## Before/After guidance

Typical A4 Portrait:
- 1–2 pairs: usually viable
- 3 pairs: often viable with compact Hero
- 4–5 pairs: landscape or multi-page should be seriously considered

These are heuristics, not rigid limits.

## Blocking conditions

Reject a layout if:
- activity photos become thin banners
- subjects would be unreadably small
- comparison pairs cannot be distinguished
- image apertures exist only to satisfy count
- Hero/decorative shell consumes space needed for core evidence

## Output behavior

EASY mode should adapt automatically when safe.

If a user explicitly locks conflicting constraints, explain the tradeoff briefly and choose the least damaging compliant solution.
