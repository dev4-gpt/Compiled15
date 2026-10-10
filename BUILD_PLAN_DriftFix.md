# DriftFix: Build Runbook (c0mpiled-15, Track 1B)

YC RFS: **Self-Maintaining APIs**. Pitch: when a vendor ships a breaking API change, DriftFix finds the affected code in a customer repo and opens a pull request with a tested fix.

Build window 12:00-8:00 PM, **code freeze 6:45 PM**, submit by 7:45 PM. No code before noon. Declare anything pre-existing on the submission form.

## Tonight (no code)
- Luminal account (psu.edu) and verify the API key. Create a GitHub org/test account and token. Get the MongoDB Atlas student credits and a free cluster. Optional: an AWS account.
- Read the official RFS page for Self-Maintaining APIs and quote it on slide 1.
- Agree on the 5 breaking changes and the repo layout on paper. Assign roles A-D.


## The plan

**Problem.** A SaaS vendor ships a breaking API change (a renamed field, moved endpoint, new required param, changed enum, re-nested response). Downstream integrations break silently. Today customers find out from production errors, and the vendor's only tool is a changelog email.

**User / buyer.**
- Wedge customer: API-first vendors (payments, logistics, CRM). They run DriftFix to auto-open migration PRs in their customers' repos, which cuts churn and support tickets.
- Second customer: platform teams consuming many APIs.

**MVP scope.**
- *In:* OpenAPI v1 to v2 diff; 5 breaking-change types; Python client code using `requests`; tests against a mock server; one real GitHub PR.
- *Out:* arbitrary languages, SDK regeneration, private-repo auth flows, non-OpenAPI APIs.

**Architecture (pipeline, each stage a module).**
1. **Detect:** load the two OpenAPI JSON specs, then diff and classify each change (breaking / non-breaking, type, path, field). Deterministic Python, no LLM.
2. **Impact:** scan the customer repo for call sites. Use ripgrep for paths/fields, then Python `ast` to locate the function and line. Output findings with confidence.
3. **Fix:** for each finding, a Luminal-hosted model (DeepSeek, GLM Flash as fallback) gets the diff, the code snippet and the change type. It returns a unified diff. Generate 2-3 candidates in parallel.
4. **Verify:** apply each candidate in a temp copy, then run `pytest` against a mock server serving spec v2. Keep the first candidate that passes and lint-cleans.
5. **Ship:** create a branch, commit and open a PR via the GitHub API. The PR body holds the change summary, per-finding explanation, test evidence and anything flagged "needs human".
6. **Record:** every run, diff, finding, candidate and result goes to MongoDB Atlas. The dashboard and "migration history" read from it (MongoDB prize).

**Data model (MongoDB collections).**
- `specs {api, version, raw, fetched_at}`
- `changes {api, from, to, type, path, field, breaking}`
- `repos {url, branch}`
- `findings {change_id, file, line, snippet, confidence}`
- `candidates {finding_id, model, diff, passed, test_log}`
- `runs {repo, changes, fixed, flagged, pr_url, duration_s, tokens}`

**Stack.**
- Backend: Python 3.11, FastAPI, `openai` client pointed at the Luminal endpoint, pytest, PyGithub (or REST), pymongo.
- Mock server: a FastAPI app generated from fixture specs, or hand-written v1/v2 apps.
- UI: Next.js or Streamlit, with a pipeline view and live stage status (SSE or polling).
- Optional: deploy the backend to AWS App Runner/Lambda for the AWS story.

**Demo fixtures (choose tonight, build after noon).**
- Fictional "Parcelly Shipping API" v1 and v2 with exactly 5 breaking changes:
  - `customer_name` renamed to `recipient.name` (re-nesting);
  - `/v1/labels` moved to `/v2/shipments/{id}/label`;
  - new required `service_level` param;
  - enum `"express"` renamed to `"priority"`;
  - error code 400 changed to 422 with a new body.
- Customer repo "shopfront-integration": about 8 Python files, 10 call sites, 12 tests. It passes on v1 and fails on v2.
- Held-out proof: a second repo ("warehouse-bot") and a 6th change never seen while prompts were tuned, run once at the end.

