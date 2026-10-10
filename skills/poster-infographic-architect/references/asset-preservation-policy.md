# Asset Preservation Policy v0.10

## Core rule

**Preserve before transform. Exact assets are composited, not regenerated.**

## Exact identity assets

The following default to ORIGINAL_ASSET_ONLY:
- logo
- emblem
- official insignia
- QR
- signature

For these assets:
- generation = FORBIDDEN
- redraw = FORBIDDEN
- recolor = FORBIDDEN
- crop = FORBIDDEN unless user explicitly requests safe crop of surrounding transparent margin
- warp/stretch/compress = FORBIDDEN
- style transfer = FORBIDDEN
- texture/pattern use = FORBIDDEN
- collage dissolution = FORBIDDEN

Allowed:
- proportional scale
- position
- protected clear space
- placement on a suitable contrast field
- direct compositing of original pixels

If the downstream system cannot composite originals exactly, reserve the placement zone and leave the asset out for post-compositing.

## Person / face

LOCKED identity unless otherwise authorized.

## Product / uniform / identifiable object

STRICT.

## Preserve-and-Harmonize

**Preserve the logo. Harmonize the environment.**

Adapt shell, never logo identity.

## QA

Any generated substitute for an exact identity asset is a blocking failure, even if visually similar.
