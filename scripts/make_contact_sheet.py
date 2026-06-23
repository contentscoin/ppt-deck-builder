#!/usr/bin/env python3
"""Make a JPEG contact sheet from rendered slide images."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+")
    parser.add_argument("--out", required=True)
    parser.add_argument("--thumb-width", type=int, default=320)
    args = parser.parse_args()

    paths = [Path(p) for p in args.images]
    thumbs = []
    for path in paths:
        image = Image.open(path).convert("RGB")
        ratio = args.thumb_width / image.width
        thumb = image.resize((args.thumb_width, max(1, int(image.height * ratio))))
        thumbs.append((path, thumb))

    cols = min(4, max(1, math.ceil(math.sqrt(len(thumbs)))))
    rows = math.ceil(len(thumbs) / cols)
    label_h = 24
    cell_w = args.thumb_width
    cell_h = max(t.height for _, t in thumbs) + label_h
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)

    for i, (path, thumb) in enumerate(thumbs):
        x = (i % cols) * cell_w
        y = (i // cols) * cell_h
        sheet.paste(thumb, (x, y))
        draw.text((x + 6, y + thumb.height + 4), f"{i + 1}. {path.name}", fill=(40, 40, 40))

    sheet.save(args.out, quality=90)
    print(f"created {args.out} from {len(paths)} images")


if __name__ == "__main__":
    main()
