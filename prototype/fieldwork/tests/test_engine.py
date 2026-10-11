import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine import ingest, metrics_donor, metrics_smb, pipeline  # noqa: E402
from engine.analyst import TemplateAnalyst  # noqa: E402
from engine.validate import is_grounded, numbers_in, validate  # noqa: E402

# Hand-computable donor file. as_of = 2026-09-30.
# A: gave LY and TY (retained). B: gave LY only (LYBUNT, $300). C: first gift TY (new).
# D: gave 3 years ago only (SYBUNT). E: first gift LY, again TY (new LY donor retained).
DONOR_CSV = """Account Number,Full Name,Primary Email,Date,Amount
A,Ann Lee,ann@x.org,2025-03-01,$100.00
A,Ann Lee,ann@x.org,2026-03-01,$150.00
B,Bob Kim,bob@x.org,2025-02-01,$300.00
C,Cy Roe,cy@x.org,2026-09-30,$50.00
D,Di Fox,di@x.org,2023-06-01,$80.00
E,Ed Wu,ed@x.org,2025-06-01,$40.00
E,Ed Wu,ed@x.org,2025-11-01,$40.00
"""


def test_detects_and_normalizes_donor_export():
    practice, df = ingest.load(DONOR_CSV)
    assert practice == "donor"
    assert set(df.columns) >= {"donor_id", "donor_name", "email", "date", "amount"}
    assert df.amount.sum() == pytest.approx(760.0)


def test_donor_metrics_hand_computed():
    _, df = ingest.load(DONOR_CSV)
    pack = metrics_donor.compute(df, "Test Org")
    m = {k: v.value for k, v in pack.metrics.items()}
    # LY window (2024-09-30, 2025-09-30]: A, B, E. TY window: A, C, E.
    assert m["donors_ly"] == 3 and m["donors_ty"] == 3
    assert m["retention_rate"] == pytest.approx(100 * 2 / 3)
    assert m["lybunt_count"] == 1 and m["lybunt_value"] == pytest.approx(300.0)
    assert m["sybunt_count"] == 1
    assert m["new_donor_retention"] == pytest.approx(100 * 2 / 3)  # A, B, E first gave in LY; A and E gave again
    assert m["new_donors_ty"] == 1
    assert pack.tables["lybunt_priority"][0]["name"] == "Bob Kim"


def test_shopify_line_items_inherit_order_fields():
    csv = ("Name,Created at,Lineitem name,Lineitem quantity,Lineitem price,Email\n"
           "#1001,2026-09-01 10:00:00 -0400,Mug,2,12.00,a@x.com\n"
           "#1001,,Tea,1,8.00,\n"
           "#1002,2026-09-02 11:00:00 -0400,Mug,1,12.00,b@x.com\n")
    practice, df = ingest.load(csv)
    assert practice == "smb"
    assert len(df) == 3
    assert df.net_sales.sum() == pytest.approx(44.0)
    assert (df[df.order_id == "#1001"].customer_id == "a@x.com").all()


def test_unrecognized_export_fails_loudly():
    with pytest.raises(ingest.IngestError):
        ingest.load("foo,bar\n1,2\n")


def test_validator_catches_invented_numbers():
    _, df = ingest.load(DONOR_CSV)
    pack = metrics_donor.compute(df, "Test Org")
    good = {"headline": "Retention is 66.7%.", "situation": "",
            "findings": [{"title": "t", "body": "Retention is 66.7% and $300 is at risk.", "metric_ids": ["retention_rate"]}],
            "recommendations": [{"title": "r", "action": "call within 2 weeks", "rationale": "", "metric_ids": ["lybunt_value"],
                                 "owner": "ED", "timeline": "2 weeks"}]}
    assert validate(good, pack) == []
    bad = dict(good, findings=[{"title": "t", "body": "Retention could hit 92% and raise $48,000.", "metric_ids": ["retention_rate"]}])
    problems = validate(bad, pack)
    assert any("92" in p for p in problems) and any("48,000" in p for p in problems)
    uncited = dict(good, findings=[{"title": "t", "body": "ok", "metric_ids": []}])
    assert any("cites no metric" in p for p in validate(uncited, pack))


def test_number_parsing():
    assert [v for _, v in numbers_in("raised $12.5k from 40 donors, 18.0% retention")] == [12500.0, 40.0, 18.0]
    assert is_grounded(12345.0, [12345.4])
    assert not is_grounded(9999.0, [12345.0])


@pytest.mark.parametrize("practice_file", ["SYNTHETIC_bloomerang_transactions.csv", "SYNTHETIC_square_item_sales.csv"])
def test_template_reports_are_fully_grounded(practice_file):
    path = ROOT / "sample_data" / practice_file
    if not path.exists():
        from sample_data.make_samples import donors, square
        donors(ROOT / "sample_data" / "SYNTHETIC_bloomerang_transactions.csv")
        square(ROOT / "sample_data" / "SYNTHETIC_square_item_sales.csv")
    result = pipeline.run(path.read_bytes(), "Sample Org", {"signer": "Jordan, Executive Director"}, use_llm=False)
    assert result.analyst == "template"
    assert result.violations == []
    assert len(result.report["findings"]) >= 3
    assert len(result.report["recommendations"]) == 3
    assert "Appendix" in result.html


def test_smb_metrics_on_sample():
    path = ROOT / "sample_data" / "SYNTHETIC_square_item_sales.csv"
    _, df = ingest.load(path.read_bytes())
    pack = metrics_smb.compute(df, "Cafe")
    assert pack.metrics["items_for_80pct"].value <= pack.metrics["items_total"].value
    assert "peak_hour_share" in pack.metrics
    assert "repeat_customer_rate" in pack.metrics
    report = TemplateAnalyst().write(pack, {})
    assert validate(report, pack) == []


def test_llm_analyst_repairs_then_strips_ungrounded(monkeypatch):
    from engine.analyst import LLMAnalyst, Provider
    import json as _json

    _, df = ingest.load(DONOR_CSV)
    pack = metrics_donor.compute(df, "Test Org")
    bad = {"headline": "Retention is 66.7%.", "situation": "",
           "findings": [{"title": "t", "body": "You could raise $48,000.", "metric_ids": ["retention_rate"]},
                        {"title": "ok", "body": "$300 is at risk.", "metric_ids": ["lybunt_value"]}],
           "recommendations": [{"title": "r", "action": "call Bob", "rationale": "", "metric_ids": ["lybunt_value"],
                                "owner": "ED", "timeline": "2 weeks"}], "letters": []}
    calls = []

    def fake_chat(self, messages):
        calls.append(messages)
        return "```json\n" + _json.dumps(bad) + "\n```"  # model ignores the repair request

    monkeypatch.setattr(LLMAnalyst, "_chat", fake_chat)
    analyst = LLMAnalyst([Provider("stub", "http://x", "k", "m")])
    report = analyst.write(pack, {})
    assert len(calls) == 2  # one repair round was attempted
    assert [f["title"] for f in report["findings"]] == ["ok"]  # the invented $48,000 was dropped
    assert validate(report, pack) == []
