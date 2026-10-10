# Logo Harmony Engine v0.8

## Core principle

**Preserve the logo. Harmonize the environment.**

The logo is not a styling surface. It is an identity anchor.

## Default mode

- logo_integration_mode = PRESERVE_AND_HARMONIZE
- logo_policy = LOCKED_100
- logo_placement_mode = DIGNIFIED_EDITORIAL
- logo_clear_space = AUTO_PROTECTED
- shell_harmony_from_logo = ENABLED

## LOCKED_100

Preserve exactly:
- geometry
- aspect ratio
- colors
- symbols
- internal text
- internal spacing
- mark-to-word relationship

Forbidden:
- redraw
- recolor
- crop
- warp
- stretch
- compress
- perspective distortion
- simplification
- stylization
- embossing/filtering that changes identity
- texture/pattern use
- collage dissolution

## Harmonization

Do not force the logo to match the template.

Adapt the shell around it through:
- compatible surrounding colors
- accent roles derived from or complementary to logo colors
- appropriate contrast field
- protected clear space
- typography character
- motif / shape language
- line weight
- geometry
- placement
- scale
- nearby whitespace

The surrounding design may echo compatible qualities of the logo, but never duplicate or distort the logo itself.

## Placement dignity

Logo placement should feel intentional and institutional.

Avoid:
- corner sticker appearance
- cramped placement
- decorative overlap
- low contrast
- excessive size
- token tiny size
- arbitrary rotation
- collision with title or imagery

## Integration with Header

The Header Designer should treat logo placement as part of masthead composition.

Possible relationships:
- logo + organization lockup
- logo anchored beside title block
- logo within protected identity field
- logo aligned to editorial grid
- logo separated by deliberate clear space

## Integration with Shell

Header, Footer, frame system, and motif may adapt to the logo's visual character.

Example:
- circular emblem → shell may use restrained arcs/rounded accents
- shield/crest → shell may use formal structured geometry
- strong institutional colors → use those as accent roles, not necessarily page-wide fills

## Downstream limitation

If a generative image model cannot guarantee exact logo fidelity:
- do not pretend that it can
- reserve a clean logo placement zone
- recommend compositing the original logo asset afterward

## QA

FAIL if:
- identity changes
- aspect ratio changes
- colors change
- any internal symbol/text changes
- logo is cropped or warped
- logo becomes decorative texture
- clear space is insufficient
- logo lacks readable contrast

REVISE if:
- logo looks pasted on
- shell visually fights the logo
- logo placement lacks hierarchy or dignity
