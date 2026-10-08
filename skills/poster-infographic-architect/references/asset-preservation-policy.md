# Asset Preservation Policy

## Core rule
**Preserve before transform.**

Supplying an image does not imply permission to redesign identity, branding, functional details, or defining characteristics.

## Policy levels
- LOCKED: no redesign/recolor/distortion/replacement without explicit permission.
- STRICT: preserve defining identity; allow presentation-level changes.
- GUIDED: preserve recognizable concept; controlled adaptation allowed.
- FLEXIBLE: strong guide with broader adaptation.
- INSPIRATION_ONLY: abstract guidance only.

## Default mapping
- Person / face → LOCKED identity
- Logo / emblem / QR / signature / official insignia → LOCKED
- Product / uniform / identifiable object → STRICT
- Background / environment → GUIDED
- Generic prop → FLEXIBLE
- Style / mood reference → INSPIRATION_ONLY

## Person / face
Protect identity, facial geometry, distinctive features, apparent age, skin tone, hairstyle/hairline, and identity-relevant body proportions.

Do not infer permission to create a look-alike, change age, skin tone, facial geometry, hairstyle, or body shape.

Compatible presentation changes may include pose, expression, crop, lighting, camera angle, and background.

## Functional assets
For logo, QR, signature, emblem:
- no redraw/regeneration
- no stretch/warp
- no recolor
- no text/symbol changes
- no QR module changes
- no signature-stroke changes

When exact generation is unreliable, reserve placement for later compositing of the original asset.

## Conflict resolution
1. Explicit user instruction wins.
2. Identity/functional integrity wins over aesthetic preference.
3. Change composition/environment/lighting/art direction before protected assets.
4. Apply only minimum necessary transformation.
5. Surface material ambiguity as an assumption.

## Prompt compiler
For each protected asset include ID, role, target section, preservation policy, protected features, allowed transformations, forbidden transformations, and fidelity.

## QA blocking failures
Reject unauthorized identity change, logo distortion, QR regeneration, signature alteration, official insignia alteration, product redesign, unauthorized brand recolor, or contradictory preservation rules.

## Downstream limitation
Do not claim downstream models guarantee 100% face fidelity, pixel-perfect logos, functional QR codes, or exact signatures.
