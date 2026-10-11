# Track 4: AI-Native Compliance Infrastructure, MVP: RegDiff (LicenseLoop vertical)

**Score:** RegDiff 7.74 weighted / 6.58 risk-adjusted; LicenseLoop 7.70 / 6.54. Rank 4 of 6.
**Decision:** the two are within 0.04 points, which is a statistical tie, so they are merged. RegDiff is the engine: regulation change in, diff of affected obligations, policies and controls out, every line cited. LicenseLoop is the first vertical: a fintech's state money-transmitter and lending licenses. This keeps RegDiff's general-purpose engine and LicenseLoop's literal fit with YC's financial-compliance and state-licensing text.

**One-liner:** When a state regulator publishes a new rule or bulletin, RegDiff tells a fintech exactly which licenses, policies and controls it affects, what has to change and by when, with the regulator's own words cited next to each item.

## 1. Thesis

Compliance today is a human pipeline: lawyers read notices, update spreadsheets and email owners. A fintech licensed in 40+ states deals with a steady stream of bulletins, renewals and exam requests. AI-native compliance means a machine-readable model of obligations that updates itself when the source text changes. Humans review diffs instead of reading everything.

## 2. Candidates considered

| Concept | Risk-adj | Verdict |
|---|---|---|
| **RegDiff** (engine) | 6.58 | **Chosen** as the engine |
| **LicenseLoop** (vertical) | 6.54 | **Chosen** as the demo vertical (statistical tie) |
| EvidenceBot, SOC 2 evidence collection | 6.02 | Crowded (Vanta, Drata); weak RFS fit |

## 3. User, buyer, wedge

- **User:** compliance analyst / licensing manager at a Series A-D fintech (payments, lending, earned-wage access, crypto on-ramps).
- **Buyer:** Chief Compliance Officer; budget replaces outside counsel hours and licensing consultants.
- **Wedge:** GRC tools (Vanta, Drata) cover security frameworks; licensing tools track deadlines. Nobody connects a new regulatory text to affected obligations and controls automatically, with citations.

## 4. MVP scope

- **In:** obligation register for 10 states × 2 license types (money transmitter, consumer lender), built from public statutes and regulations; deadline engine (renewals, reports, surety bonds); ingestion of a new regulator notice (PDF or URL); clause segmentation; obligation extraction to a typed schema; semantic + rule matching to the existing register and to a sample company policy set; diff view (added / changed / removed obligations); task generation with owners and due dates; review-required labels; audit trail.
- **Out:** filing with NMLS, real legal opinions, all 50 states.

## 5. End-to-end architecture

```
Regulator notice (PDF / HTML / Federal Register / state site)
        │
        ▼
Parse + segment (Docling / unstructured) ──► clauses with page/para anchors
        │
        ▼
Obligation extractor (LLM, JSON schema):
  {actor, action, object, condition, deadline, jurisdiction, license_type, citation}
        │
        ├──► Match against obligation register (embeddings + jurisdiction/license filters)
        │          │
        │          ▼
        │    Diff engine: NEW │ CHANGED (field-level) │ REPEALED │ NO-OP
        │          │
        ├──► Map to company policies & controls (policy chunks, control IDs)
        │          │
        ▼          ▼
  Task generator (owner, due date, severity) ──► Review queue (approve / edit / reject)
        │
        ▼
  Audit log (who approved what, which text version) ── MongoDB
```

**Grounding rule:** every generated obligation must point to a clause anchor whose text contains its key terms (string-overlap check). Ungrounded items are dropped or flagged. That check is what makes it demo-safe.

## 6. Data model

- `sources {id, jurisdiction, type: statute|reg|bulletin, url, version_hash, fetched_at}`
- `clauses {source_id, anchor, text, embedding}`
- `obligations {id, jurisdiction, license_type, actor, action, object, condition, deadline_rule, citation_anchor, status, version}`
- `licenses {company, state, type, number, renewal_date, bond_amount, status}`
- `policies {id, title, section, text, controls[]}`
- `diffs {source_id, obligation_id, change: new|changed|repealed, before, after, confidence}`
- `tasks {diff_id, owner, due, severity, state}`, `audit {actor, action, target, ts}`

## 7. Stack and resources

| Need | Choice | Resource |
|---|---|---|
| Document parsing | Docling or unstructured | `docling-project/docling`, `Unstructured-IO/unstructured` |
| Regulatory sources | Federal Register API, eCFR API, state regulator bulletin pages (CSBS for licensing context) | federalregister.gov/developers, ecfr.gov developer docs |
| Extraction | LLM with JSON schema + grounding check | Luminal endpoint; `claude-api` skill for structured outputs |
| Retrieval | MongoDB Atlas Vector Search (sponsor) or pgvector | Atlas docs |
| UI | Next.js dashboard: license map, diff view, review queue | Lovable for scaffold, Vercel deploy |
| Rules | Deadline rules as code (rrule) | `python-dateutil` |
| Fixtures | 10-state register seeded tonight; 1 real recent state bulletin for the live demo; 1 held out | Saved PDFs |

## 8. Eight-hour build plan

| Time | A (ingest) | B (extract + match) | C (register + rules) | D (UI, validation) | Done when |
|---|---|---|---|---|---|
| 12:00-1:00 | Docling parse 3 sources | Obligation schema + prompt | License register + deadlines | Wireframe | Clauses with anchors in DB |
| 1:00-2:30 | Clause segmentation + embeddings | Extraction + grounding check | Policy set + control IDs | License map UI | 20 grounded obligations extracted |
| 2:30-3:30 | Notice ingestion endpoint | Matching + diff classification | Task generator | Talk to 2-3 compliance/legal people | **Checkpoint:** new notice → diff with citations |
| 3:30-4:30 | Version hashing | Policy/control mapping | Audit trail | Diff + review queue UI | Full loop to tasks |
| 4:30-5:30 | Held-out notice run once | Precision check vs hand labels | Metrics | Deck | Eval table |
| 5:30-6:45 | Bug bash, backup video | | | Rehearse | **Code freeze 6:45** |

**Fallback:** if live extraction is noisy, pre-extract the register offline (allowed if declared) and keep only the new notice's extraction live.

## 9. 90-second demo

A map of 10 states, all green. Drop in a new state bulletin PDF. Within about 30 s, 2 states turn amber; the diff view shows "net-worth requirement changed: $100k → $250k, effective Jan 1" with the regulator's sentence highlighted, the affected policy section, and a task assigned to the treasury owner. Approve it; the audit log records it. End on extraction precision on the held-out notice.

## 10. Metrics

- Obligation extraction precision/recall vs. hand labels on the held-out notice.
- Grounding rate (% of obligations whose citation check passes).
- Time from notice to reviewed diff (minutes vs. a typical analyst's hours; cite an interview, not a guess).

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Legal accuracy | Everything is review-required; citations mandatory; positioned as an analyst copilot |
| Judges find it dry | Lead with the map changing color and the dollar amount at stake |
| Hard to validate on site | Pre-book 2 calls with fintech compliance people; LinkedIn outreach tonight |

## 12. Validation and next 30 days

- **At the event:** any fintech founders or engineers present; 2 compliance interviews.
- **Days 1-30:** cover all 50 states for money transmitter licenses; 3 design partners; price per licensed state per year.
