"""Grounding validator: every number in the report must exist in the evidence pack.

This is the product's core promise to buyers ("every number is traceable") and
the reason an LLM can write the prose without being trusted with the math.
"""

from __future__ import annotations

import re
from typing import Any, Iterable

from .evidence import EvidencePack

NUM_RE = re.compile(r"(?<![\w.])\$?\(?-?\d[\d,]*(?:\.\d+)?\)?\s*(?:%|k|K|m|M)?(?![\w])")
SAFE_SMALL_INT = 31  # day counts, step numbers, "top 5", "2 weeks"


def _parse(token: str) -> float | None:
    t = token.strip().replace("$", "").replace(",", "").replace("(", "").replace(")", "").strip()
    mult = 1.0
    if t[-1:] in "kK":
        mult, t = 1_000.0, t[:-1]
    elif t[-1:] in "mM":
        mult, t = 1_000_000.0, t[:-1]
    t = t.rstrip("%").strip()
    try:
        return float(t) * mult
    except ValueError:
        return None


def numbers_in(text: str) -> list[tuple[str, float]]:
    out = []
    for m in NUM_RE.finditer(text or ""):
        v = _parse(m.group(0))
        if v is not None:
            out.append((m.group(0).strip(), v))
    return out


def allowed_values(pack: EvidencePack) -> list[float]:
    vals: list[float] = [abs(float(v)) for v in pack.constants.values()]
    for m in pack.metrics.values():
        vals.append(abs(float(m.value)))
    for rows in pack.tables.values():
        for row in rows:
            for v in row.values():
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    vals.append(abs(float(v)))
    return vals


def is_grounded(value: float, allowed: Iterable[float]) -> bool:
    v = abs(value)
    if v.is_integer() and v <= SAFE_SMALL_INT:
        return True
    if 1990 <= v <= 2100 and v.is_integer():  # years
        return True
    for a in allowed:
        tol = max(0.5, 0.006 * a)  # display rounding, e.g. $12,345.67 shown as $12,346 or 41.66% as 41.7%
        if abs(v - a) <= tol:
            return True
        if a >= 1000 and abs(v * 1 - round(a / 1000, 1) * 1000) <= 0.06 * 1000 and abs(v - a) <= 0.05 * a:
            return True  # "$12.3k" style
    return False


def _texts(report: dict[str, Any]) -> list[tuple[str, str, list[str] | None]]:
    """(path, text, metric_ids) for every free-text field."""
    items = [("headline", report.get("headline", ""), None), ("situation", report.get("situation", ""), None)]
    for i, f in enumerate(report.get("findings", [])):
        items.append((f"findings[{i}]", f"{f.get('title', '')} {f.get('body', '')}", f.get("metric_ids")))
    for i, r in enumerate(report.get("recommendations", [])):
        text = " ".join(str(r.get(k, "")) for k in ("title", "action", "rationale", "owner", "timeline"))
        items.append((f"recommendations[{i}]", text, r.get("metric_ids")))
    for i, letter in enumerate(report.get("letters", [])):
        items.append((f"letters[{i}]", f"{letter.get('subject', '')} {letter.get('body', '')}", None))
    return items


def validate(report: dict[str, Any], pack: EvidencePack) -> list[str]:
    """Return a list of violations. Empty list = fully grounded."""
    problems: list[str] = []
    allowed = allowed_values(pack)
    for key in ("headline", "findings", "recommendations"):
        if not report.get(key):
            problems.append(f"missing '{key}'")
    for path, text, ids in _texts(report):
        if ids is not None:
            if not ids:
                problems.append(f"{path}: cites no metric ids")
            for mid in ids:
                if mid not in pack.metrics:
                    problems.append(f"{path}: unknown metric id '{mid}'")
        for raw, value in numbers_in(text):
            if not is_grounded(value, allowed):
                problems.append(f"{path}: number '{raw}' is not in the evidence pack")
    return problems


def strip_ungrounded(report: dict[str, Any], pack: EvidencePack) -> dict[str, Any]:
    """Last resort: drop findings/recommendations/letters that still fail validation."""
    allowed = allowed_values(pack)

    def ok(text: str, ids: list[str] | None) -> bool:
        if ids is not None and (not ids or any(i not in pack.metrics for i in ids)):
            return False
        return all(is_grounded(v, allowed) for _, v in numbers_in(text))

    out = dict(report)
    out["findings"] = [f for f in report.get("findings", []) if ok(f"{f.get('title','')} {f.get('body','')}", f.get("metric_ids"))]
    out["recommendations"] = [
        r for r in report.get("recommendations", [])
        if ok(" ".join(str(r.get(k, "")) for k in ("title", "action", "rationale", "owner", "timeline")), r.get("metric_ids"))
    ]
    out["letters"] = [l for l in report.get("letters", []) if ok(f"{l.get('subject','')} {l.get('body','')}", None)]
    if not ok(report.get("headline", ""), None):
        out["headline"] = ""
    if not ok(report.get("situation", ""), None):
        out["situation"] = ""
    return out
