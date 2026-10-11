"""Engagement storage: MongoDB Atlas when MONGODB_URI is set, in-memory otherwise."""

from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any


class MemoryStore:
    kind = "memory"

    def __init__(self) -> None:
        self._docs: dict[str, dict[str, Any]] = {}

    def save(self, doc: dict[str, Any]) -> None:
        self._docs[doc["_id"]] = doc

    def get(self, eid: str) -> dict[str, Any] | None:
        return self._docs.get(eid)

    def update(self, eid: str, fields: dict[str, Any]) -> None:
        if eid in self._docs:
            self._docs[eid].update(fields)

    def recent(self, n: int = 20) -> list[dict[str, Any]]:
        return sorted(self._docs.values(), key=lambda d: d["created_at"], reverse=True)[:n]


class MongoStore:
    kind = "mongodb"

    def __init__(self, uri: str, db: str = "fieldwork") -> None:
        from pymongo import MongoClient

        self._col = MongoClient(uri, serverSelectionTimeoutMS=5000)[db]["engagements"]
        self._col.create_index("created_at")

    def save(self, doc: dict[str, Any]) -> None:
        self._col.replace_one({"_id": doc["_id"]}, doc, upsert=True)

    def get(self, eid: str) -> dict[str, Any] | None:
        return self._col.find_one({"_id": eid})

    def update(self, eid: str, fields: dict[str, Any]) -> None:
        self._col.update_one({"_id": eid}, {"$set": fields})

    def recent(self, n: int = 20) -> list[dict[str, Any]]:
        return list(self._col.find().sort("created_at", -1).limit(n))


def make_store():
    uri = os.getenv("MONGODB_URI")
    if uri:
        try:
            store = MongoStore(uri)
            store.recent(1)
            return store
        except Exception as e:  # fall back so the demo never dies on Wi-Fi
            print(f"[store] MongoDB unavailable ({e}); using in-memory store")
    return MemoryStore()


def now() -> datetime:
    return datetime.now(timezone.utc)
