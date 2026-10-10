# Balanced Masonry + Panel Frame Engine v0.6

## Purpose

Create a visually balanced image-placeholder composition in the Content Section.

This is not random Pinterest-style masonry. It is controlled editorial masonry optimized for optical harmony.

## Defaults

- child_layout_type = balanced_masonry
- image_panel_count = AUTO
- panel_content_mode = IMAGE_ONLY
- panel_frame_mode = THEMED_FRAME
- masonry_balance = OPTICAL
- gutter = AUTO
- size_variation = CONTROLLED

## Panel count

If the user requests N images/panels, create exactly N panels.

Each panel is empty until the user later places an image or explicitly binds one.

Stable IDs:
- M01..MNN

## Geometry

Permitted panel aspect families:
- square
- portrait
- landscape
- tall portrait
- wide landscape

Avoid extreme ratios unless reference content or user instruction requires them.

## Optical balance rules

- distribute large and small panels across the composition
- avoid concentrating all large panels on one side
- maintain consistent gutters
- minimize dead gaps
- avoid tiny orphan panels
- maintain a stable outer silhouette
- create visual rhythm
- preserve clear Hero dominance
- keep margins consistent with the shell

## Symmetry

Mathematical symmetry is not mandatory.

Required:
- perceptual balance
- stable visual weight
- coherent rhythm

## Panel Frame Engine

### THEMED_FRAME — default

Each panel is represented as a designed photo frame/place-holder matching the template theme.

Possible attributes:
- border shape
- corner treatment
- clipping mask
- inset
- theme accent
- subtle shadow
- ornament
- label notch
- editorial line treatment

Rules:
- future photo should remain the focal content
- frame must not be over-decorated
- all frames must belong to one visual family
- controlled variants may support different masonry shapes
- frame aperture must be unambiguous

### PLAIN_GUIDE

Used when the user asks to remove decorative frames.

Rules:
- retain thin visible outline
- no ornament
- no decorative shadow
- no heavy card background
- use neutral or theme-compatible guide line
- preserve exact panel placement

## Caption mode

IMAGE_ONLY:
- image aperture only

IMAGE_WITH_CAPTION:
- reserve a compact caption zone associated with the panel
- caption zone must not distort masonry rhythm

## QA

Reject/revise if:
- exact requested panel count is wrong
- panels visually collide
- gutters are inconsistent without design reason
- empty panels resemble generic form fields
- theme frames clash with Header/Footer
- decoration overwhelms future image content
- PLAIN_GUIDE still looks decorative
