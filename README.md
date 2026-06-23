# PPT Deck Builder

End-to-end Codex skill for producing PowerPoint decks from source materials.

This is a PPT production skill, not an OpenCrab wrapper. OpenCrab context can support decisions when available, but the skill works from its bundled production workflow, source-to-deck rules, asset/chart rules, and QA scripts.

## Optional OpenCrab Context

When OpenCrab tools are available, use this public integrated support pack:

- Project: `ppt-public-integrated-pack`
- Project ID: `6c267924-fe1c-4d69-a082-9c9cf0ce09a3`
- Package: `PPT Public Integrated Ontology Pack`
- Package ID: `a48c6f4f-6432-4d0e-ad3a-f9386e2dc917`
- Version: `2.5.0`
- Snapshot: 16 documents, 128 chunks, 208 nodes, 192 edges

The pack includes reference inventories, S-tier deck analysis, source-to-deck workflow, mixed image/text handling, frame modes, chart rebuild rules, slide roles, design tokens, QA gates, failure modes, reference pattern routing, production artifact schemas, case playbooks, analyzer evidence boundaries, quality rubrics, and retrieval prompt recipes. It is support context only; final PPT quality still depends on source extraction, artifact generation, PPTX build, render/contact-sheet QA, and validation.

## What It Does

- Converts PDFs, reports, spreadsheets, websites, notes, images, screenshots, or old PPTX files into slide decks.
- Creates the production contract, source inventory, content atoms, story map, slide outline, design tokens, asset plan, chart rebuild plan, and QA report.
- Separates mixed image/text source pages instead of pasting whole screenshots as slides.
- Preserves factual images and recreates charts/tables natively when possible.
- Builds PPTX scaffolds from `slide_outline.json`.
- Supports final render/contact-sheet QA.

## Install

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/contentscoin/ppt-deck-builder.git ~/.codex/skills/ppt-deck-builder
python3 -m pip install -r ~/.codex/skills/ppt-deck-builder/requirements.txt
```

Restart Codex after installing.

For render QA, install native render tools as well:

```bash
brew install poppler libreoffice
```

In Codex Desktop, the bundled workspace Python may already include `python-pptx`, `pdf2image`, `unstructured`, pandas, and openpyxl. If default `python3` is missing optional modules, run scripts with the bundled Python path provided by the workspace dependency loader.

## Use

```text
Use $ppt-deck-builder to turn this report into a polished 12-slide executive PowerPoint deck.
```

## Helper Scripts

```bash
python3 scripts/check_toolchain.py
python3 scripts/init_deck_job.py --out-dir out/deck --title "Deck title" --audience "Executives" --target-slides 12
python3 scripts/validate_deck_job.py out/deck --phase draft
python3 scripts/outline_to_pptx.py out/deck/slide_outline.json --out out/deck/deck.pptx
python3 scripts/make_contact_sheet.py out/deck/rendered_slides/*.png --out out/deck/contact_sheet.jpg
python3 scripts/validate_deck_job.py out/deck --phase final
```

The scripts are helpers, not a substitute for design judgment. The validation script catches missing artifacts and weak production logs, but the skill still requires the agent to inspect source material, make evidence-safe asset decisions, apply design rules, and perform render QA.
