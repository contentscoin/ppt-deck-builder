# OpenCrab Support Context

OpenCrab is supporting context for this skill, not the center of the skill.

Use OpenCrab only to strengthen decisions when available:

- reference pattern selection
- source-to-deck migration rules
- mixed image/text asset handling
- chart/table evidence correction
- screenshot-only evidence limits
- final QA guardrails

## Known Project

Primary public integrated context:

- Project: `ppt-public-integrated-pack`
- Project ID: `6c267924-fe1c-4d69-a082-9c9cf0ce09a3`
- Package: `PPT Public Integrated Ontology Pack`
- Package ID: `a48c6f4f-6432-4d0e-ad3a-f9386e2dc917`
- Version: `1.9.0`
- Visibility: `draft` pack inside a `public` OpenCrab project
- Snapshot: 10 documents, 80 chunks, 130 nodes, 120 edges
- QA: A / 100, release-ready true

Legacy/private development context:

- Project: `ppt-skill-ontology`
- Project ID: `b236ce08-3fe4-40fd-ae98-ac674a35ec73`
- Production workflow: `ppt_source_to_deck_production_workflow_20260623`
- Production workflow ID: `5c872052-0aee-4f5a-b37e-3404e58fbfae`

## Workflow Nodes

The public integrated pack contains these context layers:

1. public reference inventory and S-tier reference analysis
2. source-to-deck production workflow
3. mixed image/text asset separation and recomposition
4. `ppt-deck-builder` and `ppt-design-analyzer` operating contract
5. deck archetypes and audience judgment paths
6. source types and content atoms
7. slide roles and layout patterns
8. typography, layout metrics, color surfaces, and design tokens
9. asset types, frame modes, and chart/table rules
10. QA gates, failure modes, validation artifacts, and delivery workflow

The legacy workflow contains these nodes:

1. `intake_route_contract`
2. `reference_pattern_selection`
3. `source_inventory_content_atoms`
4. `story_outline_design_tokens`
5. `mixed_asset_frame_plan`
6. `chart_table_rebuild_plan`
7. `reference_evidence_limits`
8. `ppt_build_handoff`
9. `final_qa_guardrail`

## How To Use

If OpenCrab tools are available, use narrow prompts:

```text
Using project ppt-public-integrated-pack, answer only for [case].
Return production decisions: route, artifacts, asset/frame decisions, chart/table rules, blockers, QA gates.
Do not repeat general ontology definitions.
```

For legacy context only, use project `ppt-skill-ontology`.

If OpenCrab is unavailable, continue with the bundled skill references and state that live OpenCrab retrieval was skipped.

## Case Checks

For mixed image/text pages with product screenshots, readable chart images, and legal/document evidence, OpenCrab context should retrieve these blocking checks:

- `QAGate_ChartValuesMatch`
- `QAGate_LegalClaimTrace`
- `QAGate_FinancialClaimTrace` when financial claims are present
- `QAGate_FactualImageNotGenerated`
- `QAGate_NoProtectedRegionCrop`
- `QAGate_MixedPageNotPasted`
- `QAGate_ContactSheetInspected`
- `QAGate_FinalValidationGate`

If any of these gates are missing from the retrieved answer, ask a narrower follow-up against the same project before finalizing the production plan.
