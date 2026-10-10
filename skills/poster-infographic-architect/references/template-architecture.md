# Canonical Template Architecture v0.7

## Structural invariant

```text
CANVAS
├── EDITORIAL_SHELL
│   ├── BACKGROUND_LAYER
│   ├── HEADER_REGION
│   ├── VISUAL_MOTIF_SYSTEM
│   └── FOOTER_REGION
└── CONTENT_BOX
    ├── HERO_SECTION                 [DEFAULT ENABLED]
    └── CONTENT_LAYOUT
        ├── MASONRY_CONTENT          [DEFAULT]
        └── BEFORE_AFTER_COMPARISON  [WHEN REQUESTED]
```

## Editorial Shell

Background, Header, Footer, typography, color language, and motif form a coordinated publication-style shell.

## Hero

Hero is enabled by default and disabled only through explicit user instruction.

Stable IDs:
- R01..RNN

## Masonry Content

Default multi-image content architecture.

Stable IDs:
- M01..MNN

## Before / After Comparison

Alternative content architecture when explicitly requested.

Default spatial contract:
- Before = left
- After = right
- visually equivalent comparison zones

Stable IDs:
- BA01-B / BA01-A
- BA02-B / BA02-A
- etc.

Each comparison panel remains an empty reusable image placeholder unless explicitly bound.

## Panel frames

Default:
- THEMED_FRAME

Optional:
- PLAIN_GUIDE

Both Masonry and Before/After panels follow the selected frame mode.

## Region references

Header/Footer/Background/Hero/Content may use separate user-designated reference sets.

Reference influence and literal placement are separate concepts.

## Reusability

A valid template:
- has a visually finished shell
- retains Hero by default
- provides a clear content layout
- keeps image areas empty and reusable
- remains visually balanced without inserted photos
