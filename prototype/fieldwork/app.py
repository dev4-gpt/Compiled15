"""Fieldwork web app: upload an export, get a consultant-grade deck in under a minute.

Run:  uvicorn app:app --reload
Env:  LLM_BASE_URL / LLM_API_KEY / LLM_MODEL (+ FALLBACK_1_*, FALLBACK_2_*)  optional
      MONGODB_URI            optional (in-memory otherwise)
      PAYMENT_LINK           Stripe Payment Link (or any checkout URL) shown on the preview
      ADMIN_TOKEN            unlocks /engagements/{id}/mark-paid for manual payment confirmation
      PREVIEW_ONLY=1         hide recommendations and action lists until paid
"""

from __future__ import annotations

import json
import os
import tempfile
import uuid
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse

from bloomerang import BloomerangClient
from engine import ingest, pipeline
from engine.render import render_pdf
from store import make_store, now

app = FastAPI(title="Fieldwork")
store = make_store()
OUT = Path(os.getenv("OUTPUT_DIR", tempfile.gettempdir())) / "fieldwork"
OUT.mkdir(parents=True, exist_ok=True)

INTAKE_QUESTIONS = {
    "goal": "What is the one number you most want to improve this quarter?",
    "constraint": "What is your biggest constraint (time, staff, cash, other)?",
    "tried": "What have you already tried?",
    "signer": "Who signs letters / owns the plan (name and title)?",
}

FORM = """<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Fieldwork</title><style>
body{font-family:Inter,-apple-system,Segoe UI,Roboto,sans-serif;max-width:720px;margin:40px auto;padding:0 16px;color:#14213d}
label{display:block;margin-top:14px;font-weight:600} input,select,textarea{width:100%;padding:10px;margin-top:6px;border:1px solid #cbd5e1;border-radius:8px;font:inherit}
button{margin-top:20px;padding:12px 18px;border:0;border-radius:8px;background:#0f766e;color:#fff;font-weight:700;font-size:16px;cursor:pointer}
.muted{color:#5c677d}.box{background:#f1f5f9;border-radius:10px;padding:14px;margin-top:20px}</style></head><body>
<h1>Fieldwork</h1><p class=muted>Upload your export. Get the diagnostic a consultant would charge hundreds of dollars for, in about a minute.
Every number is computed from your file and traceable in the appendix.</p>
<form action="/engagements" method="post" enctype="multipart/form-data">
<label>Organization name<input name="org_name" required></label>
<label>What are you uploading?<select name="practice">
<option value="">Detect automatically</option><option value="donor">Donor gifts (Bloomerang, Givebutter, spreadsheet)</option>
<option value="smb">Sales (Square, Shopify, Toast, POS)</option></select></label>
<label>Export file (CSV)<input type="file" name="file" accept=".csv" required></label>
__INTAKE__
<button type="submit">Run diagnostic</button></form>
<div class=box><strong>Bloomerang customer?</strong> <form action="/engagements/bloomerang" method="post">
<label>Organization name<input name="org_name" required></label>
<label>Bloomerang private API key (read-only use; never stored)<input name="api_key" type="password" required></label>
<button type="submit">Pull from Bloomerang</button></form></div></body></html>"""


def _intake_html() -> str:
    return "".join(f'<label>{q}<input name="{k}"></label>' for k, q in INTAKE_QUESTIONS.items())


def _create(data: bytes | str, org_name: str, practice: str | None, intake: dict[str, str]) -> str:
    try:
        result = pipeline.run(data, org_name, intake, practice or None)
    except ingest.IngestError as e:
        raise HTTPException(status_code=422, detail=str(e))
    eid = uuid.uuid4().hex[:10]
    store.save({
        "_id": eid, "created_at": now(), "org_name": org_name, "practice": result.pack.practice,
        "intake": intake, "evidence": result.pack.to_dict(), "report": result.report, "analyst": result.analyst,
        "violations": result.violations, "log": result.log, "seconds": result.seconds, "paid": False,
    })
    (OUT / f"{eid}.html").write_text(result.html)
    return eid


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return FORM.replace("__INTAKE__", _intake_html())


@app.post("/engagements")
async def create(org_name: str = Form(...), practice: str = Form(""), file: UploadFile = File(...),
                 goal: str = Form(""), constraint: str = Form(""), tried: str = Form(""), signer: str = Form("")):
    intake = {"goal": goal, "constraint": constraint, "tried": tried, "signer": signer}
    eid = _create(await file.read(), org_name, practice, intake)
    return RedirectResponse(f"/engagements/{eid}", status_code=303)


@app.post("/engagements/bloomerang")
def create_from_bloomerang(org_name: str = Form(...), api_key: str = Form(...)):
    try:
        csv_text = BloomerangClient(api_key).to_canonical_csv()
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Bloomerang API error: {e}")
    eid = _create(csv_text, org_name, "donor", {})
    return RedirectResponse(f"/engagements/{eid}", status_code=303)


def _doc(eid: str) -> dict:
    doc = store.get(eid)
    if not doc:
        raise HTTPException(status_code=404, detail="not found")
    return doc


@app.get("/engagements/{eid}", response_class=HTMLResponse)
def view(eid: str) -> str:
    doc = _doc(eid)
    html = (OUT / f"{eid}.html").read_text()
    pay = os.getenv("PAYMENT_LINK")
    if os.getenv("PREVIEW_ONLY") == "1" and not doc.get("paid"):
        # Show the cover and findings; recommendations and action lists unlock after payment.
        parts = html.split('<section class="slide">')
        html = '<section class="slide">'.join(parts[:3]) + "</body></html>"
    if pay and not doc.get("paid"):
        banner = (f'<div style="position:sticky;top:0;background:#0f766e;color:#fff;padding:12px;text-align:center;'
                  f'font-family:sans-serif;z-index:9">Get the full plan, priority lists and drafted letters: '
                  f'<a style="color:#fff;font-weight:700" href="{pay}?client_reference_id={eid}">unlock</a></div>')
        html = html.replace("<body>", "<body>" + banner, 1)
    return html


@app.get("/engagements/{eid}/pdf")
def pdf(eid: str):
    doc = _doc(eid)
    if os.getenv("PREVIEW_ONLY") == "1" and not doc.get("paid"):
        raise HTTPException(status_code=402, detail="payment required")
    path = OUT / f"{eid}.pdf"
    if not path.exists() and not render_pdf((OUT / f"{eid}.html").read_text(), path):
        raise HTTPException(status_code=503, detail="PDF renderer unavailable; use the HTML view and print to PDF")
    return FileResponse(path, media_type="application/pdf", filename=f"{doc['org_name']}-diagnostic.pdf")


@app.get("/engagements/{eid}/evidence.json")
def evidence(eid: str):
    doc = _doc(eid)
    return JSONResponse(json.loads(json.dumps({k: doc[k] for k in ("evidence", "report", "analyst", "violations", "log")},
                                              default=str)))


@app.post("/engagements/{eid}/mark-paid")
def mark_paid(eid: str, token: str = Form(...)):
    if not os.getenv("ADMIN_TOKEN") or token != os.getenv("ADMIN_TOKEN"):
        raise HTTPException(status_code=403, detail="bad token")
    _doc(eid)
    store.update(eid, {"paid": True, "paid_at": now()})
    return {"ok": True}


@app.get("/health")
def health():
    from engine.analyst import providers_from_env
    return {"store": store.kind, "llm_providers": [p.name for p in providers_from_env()]}
