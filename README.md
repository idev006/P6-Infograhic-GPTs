# P6-Infograhic-GPTs

> Working title: **Visual Prompt Architect**

A ChatGPT Plugin project for converting user requirements, optional reference images (0–12), and design parameters into production-ready prompts for professional posters and infographics.

## Project goal

Build a reusable ChatGPT Plugin that behaves like a multidisciplinary design team:
- Senior Software Engineer
- Senior Process Engineer
- Senior Prompt / Loop Engineer
- Senior Graphic Designer
- Senior Infographic / One-page Report Designer
- Information Designer
- Art Director
- QA / Design Critic

The plugin does **not** merely rewrite user text into a prompt. It performs a structured design process through a multi-layer blackbox, maps content and images to poster/infographic sections, protects user-supplied identity and brand assets, and compiles a final master prompt.

## Core principles

1. Design before prompt compilation.
2. Preserve before transform.
3. Explicit user instructions override inference and defaults.
4. Section semantics and physical layout are separate.
5. Each reference image receives an explicit role.
6. QA blocks unauthorized changes to protected assets.

## Core flow

User Input
→ Input Normalization
→ Communication Strategy
→ Information Architecture
→ Section Architecture
→ Asset / Image Intelligence
→ Preservation Gate
→ Art Direction
→ Composition & Layout
→ Visual System
→ Prompt Compiler
→ QA / Critic
→ Final Master Prompt

## Default document

- Canvas: A4
- Orientation: Portrait
- Size: 210 × 297 mm
- All defaults are overrideable by explicit user parameters.

## Primary structural model

Foreground sections:
- Header
- Hero
- Content
- Footer

Layered systems:
- Background Layer
- Overlay / Decorative Layer

Content may contain multiple modules inside the Content Section.

## Asset preservation defaults

- Person / face: identity LOCKED
- Logo / emblem / QR / signature: LOCKED
- Product / uniform / identifiable object: STRICT
- Background / environment: GUIDED
- Style / mood reference: INSPIRATION_ONLY

Silence is not permission to alter protected identity, brand, or functional features.

## Repository structure

```text
plugin.json
skills/
  poster-infographic-architect/
    SKILL.md
docs/
  architecture.md
  parameter-groups.md
  design-foundations.md
  asset-preservation-policy.md
  roadmap.md
```

## Status

Architecture and specification phase.

## Repository

idev006/P6-Infograhic-GPTs
