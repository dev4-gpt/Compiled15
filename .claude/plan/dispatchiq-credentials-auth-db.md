# Plan: DispatchIQ credentials, login and database

Format follows ECC `/multi-plan` (plan only, no production code), with an `/orchestrate`-style workstream split at the end. ECC's dual-model step (Codex + Antigravity through `ccg-workflow`) isn't installed here, so this plan was written directly from the code. There are no session IDs.

Retargeted from the earlier DriftFix version: the team chose DispatchIQ (`master-plan/v4/IDEAS.md`, "Status").

Grounded in: `prototype/dispatchiq/` (`evolve.py`, `heldout.py`, `app.py`, `dispatchiq/proposers.py`, `dispatchiq/sandbox.py`, `RUNBOOK.md`), and the store pattern in `prototype/fieldwork/store.py`.

---

## Implementation Plan: Credentials + Login + MongoDB for DispatchIQ

### Task Type
- [ ] Frontend
- [x] Backend (config, store, evolve/heldout logging)
- [ ] Fullstack. The only UI work is the Streamlit app reading from the store, plus an optional passcode gate.

### What exists today
| Area | Current state | Gap |
|---|---|---|
| Credentials | `proposers.providers_from_env()` reads `LLM_*`, `FALLBACK_1_*` and `FALLBACK_2_*` (`API_KEY`, `BASE_URL`, `MODEL`). `MONGODB_URI` is read in `evolve.log_mongo`. `.env` is in `prototype/dispatchiq/.gitignore` | Nothing loads `.env`, so everyone must `export` by hand. There's no startup check. A provider with a typo silently disappears from the list. There's no `.env.example`, and the repo root has no `.gitignore` |
| Secret isolation | `sandbox.evaluate` runs candidates with `env={"PATH": ...}` and `-I`, so agent-written code **cannot read the API keys or Mongo URI** | Keep it that way: never pass the env into the sandbox. Add a test |
| Database | `evolve.log_mongo` inserts one doc per round into `dispatchiq.rounds`. It **opens a new MongoClient every round**, swallows errors, and stores no run doc, candidate code or held-out result | The source of truth is `runs/*.json` on one laptop, so teammates and the deployed app can't see runs. That's thin for the MongoDB prize |
| Held-out | `heldout.py` checks the hash, then writes `runs/heldout_result.json`. Nothing stops a second run | A DB record can make "ran once" checkable |
| Login | None. `app.py` is a read-only Streamlit viewer | It has no actions to protect. Judges should be able to open it with no account |

### Decisions
1. **Credentials:** add `python-dotenv` and a small `dispatchiq/config.py` that loads `prototype/dispatchiq/.env`, then validates it.
   - Keep the existing env var names. `proposers.py` already works with them, so no renames.
   - Add `MONGODB_DB` (default `dispatchiq`) and an optional `APP_PASSCODE`.
   - If the app is deployed to Streamlit Community Cloud, read `st.secrets` there instead of `.env`. Same keys.
2. **Database:** add `dispatchiq/store.py`, mirroring `fieldwork/store.py`.
   - `MongoStore` is used when `MONGODB_URI` is set and reachable. Otherwise a `FileStore` writes the existing `runs/*.json`, so the offline demo never dies on Wi-Fi.
   - Keep writing the JSON files **as well**. They're the backup and what `heldout.py` reads by default.
   - Create one client per process, not per round.
3. **Login:** **skip real accounts.**
   - The app stays public and read-only, because judges must open it with one click.
   - If it's deployed publicly, an optional `APP_PASSCODE` gate (shared passcode, compared with `hmac.compare_digest` and kept in `st.session_state`) can hide the run picker and code view.
   - Not today: Streamlit's built-in OIDC `st.login()`, user tables or GitHub OAuth. They add risk and earn no Track 1 points.

### Data model (MongoDB, db `dispatchiq`)
| Collection | Document | Indexes |
|---|---|---|
| `runs` | `_id` = run id (`%Y%m%d-%H%M%S`), `mode`, `agents`, `rounds_planned`, `start_policy`, `heldout_hash`, `baseline {dev, val}`, `round0_code`, `champion_code`, `status` (`running`, `done` or `failed`), `tokens`, `started_at`, `finished_at`, `host` | `started_at` desc |
| `rounds` | `run_id`, `round`, `seconds`, `accepted`, `champion_dev`, `champion_val`, `champion` (summary), `tokens` | unique (`run_id`, `round`) |
| `candidates` | `run_id`, `round`, `agent`, `provider_model` (from `note`), `strategy`, `code`, `dev_cost`, `infeasible`, `error` | (`run_id`, `round`) |
| `heldout_results` | `run_id`, `heldout_hash`, `results` [rows from `heldout.py`], `improvement_pct`, `ran_at` | **unique `run_id`**: a second held-out run for the same run is refused and logged |

