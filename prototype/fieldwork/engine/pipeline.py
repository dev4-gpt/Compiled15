"""End-to-end run: export -> evidence -> grounded report -> deck."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any

from . import ingest, metrics_donor, metrics_smb
from .analyst import LLMAnalyst, TemplateAnalyst
from .evidence import EvidencePack
from .render import render_html
from .validate import validate


@dataclass
class RunResult:
    pack: EvidencePack
    report: dict[str, Any]
    html: str
    analyst: str
    violations: list[str]
    log: list[str] = field(default_factory=list)
    seconds: float = 0.0


def run(data: bytes | str, org_name: str, intake: dict[str, str] | None = None,
        practice: str | None = None, use_llm: bool = True) -> RunResult:
    t0 = time.time()
    intake = intake or {}
    practice, df = ingest.load(data, practice)
    pack = (metrics_donor.compute if practice == "donor" else metrics_smb.compute)(df, org_name)

    log: list[str] = [f"ingested {len(df)} rows as practice '{practice}'"]
    report, analyst_name = None, "template"
    llm = LLMAnalyst()
    if use_llm and llm.available():
        try:
            report = llm.write(pack, intake)
            analyst_name = "llm"
        except Exception as e:
            log.append(f"LLM analyst failed, using template: {e}")
        log += llm.log
    if report is None or not report.get("findings") or not report.get("recommendations"):
        report = TemplateAnalyst().write(pack, intake)
        analyst_name = "template"
    violations = validate(report, pack)
    html = render_html(pack, report, {"analyst": analyst_name, "violations": violations, "intake": intake})
    return RunResult(pack, report, html, analyst_name, violations, log, round(time.time() - t0, 2))
