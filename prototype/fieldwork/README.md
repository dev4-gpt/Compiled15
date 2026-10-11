# Fieldwork

**Consultant-grade diagnostics from the data a small organization already has.** Upload a donor export or a POS sales export. About a minute later you get the deck a consultant would produce:
- findings;
- three recommendations, each with an owner and a deadline;
- priority action lists;
- drafted outreach letters;
- an appendix listing every metric with its formula.

**Every number is computed by code, and the writer (LLM or template) may only cite those numbers.** A validator rejects anything it can't trace back.

Practices:
- **Donor retention audit (DonorPulse):** for nonprofits on Bloomerang (CSV export or REST API), Givebutter, or a spreadsheet. Covers retention vs. sector benchmark, first-year retention, LYBUNT/SYBUNT, revenue at risk, a win-back priority list, upgrade candidates, lapse risk and drafted letters.
- **Sales diagnostic:** for Square item-detail, Shopify order and generic POS exports. Covers trend, 80/20 item concentration, slow days, peak hour, declining items, basket size and repeat customers.

## Architecture

```
CSV export / Bloomerang API / intake answers
  -> engine/ingest.py        detect source, map column aliases, normalize (Shopify multi-row orders handled)
  -> engine/metrics_*.py     deterministic pandas metrics; each has id, value, unit, formula, source
  -> engine/evidence.py      EvidencePack: metrics + action tables + declared method constants
  -> engine/analyst.py       LLMAnalyst (any OpenAI-compatible endpoint, ordered fallback) or TemplateAnalyst
  -> engine/validate.py      every number must exist in the pack; every finding must cite metric ids;
                             one repair round, then ungrounded items are dropped
  -> engine/render.py        Jinja2 deck (templates/deck.html) -> PDF via headless Chromium
  -> app.py + store.py       FastAPI app, MongoDB Atlas (or in-memory), payment link + paywall
```

## Run

```bash
pip install -r requirements.txt
python sample_data/make_samples.py     # SYNTHETIC files for local testing only
pytest -q                              # 10 tests
uvicorn app:app --reload               # open http://localhost:8000
```

Optional environment variables:

| Var | Purpose |
|---|---|
| `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` | Primary analyst (put Luminal here) |
| `FALLBACK_1_*`, `FALLBACK_2_*` | Same three keys for backup providers (Groq, Cerebras, OpenRouter) |
| `MONGODB_URI` | Atlas connection string; falls back to memory if unreachable |
| `PAYMENT_LINK` | Stripe Payment Link (or any checkout URL) shown on the report |
| `PREVIEW_ONLY=1` | Show only the cover and findings until paid |
| `ADMIN_TOKEN` | Enables `POST /engagements/{id}/mark-paid` |
| `CHROME_PATH` | Chromium binary for PDF output |

Endpoints:
- `GET /` upload form
- `POST /engagements` run on an upload
- `POST /engagements/bloomerang` pull from the Bloomerang API
- `GET /engagements/{id}` deck
- `/engagements/{id}/pdf`
- `/engagements/{id}/evidence.json` the full audit trail
- `/health`

## Honest limits
- Bloomerang API paths and export headers come from public docs and integrator write-ups, not a live account. Bloomerang has **no sandbox**, so test only with a key the organization gives you. Unknown headers fail loudly and list the columns found.
- The FEP retention benchmark (43.3%, full-year 2025) came from search extracts. Verify it before quoting.
- Template wording is rule-based. With an LLM key the prose improves, and the validator still guarantees the numbers.
- Sample files are synthetic and exist for tests only. Proof comes from a real organization's own export.
