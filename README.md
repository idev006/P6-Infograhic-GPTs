# P6-Infograhic-GPTs

> Working title: **Visual Prompt Architect**

A ChatGPT Plugin project for converting user requirements, optional reference images (0–12), and design parameters into production-ready prompts for professional posters and infographics.

## Project goal

Build a reusable ChatGPT Plugin that behaves like a multidisciplinary design team:
- Graphic Designer
- Information Designer
- Art Director
- Process Engineer
- Software Engineer
- Prompt Engineer
- QA / Design Critic

The plugin does **not** merely rewrite user text into a prompt. It performs a structured design process through a multi-layer blackbox, maps content and images to poster/infographic sections, and compiles a final master prompt.

## Core flow

User Input
→ Input Normalization
→ Communication Strategy
→ Information Architecture
→ Section Architecture
→ Asset / Image Intelligence
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
  roadmap.md
```

## Status

Initial architecture and specification phase.

## Repository

idev006/P6-Infograhic-GPTs
