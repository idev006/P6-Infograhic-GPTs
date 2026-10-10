# Adaptive Collage & Masonry Engine v0.10

## Purpose

Create photo layouts that feel editorially composed and visually balanced while remaining practical for real image placement.

## Modes

### BALANCED_MASONRY
General-purpose multi-image editorial layout.

### PAIRED_BALANCED_MASONRY
Before/After or other paired-image content.

### EDITORIAL_COLLAGE
Narrative magazine/journal layout with stronger hierarchy and freer rhythm.

## Anti-grid invariant

For all three modes:

**Equal-size repetitive grids are forbidden unless explicitly requested.**

Do not satisfy image count by producing rows of identical rectangular boxes.

## Geometry

Use a controlled mixture of:
- landscape
- portrait
- square
- wide
- tall

Avoid extreme thin banners for ordinary photos.

## Panel hierarchy

Each composition should have:
- dominant panel(s)
- supporting panels
- rhythm between larger and smaller apertures

Not every panel must carry equal visual weight.

## Optical balance

Control:
- left/right weight
- top/bottom weight
- density
- color-neutral placeholder mass
- gutter rhythm
- outer silhouette

## Paired Masonry

Before/After pairs must remain discoverable immediately.

Possible structures:
- coordinated mirrored clusters
- paired modules with varied row heights
- dominant pair + supporting pairs
- staggered paired collage with clear alignment cues

Forbidden:
- five identical thin paired rows as a default
- unrelated Before/After geometry that obscures pairing

## Real-photo viability

Every aperture should accept a plausible real-world crop.

Prefer apertures broadly compatible with 4:3, 3:2, 1:1, or portrait ratios.

## Frame system

THEMED_FRAME should be a frame family, not identical double-line rectangles.

Use controlled variants such as:
- accent corner
- selective edge
- subtle inset
- theme mask
- asymmetric mat
- minimal depth

PLAIN_GUIDE = thin boundary only.

## Final rule

The composition should look intentional before photos are inserted and still look strong after real photos replace the placeholders.
