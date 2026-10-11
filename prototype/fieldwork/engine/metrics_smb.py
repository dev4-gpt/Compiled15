"""Fieldwork SMB metrics: the sales diagnostic a small-business consultant would run.

Works on item-level sales exports (Square item detail, Shopify orders, generic POS).
The analysis window is the last 8 weeks ending at the latest sale, compared with
the 8 weeks before, so trends are like-for-like.
"""

from __future__ import annotations

import pandas as pd

from .evidence import EvidencePack, Metric

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def compute(df: pd.DataFrame, org_name: str, weeks: int = 8) -> EvidencePack:
    as_of = df["date"].max()
    cur_start = as_of - pd.Timedelta(weeks=weeks)
    prev_start = cur_start - pd.Timedelta(weeks=weeks)
    cur = df[df["date"] > cur_start]
    prev = df[(df["date"] > prev_start) & (df["date"] <= cur_start)]

    pack = EvidencePack(
        practice="smb",
        org_name=org_name,
        as_of=as_of.date().isoformat(),
        period=f"last {weeks} weeks to {as_of.date()} vs the {weeks} weeks before",
    )
    add = pack.add
    pack.constants.update({"Pareto cut (%)": 80, "tail cut (%)": 5, "analysis window (weeks)": weeks})

    rev_cur, rev_prev = float(cur.net_sales.sum()), float(prev.net_sales.sum())
    orders_cur = cur.order_id.nunique()
    add(Metric("revenue_cur", f"Net sales, last {weeks} weeks", rev_cur, "usd", "sum(net_sales) in current window"))
    add(Metric("revenue_prev", f"Net sales, prior {weeks} weeks", rev_prev, "usd", "sum(net_sales) in prior window"))
    if rev_prev > 0:
        add(Metric("revenue_change_pct", "Net sales change vs prior period", 100 * (rev_cur / rev_prev - 1), "pct",
                   "(revenue_cur / revenue_prev - 1) x 100"))
    add(Metric("orders_cur", f"Orders, last {weeks} weeks", orders_cur, "count", "unique order_id in current window"))
    if orders_cur:
        add(Metric("avg_ticket", "Average order value", rev_cur / orders_cur, "usd", "revenue_cur / orders_cur"))
        prev_orders = prev.order_id.nunique()
        if prev_orders:
            add(Metric("avg_ticket_prev", "Average order value, prior period", rev_prev / prev_orders, "usd",
                       "revenue_prev / prior orders"))
        items_per_order = cur.groupby("order_id").qty.sum().mean()
        add(Metric("items_per_order", "Items per order", float(items_per_order), "ratio", "mean(sum(qty) per order)"))
    add(Metric("weekly_revenue", "Average weekly net sales", rev_cur / weeks, "usd", f"revenue_cur / {weeks}"))

    # Item concentration (Pareto).
    by_item = cur.groupby("item").net_sales.sum().sort_values(ascending=False)
    if len(by_item):
        cum = by_item.cumsum() / by_item.sum()
        n80 = int((cum < 0.8).sum() + 1)
        add(Metric("items_total", "Items sold in period", len(by_item), "count", "unique items with sales"))
        add(Metric("items_for_80pct", "Items producing 80% of sales", n80, "count", "smallest top-N items reaching 80% of revenue"))
        add(Metric("top_item_share", f"Share of sales from top item ({by_item.index[0]})",
                   100 * by_item.iloc[0] / by_item.sum(), "pct", "top item revenue / revenue_cur"))
        tail = by_item[cum > 0.95]
        add(Metric("tail_items", "Items in the bottom 5% of sales", len(tail), "count", "items after cumulative 95%"))
        prev_item = prev.groupby("item").net_sales.sum()
        movers = []
        for item, value in by_item.items():
            before = float(prev_item.get(item, 0.0))
            movers.append({"item": item, "current": round(float(value), 2), "prior": round(before, 2),
                           "change": round(float(value) - before, 2)})
        decliners = sorted([m for m in movers if m["prior"] > 0], key=lambda m: m["change"])[:5]
        pack.tables["top_items"] = [{"item": i, "net_sales": round(float(v), 2),
                                     "share_pct": round(100 * float(v) / by_item.sum(), 1)} for i, v in by_item.head(10).items()]
        pack.tables["declining_items"] = [m for m in decliners if m["change"] < 0]
        pack.tables["tail_items"] = [{"item": i, "net_sales": round(float(v), 2)} for i, v in tail.items()][:15]
        if decliners and decliners[0]["change"] < 0:
            d = decliners[0]
            add(Metric("top_decliner_drop", f"Largest item decline ({d['item']})", -d["change"], "usd",
                       "prior - current net sales for the item with the largest drop"))

    # Day-of-week and hour patterns.
    dow = cur.groupby(cur.date.dt.dayofweek).net_sales.sum() / weeks
    if len(dow):
        best, worst = int(dow.idxmax()), int(dow.idxmin())
        add(Metric("best_day_revenue", f"Average sales on {DAYS[best]} (best day)", float(dow.max()), "usd",
                   "mean weekly net sales on that weekday"))
        add(Metric("worst_day_revenue", f"Average sales on {DAYS[worst]} (slowest day)", float(dow.min()), "usd",
                   "mean weekly net sales on that weekday"))
        pack.tables["by_weekday"] = [{"day": DAYS[d], "avg_net_sales": round(float(v), 2)} for d, v in dow.sort_index().items()]
    has_time = (cur.date.dt.hour != 0).any()
    if has_time:
        hours = cur.groupby(cur.date.dt.hour).net_sales.sum() / weeks
        add(Metric("peak_hour_share", f"Share of sales in peak hour ({int(hours.idxmax())}:00)",
                   100 * hours.max() / hours.sum(), "pct", "peak hour revenue / revenue_cur"))
        pack.tables["by_hour"] = [{"hour": int(h), "avg_weekly_net_sales": round(float(v), 2)} for h, v in hours.items()]
    else:
        pack.notes.append("No time-of-day in the export, so hourly staffing analysis is skipped.")

    # Repeat customers (only if the export identifies customers).
    known = cur[cur.customer_id.astype(str).str.strip().ne("") & cur.customer_id.ne("nan")]
    if known.customer_id.nunique() >= 10:
        visits = known.groupby("customer_id").order_id.nunique()
        add(Metric("repeat_customer_rate", "Identified customers with 2+ orders", 100 * (visits >= 2).mean(), "pct",
                   "customers with >= 2 orders / identified customers"))
        add(Metric("identified_order_share", "Orders linked to a known customer",
                   100 * known.order_id.nunique() / max(orders_cur, 1), "pct", "orders with customer_id / all orders"))
    else:
        pack.notes.append("Fewer than 10 identified customers, so repeat-rate analysis is skipped.")

    by_cat = cur.groupby("category").net_sales.sum().sort_values(ascending=False)
    pack.tables["by_category"] = [{"category": c, "net_sales": round(float(v), 2),
                                   "share_pct": round(100 * float(v) / max(by_cat.sum(), 1e-9), 1)} for c, v in by_cat.items()]
    if prev.empty:
        pack.notes.append("No prior period in the file, so trend metrics are unavailable.")
    return pack
