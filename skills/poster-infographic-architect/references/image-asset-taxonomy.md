# Image & Asset Taxonomy v0.1

## Purpose

Define how 0–12 user-supplied images and visual assets are interpreted before design decisions.

## Semantic roles

- PERSON_FACE_REFERENCE
- FULL_BODY_REFERENCE
- PRODUCT_REFERENCE
- UNIFORM_REFERENCE
- LOGO
- EMBLEM
- QR_CODE
- SIGNATURE
- OFFICIAL_INSIGNIA
- BACKGROUND_REFERENCE
- LOCATION_REFERENCE
- STYLE_REFERENCE
- MOOD_REFERENCE
- COLOR_REFERENCE
- LAYOUT_REFERENCE
- DATA_REFERENCE
- CHART_REFERENCE
- DIAGRAM_REFERENCE
- TEXT_REFERENCE
- GENERIC_PROP
- OTHER

## Visual roles

- PRIMARY_HERO
- SECONDARY_HERO
- SUPPORTING_VISUAL
- BACKGROUND
- CONTENT_VISUAL
- BRAND_ASSET
- FUNCTIONAL_ASSET
- STYLE_GUIDE
- COLOR_GUIDE
- LAYOUT_GUIDE
- DATA_SOURCE

## Target sections

- HEADER
- HERO
- CONTENT
- FOOTER
- BACKGROUND
- OVERLAY
- GLOBAL
- AUTO

## Default preservation mapping

- PERSON_FACE_REFERENCE → LOCKED identity
- FULL_BODY_REFERENCE → LOCKED identity + STRICT body appearance
- PRODUCT_REFERENCE → STRICT
- UNIFORM_REFERENCE → STRICT
- LOGO → LOCKED
- EMBLEM → LOCKED
- QR_CODE → LOCKED
- SIGNATURE → LOCKED
- OFFICIAL_INSIGNIA → LOCKED
- BACKGROUND_REFERENCE → GUIDED
- LOCATION_REFERENCE → GUIDED; elevate to STRICT when exact identity matters
- STYLE_REFERENCE → INSPIRATION_ONLY
- MOOD_REFERENCE → INSPIRATION_ONLY
- COLOR_REFERENCE → GUIDED
- LAYOUT_REFERENCE → INSPIRATION_ONLY unless user requests close structural adherence
- DATA_REFERENCE → LOCKED factual meaning
- CHART_REFERENCE → STRICT data meaning, FLEXIBLE rendering unless exact reproduction requested
- DIAGRAM_REFERENCE → STRICT semantic relationships
- TEXT_REFERENCE → LOCKED wording when user says exact text
- GENERIC_PROP → FLEXIBLE

## Role inference rules

1. Prefer explicit user labels.
2. If a visible human is the subject and no role is specified, classify as PERSON_FACE_REFERENCE or FULL_BODY_REFERENCE.
3. If an asset is clearly a logo, QR, signature, or official insignia, classify as functional/identity-critical even if user does not label it.
4. A style reference must not silently become the source of subject identity or exact composition.
5. One asset may have multiple semantic roles, but one primary visual role should be selected.

## Multi-image conflict resolution

When two references conflict:
- explicit user priority wins
- LOCKED assets cannot be overwritten by GUIDED/FLEXIBLE references
- subject identity references outrank style references
- exact text/data constraints outrank aesthetic references
- unresolved noncritical conflicts may be normalized by the engine
- unresolved critical conflicts should be surfaced as an assumption in output rather than silently merged

## Fidelity levels

- MAXIMUM_PRACTICAL
- HIGH
- MEDIUM
- LOW
- INSPIRATIONAL

Default:
- LOCKED → MAXIMUM_PRACTICAL
- STRICT → HIGH
- GUIDED → MEDIUM
- FLEXIBLE → LOW/MEDIUM
- INSPIRATION_ONLY → INSPIRATIONAL

## Safe placement rule

When exact rendering of a functional asset is unreliable for the downstream image model, instruct the model to reserve a clean placement area and composite the original asset afterward.