**Metrics shown on stage.**
- Breaking changes detected (5/5).
- Call sites found vs ground truth (precision/recall).
- Auto-fixed with tests passing (target at least 8/10).
- Flagged for humans (rest).
- Time to PR (target under 2 min).
- Held-out repo result.

**Team roles (4 people; with 3, merge D into C).**
- A, Detect + mock servers + fixtures.
- B, Fix agent (Luminal prompts, candidates, diff application).
- C, Verify + GitHub PR + MongoDB logging + orchestration API.
- D, UI + pitch + customer validation. D talks to 5+ developers and sponsors at the event and records quotes ("would you install this?").

**Hour-by-hour (each block has a definition of done, DoD).**

| Time | A | B | C | D | DoD / checkpoint |
|---|---|---|---|---|---|
| 12:00-12:30 | Repo skeleton, write specs v1/v2 | Luminal API smoke test, model pick | GitHub token, test repo, Mongo Atlas cluster | UI wireframe, pitch outline | Everyone can call Luminal; specs committed |
| 12:30-1:30 | Spec differ + classifier | Prompt v1 for fixes on hand-picked snippets | Customer repo + 12 tests passing on v1 | UI shell with stage list | `diff(v1,v2)` prints 5 typed changes |
| 1:30-2:30 | Mock servers v1/v2 | Unified-diff output + apply logic | Impact scanner (rg + ast) | Talk to 3 devs; collect pain stories | Tests fail on v2 as expected; findings list printed |
| 2:30-3:30 | Help B: change-type-specific prompt hints | Parallel 3-candidate generation | Verify loop (temp dir, pytest, pick first pass) | Wire UI to backend status API | **Checkpoint 3:30:** at least 1 finding auto-fixed end-to-end |
| 3:30-4:30 | Edge cases: enum + error-code changes | Retry with test-failure feedback (1 round) | PR creation + PR body template | Live pipeline view | Full run opens a real PR |
| 4:30-5:30 | Held-out repo + 6th change (do not tune on it) | Prompt hardening on dev repo only | Mongo logging + history page data | Metrics panel, PR link card | 8/10 fixed on dev repo |
| 5:30-6:15 | Bug bash | Bug bash | Deploy (AWS or local fallback) | Pitch deck (5 slides) | Two clean back-to-back runs |
| 6:15-6:45 | Run held-out once, record numbers | Record backup screen capture | Freeze code, tag `v-demo` | Rehearse 90 s + 3 min | **Code freeze 6:45** |
| 6:45-8:00 | Video, submission form (declare nothing pre-built), rehearse Q&A, buffer | | | | Submitted by 7:45 |

**Fallbacks (decide at checkpoints, not later).**
- If LLM fixes are flaky by 3:30, add deterministic rewrite rules for field renames and path moves, and use the LLM only for required-param and error changes. Say so honestly.
- If the GitHub API fails, generate a local branch + `.patch` and show it in the UI. Keep a pre-recorded run as video backup.
- If Luminal is slow or down, swap the endpoint to any OpenAI-compatible fallback via an env var. Note it in the demo.

**90-second demo script.**
- 0-10s: "APIs change; integrations rot silently. YC asked for agents that open the PR."
- 10-25s: show v2 spec; the customer test suite goes red.
- 25-55s: click Run. Stages light up: 5 changes, 10 call sites, candidates, tests going green.
- 55-70s: open the real GitHub PR with the explanations and test evidence.
- 70-85s: metrics plus held-out repo result; the "needs human" items are shown honestly.
- 85-90s: who pays (API vendors cutting churn) and next step.

**Judge Q&A prep.**
- *How is this different from Dependabot/Renovate?* They bump versions; we rewrite your code to a changed contract and prove it with tests.
- *Versus Claude Code or Copilot?* Those are general agents run by a human. This triggers on the spec change, runs at fleet scale and verifies against the vendor's contract.
- *Hallucinated fixes?* Nothing ships without passing tests. Anything unverified is flagged, never auto-merged.
- *Who pays?* API vendors, per connected customer repo. Show event quotes.
- *Moat?* A corpus of real migrations, change-type playbooks and vendor distribution.

**Validation during the event (C dimension).** D collects 5+ developer interviews and at least 1 "I'd try this on my repo" commitment, plus a sponsor reaction (Luminal and MongoDB engineers count). Put the quotes on slide 4.

