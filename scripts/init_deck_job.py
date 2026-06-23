#!/usr/bin/env python3
"""Create a PPT deck production workspace with required artifact skeletons."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--title", default="Untitled deck")
    parser.add_argument("--audience", default="")
    parser.add_argument("--use-mode", default="")
    parser.add_argument("--target-slides", type=int, default=0)
    parser.add_argument("--archetype", default="")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for folder in ["extracted_assets", "rendered_source_pages", "rendered_slides"]:
        (out_dir / folder).mkdir(exist_ok=True)

    contract = {
        "created": date.today().isoformat(),
        "title": args.title,
        "audience": args.audience,
        "use_mode": args.use_mode,
        "target_slides": args.target_slides,
        "archetype": args.archetype,
        "desired_action": "",
        "brand_constraints": {},
        "source_files": [],
        "output_formats": ["pptx", "pdf", "contact_sheet"],
    }

    write_json(out_dir / "production_contract.json", contract)
    write_json(out_dir / "source_inventory.json", {"sources": []})
    write_json(out_dir / "content_atoms.json", {"atoms": []})
    write_json(out_dir / "slide_outline.json", {"slides": []})
    write_json(out_dir / "design_tokens.json", {"canvas": "16:9", "typography": {}, "colors": {}, "layout": {}, "charts": {}, "images": {}})
    write_json(out_dir / "asset_manifest.json", {"assets": []})
    write_json(out_dir / "image_decision_log.json", {"decisions": []})
    write_json(out_dir / "chart_rebuild_spec.json", {"charts": []})
    write_json(out_dir / "composition_plan.json", {"slides": []})
    write_json(out_dir / "frame_spec.json", {"frames": []})

    (out_dir / "story_map.md").write_text(f"# Story Map\n\nDeck: {args.title}\n", encoding="utf-8")
    (out_dir / "pptx_build_log.md").write_text("# PPTX Build Log\n", encoding="utf-8")
    (out_dir / "qa_report.md").write_text("# QA Report\n\n- status: draft\n", encoding="utf-8")

    print(json.dumps({"ok": True, "out_dir": str(out_dir), "created": sorted(p.name for p in out_dir.iterdir())}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
