#!/usr/bin/env python3
"""Lightweight source-only audit of links/anchors and required site pages.

No HTTP requests, browsers, third-party Python packages or JS execution required.
External research URLs are cited but not probed by this script.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted(ROOT.rglob("*.html"))
IGNORE = {".git", ".venv", "node_modules"}
REQUIRED = ["index.html", "projects/index.html", "notes/001-a-pass-isnt-proof.html"]
PROBLEMS: list[str] = []


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.refs: list[tuple[str, str]] = []
        self.page_titles: list[str] = []
        self._in_title = False
        self.main_count = 0
        self.image_issues: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        att = dict(attrs)
        name = att.get("id")
        if name:
            if name in self.ids:
                self.image_issues.append(f"duplicate id #{name}")
            self.ids.add(name)
        if tag == "main":
            self.main_count += 1
        if tag == "title":
            self._in_title = True
        for attr in ("href", "src"):
            url = att.get(attr)
            if url:
                self.refs.append((attr, url))
        if tag == "img" and att.get("alt") is None:
            self.image_issues.append("image missing alt attribute")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.page_titles.append(data)


def site_file(page: Path, url: str) -> tuple[Path | None, str]:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or url.startswith(("mailto:", "tel:", "#")):
        return None, parsed.fragment
    target_text = unquote(parsed.path)
    if not target_text:
        return page, parsed.fragment
    if target_text.startswith("/"):
        target = ROOT / target_text.lstrip("/")
    else:
        target = page.parent / target_text
    # pathlib resolve is safe here: URLs are authored in this repository.
    target = target.resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        PROBLEMS.append(f"{page.relative_to(ROOT)}: local path escapes repository: {url}")
        return None, parsed.fragment
    if target.is_dir():
        target = target / "index.html"
    return target, parsed.fragment


for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        PROBLEMS.append(f"required public page missing: {relative}")

parsed: dict[Path, Page] = {}
for page in PAGES:
    if any(name in page.parts for name in IGNORE):
        continue
    doc = Page()
    doc.feed(page.read_text(encoding="utf-8"))
    parsed[page.resolve()] = doc
    if not "".join(doc.page_titles).strip():
        PROBLEMS.append(f"{page.relative_to(ROOT)}: no title")
    if doc.main_count != 1:
        PROBLEMS.append(f"{page.relative_to(ROOT)}: expected one <main>, got {doc.main_count}")
    for issue in doc.image_issues:
        PROBLEMS.append(f"{page.relative_to(ROOT)}: {issue}")

for page, doc in parsed.items():
    for attr, url in doc.refs:
        if url.startswith("#"):
            if url[1:] and url[1:] not in doc.ids:
                PROBLEMS.append(f"{page.relative_to(ROOT)}: missing anchor {url}")
            continue
        target, fragment = site_file(page, url)
        if target is None:
            continue
        if not target.is_file():
            PROBLEMS.append(f"{page.relative_to(ROOT)}: missing file for {attr}={url}")
            continue
        if fragment and target.suffix.lower() in {".html", ".htm"}:
            other = parsed.get(target.resolve())
            if other and fragment not in other.ids:
                PROBLEMS.append(
                    f"{page.relative_to(ROOT)}: {url} targets missing #{fragment}"
                )

if PROBLEMS:
    print("Website audit FAILED:")
    for problem in PROBLEMS:
        print("  -", problem)
    sys.exit(1)
print(f"Website audit PASS: {len(parsed)} HTML pages, locally resolvable references and anchors.")
