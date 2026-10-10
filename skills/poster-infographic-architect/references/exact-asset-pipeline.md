# Exact Asset Pipeline v0.10

## Purpose

Guarantee that identity-critical assets are never intentionally regenerated as approximate graphics.

## Exact assets

Default exact assets:
- logo
- emblem
- official insignia
- QR
- signature

## Core rule

**Analyze for harmony; composite for fidelity.**

The generative design pass may inspect the exact asset to understand:
- color relationships
- geometry
- institutional character
- placement needs

But it must not recreate the asset.

## Pipeline

1. classify asset as ORIGINAL_ASSET_ONLY
2. inspect for shell-harmony cues
3. reserve protected placement area
4. design surrounding shell
5. composite supplied original asset without internal modification
6. compare final placement against source
7. fail QA if substitute/recreation appears

## Allowed transformations

Only presentation-level transformations that preserve exact content:
- proportional scaling
- translation/placement
- transparent-background compositing
- protected clear-space allocation

## Forbidden

- redraw
- inpainting/reconstruction
- recolor
- crop of actual mark
- perspective transform
- warp
- stretch/compress
- stylization
- glow/emboss/filter that changes mark appearance
- texture/pattern conversion
- hallucinated replacement

## Downstream limitation

If exact compositing cannot be performed in the target image-generation workflow:
- leave a clean reserved zone
- specify exact placement and scale behavior
- composite original asset in a later deterministic graphics step

Never claim an AI-rendered approximation is the original.
