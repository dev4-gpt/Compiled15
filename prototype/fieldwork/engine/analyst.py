"""Analyst: turns an evidence pack into a consultant-style report.

Two implementations share one output schema:
- LLMAnalyst: any OpenAI-compatible endpoint (Luminal, Groq, Cerebras, OpenRouter, ...),
  configured by env vars, with ordered fallback across providers.
- TemplateAnalyst: deterministic rules. Used when no key is set, or when the LLM
  output still fails grounding after one repair attempt. Never fails the run.

Report schema:
{
  "headline": str,
  "situation": str,
  "findings": [{"title", "body", "metric_ids": [..]}],
  "recommendations": [{"title", "action", "rationale", "metric_ids": [..], "owner", "timeline"}],
  "letters": [{"donor_id", "name", "subject", "body"}]   # donor practice only
}
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from typing import Any

from .evidence import EvidencePack
from .validate import strip_ungrounded, validate

SYSTEM = """You are a senior consultant writing a client diagnostic.
Rules you must follow:
1. Use ONLY facts from the evidence JSON. Every number you write must appear in a metric "display" value or a table row. Never compute new numbers, never round differently, never invent benchmarks.
2. Every finding and recommendation must list the metric ids it relies on in "metric_ids".
3. Be specific and actionable: who does what, by when. Plain English, no jargon, no hype.
4. Output a single JSON object matching the schema. No markdown, no commentary."""

SCHEMA_HINT = {
    "headline": "one sentence, the single most important takeaway",
    "situation": "2-3 sentences describing the current state",
    "findings": [{"title": "short", "body": "2-3 sentences", "metric_ids": ["id"]}],
    "recommendations": [{"title": "short", "action": "concrete step", "rationale": "why, citing numbers",
                         "metric_ids": ["id"], "owner": "role", "timeline": "e.g. next 2 weeks"}],
}
LETTER_HINT = {"letters": [{"donor_id": "id from lybunt_priority", "name": "donor name", "subject": "...",
                            "body": "warm 90-120 word personal note from the executive director; thank them for "
                                    "their past support (you may mention their last_year_total), share impact in "
                                    "general terms, invite them back; no new numbers"}]}


@dataclass
class Provider:
    name: str
    base_url: str
    api_key: str
    model: str


def providers_from_env() -> list[Provider]:
    """LLM_BASE_URL/LLM_API_KEY/LLM_MODEL first, then FALLBACK_1_*, FALLBACK_2_*."""
    out = []
    for prefix in ("LLM", "FALLBACK_1", "FALLBACK_2"):
        key = os.getenv(f"{prefix}_API_KEY")
        url = os.getenv(f"{prefix}_BASE_URL")
        model = os.getenv(f"{prefix}_MODEL")
        if key and url and model:
            out.append(Provider(prefix, url, key, model))
    return out


def _extract_json(text: str) -> dict[str, Any]:
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M)
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < 0:
        raise ValueError("no JSON object in model output")
    return json.loads(text[start:end + 1])


class LLMAnalyst:
    def __init__(self, providers: list[Provider] | None = None, timeout: float = 60.0):
        self.providers = providers if providers is not None else providers_from_env()
        self.timeout = timeout
        self.log: list[str] = []

    def available(self) -> bool:
        return bool(self.providers)

    def _chat(self, messages: list[dict[str, str]]) -> str:
        from openai import OpenAI

        last_err: Exception | None = None
        for p in self.providers:
            try:
                client = OpenAI(base_url=p.base_url, api_key=p.api_key, timeout=self.timeout)
                resp = client.chat.completions.create(model=p.model, messages=messages, temperature=0.2)
                self.log.append(f"used provider {p.name} ({p.model})")
                return resp.choices[0].message.content or ""
            except Exception as e:  # provider down, rate-limited, bad key: try the next one
                self.log.append(f"provider {p.name} failed: {type(e).__name__}: {e}")
                last_err = e
        raise RuntimeError(f"all LLM providers failed: {last_err}")

    def write(self, pack: EvidencePack, intake: dict[str, str]) -> dict[str, Any]:
        schema = dict(SCHEMA_HINT)
        if pack.practice == "donor":
            schema.update(LETTER_HINT)
        user = (
            f"Client intake answers: {json.dumps(intake)}\n\n"
            f"Evidence JSON:\n{json.dumps(pack.for_prompt())}\n\n"
            f"Write 3-5 findings and exactly 3 recommendations"
            + (" and personal letters for the top 3 donors in lybunt_priority" if pack.practice == "donor" else "")
            + f". Schema:\n{json.dumps(schema)}"
        )
        messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
        report = _extract_json(self._chat(messages))
        problems = validate(report, pack)
        if problems:
            self.log.append(f"repair round: {len(problems)} grounding problems")
            messages += [
                {"role": "assistant", "content": json.dumps(report)},
                {"role": "user", "content": "These statements are not grounded in the evidence. Fix them by using only "
                                            "exact displayed values, and return the full JSON again:\n- " + "\n- ".join(problems[:20])},
            ]
            report = _extract_json(self._chat(messages))
            problems = validate(report, pack)
            if problems:
                self.log.append(f"dropping {len(problems)} still-ungrounded items")
                report = strip_ungrounded(report, pack)
        return report


def _m(pack: EvidencePack, mid: str) -> str:
    return pack.metrics[mid].display()


class TemplateAnalyst:
    """Deterministic consultant rules. Every sentence is built from metric displays."""

    def write(self, pack: EvidencePack, intake: dict[str, str]) -> dict[str, Any]:
        return self._donor(pack, intake) if pack.practice == "donor" else self._smb(pack, intake)

    def _donor(self, pack: EvidencePack, intake: dict[str, str]) -> dict[str, Any]:
        has = pack.metrics.__contains__
        findings, recs = [], []
        if has("retention_rate"):
            above = pack.get("retention_rate").value >= pack.get("bench_fep_retention").value
            findings.append({
                "title": "Retention beats the sector, but lapsed donors still cost money" if above
                         else "Retention is below the sector benchmark",
                "body": f"{_m(pack, 'retention_rate')} of last year's donors gave again this year, versus a sector "
                        f"benchmark of {_m(pack, 'bench_fep_retention')}.",
                "metric_ids": ["retention_rate", "bench_fep_retention"]})
        findings.append({
            "title": "Revenue at risk from lapsed donors",
            "body": f"{_m(pack, 'lybunt_count')} donors gave last year but not this year; together they gave "
                    f"{_m(pack, 'lybunt_value')} last year.",
            "metric_ids": ["lybunt_count", "lybunt_value"]})
        if has("new_donor_retention"):
            weak = pack.get("new_donor_retention").value < pack.get("retention_rate").value if has("retention_rate") else True
            findings.append({
                "title": "First-time donors churn faster than repeat donors" if weak else "First-time donors are sticking",
                "body": f"{_m(pack, 'new_donor_retention')} of first-time donors from the prior year gave again. "
                        f"The organisation acquired {_m(pack, 'new_donors_ty')} new donors in the last 12 months.",
                "metric_ids": ["new_donor_retention", "new_donors_ty"]})
        if has("top10_share"):
            findings.append({
                "title": "Revenue concentration",
                "body": f"The top 10% of donors gave {_m(pack, 'top10_share')} of last-12-month revenue "
                        f"({_m(pack, 'revenue_ty')} in total).",
                "metric_ids": ["top10_share", "revenue_ty"]})
        recs.append({
            "title": "Run a LYBUNT win-back sprint",
            "action": "Call or hand-write to the LYBUNT priority list in order, starting with the largest prior-year donors.",
            "rationale": (f"Winning back 10% of lapsed donors is worth about {_m(pack, 'win_back_10pct_value')}."
                          if has("win_back_10pct_value") else f"{_m(pack, 'lybunt_value')} of last year's giving is at risk."),
            "metric_ids": ["win_back_10pct_value"] if has("win_back_10pct_value") else ["lybunt_value"],
            "owner": "Executive director + board members", "timeline": "next 3 weeks"})
        recs.append({
            "title": "Second-gift program for new donors",
            "action": "Send every first-time donor a thank-you within 48 hours, an impact update at 30 days and a "
                      "specific second ask at 90 days.",
            "rationale": (f"First-year retention is {_m(pack, 'new_donor_retention')}." if has("new_donor_retention")
                          else f"{_m(pack, 'new_donors_ty')} new donors joined this year."),
            "metric_ids": ["new_donor_retention"] if has("new_donor_retention") else ["new_donors_ty"],
            "owner": "Development staff", "timeline": "start this month"})
        recs.append({
            "title": "Catch lapse risk before it happens",
            "action": "Contact current donors on the lapse-risk list (one gift, 9+ months ago) with a personal update "
                      "before their giving anniversary.",
            "rationale": f"{_m(pack, 'lapse_risk_count')} current donors fit this pattern.",
            "metric_ids": ["lapse_risk_count"], "owner": "Development staff", "timeline": "next 30 days"})
        letters = []
        for row in pack.tables.get("lybunt_priority", [])[:3]:
            first = str(row["name"]).split(" ")[0]
            letters.append({
                "donor_id": row["donor_id"], "name": row["name"],
                "subject": f"We miss you, {first}",
                "body": (f"Dear {first},\n\nThank you for your generous support last year. Gifts like yours kept our "
                         f"programs running and reached people who needed us. I wanted to personally share what your "
                         f"support made possible and to invite you to stay part of this work. Would you have ten "
                         f"minutes for a quick call or a visit? I would love to show you what is next.\n\nWith gratitude,\n"
                         f"{intake.get('signer', 'Executive Director')}")})
        headline = (f"{_m(pack, 'lybunt_count')} lapsed donors represent {_m(pack, 'lybunt_value')} of last year's "
                    f"giving, and winning them back is the fastest path to growth.")
        situation = (f"{pack.org_name} raised {_m(pack, 'revenue_ty')} from {_m(pack, 'donors_ty')} donors in the last "
                     f"12 months, versus {_m(pack, 'revenue_ly')} from {_m(pack, 'donors_ly')} donors the year before.")
        return {"headline": headline, "situation": situation, "findings": findings,
                "recommendations": recs, "letters": letters}

    def _smb(self, pack: EvidencePack, intake: dict[str, str]) -> dict[str, Any]:
        has = pack.metrics.__contains__
        findings, recs = [], []
        if has("revenue_change_pct"):
            chg = pack.get("revenue_change_pct").value
            findings.append({
                "title": "Sales are growing" if chg > 2 else ("Sales are falling" if chg < -2 else "Sales are flat"),
                "body": f"Net sales were {_m(pack, 'revenue_cur')} in the period, a {_m(pack, 'revenue_change_pct')} "
                        f"change versus {_m(pack, 'revenue_prev')} in the prior period.",
                "metric_ids": ["revenue_cur", "revenue_change_pct", "revenue_prev"]})
        if has("items_for_80pct"):
            findings.append({
                "title": "A few items carry the business",
                "body": f"{_m(pack, 'items_for_80pct')} of {_m(pack, 'items_total')} items produce 80% of sales, and "
                        f"{_m(pack, 'tail_items')} items sit in the bottom 5%.",
                "metric_ids": ["items_for_80pct", "items_total", "tail_items"]})
        if has("best_day_revenue"):
            findings.append({
                "title": "Weekly rhythm",
                "body": f"{pack.metrics['best_day_revenue'].label}: {_m(pack, 'best_day_revenue')}. "
                        f"{pack.metrics['worst_day_revenue'].label}: {_m(pack, 'worst_day_revenue')}.",
                "metric_ids": ["best_day_revenue", "worst_day_revenue"]})
        if has("repeat_customer_rate"):
            findings.append({
                "title": "Repeat customers",
                "body": f"{_m(pack, 'repeat_customer_rate')} of identified customers ordered more than once.",
                "metric_ids": ["repeat_customer_rate"]})
        if has("avg_ticket"):
            findings.append({
                "title": "Basket size",
                "body": f"The average order is {_m(pack, 'avg_ticket')} with {_m(pack, 'items_per_order')} items per order.",
                "metric_ids": ["avg_ticket", "items_per_order"]})
        if has("tail_items"):
            recs.append({
                "title": "Simplify the menu or catalog",
                "action": "Review the bottom-5% items list; cut or reprice the ones that also carry prep or inventory cost.",
                "rationale": f"{_m(pack, 'tail_items')} items add little revenue but add complexity.",
                "metric_ids": ["tail_items"], "owner": "Owner", "timeline": "next 2 weeks"})
        if has("worst_day_revenue"):
            recs.append({
                "title": "Fix the slowest day",
                "action": "Run one targeted offer or event on the slowest day for four weeks and compare against this baseline.",
                "rationale": f"{pack.metrics['worst_day_revenue'].label} is {_m(pack, 'worst_day_revenue')}.",
                "metric_ids": ["worst_day_revenue"], "owner": "Owner / manager", "timeline": "next 4 weeks"})
        if has("avg_ticket"):
            recs.append({
                "title": "Raise the average order",
                "action": "Add one bundle or add-on prompt at checkout built around the top-selling items.",
                "rationale": f"Average order value is {_m(pack, 'avg_ticket')}; the top item alone is "
                             f"{_m(pack, 'top_item_share')} of sales.",
                "metric_ids": ["avg_ticket", "top_item_share"], "owner": "Front-of-house lead", "timeline": "next 2 weeks"})
        headline = (f"{_m(pack, 'items_for_80pct')} items drive 80% of {pack.org_name}'s sales; focus there and fix the "
                    f"slowest day." if has("items_for_80pct") and has("worst_day_revenue") else
                    f"{pack.org_name} sold {_m(pack, 'revenue_cur')} in the period.")
        situation = (f"Over {pack.period}, {pack.org_name} took {_m(pack, 'orders_cur')} orders worth "
                     f"{_m(pack, 'revenue_cur')}, about {_m(pack, 'weekly_revenue')} per week.")
        return {"headline": headline, "situation": situation, "findings": findings, "recommendations": recs[:3],
                "letters": []}
