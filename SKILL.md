---
name: ppt-deck-builder
description: End-to-end PowerPoint deck production skill for creating, rebuilding, or improving PPT/PPTX presentations from PDFs, reports, websites, spreadsheets, notes, images, screenshots, old PPTX decks, or rough user briefs. Use when the user asks to make a PPT, build a slide deck, convert source material into slides, redesign an existing deck, create a proposal/investor/report/brand/technical presentation, separate mixed image/text materials, recreate charts/tables, preserve factual images, generate slide outlines/design tokens, build PPTX files, or run final render/contact-sheet QA.
---

# PPT Deck Builder

## Core Rule

Treat PPT production as a design-and-evidence workflow, not summarization. Build the deck around the audience's judgment path, preserve source evidence, and verify the rendered slides before calling the work complete.

## Start Every Job

1. Define the production contract:
   - audience
   - use mode: presentation, read-ahead, sales, internal decision, investor, report, guideline
   - desired action after viewing
   - source files and source type
   - target slide count and appendix policy
   - brand constraints, required language, deadline, output formats
2. If source files exist, create a task output folder and run:

```bash
python3 scripts/init_deck_job.py --out-dir OUTPUT_DIR --title "Deck title" --audience "Audience" --target-slides 12
python3 scripts/check_toolchain.py
python3 scripts/validate_deck_job.py OUTPUT_DIR --phase draft
```

3. Read the relevant references:
   - [references/source-to-deck-workflow.md](references/source-to-deck-workflow.md) for source conversion.
   - [references/design-system-rules.md](references/design-system-rules.md) for slide roles, flow, typography, layout, and copy.
   - [references/asset-chart-rules.md](references/asset-chart-rules.md) for image/text separation, frame modes, chart/table decisions.
   - [references/qa-and-render.md](references/qa-and-render.md) before final delivery.
   - [references/opencrab-support.md](references/opencrab-support.md) only as optional supporting context when OpenCrab tools/packs are available.

## Production Workflow

1. Source inventory: extract all source text, tables, figures, screenshots, images, numbers, links, dates, and evidence traces into `source_inventory.json`.
2. Content atoms: split source material into `claim`, `evidence_text`, `metric`, `table`, `quote`, `image`, `screenshot`, `process`, `comparison`, `risk`, `ask`, and `source` atoms in `content_atoms.json`.
3. Deck archetype: choose one primary archetype before drafting slides.
4. Story map: reorder the material by audience judgment path in `story_map.md`.
5. Slide outline: create `slide_outline.json` with one role, one main claim, and one primary visual per slide.
6. Design tokens: create `design_tokens.json` with canvas, typography, color, margins, chart style, image frame rules, footer/source note behavior.
7. Asset plan: for mixed image/text sources, create `asset_manifest.json`, `image_decision_log.json`, `composition_plan.json`, and `frame_spec.json`.
8. Chart plan: for charts/tables, create `chart_rebuild_spec.json`; rebuild as native PPT objects when data or readable chart logic exists.
9. Validation gate: run `python3 scripts/validate_deck_job.py OUTPUT_DIR --phase draft` before build, then fix artifact errors.
10. PPTX build: create or edit the PPTX. Use `scripts/outline_to_pptx.py` as a scaffold when useful, then refine manually or with `python-pptx`.
11. Render QA: render PPTX to PDF/images, create `contact_sheet.jpg`, inspect it, repair failures, update `qa_report.md`, and run final validation.

## Required Artifacts

Core production artifacts:

- `source_inventory.json`
- `content_atoms.json`
- `story_map.md`
- `slide_outline.json`
- `design_tokens.json`
- `pptx_build_log.md`
- `qa_report.md`
- `contact_sheet.jpg`

Mixed image/text artifacts:

- `asset_manifest.json`
- `image_decision_log.json`
- `chart_rebuild_spec.json`
- `composition_plan.json`
- `frame_spec.json`
- `extracted_assets/`
- `rendered_source_pages/`
- `before_after_contact_sheet.jpg`

If the user only asks for a plan, do not fabricate completed artifacts. State which artifacts would be produced during execution.

## Non-Negotiable Decisions

- Do not paste a full mixed image/text page as a body slide image.
- Do not turn source paragraphs into slide bullets by line-wrapping. Rewrite as `claim + proof + implication`.
- Preserve factual images: product UI, logos, packaging, real people/place/event photos, legal/financial/audit evidence, maps, research figures, before/after evidence.
- Recreate charts/tables natively when source data, extracted tables, or readable values exist.
- Use `contain_panel` or `evidence_panel` for chart, table, UI, logo, document, and research evidence.
- Use generated/replacement imagery only for non-factual decorative or mood assets.
- Do not crop out faces, products, logos, UI controls, chart axes, legends, labels, footnotes, or source notes.
- Do not claim exact font sizes, object coordinates, grid geometry, or master layout values from screenshots alone.
- Do not mark a final PPTX complete without rendered visual QA unless the user explicitly requested only a draft/outline.
- Do not skip `validate_deck_job.py --phase final` before delivery unless the user explicitly asked for a conceptual plan only.

## Build Guidance

Prefer native PPT objects for:

- editable text
- simple diagrams
- tables
- charts
- timelines
- comparison matrices
- callouts and annotations

Preserve image files for:

- product/UI screenshots
- original logos and brand assets
- factual photos
- legal/financial/document evidence
- complex scientific plots, heatmaps, maps, and research figures when rebuilding would alter meaning

Use generated or replacement images only after recording the reason in `image_decision_log.json`.

## Validation Gate

Before claiming a deck is ready, run:

```bash
python3 scripts/validate_deck_job.py OUTPUT_DIR --phase final
```

For work in progress, run:

```bash
python3 scripts/validate_deck_job.py OUTPUT_DIR --phase draft
```

For mixed image/text sources, add `--require-mixed` after the source has been classified as mixed. If validation fails, repair the artifacts or report the blocking errors clearly.

## Final Response Contract

When finishing a PPT task, report:

- output PPTX/PDF/contact sheet paths
- source files used
- deck archetype and slide count
- major asset/chart decisions
- QA performed and remaining risks
- any skipped checks, with reason

If the work is blocked, report the exact missing input or unavailable tool and the safest next step.
