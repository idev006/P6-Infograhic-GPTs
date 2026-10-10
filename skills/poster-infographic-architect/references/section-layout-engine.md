# Section & Layout Engine v0.6

## Page hierarchy

```text
PAGE
├── BACKGROUND      ← auto-designed shell
├── HEADER          ← auto-designed shell
├── CONTENT BOX
│   ├── HERO        ← enabled by default
│   └── MASONRY     ← balanced image panels
└── FOOTER          ← auto-designed shell
```

## Hero

Default:
- enabled
- one dominant slot

Disable only if the user explicitly requests no Hero.

Typical A4 portrait Hero share:
- 22–45% of Content Box depending on density and panel count

## Balanced Masonry

Default child layout:
- balanced_masonry

Principles:
- consistent gutters
- controlled size variation
- mixed but compatible aspect ratios
- optical left/right weight balance
- stable outer silhouette
- no accidental dead space
- visual rhythm
- no excessively tiny orphan panel
- preserve readable margins
- adapt to exact requested panel count

The system may use portrait, landscape, square, tall, or wide panels as long as the overall composition remains harmonious.

## Panel Frame Engine

Default:
- THEMED_FRAME

THEMED_FRAME:
- derive border/mask/frame language from shell theme
- use restrained decorative treatment
- maintain a clearly visible image aperture
- keep visual priority below the photographs that will later be inserted
- use one frame family, with limited controlled variants if needed for masonry rhythm

PLAIN_GUIDE:
- thin boundary only
- no ornament
- no heavy card
- no shadow unless necessary for visibility
- maintain exact placement cue

## Editorial shell relationship

Header, Footer, Background and Panel Frame Engine should share:
- corner language
- line weight vocabulary
- motif
- accent shape
- color roles
- level of formality

Do not copy the same decoration everywhere; create family resemblance, not repetition.

## Region ratios

A4 portrait starting ranges:
- Header: 8–16%
- Content Box: 72–86%
- Footer: 5–11%

Within Content:
- Hero: 22–45%
- Masonry: remaining area

Ratios are adaptive.

## Quality rule

The final template must look attractive even before any photos are inserted.

Empty Masonry panels should read as deliberate photo frames/placeholders—not generic form fields.
