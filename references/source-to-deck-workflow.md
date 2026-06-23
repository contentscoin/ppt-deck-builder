# Source-To-Deck Workflow

## Purpose

Convert source material into a deck by redesigning the audience's judgment path.

## Intake Contract

Capture:

- `audience`
- `use_mode`
- `desired_action`
- `source_type`
- `target_length`
- `brand_constraints`
- `language`
- `output_formats`
- `appendix_policy`

## Source Inventory

Create `source_inventory.json`. Extract:

- headings and section path
- raw text
- tables
- figures
- screenshots
- images
- numbers and dates
- links and source URI
- page/slide/object trace
- confidence

Tool choices:

- PPTX: `python-pptx`, OOXML, optional `unstructured.partition_pptx`
- PDF/DOCX/HTML/Markdown: `unstructured` or structured parsers
- Spreadsheet: pandas/openpyxl
- Image/scans: OCR and rendered-page segmentation
- Existing PPT: slide inventory plus rendered contact sheet

## Content Atoms

Create `content_atoms.json`. Valid atom types:

| Atom | Use in deck |
| --- | --- |
| `claim` | claim slide, section opener, title claim |
| `evidence_text` | body, speaker note, appendix |
| `metric` | KPI, big number, chart |
| `table` | simplified table, chart, appendix |
| `quote` | quote slide |
| `image` | image hero, card, evidence panel |
| `screenshot` | product demo, annotated screenshot |
| `process` | timeline/process slide |
| `comparison` | matrix or before/after |
| `risk` | risk/assumption slide |
| `ask` | next steps, budget, decision request |
| `source` | source note, methodology, appendix |

Every atom needs a `source_trace`. Numbers, quotes, legal/financial claims, and factual images cannot enter body slides without trace.

## Archetype Selection

Choose one primary archetype:

- `investor_pitch`: cover -> thesis -> problem -> market/timing -> solution -> product -> traction -> model -> team -> financials -> ask
- `trend_report`: cover -> executive summary -> methodology -> key findings -> chapters -> data -> examples -> implications -> sources
- `brand_guideline`: cover -> principles -> logo/color/type -> imagery -> layout/components -> applications -> do/don't -> asset index
- `financial_update`: cover -> safe harbor/context -> highlights -> KPI -> product/customer -> financials -> outlook -> appendix
- `agency_portfolio`: cover -> positioning -> capabilities -> process -> case studies -> team/proof -> next steps
- `technical_guide`: cover -> overview -> principles -> rules -> annotated examples -> edge cases -> checklist -> appendix

## Story Map

Create `story_map.md`:

- section title
- section claim
- required evidence atoms
- visual strategy
- slide roles
- expected slide count
- appendix candidates

Do not follow source order blindly. Reorder by what the audience must understand, believe, compare, and decide.

## Slide Outline

Create `slide_outline.json` with:

- `slide_no`
- `role`
- `title_claim`
- `supporting_points`
- `primary_visual`
- `data_source`
- `layout_pattern`
- `asset_ids`
- `notes`
- `appendix_link`

Rules:

- One slide = one role.
- One slide = one main claim.
- One slide = one primary visual.
- A source paragraph usually becomes one or two proof points, not a bullet dump.
- Long detail goes to notes or appendix.

## Design Tokens

Create `design_tokens.json`:

- canvas size
- primary and neutral colors
- type scale
- margins
- title/body/source styles
- chart style
- image frame rules
- footer/source note behavior
- layout family per slide role

## Build Log

Maintain `pptx_build_log.md`:

- source files used
- slides added/merged/removed
- images preserved/regenerated/discarded
- charts recreated/preserved
- appendix decisions
- known limitations
