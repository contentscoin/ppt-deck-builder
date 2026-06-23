# Asset And Chart Rules

## Mixed Image/Text Rule

Never paste a whole mixed source page as a body slide image. Decompose it into:

- text layer
- image layer
- data/chart layer
- layout geometry layer
- source trace layer

Then rebuild the slide with editable text and reinsert only the visual assets that should remain visual.

## Asset Decisions

Use one of four decisions for every visual asset:

- `preserve_original`: real product/UI screenshots, logos, packaging, factual photos, legal/financial/audit documents, research figures, maps, before/after evidence.
- `recreate_native`: charts, tables, diagrams, timelines, funnels, matrices, process flows, structured infographics.
- `regenerate_similar`: non-factual decorative photos, abstract textures, generic mood images, low-originality stock-like imagery.
- `discard_or_appendix`: duplicate, low-signal, low-quality, unreadable, rights-unclear, or too dense for the body deck.

Record the decision and reason in `image_decision_log.json`.

## Asset Manifest

Create `asset_manifest.json` with:

- `asset_id`
- `source_trace`
- `asset_type`
- `contains_text`
- `text_role`
- `semantic_role`
- `rights_status`
- `quality`
- `decision`
- `decision_reason`

## Text Inside Images

- If image text is a duplicate caption or explanation, move it into editable PPT text.
- If image text is product UI, signage, legal document, chart label, axis, or source evidence, preserve it.

## Frame Modes

| Mode | Use for | Avoid for |
| --- | --- | --- |
| `contain_panel` | UI, logos, charts, tables, documents, research figures | mood hero images |
| `evidence_panel` | original evidence plus summary claim/facts | decorative visuals |
| `cover_crop` | non-critical photos, mood images | charts, UI, documents, logos |
| `crop_to_shape` | decorative/photo geometry | factual/evidence assets |
| `picture_fill_shape` | reusable non-factual image slots | exact evidence assets |
| `freeform_mask` | brand/editorial cutouts | charts, UI, legal/financial docs |
| `collage_grid` | related image sets | dense evidence needing explanation |

## Protected Regions

Every preserved image needs protected regions when relevant:

- face
- product
- logo
- UI controls
- chart axes
- legend
- footnote/source
- signature/legal text

Fail QA if a protected region is cropped or distorted.

## Chart/Table Rule

Charts and tables are evidence, not decoration.

Recreate natively when:

- source spreadsheet exists
- source data table exists
- data can be extracted from PDF/image
- readable values can be digitized with confidence

Preserve original with `contain_panel` or `evidence_panel` when:

- chart is legal, financial, audit, medical, scientific, map, heatmap, or original research evidence
- underlying data is unavailable or risky to infer
- original figure must remain traceable

Forbidden for factual charts/tables/documents:

- `cover_crop`
- `crop_to_shape`
- `picture_fill_shape`
- `freeform_mask`

## Chart Rebuild Spec

Create `chart_rebuild_spec.json` with:

- `chart_id`
- `source_trace`
- `source_chart_type`
- `target_chart_type`
- `data_status`: `source_data`, `extracted_table`, `digitized_estimate`, or `unavailable`
- `data_confidence`
- `series`
- `unit`
- `period`
- `baseline`
- `source_note`
- `rebuild_decision`
- `appendix_original`
