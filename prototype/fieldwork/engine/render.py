"""Render the deliverable: HTML deck (always) and PDF (when Chromium is available)."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .evidence import EvidencePack

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"
_env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]))

CHROME_CANDIDATES = [
    os.getenv("CHROME_PATH", ""),
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium",
]

PRACTICE_TITLES = {"donor": "Donor Retention Audit", "smb": "Sales Diagnostic"}


def render_html(pack: EvidencePack, report: dict[str, Any], meta: dict[str, Any] | None = None) -> str:
    return _env.get_template("deck.html").render(
        pack=pack, report=report, meta=meta or {}, title=PRACTICE_TITLES.get(pack.practice, "Diagnostic"),
        metrics=list(pack.metrics.values()),
    )


def render_pdf(html: str, out_path: str | Path) -> bool:
    """Print HTML to PDF with headless Chromium via Playwright. Returns False if unavailable."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    exe = next((p for p in CHROME_CANDIDATES if p and Path(p).is_file()), None)
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=exe) if exe else pw.chromium.launch()
            page = browser.new_page()
            page.set_content(html, wait_until="load")
            page.pdf(path=str(out_path), format="Letter", landscape=True, print_background=True,
                     margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
            browser.close()
        return True
    except Exception:
        return False
