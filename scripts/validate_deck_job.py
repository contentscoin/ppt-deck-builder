#!/usr/bin/env python3
"""Validate PPT deck-builder job artifacts before build or delivery."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


CORE_FILES = [
    "production_contract.json",
    "source_inventory.json",
    "content_atoms.json",
    "story_map.md",
    "slide_outline.json",
    "design_tokens.json",
    "pptx_build_log.md",
    "qa_report.md",
]

MIXED_SOURCE_FILES = [
    "asset_manifest.json",
    "image_decision_log.json",
    "chart_rebuild_spec.json",
    "composition_plan.json",
    "frame_spec.json",
]

OPTIONAL_WORK_DIRS = [
    "extracted_assets",
    "rendered_source_pages",
    "rendered_slides",
]

VALID_SLIDE_ROLES = {
    "cover",
    "agenda",
    "context",
    "problem",
    "opportunity",
    "thesis",
    "evidence",
    "metric",
    "chart",
    "comparison",
    "process",
    "timeline",
    "case_study",
    "solution",
    "recommendation",
    "roadmap",
    "risk",
    "ask",
    "closing",
    "appendix",
}

VALID_ASSET_DECISIONS = {
    "preserve_original",
    "recreate_native",
    "regenerate_similar",
    "discard_or_appendix",
}

VALID_FRAME_MODES = {
    "contain_panel",
    "evidence_panel",
    "cover_crop",
    "crop_to_shape",
    "picture_fill_shape",
    "freeform_mask",
    "collage_grid",
}

CHART_REQUIRED_FIELDS = [
    "chart_id",
    "source_trace",
    "source_chart_type",
    "target_chart_type",
    "data_status",
    "data_confidence",
    "unit",
    "period",
    "source_note",
    "rebuild_decision",
]


class Report:
    def __init__(self, job_dir: Path, phase: str) -> None:
        self.job_dir = job_dir
        self.phase = phase
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors

    def print(self) -> None:
        payload = {
            "ok": self.ok,
            "phase": self.phase,
            "job_dir": str(self.job_dir),
            "errors": self.errors,
            "warnings": self.warnings,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))


def load_json(path: Path, report: Report) -> Any | None:
    if not path.exists():
        report.error(f"Missing required file: {path.name}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.error(f"Invalid JSON in {path.name}: line {exc.lineno}, column {exc.colno}")
        return None


def list_payload(data: Any, key: str) -> list[Any] | None:
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get(key), list):
        return data[key]
    return None


def validate_required_files(job_dir: Path, report: Report, require_mixed: bool) -> None:
    for name in CORE_FILES:
        path = job_dir / name
        if not path.exists():
            report.error(f"Missing required file: {name}")
        elif path.stat().st_size == 0:
            report.warn(f"Empty artifact file: {name}")

    if require_mixed:
        for name in MIXED_SOURCE_FILES:
            path = job_dir / name
            if not path.exists():
                report.error(f"Missing mixed-source artifact: {name}")

    for dirname in OPTIONAL_WORK_DIRS:
        path = job_dir / dirname
        if not path.exists():
            report.warn(f"Optional work folder not found: {dirname}/")

    if report.phase == "final":
        if not (job_dir / "contact_sheet.jpg").exists():
            report.error("Missing final artifact: contact_sheet.jpg")
        if not list(job_dir.glob("*.pptx")):
            report.error("No PPTX file found in job folder")


def validate_slide_outline(job_dir: Path, report: Report) -> None:
    data = load_json(job_dir / "slide_outline.json", report)
    if data is None:
        return

    slides = list_payload(data, "slides")
    if slides is None:
        report.error("slide_outline.json must be a list or contain a 'slides' list")
        return

    if not slides:
        if report.phase == "final":
            report.error("slide_outline.json has no slides")
        else:
            report.warn("slide_outline.json has no slides")
        return

    seen_slide_numbers: set[Any] = set()
    for index, slide in enumerate(slides, start=1):
        if not isinstance(slide, dict):
            report.error(f"Slide {index} is not an object")
            continue

        slide_no = slide.get("slide_no", index)
        if slide_no in seen_slide_numbers:
            report.error(f"Duplicate slide_no: {slide_no}")
        seen_slide_numbers.add(slide_no)

        role = slide.get("role")
        if not role:
            report.error(f"Slide {slide_no} is missing role")
        elif str(role) not in VALID_SLIDE_ROLES:
            report.warn(f"Slide {slide_no} has uncommon role '{role}'")

        title = slide.get("title_claim") or slide.get("title")
        if not title:
            report.error(f"Slide {slide_no} is missing title_claim/title")
        elif len(str(title)) > 95:
            report.warn(f"Slide {slide_no} title is long; check thumbnail readability")

        support_points = slide.get("support_points") or slide.get("evidence") or []
        if isinstance(support_points, list) and len(support_points) > 4:
            report.warn(f"Slide {slide_no} has more than 4 support points")


def validate_assets(job_dir: Path, report: Report) -> None:
    asset_manifest = job_dir / "asset_manifest.json"
    if asset_manifest.exists():
        data = load_json(asset_manifest, report)
        assets = list_payload(data, "assets") if data is not None else None
        if assets is None:
            report.error("asset_manifest.json must be a list or contain an 'assets' list")
        else:
            for index, asset in enumerate(assets, start=1):
                if not isinstance(asset, dict):
                    report.error(f"Asset {index} is not an object")
                    continue
                decision = asset.get("decision") or asset.get("use_decision")
                if decision and decision not in VALID_ASSET_DECISIONS:
                    report.warn(f"Asset {index} has unknown decision '{decision}'")
                if decision == "preserve_original" and not asset.get("source_trace"):
                    report.error(f"Asset {index} preserves original without source_trace")

    frame_spec = job_dir / "frame_spec.json"
    if frame_spec.exists():
        data = load_json(frame_spec, report)
        frames = list_payload(data, "frames") if data is not None else None
        if frames is None:
            report.error("frame_spec.json must be a list or contain a 'frames' list")
        else:
            for index, frame in enumerate(frames, start=1):
                if not isinstance(frame, dict):
                    report.error(f"Frame {index} is not an object")
                    continue
                mode = frame.get("frame_mode") or frame.get("mode")
                if mode and mode not in VALID_FRAME_MODES:
                    report.warn(f"Frame {index} has unknown frame mode '{mode}'")


def validate_charts(job_dir: Path, report: Report) -> None:
    chart_spec = job_dir / "chart_rebuild_spec.json"
    if not chart_spec.exists():
        return

    data = load_json(chart_spec, report)
    charts = list_payload(data, "charts") if data is not None else None
    if charts is None:
        report.error("chart_rebuild_spec.json must be a list or contain a 'charts' list")
        return

    for index, chart in enumerate(charts, start=1):
        if not isinstance(chart, dict):
            report.error(f"Chart {index} is not an object")
            continue
        chart_id = chart.get("chart_id", index)
        for field in CHART_REQUIRED_FIELDS:
            if field not in chart or chart.get(field) in (None, ""):
                report.warn(f"Chart {chart_id} is missing '{field}'")
        decision = chart.get("rebuild_decision")
        if decision and decision not in VALID_ASSET_DECISIONS:
            report.warn(f"Chart {chart_id} has unknown rebuild_decision '{decision}'")


def validate_final_notes(job_dir: Path, report: Report) -> None:
    qa_path = job_dir / "qa_report.md"
    if not qa_path.exists():
        return
    qa_text = qa_path.read_text(encoding="utf-8", errors="replace").lower()
    if report.phase == "final" and "final" not in qa_text and "pass" not in qa_text:
        report.warn("qa_report.md does not clearly mention final/pass status")


def validate(job_dir: Path, phase: str, require_mixed: bool) -> Report:
    report = Report(job_dir.resolve(), phase)
    if not job_dir.exists():
        report.error(f"Job folder does not exist: {job_dir}")
        return report
    if not job_dir.is_dir():
        report.error(f"Job path is not a folder: {job_dir}")
        return report

    validate_required_files(job_dir, report, require_mixed)
    validate_slide_outline(job_dir, report)
    validate_assets(job_dir, report)
    validate_charts(job_dir, report)
    validate_final_notes(job_dir, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PPT deck-builder job artifacts.")
    parser.add_argument("job_dir", help="Deck job output folder")
    parser.add_argument(
        "--phase",
        choices=["draft", "final"],
        default="draft",
        help="Validation strictness; final requires PPTX and contact_sheet.jpg",
    )
    parser.add_argument(
        "--require-mixed",
        action="store_true",
        help="Require mixed image/text asset planning artifacts",
    )
    args = parser.parse_args()

    report = validate(Path(args.job_dir), args.phase, args.require_mixed)
    report.print()
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
