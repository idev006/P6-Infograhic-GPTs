# Template Presets v0.10

Global defaults:
- presentation_viability = REQUIRED
- Hero = ENABLED but adaptive
- panel_frame = THEMED_FRAME
- equal-size grid fallback = FORBIDDEN unless requested
- exact assets = ORIGINAL_ASSET_ONLY
- real-photo simulation = REQUIRED

## Content-layout mapping

General photo-led presets:
- favor BALANCED_MASONRY

Magazine / journal / visual-story presets:
- may favor EDITORIAL_COLLAGE

Before/After:
- 1 pair → paired comparison
- 2 pairs → paired comparison or paired masonry
- 3+ pairs → PAIRED_BALANCED_MASONRY by default

## P27 Before / After

Defaults:
- comparison_pair_count = 1
- Before left / After right
- panel_frame = THEMED_FRAME

Adaptive rules:
- 1–2 pairs: A4 Portrait usually viable with Hero
- 3 pairs: compact Hero or denser paired masonry
- 4–5 pairs: evaluate landscape or multi-page before accepting portrait single-page
- 4+ pairs in A4 Portrait single-page: never fall back to five identical thin rows solely to satisfy count

## P28 Meeting / Activity Summary

Default:
- Hero 1
- supporting images use BALANCED_MASONRY
- frame family is editorial, not form-like

## Override

Explicit user choice may force portrait/single-page, but QA must still preserve practical image usability and may warn about tradeoffs.
