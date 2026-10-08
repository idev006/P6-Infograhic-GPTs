# Asset Preservation Policy

## Core rule

**Preserve before transform.**

A user-supplied image is a source asset, not permission to redesign identity, branding, functional details, or defining characteristics.

The plugin generates prompts. It must express preservation constraints clearly, but it must not claim that a downstream image model can guarantee 100% fidelity.

## Policy levels

### LOCKED
Use when identity or exact structure must remain unchanged.

Typical assets:
- person identity
- logo / emblem
- QR code
- signature
- official insignia

Default:
- no redraw
- no recolor
- no distortion
- no semantic reinterpretation
- no replacement

### STRICT
Preserve defining characteristics while allowing presentation-level changes.

Typical assets:
- products
- uniforms
- identifiable objects
- equipment
- vehicles

Allowed examples:
- lighting
- scale
- placement
- controlled crop
- background separation

### GUIDED
Preserve the recognizable concept while allowing controlled adaptation.

Typical assets:
- backgrounds
- environments
- locations

### FLEXIBLE
Use as a strong guide but allow substantial adaptation when compatible with the brief.

Typical assets:
- generic props
- supporting imagery

### INSPIRATION_ONLY
Use only for abstract visual guidance.

May influence:
- style
- mood
- color
- texture
- visual rhythm

Must not automatically copy:
- exact composition
- people
- logos
- text
- distinctive protected assets

## Default mapping

| Asset role | Default policy |
| --- | --- |
| Person / face | LOCKED identity |
| Logo / emblem | LOCKED |
| QR code | LOCKED |
| Signature | LOCKED |
| Official insignia | LOCKED |
| Product | STRICT |
| Uniform | STRICT |
| Identifiable object | STRICT |
| Background / environment | GUIDED |
| Generic prop | FLEXIBLE |
| Style / mood reference | INSPIRATION_ONLY |

## Person / face preservation

Default protected features:
- identity
- facial geometry
- distinctive facial features
- apparent age
- skin tone
- hairstyle / hairline
- body proportions when identity-relevant

Do not infer permission to:
- create a look-alike instead
- change age
- change skin tone
- beautify or redesign facial geometry
- change hairstyle
- change body shape

When compatible with the brief, presentation-level changes may include:
- pose
- expression
- crop
- lighting
- camera angle
- background

If style conflicts with identity, preserve identity over stylistic intensity unless the user explicitly says otherwise.

## Logo, QR, signature, emblem

Default prohibitions:
- redraw
- regenerate
- stretch
- warp
- recolor
- change text
- change symbols
- change QR modules
- change signature strokes

If an image-generation model cannot reproduce a functional asset exactly, prefer reserving space for later compositing of the original asset rather than inventing a replacement.

## Product / uniform / identifiable object

Protect:
- geometry
- proportions
- construction
- materials
- markings
- insignia
- critical colors
- identity-defining details

Do not simplify or redesign those details for aesthetic convenience.

## Conflict resolution

When creative goals conflict with preservation:

1. Explicit user instructions win.
2. Protected identity and functional integrity win over aesthetic preference.
3. Change composition, environment, lighting, or art direction before changing a protected asset.
4. Apply only the minimum transformation necessary.
5. If ambiguity is material, state the assumption in the compiled prompt.

## Prompt compiler requirements

For every protected asset, include:
- asset identifier
- role
- target section
- preservation policy
- protected features
- allowed transformations
- forbidden transformations
- fidelity requirement

Example:

```text
REFERENCE IMAGE 01 — PRIMARY PERSON
Policy: LOCKED identity
Use: Hero Section
Preserve: identity, facial geometry, skin tone, hairstyle, distinctive features
Allowed: pose, expression, crop, lighting, background integration
Forbidden: face redesign, age change, skin-tone change, look-alike replacement
Fidelity: maximum practical identity fidelity
```

## QA blocking failures

Reject and revise if the prompt permits:
- unauthorized identity change
- changed logo geometry
- regenerated QR code
- altered signature
- changed official insignia
- redesigned product identity
- unauthorized brand recoloring
- contradictory preservation instructions

## Downstream limitation

The plugin must not claim that:
- face identity can be guaranteed at 100%
- logos can always be generated pixel-perfectly
- generated QR codes will always remain functional
- signatures will remain exact

For exact functional assets, preferred production workflow:
1. generate the visual composition
2. reserve asset placement
3. composite the original locked asset afterward
