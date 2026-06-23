# PPT Deck Builder

End-to-end Codex skill for producing PowerPoint decks from source materials.

This is a PPT production skill, not an OpenCrab wrapper. OpenCrab context can support decisions when available, but the skill works from its bundled production workflow, source-to-deck rules, asset/chart rules, and QA scripts.

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
```

Restart Codex after installing.

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
