#!/usr/bin/env python3
"""Convert paper teaser images to lightweight WebP thumbnails.

Usage:
  python3 scripts/convert_paper_teasers_to_webp.py
  python3 scripts/convert_paper_teasers_to_webp.py --max-width 800 --quality 82

The script reads PNG/JPG/JPEG files directly under images/papers and writes
compressed WebP thumbnails to images/papers/webp. It intentionally skips any
nested folders so reruns do not reprocess generated files.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - user-facing dependency message
    raise SystemExit(
        "Pillow is required. Install it with: python3 -m pip install Pillow"
    ) from exc

SOURCE_EXTS = {".png", ".jpg", ".jpeg"}


def iter_source_images(source_dir: Path) -> Iterable[Path]:
    for path in sorted(source_dir.iterdir()):
        if path.is_file() and path.suffix.lower() in SOURCE_EXTS:
            yield path


def resize_to_width(image: Image.Image, max_width: int) -> Image.Image:
    if image.width <= max_width:
        return image.copy()
    ratio = max_width / image.width
    target_size = (max_width, max(1, round(image.height * ratio)))
    return image.resize(target_size, Image.Resampling.LANCZOS)


def flatten_on_white(image: Image.Image) -> Image.Image:
    """Composite transparent images onto white for smaller homepage teasers."""
    if image.mode in ("RGBA", "LA") or (image.mode == "P" and "transparency" in image.info):
        rgba = image.convert("RGBA")
        background = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        background.alpha_composite(rgba)
        return background.convert("RGB")
    return image.convert("RGB")


def convert_one(src: Path, dst: Path, max_width: int, quality: int) -> tuple[int, int]:
    with Image.open(src) as image:
        image = resize_to_width(image, max_width)
        image = flatten_on_white(image)
        dst.parent.mkdir(parents=True, exist_ok=True)
        image.save(dst, "WEBP", quality=quality, method=6)
    return src.stat().st_size, dst.stat().st_size


DEFAULT_DIRS = [
    ("images/papers", "images/papers/webp"),
    ("images/experience", "images/experience/webp"),
]


def process_dir(source_dir: Path, output_dir: Path, max_width: int, quality: int, force: bool) -> None:
    converted = 0
    skipped = 0
    total_before = 0
    total_after = 0

    for src in iter_source_images(source_dir):
        dst = output_dir / f"{src.stem}.webp"
        if dst.exists() and not force and dst.stat().st_mtime >= src.stat().st_mtime:
            skipped += 1
            continue
        before, after = convert_one(src, dst, max_width, quality)
        converted += 1
        total_before += before
        total_after += after
        print(f"  {src} -> {dst}  {before / 1024:.1f}KB -> {after / 1024:.1f}KB")

    if converted:
        saved = total_before - total_after
        print(f"  Converted {converted} image(s); saved {saved / 1024 / 1024:.2f}MB total.")
    if skipped:
        print(f"  Skipped {skipped} up-to-date image(s).")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert images to WebP thumbnails. Processes images/papers and images/experience by default."
    )
    parser.add_argument("--source-dir", default=None, help="Override: single source directory (disables default dirs).")
    parser.add_argument("--output-dir", default=None, help="Override: single output directory (requires --source-dir).")
    parser.add_argument("--max-width", type=int, default=800, help="Maximum output width in pixels.")
    parser.add_argument("--quality", type=int, default=82, help="WebP quality, 1-100.")
    parser.add_argument("--force", action="store_true", help="Regenerate even when output is newer than source.")
    args = parser.parse_args()

    if args.source_dir:
        if not Path(args.source_dir).exists():
            raise SystemExit(f"Source directory does not exist: {args.source_dir}")
        output_dir = args.output_dir or f"{args.source_dir}/webp"
        dirs = [(args.source_dir, output_dir)]
    else:
        if args.output_dir:
            parser.error("--output-dir requires --source-dir when overriding a single directory.")
        dirs = [(s, o) for s, o in DEFAULT_DIRS if Path(s).exists()]

    for source, output in dirs:
        print(f"\n{'='*60}\nProcessing {source}/ -> {output}/\n{'='*60}")
        process_dir(Path(source), Path(output), args.max_width, args.quality, args.force)


if __name__ == "__main__":
    main()
