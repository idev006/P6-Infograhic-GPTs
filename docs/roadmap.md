# Implementation Roadmap

## Phase 0 — Repository initialization
Status: In progress

Deliverables:
- plugin manifest
- core skill
- architecture documents
- parameter groups
- design foundations

## Phase 1 — Specification v1

Create:
- full parameter schema with data types
- enums and AUTO behavior
- defaults and override rules
- image role taxonomy
- section model
- output prompt schema
- QA scoring model

## Phase 2 — Skill workflow v1

Expand SKILL.md and supporting references so the plugin can reliably:
1. accept free-form requirements
2. accept 0–12 reference images
3. normalize inputs
4. infer missing parameters
5. generate a design specification
6. compile the final prompt
7. self-review before output

## Phase 3 — Examples & Test Cases

Build a test suite containing:
- no-image poster
- one-image hero poster
- multi-reference infographic
- data-heavy infographic
- government communication poster
- social media 4:5
- A4 portrait
- A4 landscape
- conflicting references
- locked logo / locked identity asset

## Phase 4 — Plugin package validation

Validate:
- plugin.json
- skill discovery
- default prompts
- reference files
- naming conventions
- package structure

## Phase 5 — Private ChatGPT Plugin

Package as a standalone skills-first plugin and install privately for live testing.

## Phase 6 — Optional MCP / App layer

Only add MCP tools or interactive UI when they provide clear value.

Potential future capabilities:
- structured parameter form
- user presets
- brand guideline retrieval
- asset library retrieval
- prompt history
- export to JSON
- direct generation workflow

## Phase 7 — Public readiness

If required:
- branding
- icon
- submission metadata
- privacy review
- safety review
- examples
- listing copy
- reviewer instructions
