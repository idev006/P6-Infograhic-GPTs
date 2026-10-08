# Multi-Layer Blackbox Architecture

## Principle

The system must design before it writes the final image-generation prompt.

A linear prompt rewrite is insufficient for professional visual communication.

A second core principle is **preserve before transform**. User-supplied identity, brand, functional, and product assets must be classified before any creative modification is considered.

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
L5.5 Preservation Gate
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

For each asset identify:
- semantic role
- visual role
- target section
- priority
- likely protected characteristics
- required fidelity
- transformation permissions

## L5.5 — Preservation Gate

The Preservation Gate executes before Creative Strategy and Art Direction.

Its purpose is to prevent creative decisions from unintentionally altering protected user assets.

Classify each asset using:
- LOCKED
- STRICT
- GUIDED
- FLEXIBLE
- INSPIRATION_ONLY

Default classifications:
- Person / face → LOCKED identity
- Logo / emblem / QR / signature → LOCKED
- Product / uniform / identifiable object → STRICT
- Background / environment → GUIDED
- Style / mood reference → INSPIRATION_ONLY

The gate produces:
- protected_features
- allowed_transformations
- forbidden_transformations
- required prompt constraints

Explicit user permission may relax a default policy. Silence must not be interpreted as permission to transform protected characteristics.

## L6 — Creative Strategy

Develop a concept, visual metaphor, or communication device appropriate to the goal.

Avoid obvious or generic visual clichés when stronger concepts are available.

Creative concepts must work around protected assets, not rewrite them.

## L7 — Art Direction

Define:
- style
- mood
- tone
- visual language
- realism
- creative intensity

Art direction may change environment, lighting, graphics, or composition when permitted, but may not override Preservation Gate constraints.

## L8 — Composition & Spatial Layout

Define:
- grid
- focal point
- visual flow
- balance
- alignment
- negative space
- section proportions

Composition may crop or reposition assets only within allowed transformation rules.

## L9 — Visual System

Define:
- typography
- color roles
- iconography
- chart / diagram style
- illustration / photography treatment
- recurring shapes and graphic elements

The visual system must not recolor, redraw, distort, or reinterpret LOCKED assets.

## L10 — Asset-to-Section Mapping

Map each asset to its intended section and usage rule.

Explicit user mapping always wins over AUTO.

Mapping must preserve the asset's assigned preservation policy.

## L11 — Prompt Compiler

Compile the design into a structured production prompt.

Suggested prompt order:
1. Role
2. Project objective
3. Canvas & output
4. Creative concept
5. Reference image instructions
6. Asset preservation constraints
7. Subject / scene
8. Section architecture
9. Composition
10. Visual hierarchy
11. Typography
12. Content
13. Color system
14. Lighting / atmosphere
15. Graphic elements
16. Branding
17. Technical quality
18. Negative constraints
19. Final QA rules

For protected assets, the compiled prompt must state what must remain unchanged and what transformations are allowed.

## L12 — QA / Design Critic

Check:
- objective alignment
- content completeness
- reference compliance
- preservation compliance
- identity integrity
- functional asset integrity
- section logic
- visual hierarchy
- composition balance
- readability
- brand integrity
- prompt ambiguity
- generation feasibility

Any unauthorized identity or asset alteration is a blocking QA failure.

If QA fails, return to the responsible layer and revise before output.

## Feedback-loop model

The blackbox should not be purely linear.

Examples:
- Typography may force a composition revision.
- Long content may force information architecture changes.
- Asset conflicts may force layout or art-direction changes.
- A preservation conflict may force the concept to change instead of changing the asset.
- QA may send the workflow back to any prior layer.