Storing every candidate's `code` gives the demo its "what did the agents write?" view, and lets anyone audit why a champion won.

### Implementation Steps
1. **Secrets bootstrap (no code, ~10 min).**
   - Get the Luminal URL, key and model at check-in, plus one fallback (Groq or Cerebras, per the README). Create the Atlas free cluster with a DB user scoped to `dispatchiq`, and open the network access list for the event.
   - Share secrets in DMs or a password manager, **never** in the repo, Slack channels or prompts.
   - Deliverable: each teammate has `prototype/dispatchiq/.env`.
2. **Hygiene.**
   - Add a repo-root `.gitignore` with `.env`, `**/.env`, `**/runs/`, `__pycache__/` and `.venv/`.
   - Add `prototype/dispatchiq/.env.example` with every key and blank values.
   - Before each push, run a secret scan: `sonar` CLI or `gitleaks` (both on the starred list), or GitHub secret scanning.
   - Deliverable: `git status` never shows `.env`, and the scan is clean.
3. **`dispatchiq/config.py`.**
   - `load()` calls `dotenv.load_dotenv(ROOT/".env", override=False)`, so real exported env vars still win.
   - `check()` reports, without printing values:
     - each provider prefix: complete, partial (which key is missing) or absent;
     - a one-token ping to each complete provider;
     - Mongo `ping` and the database name.
   - `evolve.py`, `heldout.py` and `app.py` call `config.load()` first.
   - CLI: `python -m dispatchiq.config --check`.
   - Deliverable: ✓/✗ lines; any ✗ prints the exact fix.
4. **`dispatchiq/store.py`.**
   - `make_store()` returns a `MongoStore` or a `FileStore`, logging which one it chose and why.
   - Shared interface: `start_run(doc)`, `log_round(run_id, rec, candidates)`, `finish_run(run_id, champion_code, status, tokens)`, `latest_run()`, `list_runs(n)`, `get_run(run_id)` (rehydrated into the same shape as `runs/latest.json`), `save_heldout(run_id, doc)` (raises `AlreadyRan` on a duplicate) and `get_heldout(run_id)`.
   - `ensure_indexes()` runs on init.
   - All Mongo calls catch `PyMongoError`. On failure the store degrades to file-only for the rest of the process and prints one warning, not one per round.
   - Deliverable: a smoke script writes a fake run with two rounds and reads it back.
5. **Wire `evolve.py`.**
   - Replace `log_mongo` with the store: `start_run` after baseline eval, `log_round` with full candidate docs (including `code`) each round, and `finish_run` in a `try/finally` so crashes record `status="failed"`.
   - The JSON writes stay as they are.
   - Deliverable: `python evolve.py --rounds 2 --agents 2 --mode random` shows 1 run, 2 rounds and 4 candidates in Atlas.
6. **Wire `heldout.py`.**
   - Load the run from the store, falling back to the JSON path argument.
   - Call `save_heldout` before printing the "official" line. If the run already has a held-out record, print that stored result and exit non-zero instead of re-running.
   - Deliverable: a second invocation shows "already ran at HH:MM" with the stored table.
7. **Wire `app.py`.**
   - Load runs from the store (`list_runs`) into a sidebar run picker. The default is the latest `done` run, falling back to `runs/latest.json`.
   - Read the held-out table from `get_heldout`.
   - New expander, "What the agents wrote": a round, then its candidates with strategy, cost and code.
   - Show a store badge: "MongoDB Atlas" or "local files".
   - Optional `APP_PASSCODE` gate, which wraps only the run picker and code expander.
   - Deliverable: a teammate's laptop shows runs started on another laptop.
