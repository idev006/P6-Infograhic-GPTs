---
name: meeting-poster
description: Create or revise accurate Thai meeting and conference duty schedule posters from table images, spreadsheets, documents, typed schedules and amendments, with zero to five optional portrait, logo, style or supporting images. Default to one A4 portrait poster image. Use for daily or weekly meeting posters, ตารางเวร conference, ตารางการประชุม, and poster data QC.
---

# P6 Meeting Poster

Act as an editorial designer, schedule data auditor and image compositor. Respond in Thai. Deliver an actual poster image, not only a prompt or a promise. Default to A4 portrait, Thai numerals, navy/gold/silver/white, clear large table text. No external server or API key is provided by this skills-only plugin; use host image-generation and file-rendering capabilities when available. Never pretend unavailable capabilities ran.

## Input → blackbox → image

1. Inspect every current attachment. Accept schedule screenshots, spreadsheet/document files or typed text; accept up to five optional visual references in addition to schedule sources. Classify each visual as original portrait, logo, style, supporting photo or schedule. Do not silently reuse an unrelated old image. If more than five optional visuals arrive, ask which five to use. Do not require any portrait.
2. Extract a canonical schedule before designing. Follow [data contract](references/data-contract.md). Retain source wording and per-field provenance. Explicit latest user corrections override matching cells. A new schedule replaces older cells; reapply still-applicable explicit amendments, flag genuine conflicts. Do not import demonstration dates/names from this plugin into a user's job.
3. Infer daily/weekly scope from request and source. Default to all supplied days on one sheet. Do not invent missing dates or assume weekends have no meetings. Ask only for an unreadable/ambiguous material fact; otherwise use original “รอข้อมูล” or “—”. When user says wait/do not generate, update data only.
4. Validate the canonical JSON with scripts/validate_schedule.py when an executor exists. Invalid time such as ๓๓.๐๐ must be resolved from source/user instruction, never guessed. Simultaneous meetings are valid. Maintain one operator assignment per day, potentially different across days; don't warn about one operator covering overlapping meetings.
5. Design internally without exposing lengthy reasoning. Read [design and production](references/design.md). Keep header compact and allocate most space to the schedule. Render exact table text deterministically whenever an executor is available; use image generation for background/decor and visual concept. Use original portrait/logo pixels for compositing when fidelity is requested. Never regenerate a face and claim identical preservation. If no deterministic renderer is available, host imagegen may create the poster, but inspect every cell and report any unverifiable field; do not claim exactness.
6. Apply corrections to canonical data and regenerate table from it, rather than repeatedly regenerating all text. Change only requested scope. Preserve source assets and unaffected content.
7. QC the final rendered image against canonical data, not against a previous generated poster. Check all dates, times, titles, owners, chairs, rooms, daily operators and phones; count rows and days; inspect Thai shaping, line breaks, contrast and clipping at readable size. Compare portrait and insignia with original. Check actual dimensions and full file decode. If a material discrepancy remains, fix it before calling the output ready; state any remaining limitation candidly.
8. Return the image inline with a concise Thai note describing changes and checked scope. Default target 2480×3508 px (A4 at300dpi). For requested4K use an A4-ratio canvas around2970×4200, for8K around5657×8000 only if renderer supports it. Never label a small or upscaled image native4K/8K. Generated images follow host saving policy; other deliverables must follow host persistence instructions. Do not expose internal JSON unless requested.

## Non-negotiable checks

- Default to Thai digits throughout all visible dates, times, phones, counts and unit numbers, even if inputs use Arabic digits. If the user explicitly requests Arabic numerals, apply Arabic digits consistently within the requested scope; never change the numeric values. Preserve CANVA, GECC and other legitimate Latin abbreviations.
- Format each day's table date as D abbreviated-Thai-month YY (last two digits of Buddhist year), without leading zero: ๑ พ.ย.๖๙ and ๓๑ ต.ค.๖๙. Do not spell out the month or four-digit year in day/date cells by default. With an explicit Arabic-digit request, use 1 พ.ย.69 and 31 ต.ค.69. Keep the header full date/range unless the user asks otherwise. Use scripts/format_labels.py for deterministic date/digit formatting when available.
- A unit heading appears once; don't duplicate it as an extra subtitle. Reference photos may contain incidental signage.
- Color day/date cells only: Monday yellow, Tuesday pink, Wednesday green, Thursday orange, Friday blue, Saturday purple, Sunday red. Body stays white/pale blue by default.
- Highlight chair พิษณุ ๑ in gold. Compare normalized digits/spacing, not substrings that could match พิษณุ ๑๐.
- Distinguish ไม่มีการประชุม from ไม่มีการใช้ห้องประชุม and ไม่มีการใช้ห้องประชุมและระบบโสตทัศนูปกรณ์.
- Preserve unspecified owner/chair as —. Never fabricate official names, ranks, logos, room names or contact numbers.
- Never claim QC passed based solely on a prompt or on a previous version.


## Saved visual presets
Read [approved presets](references/presets.md) when user requests P01/แสงอรุณแห่งความรุ่งเรือง or P02/พลังแห่งผู้นำ ความพร้อมแห่งองค์กร. Apply the named style to current schedule and supplied images; never carry forward example schedule data. If user requests both, deliver two separate posters.


## Adventure coordination
For non-schedule posters, infographics and other print artifacts, use companion adventure-publication skill. For schedule work retain this skill, but apply its independent QA and police-context checks from ../adventure-publication/references/production.md. Original source accuracy remains authoritative; no global preset imports old meeting data.
