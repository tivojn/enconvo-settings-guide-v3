#!/usr/bin/env python3
"""Audit an EnConvo screenshot-backed HTML guide without modifying files."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


COPY_PATTERNS = re.compile(
    r"\b(showing|shown|visible|observed|captured|this screenshot|screenshot shows|"
    r"related screenshot|click to enlarge|masked api key|document the menu)\b",
    re.IGNORECASE,
)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").expanduser().resolve()
    html_path = root / "index.html"
    screenshots = root / "screenshots"
    problems: list[str] = []

    if not html_path.exists():
        print(f"missing index.html: {html_path}")
        return 2

    html = html_path.read_text(encoding="utf-8")

    try:
        HTMLParser().feed(html)
    except Exception as exc:  # HTMLParser is permissive, but keep this guard.
        problems.append(f"html parse error: {exc}")

    for script in re.findall(r"<script>([\s\S]*?)</script>", html):
        # This script cannot compile JavaScript itself; caller should still run node.
        if "const sections" in script and "function renderGuide" not in script:
            problems.append("inline script has sections but no renderGuide function")

    refs = re.findall(r'"([^"]+\.png)"', html)
    missing = []
    for ref in refs:
        ref_path = Path(ref)
        if ref_path.exists() or (screenshots / ref).exists() or (root / ref).exists():
            continue
        missing.append(ref)
    for ref in sorted(set(missing)):
        problems.append(f"missing image ref: {ref}")

    png_png = sorted(root.rglob("*.png.png"))
    for path in png_png:
        problems.append(f"duplicate extension candidate: {path.relative_to(root)}")

    copy_candidates = []
    for lineno, line in enumerate(html.splitlines(), 1):
        if COPY_PATTERNS.search(line):
            copy_candidates.append((lineno, line.strip()[:220]))

    print(f"guide={root}")
    print(f"png_refs={len(refs)} unique={len(set(refs))} missing={len(set(missing))}")
    print(f"png_png={len(png_png)} copy_candidates={len(copy_candidates)}")
    if copy_candidates:
        print("copy review candidates:")
        for lineno, line in copy_candidates[:40]:
            print(f"- line {lineno}: {line}")
        if len(copy_candidates) > 40:
            print(f"- truncated: {len(copy_candidates) - 40} more")
    if problems:
        print("problems:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("audit-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
