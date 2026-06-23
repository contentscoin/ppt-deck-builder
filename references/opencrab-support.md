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

- Project: `ppt-skill-ontology`
- Project ID: `b236ce08-3fe4-40fd-ae98-ac674a35ec73`
- Production workflow: `ppt_source_to_deck_production_workflow_20260623`
- Production workflow ID: `5c872052-0aee-4f5a-b37e-3404e58fbfae`

## Workflow Nodes

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
Using project ppt-skill-ontology, answer only for [case].
Return production decisions: route, artifacts, asset/frame decisions, chart/table rules, blockers, QA gates.
Do not repeat general ontology definitions.
```

If OpenCrab is unavailable, continue with the bundled skill references and state that live OpenCrab retrieval was skipped.
