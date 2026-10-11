"""Load client exports and normalize them to canonical schemas.

Donor (practice "donor") canonical columns:
    donor_id, donor_name, email, date, amount
SMB (practice "smb") canonical columns:
    order_id, date, item, category, qty, net_sales, customer_id

Column aliases cover Bloomerang, generic donor CRMs, Square item-detail exports and
Shopify order exports. Export headers vary by account settings, so unknown headers
fail loudly with the list of columns we did find rather than guessing.
"""

from __future__ import annotations

import io
import re
from typing import Iterable

import pandas as pd

DONOR_ALIASES = {
    "donor_id": ["account number", "account id", "accountid", "constituent id", "constituent account number",
                 "donor id", "id", "account"],
    "donor_name": ["name", "full name", "constituent name", "account name", "donor name", "full custom name",
                   "informal name"],
    "first_name": ["first name", "first"],
    "last_name": ["last name", "last"],
    "email": ["email", "primary email", "email address", "primary email address"],
    "date": ["date", "gift date", "transaction date", "donation date", "received date"],
    "amount": ["amount", "gift amount", "total amount", "transaction amount", "donation amount", "net amount"],
}

SMB_ALIASES = {
    "order_id": ["transaction id", "order id", "name", "order", "check #", "order number", "receipt number"],
    "date": ["date", "created at", "order date", "paid at", "opened", "business date"],
    "time": ["time"],
    "item": ["item", "lineitem name", "item name", "menu item", "product", "product name"],
    "category": ["category", "menu group", "product type", "sales category"],
    "qty": ["qty", "quantity", "lineitem quantity", "item qty", "count"],
    "net_sales": ["net sales", "net amount", "net price", "total"],
    "unit_price": ["lineitem price", "price", "unit price", "avg. price"],
    "customer_id": ["customer id", "customer reference id", "email", "customer email", "customer"],
}


class IngestError(ValueError):
    pass


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", str(s).strip().lower())


def _pick(columns: Iterable[str], aliases: list[str]) -> str | None:
    lookup = {_norm(c): c for c in columns}
    for a in aliases:
        if a in lookup:
            return lookup[a]
    return None


def read_csv(data: bytes | str) -> pd.DataFrame:
    if isinstance(data, bytes):
        data = data.decode("utf-8-sig", errors="replace")
    try:
        df = pd.read_csv(io.StringIO(data))
    except (pd.errors.ParserError, pd.errors.EmptyDataError, UnicodeDecodeError) as e:
        raise IngestError(f"This does not look like a CSV export: {e}") from e
    if df.empty:
        raise IngestError("The file has no rows.")
    return df


def _money(series: pd.Series) -> pd.Series:
    cleaned = series.astype(str).str.replace(r"[$,\s]", "", regex=True).str.replace(r"^\((.*)\)$", r"-\1", regex=True)
    return pd.to_numeric(cleaned, errors="coerce")


def detect_practice(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    smb_hits = sum(_pick(cols, SMB_ALIASES[k]) is not None for k in ("item", "qty", "net_sales"))
    donor_hits = sum(_pick(cols, DONOR_ALIASES[k]) is not None for k in ("donor_id", "amount"))
    if _pick(cols, SMB_ALIASES["item"]) and smb_hits >= 2:
        return "smb"
    if donor_hits == 2:
        return "donor"
    raise IngestError(f"Could not recognise this export. Columns found: {cols}")


def normalize_donor(df: pd.DataFrame) -> pd.DataFrame:
    cols = list(df.columns)
    m = {k: _pick(cols, v) for k, v in DONOR_ALIASES.items()}
    missing = [k for k in ("date", "amount") if not m[k]]
    if missing or not (m["donor_id"] or m["donor_name"] or m["email"]):
        raise IngestError(f"Donor export needs a date, an amount and a donor identifier. Columns found: {cols}")
    out = pd.DataFrame()
    if m["donor_name"]:
        out["donor_name"] = df[m["donor_name"]].astype(str)
    elif m["first_name"] or m["last_name"]:
        first = df[m["first_name"]].fillna("").astype(str) if m["first_name"] else ""
        last = df[m["last_name"]].fillna("").astype(str) if m["last_name"] else ""
        out["donor_name"] = (first + " " + last).str.strip()
    else:
        out["donor_name"] = ""
    out["email"] = df[m["email"]].astype(str) if m["email"] else ""
    if m["donor_id"]:
        out["donor_id"] = df[m["donor_id"]].astype(str)
    else:
        out["donor_id"] = out["email"].where(out["email"] != "", out["donor_name"])
    out["date"] = pd.to_datetime(df[m["date"]], errors="coerce")
    out["amount"] = _money(df[m["amount"]])
    out = out.dropna(subset=["date", "amount"])
    out = out[out["amount"] > 0]
    if out.empty:
        raise IngestError("No valid gifts (date + positive amount) found.")
    out.loc[out["donor_name"].isin(["", "nan"]), "donor_name"] = out["donor_id"]
    return out.reset_index(drop=True)


def normalize_smb(df: pd.DataFrame) -> pd.DataFrame:
    cols = list(df.columns)
    m = {k: _pick(cols, v) for k, v in SMB_ALIASES.items()}
    if not (m["date"] and m["item"] and (m["net_sales"] or m["unit_price"])):
        raise IngestError(f"Sales export needs date, item and sales columns. Columns found: {cols}")
    out = pd.DataFrame()
    date = df[m["date"]].astype(str)
    if m["time"]:
        date = date + " " + df[m["time"]].astype(str)
    out["date"] = pd.to_datetime(date, errors="coerce", utc=True).dt.tz_localize(None)
    out["item"] = df[m["item"]].astype(str)
    out["category"] = df[m["category"]].fillna("Uncategorized").astype(str) if m["category"] else "Uncategorized"
    out["qty"] = pd.to_numeric(df[m["qty"]], errors="coerce").fillna(1) if m["qty"] else 1
    if m["net_sales"] and _norm(m["net_sales"]) != "total":
        out["net_sales"] = _money(df[m["net_sales"]])
    elif m["unit_price"]:
        out["net_sales"] = _money(df[m["unit_price"]]) * out["qty"]
    else:
        out["net_sales"] = _money(df[m["net_sales"]])
    out["order_id"] = df[m["order_id"]].astype(str) if m["order_id"] else out.index.astype(str)
    out["customer_id"] = df[m["customer_id"]].fillna("").astype(str) if m["customer_id"] else ""
    # Shopify repeats only line-item fields on extra rows of the same order; fill order-level fields.
    if m["order_id"]:
        out["date"] = out.groupby("order_id")["date"].transform("first")
        out["customer_id"] = out.groupby("order_id")["customer_id"].transform(
            lambda s: s[s.ne("") & s.ne("nan")].iloc[0] if (s.ne("") & s.ne("nan")).any() else "")
    out = out.dropna(subset=["date", "net_sales"])
    if out.empty:
        raise IngestError("No valid sales rows found.")
    return out.reset_index(drop=True)


def load(data: bytes | str, practice: str | None = None) -> tuple[str, pd.DataFrame]:
    df = read_csv(data)
    practice = practice or detect_practice(df)
    if practice == "donor":
        return practice, normalize_donor(df)
    if practice == "smb":
        return practice, normalize_smb(df)
    raise IngestError(f"Unknown practice {practice!r}")
