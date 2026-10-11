"""DonorPulse metrics: the retention audit a fundraising consultant would run.

Windows are trailing 12 months ("this year", TY) and the 12 months before that
("last year", LY), ending at the latest gift date in the file. This avoids
fiscal-year assumptions and works on any export.

Terms:
- Retention rate = donors who gave in LY and again in TY / donors who gave in LY.
- LYBUNT = gave Last Year But Unfortunately Not This year.
- SYBUNT = gave Some Year (before LY) But Unfortunately Not This year (or LY).
"""

from __future__ import annotations

import pandas as pd

from .evidence import EvidencePack, Metric

# External benchmark shown for context only, never mixed into client metrics.
FEP_RETENTION_BENCHMARK = Metric(
    id="bench_fep_retention",
    label="Sector donor retention benchmark (FEP, full-year 2025)",
    value=43.3,
    unit="pct",
    formula="Fundraising Effectiveness Project year-end report",
    source="FEP 2025 year-end figure via search extracts (verify before quoting)",
)


def compute(df: pd.DataFrame, org_name: str) -> EvidencePack:
    as_of = df["date"].max()
    ty_start = as_of - pd.DateOffset(years=1)
    ly_start = as_of - pd.DateOffset(years=2)

    ty = df[df["date"] > ty_start]
    ly = df[(df["date"] > ly_start) & (df["date"] <= ty_start)]
    before = df[df["date"] <= ly_start]

    ty_donors, ly_donors, before_donors = set(ty.donor_id), set(ly.donor_id), set(before.donor_id)
    retained = ly_donors & ty_donors
    lybunt = ly_donors - ty_donors
    sybunt = before_donors - ly_donors - ty_donors
    first_gift = df.groupby("donor_id")["date"].min()
    ly_new = {d for d in ly_donors if ly_start < first_gift[d] <= ty_start}
    ty_new = {d for d in ty_donors if first_gift[d] > ty_start}

    pack = EvidencePack(
        practice="donor",
        org_name=org_name,
        as_of=as_of.date().isoformat(),
        period=f"{(ty_start + pd.Timedelta(days=1)).date()} to {as_of.date()} vs prior 12 months",
    )
    add = pack.add
    pack.constants.update({"top donor share cut (%)": 10, "win-back scenario (%)": 10,
                           "lapse-risk age (months)": 9, "lapse-risk age (days)": 270,
                           "thank-you window (hours)": 48, "impact update (days)": 30, "second ask (days)": 90})

    add(Metric("donors_ty", "Donors in the last 12 months", len(ty_donors), "count", "unique donor_id with a gift in TY"))
    add(Metric("donors_ly", "Donors in the prior 12 months", len(ly_donors), "count", "unique donor_id with a gift in LY"))
    add(Metric("revenue_ty", "Gift revenue, last 12 months", float(ty.amount.sum()), "usd", "sum(amount) in TY"))
    add(Metric("revenue_ly", "Gift revenue, prior 12 months", float(ly.amount.sum()), "usd", "sum(amount) in LY"))
    if ly.amount.sum() > 0:
        add(Metric("revenue_change_pct", "Revenue change vs prior 12 months",
                   100 * (ty.amount.sum() / ly.amount.sum() - 1), "pct", "(revenue_ty / revenue_ly - 1) x 100"))
    if ly_donors:
        add(Metric("retention_rate", "Donor retention rate", 100 * len(retained) / len(ly_donors), "pct",
                   "donors in both LY and TY / donors in LY"))
    if ly_new:
        add(Metric("new_donor_retention", "First-year donor retention", 100 * len(ly_new & ty_donors) / len(ly_new),
                   "pct", "donors whose first gift was in LY and who gave again in TY / those first-time LY donors"))
    add(Metric("new_donors_ty", "New donors acquired, last 12 months", len(ty_new), "count", "donors whose first gift is in TY"))
    add(Metric("lybunt_count", "LYBUNT donors (gave last year, not this year)", len(lybunt), "count", "LY donors - TY donors"))
    lybunt_value = float(ly[ly.donor_id.isin(lybunt)].amount.sum())
    add(Metric("lybunt_value", "Last-year giving from LYBUNT donors (revenue at risk)", lybunt_value, "usd",
               "sum(LY amount) for LYBUNT donors"))
    add(Metric("sybunt_count", "SYBUNT donors (lapsed 2+ years)", len(sybunt), "count", "donors before LY with no gift in LY or TY"))
    if len(ty):
        add(Metric("avg_gift_ty", "Average gift, last 12 months", float(ty.amount.mean()), "usd", "mean(amount) in TY"))
        per_donor = ty.groupby("donor_id").amount.sum().sort_values(ascending=False)
        top_n = max(1, int(round(len(per_donor) * 0.10)))
        add(Metric("top10_share", "Share of TY revenue from top 10% of donors",
                   100 * per_donor.head(top_n).sum() / per_donor.sum(), "pct", "sum(top 10% donors) / revenue_ty"))
        gifts_per_donor = ty.groupby("donor_id").size()
        add(Metric("multi_gift_share", "Donors giving 2+ times in last 12 months",
                   100 * (gifts_per_donor >= 2).mean(), "pct", "donors with >= 2 TY gifts / TY donors"))
    if len(retained) and len(ly_donors):
        # What one more retention point is worth: avg LY giving of a retained donor.
        avg_retained_value = float(ty[ty.donor_id.isin(retained)].groupby("donor_id").amount.sum().mean())
        add(Metric("value_per_retained_donor", "Average 12-month giving of a retained donor", avg_retained_value,
                   "usd", "mean(TY total) over retained donors"))
        win_back_10 = 0.10 * len(lybunt) * avg_retained_value
        add(Metric("win_back_10pct_value", "Revenue if 10% of LYBUNT donors are won back", win_back_10, "usd",
                   "0.10 x lybunt_count x value_per_retained_donor"))
    add(FEP_RETENTION_BENCHMARK)

    # Action tables.
    names = df.drop_duplicates("donor_id", keep="last").set_index("donor_id")[["donor_name", "email"]]
    last_gift = df.groupby("donor_id")["date"].max()
    ly_totals = ly.groupby("donor_id").amount.sum()
    lifetime = df.groupby("donor_id").amount.sum()
    n_gifts = df.groupby("donor_id").size()

    lyb = sorted(lybunt, key=lambda d: -ly_totals.get(d, 0))
    pack.tables["lybunt_priority"] = [
        {
            "donor_id": d,
            "name": names.loc[d, "donor_name"],
            "email": names.loc[d, "email"],
            "last_year_total": round(float(ly_totals.get(d, 0)), 2),
            "lifetime_total": round(float(lifetime[d]), 2),
            "gifts": int(n_gifts[d]),
            "days_since_last_gift": int((as_of - last_gift[d]).days),
        }
        for d in lyb
    ]

    # Upgrade candidates: retained donors whose TY giving exceeds LY giving, ranked by TY total.
    ty_totals = ty.groupby("donor_id").amount.sum()
    up = [d for d in retained if ty_totals[d] > ly_totals.get(d, 0)]
    up.sort(key=lambda d: -ty_totals[d])
    pack.tables["upgrade_candidates"] = [
        {"donor_id": d, "name": names.loc[d, "donor_name"], "this_year_total": round(float(ty_totals[d]), 2),
         "last_year_total": round(float(ly_totals.get(d, 0)), 2), "gifts": int(n_gifts[d])}
        for d in up
    ]

    # Lapse risk among current donors: single-gift TY donors whose gift is 9+ months old.
    risk = [d for d in ty_donors if (ty.donor_id == d).sum() == 1 and (as_of - last_gift[d]).days >= 270]
    risk.sort(key=lambda d: -ty_totals[d])
    add(Metric("lapse_risk_count", "Current donors at lapse risk (one gift, 9+ months ago)", len(risk), "count",
               "TY donors with exactly 1 TY gift and last gift >= 270 days before as_of"))
    pack.tables["lapse_risk"] = [
        {"donor_id": d, "name": names.loc[d, "donor_name"], "this_year_total": round(float(ty_totals[d]), 2),
         "days_since_last_gift": int((as_of - last_gift[d]).days)}
        for d in risk
    ]

    if len(df) < 50:
        pack.notes.append("Small file: fewer than 50 gifts, so percentages move a lot with each donor.")
    if before.empty:
        pack.notes.append("File covers under 2 years, so SYBUNT (2+ year lapsed) cannot be measured.")
    return pack
