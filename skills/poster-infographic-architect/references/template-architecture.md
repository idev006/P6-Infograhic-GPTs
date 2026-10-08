# Canonical Template Architecture v0.2

## Structural invariant

Every generated template follows this semantic tree unless the user explicitly disables a region:

```text
CANVAS
├── BACKGROUND_LAYER
├── HEADER_REGION
│   └── HEADER_SLOT[0..N]
├── CONTENT_BOX
│   ├── HERO_SECTION
│   │   └── HERO_SLOT[0..N]
│   └── CHILD_CONTENT_SECTION
│       └── CHILD_SLOT[0..N]
└── FOOTER_REGION
    └── FOOTER_SLOT[0..N]
```

## Slot semantics

A slot is a bounded placeholder with an ID, role, accepted content type, relative size, and editability state.

Stable IDs:
- H01..HNN Header
- R01..RNN Hero
- C01..CNN Child
- F01..FNN Footer

## User control

The user can set each slot count independently.

Example:
```text
header_slot_count = 2
hero_slot_count = 1
child_slot_count = 6
footer_slot_count = 2
```

The engine must create exactly those counts unless the user changes them.

## Background

Background is global and uncounted. It may contain visual treatment or a GUIDED reference image but must support foreground readability.

## Content Box

Content Box is the main interior workspace. It always owns Hero and Child sections.

Hero should normally receive greater visual weight. Child Content provides modular repeatable units.

## Template versus content

The template defines places and roles. It should not invent final business facts, names, statistics, or copy.

Placeholder labels may be used for clarity, for example:
- [LOGO]
- [MAIN HEADLINE]
- [HERO IMAGE]
- [KEY STATISTIC]
- [CHILD CONTENT 01]
- [QR]
- [SOURCE]

## Reusability

A good template:
- preserves consistent grid and rhythm
- has clear slot boundaries
- supports content replacement
- separates locked brand assets from editable content
- can be reused without redesigning the page architecture
