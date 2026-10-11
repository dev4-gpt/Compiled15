"""Evidence pack: the only facts the analyst is allowed to state.

Every number in a deliverable must trace to a Metric here. Metrics are computed
by deterministic code (metrics_donor.py, metrics_smb.py), never by the LLM.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class Metric:
    id: str
    label: str
    value: float
    unit: str  # "usd", "pct", "count", "days", "ratio"
    formula: str
    source: str = "client data"  # or an external citation for benchmarks

    def display(self) -> str:
        return format_value(self.value, self.unit)


def format_value(value: float, unit: str) -> str:
    if unit == "usd":
        return f"${value:,.0f}" if abs(value) >= 100 else f"${value:,.2f}"
    if unit == "pct":
        return f"{value:.1f}%"
    if unit == "count":
        return f"{int(round(value)):,}"
    if unit == "days":
        return f"{value:.0f} days"
    if unit == "ratio":
        return f"{value:.2f}x"
    return f"{value:,.2f}"


@dataclass
class EvidencePack:
    practice: str
    org_name: str
    as_of: str
    period: str
    metrics: dict[str, Metric] = field(default_factory=dict)
    tables: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)
    # Declared methodology constants (e.g. the 80% Pareto cut, a 10% win-back scenario).
    # They may appear in text and are listed in the appendix, but are not client facts.
    constants: dict[str, float] = field(default_factory=dict)

    def add(self, metric: Metric) -> Metric:
        self.metrics[metric.id] = metric
        return metric

    def get(self, metric_id: str) -> Metric:
        return self.metrics[metric_id]

    def to_dict(self) -> dict[str, Any]:
        return {
            "practice": self.practice,
            "org_name": self.org_name,
            "as_of": self.as_of,
            "period": self.period,
            "metrics": {k: {**asdict(m), "display": m.display()} for k, m in self.metrics.items()},
            "tables": self.tables,
            "notes": self.notes,
            "constants": self.constants,
        }

    def for_prompt(self, max_rows: int = 10) -> dict[str, Any]:
        """Compact view sent to the LLM."""
        return {
            "practice": self.practice,
            "org_name": self.org_name,
            "as_of": self.as_of,
            "period": self.period,
            "metrics": {k: {"label": m.label, "display": m.display(), "unit": m.unit} for k, m in self.metrics.items()},
            "tables": {k: v[:max_rows] for k, v in self.tables.items()},
            "notes": self.notes,
            "method_constants": self.constants,
        }
