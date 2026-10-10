# Region Source Mapping v0.6

## Purpose

Allow users to control which supplied images influence Header, Footer, Background, Hero, or Content design.

## Region arrays

- header_reference_images
- footer_reference_images
- background_reference_images
- style_reference_images
- hero_reference_images
- content_reference_images
- locked_assets

## Per-image usage modes

- palette_source
- motif_source
- texture_source
- composition_source
- shape_source
- atmosphere_source
- silhouette_source
- reference_only
- locked_asset
- bind_to_slot
- prohibited

Multiple non-conflicting usage modes may apply to the same image.

## Precedence

1. explicit user region mapping
2. explicit usage_mode
3. locked-asset classification
4. semantic inference
5. generic style-reference fallback

## Important distinction

"Use image 2 for Header design" does not automatically mean:
- paste image 2 into Header
- crop image 2 into Header
- blend image 2 visibly into Header

It means the Header Designer may extract permitted design qualities unless the user explicitly requests literal compositing.

## Locked assets

Logo, emblem, QR, signature, and other identity-critical assets default to LOCKED.

Locked assets:
- may be positioned/scaled proportionally when explicitly bound
- may not be redrawn
- may not be recolored
- may not be stretched
- may not be used as a texture
- may not be dissolved into a collage

## Shared references

An image may support multiple regions if explicitly mapped.

When the same image supports Header and Footer, vary the interpretation to avoid obvious repetition.

Example:
- Header → motif_source + composition_source
- Footer → palette_source + silhouette_source

## Unmapped images

If the user provides images without region mapping, classify them automatically.

Do not ask a question unless ambiguity materially affects the design or asset safety.
