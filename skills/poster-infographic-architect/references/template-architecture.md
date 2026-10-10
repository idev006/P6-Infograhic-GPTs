# Canonical Template Architecture v0.6

## Structural invariant

```text
CANVAS
├── EDITORIAL_SHELL
│   ├── BACKGROUND_LAYER
│   ├── HEADER_REGION
│   ├── VISUAL_MOTIF_SYSTEM
│   └── FOOTER_REGION
└── CONTENT_BOX
    ├── HERO_SECTION              [DEFAULT ENABLED]
    └── MASONRY_CONTENT_SECTION
        └── IMAGE_PANEL[1..N]
```

## Editorial Shell

The shell is a coordinated page identity system. Background, Header, Footer, motifs, typography, and color language must feel intentionally related.

The shell is designed even when content slots are empty.

## Hero

Hero Section is enabled by default and may be disabled only through explicit user instruction.

Stable IDs:
- R01..RNN

## Masonry Content

The standard image-content layout is Balanced Masonry.

Stable IDs:
- M01..MNN

When image_panel_count is explicit, create exactly that many panels.

Panels remain empty placeholders unless explicit binding is requested.

## Panel frames

Default:
- panel_frame_mode = THEMED_FRAME

THEMED_FRAME creates a reusable decorative photo frame whose visual language matches the shell.

Alternative:
- panel_frame_mode = PLAIN_GUIDE

PLAIN_GUIDE retains only a thin visible panel boundary for image placement.

Neither mode populates the panel with a reference image automatically.

## Region references

Header/Footer/Background may each use different user-designated reference image sets.

Reference role and literal image placement are separate concepts.

## Reusability

A valid template:
- has a visually finished shell
- has a default Hero unless disabled
- has clear empty image-placement panels
- has balanced masonry geometry
- allows photos to be replaced without redesigning the shell
