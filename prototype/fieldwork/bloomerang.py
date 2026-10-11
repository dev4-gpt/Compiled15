"""Minimal Bloomerang REST v2 client (read-only by default).

Per public docs and integrator write-ups (verify with Bloomerang staff at the event):
- Base URL https://api.bloomerang.co/v2, private key in the X-API-KEY header.
- GET /transactions and GET /constituents page with skip/take (take <= 50).
- There is NO sandbox: every call hits the nonprofit's live data, so this client
  never writes unless write_note() is called explicitly.

Output is a CSV string in the canonical donor schema, so the rest of the
pipeline treats API data and CSV exports identically.
"""

from __future__ import annotations

import csv
import io
import time
from typing import Any, Iterator

import httpx

BASE_URL = "https://api.bloomerang.co/v2"


class BloomerangClient:
    def __init__(self, api_key: str, base_url: str = BASE_URL, timeout: float = 30.0):
        self._http = httpx.Client(base_url=base_url, timeout=timeout,
                                  headers={"X-API-KEY": api_key, "Accept": "application/json"})

    def _paged(self, path: str, params: dict[str, Any] | None = None, take: int = 50,
               limit: int = 20000) -> Iterator[dict[str, Any]]:
        skip = 0
        while skip < limit:
            for attempt in range(4):
                r = self._http.get(path, params={**(params or {}), "skip": skip, "take": take})
                if r.status_code != 429:
                    break
                time.sleep(2 ** attempt)
            r.raise_for_status()
            body = r.json()
            rows = body.get("Results", body if isinstance(body, list) else [])
            yield from rows
            if len(rows) < take:
                return
            skip += take

    def constituents(self) -> dict[int, dict[str, Any]]:
        out = {}
        for c in self._paged("/constituents"):
            email = (c.get("PrimaryEmail") or {}).get("Value", "") if isinstance(c.get("PrimaryEmail"), dict) else ""
            out[c.get("Id")] = {"name": c.get("FullName") or c.get("InformalName") or str(c.get("AccountNumber")),
                                "account": c.get("AccountNumber"), "email": email}
        return out

    def transactions(self) -> Iterator[dict[str, Any]]:
        yield from self._paged("/transactions", {"orderBy": "Date", "orderDirection": "Asc"})

    def to_canonical_csv(self) -> str:
        people = self.constituents()
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(["donor_id", "donor_name", "email", "date", "amount"])
        for t in self.transactions():
            cid = t.get("AccountId")
            p = people.get(cid, {"name": str(cid), "account": cid, "email": ""})
            w.writerow([p["account"] or cid, p["name"], p["email"], t.get("Date"), t.get("Amount")])
        return buf.getvalue()

    def write_note(self, account_id: int, subject: str, note: str) -> dict[str, Any]:
        """Optional write-back: log the audit as an interaction on a constituent (live data!)."""
        r = self._http.post("/interaction", json={
            "AccountId": account_id, "Date": time.strftime("%Y-%m-%d"), "Channel": "Other",
            "Purpose": "Other", "Subject": subject, "Note": note, "IsInbound": False})
        r.raise_for_status()
        return r.json()
