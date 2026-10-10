# Section & Layout Engine v0.7

## Page hierarchy

```text
PAGE
├── BACKGROUND
├── HEADER
├── CONTENT BOX
│   ├── HERO              ← enabled by default
│   └── CONTENT LAYOUT
│       ├── BALANCED MASONRY
│       └── BEFORE / AFTER
└── FOOTER
```

## Hero

Default:
- enabled
- one dominant slot

Disable only by explicit request.

Typical A4 portrait Hero share:
- 20–42% of Content Box depending on layout and density

## Balanced Masonry

Default content layout unless the user requests comparison.

Rules:
- consistent gutters
- controlled size variation
- optical balance
- stable silhouette
- no accidental dead space
- no tiny orphan panel
- exact requested panel count

## Before / After Layout

Triggered by explicit transformation/comparison intent.

Default:
```text
orientation = LEFT_RIGHT
BEFORE = LEFT
AFTER = RIGHT
```

Design rules:
- two comparison zones should have equal or optically equivalent visual weight
- image apertures should be matched in scale/aspect where feasible
- use the same frame family on both sides
- central divider, arrow, transition line, or directional cue may be used when it improves clarity
- labels should be visually parallel
- preserve enough separation that users immediately perceive comparison
- do not let one side dominate unless explicitly requested
- do not fabricate explanatory copy

When multiple pairs are requested, use repeated paired modules while preserving a clear reading sequence.

A4 portrait options:
- one large left/right pair
- two stacked left/right pairs
- compact paired masonry for 3+ pairs only when readability remains high

## Panel Frame Engine

THEMED_FRAME is default for Masonry and Before/After.

PLAIN_GUIDE provides thin placement outlines only.

Before/After panels should use synchronized framing unless explicitly overridden.

## Editorial shell relationship

Header, Footer, Background, Masonry frames, and comparison frames should belong to one visual family.

## Quality rule

The empty template must already look intentionally designed before any user photos are inserted.
