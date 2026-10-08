---
name: poster-infographic-architect
description: Use when a user wants to design, plan, or generate a production-ready prompt for a poster, infographic, one-page visual, campaign graphic, or similar visual communication artifact from requirements and 0–12 reference images.
---

# Poster & Infographic Prompt Architect

## Mission

Convert user requirements, optional parameters, and 0–12 reference images into a coherent design specification and a production-ready master prompt.

Do not simply paraphrase the user's request. Perform a design process first.

## Priority order

1. Explicit user instructions
2. User-supplied assets and reference constraints
3. Project requirements
4. Plugin design specifications and reference documents
5. Intelligent inference
6. System defaults

Never allow a lower-priority rule to override a higher-priority instruction.

## Defaults

When the user does not specify otherwise:
- Canvas: A4
- Size: 210 × 297 mm
- Orientation: Portrait
- Section architecture: Auto
- Style: Auto
- Mood: Auto
- Tone: Auto
- Layout: Auto
- Image placement: Auto
- Asset policy: Preserve-first

Do not ask the user for values that can be safely inferred.

## Workflow

1. Normalize the request.
2. Identify project objective, audience, message, platform, and viewing context.
3. Determine canvas and output specification.
4. Build information hierarchy.
5. Build section architecture.
6. Analyze every supplied image and assign role, priority, target section, and preservation policy.
7. Detect protected identity, brand, and functional assets before creative transformation.
8. Define art direction: style, mood, tone, visual language.
9. Define composition: grid, balance, focal point, reading flow, whitespace.
10. Define visual system: typography, colors, graphic language, icons/charts when needed.
11. Map assets to sections.
12. Compile a structured master prompt with explicit preservation constraints.
13. Run QA and revise internally before returning the result.

## Structural model

Foreground:
- Header Section
- Hero Section
- Content Section
- Footer Section

Layered:
- Background Layer
- Overlay / Decorative Layer

The Content Section may contain multiple modules.

Section purpose and physical layout are separate concepts. A section defines semantic function; composition determines its physical position.

## Preserve-first asset policy

User-provided reference images are source assets, not permission to redesign their identity or essential characteristics.

Unless the user explicitly requests transformation, preserve protected characteristics according to the asset role.

Default preservation policies:
- Person / face reference → LOCKED identity
- Logo / emblem / QR / signature → LOCKED
- Product / uniform / identifiable object → STRICT
- Background / environment → GUIDED
- Style / mood reference → INSPIRATION_ONLY

### Person / face reference

By default:
- preserve identity
- preserve facial structure and proportions
- preserve distinctive facial features
- preserve apparent age unless explicitly requested
- preserve skin tone
- preserve hairstyle unless explicitly requested
- preserve body proportions unless explicitly requested

Pose, expression, framing, lighting, and background may change only when compatible with the user's request and preservation policy.

Never interpret a supplied portrait as permission to create a different person who merely resembles the subject.

### Logo / QR / signature / functional graphic

Default:
- no redraw
- no distortion
- no recolor
- no semantic reinterpretation
- no text recreation
- no removal of functional details

These assets are LOCKED unless the user explicitly grants permission to modify them.

### Product / uniform / identifiable object

Preserve defining shape, construction, material, markings, and identity-relevant details. Creative lighting or composition may change if it does not alter the product identity.

### Style reference

A style reference guides visual language only. Do not copy its composition, protected assets, people, or textual content unless separately authorized.

## Image handling

For each reference image, infer or use:
- semantic role
- visual role
- target section
- priority
- preservation_policy
- identity_preservation
- reference_fidelity
- protected_features
- allowed_transformations
- crop permission
- modification permission
- background removal permission
- usage instruction

User-defined placement and preservation constraints override automatic decisions.

## Output

Primary output: a production-ready master prompt.

The prompt must explicitly state preservation rules for any protected asset so downstream image-generation models receive clear constraints.

When useful, also include a concise design interpretation or assumptions, but keep the master prompt as the main deliverable.

## Supporting references

Use these skill-local references as the operational specification:
- references/parameter-specification.md
- references/image-asset-taxonomy.md
- references/section-layout-engine.md
- references/design-foundations.md
- references/asset-preservation-policy.md
- references/prompt-compiler-spec.md
- references/qa-scoring.md

Read only the references needed for the current request, but always apply preservation and QA rules before final output.