8. **Tests (add to `tests/`).**
   - `test_config`: partial provider env is reported; `.env` does not override exported vars.
   - `test_store`: `FileStore` round trip; `get_run` shape matches what `app.py` and `heldout.py` expect; duplicate `save_heldout` raises. Use `mongomock` if installed, else skip the Mongo variant.
   - `test_sandbox_env`: a candidate that reads `os.environ.get("LLM_API_KEY")` gets `None`.
   - Deliverable: `pytest -q` is green, with 8 existing tests plus the new ones.

### Key Files
| File | Operation | Description |
|---|---|---|
| `.gitignore` (repo root) | Create | Secrets and run artifacts |
| `prototype/dispatchiq/.env.example` | Create | `LLM_*`, `FALLBACK_1_*`, `FALLBACK_2_*`, `MONGODB_URI`, `MONGODB_DB`, `APP_PASSCODE` |
| `prototype/dispatchiq/dispatchiq/config.py` | Create | `load()` and `check()`; CLI |
| `prototype/dispatchiq/dispatchiq/store.py` | Create | `MongoStore`, `FileStore`, `make_store()` |
| `prototype/dispatchiq/evolve.py` | Modify | Replace `log_mongo` (L28–37 of the current file) with store calls; `try/finally` for `finish_run` |
| `prototype/dispatchiq/heldout.py` | Modify | Store-backed load; run-once guard |
| `prototype/dispatchiq/app.py` | Modify | Run picker, agent-code expander, store badge, optional passcode |
| `prototype/dispatchiq/tests/test_store.py`, `test_config.py` | Create | Step 8 |
| `prototype/dispatchiq/README.md`, `RUNBOOK.md` | Modify | Replace `export` lines with `cp .env.example .env`, then `python -m dispatchiq.config --check` |

### Risks and Mitigation
| Risk | Mitigation |
|---|---|
| Atlas unreachable on venue Wi-Fi or SRV DNS | `FileStore` fallback (same pattern as Fieldwork). The non-SRV connection string is the second option. The demo never depends on Mongo being up |
| A key leaks: public repo, screen-shared terminal, recorded video | `.env` ignored at the root, `--check` never prints values, secret scan before push, keys rotated after the event. Don't `cat .env` while recording |
| Agent-written code exfiltrates secrets | The sandbox already strips env and runs `-I`. The new test locks that in. Never add `env=os.environ` to `sandbox.evaluate` |
| Storing every candidate's code makes docs large | One candidate is a few KB. 10 rounds × 6 agents ≈ 60 docs, well under the free-tier limits |
| The store refactor breaks the working offline pipeline mid-event | JSON writes are unchanged and the store is additive. Land the steps behind `make_store()`, and run `--mode random` after each step |
| Login slows judges down | No login for viewing. The passcode only hides extras, and only when `APP_PASSCODE` is set |
| Time pressure (the runbook checkpoint is at 3:30) | Steps 1–3 take about 30 min and unblock agents. Steps 4–6 belong to whoever isn't tuning prompts. Step 7 comes after the checkpoint |

---

## Orchestration (`/orchestrate`-style workstreams)

Roles follow `prototype/dispatchiq/RUNBOOK.md`: A runs the agents, B owns the checker and sim, C owns the UI and pitch.

| Order | Workstream | Owner | Depends on | Done when |
|---|---|---|---|---|
| 1 | Steps 1–3: secrets, hygiene, `config --check` | A (needs Luminal first) | none | All ✓ on every laptop; `evolve.py --rounds 1 --agents 1` passes |
| 2 | Step 4: `store.py` + `test_store` | B (doesn't touch the checker or held-out data) | 1 (only for the Mongo URI) | Smoke run in Atlas; tests green |
| 3 | Step 5: `evolve.py` logging | B, after asking A to pause runs for 5 min | 2 | Random-mode run fully in Atlas |
| 4 | Step 7: app reads the store | C | 3 | Run picker shows runs from 2 laptops |
| 5 | Step 6: held-out run-once guard | B | 3 | **Must land before the 5:00 held-out run** |
| 6 | Step 8 security tests + secret scan | Whoever is free at 5:00 | 1–5 | `pytest -q` green; scan clean |

Per-workstream chain (ECC `/orchestrate feature`): plan (this file), then a failing test first (step 8 test for that unit), then implement, then code review, then security review. The security review covers `config.py` printing, the sandbox env and the passcode compare.

### Next step
Review this plan. If approved, implement workstreams 1 → 2 → 3, keeping `--mode random` green after each one.
