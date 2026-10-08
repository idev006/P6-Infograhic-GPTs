# Multi-Layer Blackbox Architecture

## Principle

The system must design before it writes the final image-generation prompt.

A linear prompt rewrite is insufficient for professional visual communication.

## Main pipeline

```text
USER INPUT
  ↓
L0 Input Normalization
  ↓
L1 Communication Strategy
  ↓
L2 Canvas & Output Specification
  ↓
L3 Information Architecture
  ↓
L4 Section Architecture
  ↓
L5 Reference / Asset Intelligence
  ↓
L6 Creative Strategy
  ↓
L7 Art Direction
  ↓
L8 Composition & Spatial Layout
  ↓
L9 Visual System
  ↓
L10 Asset-to-Section Mapping
  ↓
L11 Prompt Compiler
  ↓
L12 QA / Design Critic
  ↓
FINAL MASTER PROMPT
```

## L0 — Input Normalization

Convert free-form user input into structured project requirements.
Detect missing values and mark them AUTO.

## L1 — Communication Strategy

Identify:
- objective
- target audience
- primary message
- desired response
- CTA
- communication priority

## L2 — Canvas & Output Specification

Determine:
- document size
- aspect ratio
- orientation
- print/digital context
- viewing distance or device

Default: A4 portrait.

## L3 — Information Architecture

Transform raw content into a readable hierarchy.

Typical order:
Attention → Understanding → Detail → Action

## L4 — Section Architecture

Semantic structure:
- Header
- Hero
- Content
- Footer
- Background Layer
- Overlay Layer

Sections may be omitted, merged, or repositioned when justified.

## L5 — Reference / Asset Intelligence

Analyze 0–12 images.

Do not blend all images indiscriminately. Assign a distinct purpose to each asset.

## L6 — Creative Strategy

Develop a concept, visual metaphor, or communication device appropriate to the goal.

Avoid obvious or generic visual clichés when stronger concepts are available.

## L7 — Art Direction

Define:
- style
- mood
- tone
- visual language
- realism
- creative intensity

## L8 — Composition & Spatial Layout

Define:
- grid
- focal point
- visual flow
- balance
- alignment
- negative space
- section proportions

## L9 — Visual System

Define:
- typography
- color roles
- iconography
- chart / diagram style
- illustration / photography treatment
- recurring shapes and graphic elements

## L10 — Asset-to-Section Mapping

Map each asset to its intended section and usage rule.

Explicit user mapping always wins over AUTO.

## L11 — Prompt Compiler

Compile the design into a structured production prompt.

Suggested prompt order:
1. Role
2. Project objective
3. Canvas & output
4. Creative concept
5. Reference image instructions
6. Subject / scene
7. Section architecture
8. Composition
9. Visual hierarchy
10. Typography
11. Content
12. Color system
13. Lighting / atmosphere
14. Graphic elements
15. Branding
16. Technical quality
17. Negative constraints
18. Final QA rules

## L12 — QA / Design Critic

Check:
- objective alignment
- content completeness
- reference compliance
- section logic
- visual hierarchy
- composition balance
- readability
- brand integrity
- prompt ambiguity
- generation feasibility

If QA fails, return to the responsible layer and revise before output.

## Feedback-loop model

The blackbox should not be purely linear.

Examples:
- Typography may force a composition revision.
- Long content may force information architecture changes.
- Asset conflicts may force layout or art-direction changes.
- QA may send the workflow back to any prior layer.
