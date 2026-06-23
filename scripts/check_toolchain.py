#!/usr/bin/env python3
"""Check optional PPT production dependencies."""

from __future__ import annotations

import importlib.util
import json
import shutil


PYTHON_MODULES = {
    "python-pptx": "pptx",
    "Pillow": "PIL",
    "pdf2image": "pdf2image",
    "unstructured": "unstructured",
    "pandas": "pandas",
    "openpyxl": "openpyxl",
}

BINARIES = {
    "libreoffice/soffice": ["soffice", "libreoffice"],
    "poppler/pdftoppm": ["pdftoppm"],
}


def module_available(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None


def first_binary(names: list[str]) -> str | None:
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


def main() -> None:
    modules = {
        label: {"module": module, "available": module_available(module)}
        for label, module in PYTHON_MODULES.items()
    }
    binaries = {
        label: {"available": bool(path := first_binary(names)), "path": path}
        for label, names in BINARIES.items()
    }
    payload = {
        "ok": True,
        "modules": modules,
        "binaries": binaries,
        "notes": [
            "python-pptx is needed for PPTX scaffold/build work.",
            "LibreOffice plus pdf2image/Poppler is recommended for render QA.",
            "unstructured is useful for source document partitioning but the skill can continue without it.",
        ],
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
