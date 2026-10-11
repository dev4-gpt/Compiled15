# Plan: DriftFix credentials, login and database

Format follows ECC `/multi-plan` (plan only, no production code), with an `/orchestrate`-style workstream split added at the end.

Note: ECC `/multi-plan` normally drafts with Codex + Antigravity through the external `ccg-workflow` runtime. That runtime isn't installed here, so this plan was written directly from the repo docs. There are no `CODEX_SESSION` / `ANTIGRAVITY_SESSION` IDs.

Sources: `BUILD_PLAN_DriftFix.md`, `Compiled15_1B_YC_RFS_Strategy.docx` (section 4).

---

## Implementation Plan: Credentials + Login + MongoDB

### Task Type
- [ ] Frontend
- [ ] Backend
- [x] Fullstack (mostly backend; the UI only needs a login button and the session user)

### Requirement (restated)
1. **Credentials.** One place loads and validates every secret DriftFix needs: the Luminal API key and base URL, a fallback OpenAI-compatible endpoint, a GitHub token, the MongoDB Atlas URI and a session secret. No secret is ever committed. The app fails fast at startup with a clear message when one is missing.
2. **Login.** A user signs in to the dashboard. "Sign in with GitHub" is the natural choice: judges already have accounts, and it gives the "connect your repo" story. Private-repo auth flows stay **out of MVP scope**, per the runbook.
3. **Database.** MongoDB Atlas holds the six runbook collections (`specs`, `changes`, `repos`, `findings`, `candidates`, `runs`) plus `users`. The dashboard and "migration history" read from it, which counts toward the MongoDB prize.

### Technical Solution
- **Settings:** `pydantic-settings` `Settings` class reading `.env`. `.env.example` is committed; `.env` is gitignored. One `get_settings()` used everywhere.
- **LLM client:** `openai.OpenAI(base_url=settings.llm_base_url, api_key=settings.llm_api_key)`. A `LLM_PROVIDER=luminal|fallback` switch covers the runbook fallback ("swap the endpoint via an env var").
- **GitHub, two credentials, kept separate:**
  - `GITHUB_BOT_TOKEN`: a fine-grained PAT on the team's test org. The pipeline uses it to push the branch and open the PR on the demo repo, so the demo works even if OAuth breaks.
  - GitHub OAuth App (`GITHUB_CLIENT_ID` / `GITHUB_CLIENT_SECRET`): used **only for login**, with scope `read:user`. Don't ask for `repo` scope today.
- **Login flow (FastAPI, UI-agnostic, so it works with Next.js or Streamlit):**
  `GET /auth/login` → redirect to GitHub with a `state` stored in the session → `GET /auth/callback` → swap the code for a token (httpx) → `GET https://api.github.com/user` → upsert into `users` → set a signed session cookie (Starlette `SessionMiddleware`, `SESSION_SECRET`) → redirect to the UI. Add `GET /auth/me` and `POST /auth/logout`. A `require_user` dependency guards `POST /runs`.
  - Don't store the OAuth access token. It isn't needed after `/user`, and not storing it removes any need to encrypt it.
  - `DEMO_MODE=true` skips the login guard and uses a fixed "demo" user. This is the stage fallback and is off by default.
- **Database:** `pymongo` (sync is fine for a FastAPI threadpool at hackathon scale; use `motor` only if the orchestrator is async anyway). `db.py` exposes `get_db()`, an idempotent `ensure_indexes()` run at startup, and small typed insert and update helpers. Each pipeline stage writes through the helpers, never raw.

### Data model (runbook collections + additions)
| Collection | Fields | Indexes |
|---|---|---|
| `users` *(new)* | `github_id`, `login`, `name`, `avatar_url`, `created_at`, `last_login_at` | unique `github_id` |
| `specs` | `api`, `version`, `raw`, `fetched_at` | unique (`api`, `version`) |
| `changes` | `api`, `from`, `to`, `type`, `path`, `field`, `breaking`, `run_id` | `run_id` |
| `repos` | `url`, `branch`, `owner_user_id` *(new)* | unique `url` |
| `findings` | `run_id`, `change_id`, `file`, `line`, `snippet`, `confidence` | `run_id`, `change_id` |
| `candidates` | `run_id`, `finding_id`, `model`, `diff`, `passed`, `test_log` | `finding_id` |
| `runs` | `repo`, `user_id` *(new)*, `status`, `stage` *(new)*, `changes`, `fixed`, `flagged`, `pr_url`, `duration_s`, `tokens`, `started_at`, `finished_at` | (`user_id`, `started_at` desc) |

`run_id` on every child doc lets the history page load a whole run in one query per collection. `runs.stage` plus `status` is what the live pipeline view polls (or streams over SSE).

### Implementation Steps
1. **Secrets bootstrap (no code, ~10 min).** Create the Atlas free cluster and a DB user with a strong password. Open the network access list to `0.0.0.0/0` for the event only. Create the GitHub OAuth App: callback `http://localhost:8000/auth/callback`, plus the deployed URL if you have one. Create a fine-grained PAT scoped to the demo repo only (Contents RW, Pull requests RW). Put everything in a shared password manager or DM, **not** in the repo or chat logs. Deliverable: every teammate has a working `.env`.
2. **`.gitignore`, `.env.example` and a pre-commit secret scan.** Deliverable: `git status` never shows `.env`. Running `sonar`/`gitleaks` (or GitHub secret scanning) on the repo comes back clean.
3. **`driftfix/config.py`.** `Settings` holds: `llm_provider`, `luminal_base_url`, `luminal_api_key`, `fallback_base_url`, `fallback_api_key`, `llm_model`, `github_bot_token`, `github_client_id`, `github_client_secret`, `mongodb_uri`, `mongodb_db="driftfix"`, `session_secret`, `ui_origin`, `demo_mode=False`. Deliverable: `python -m driftfix.config --check` prints a ✓ or ✗ for each secret without printing any values.
4. **`driftfix/db.py`.** Provides `get_db()`, `ensure_indexes()` and the helpers `create_run`, `set_stage`, `add_changes`, `add_findings`, `add_candidate`, `finish_run`, `list_runs(user_id)` and `get_run(run_id)`. Deliverable: a smoke script inserts a fake run with children and reads it back from Atlas.
5. **`driftfix/auth.py` (FastAPI router).** Routes `/auth/login`, `/auth/callback`, `/auth/me`, `/auth/logout`, plus the `require_user` dependency. Add `SessionMiddleware(same_site="lax", https_only=<prod>)` and CORS for `ui_origin` with credentials. Deliverable: in a browser, log in, then `/auth/me` returns your GitHub login.
6. **Wire into the orchestration API.** `POST /runs` (auth-guarded) creates the run doc, and every stage calls `set_stage`. Add `GET /runs` and `GET /runs/{id}` for history. Deliverable: one pipeline run is visible in Atlas with all children linked.
7. **UI hooks.** Add a "Sign in with GitHub" button that links to `/auth/login`. Show the avatar from `/auth/me`. Add a history list from `GET /runs`. In Streamlit, read the cookie through the backend; don't do OAuth inside Streamlit. Deliverable: a judge can log in and see past runs.
8. **Tests (pytest).** `config` errors when a var is missing. A `db` round trip uses `mongomock` or a throwaway Atlas DB named `driftfix_test`. The `auth` callback is tested with GitHub calls mocked via `respx`. A guarded route returns 401 without a session and 200 with `DEMO_MODE`. Deliverable: green locally.

### Key Files (all new; the repo currently has docs only)
| File | Operation | Description |
|---|---|---|
| `.gitignore` | Create | `.env`, `__pycache__/`, `.venv/`, temp clone dirs |
| `.env.example` | Create | Every variable from step 3, with blank values |
| `driftfix/config.py` | Create | `Settings` + `--check` |
| `driftfix/db.py` | Create | Client, indexes, helpers |
| `driftfix/auth.py` | Create | GitHub OAuth router + `require_user` |
| `driftfix/api.py` | Create/Modify | Mount the auth router, middleware, `/runs` |
| `driftfix/llm.py` | Create | OpenAI client from settings with provider switch |
| `tests/test_config.py`, `tests/test_db.py`, `tests/test_auth.py` | Create | Step 8 |

### Risks and Mitigation
| Risk | Mitigation |
|---|---|
| OAuth callback URL mismatch or redirect bugs eat an hour | Build it after the 3:30 checkpoint. `DEMO_MODE` keeps the demo unblocked. The PR-opening path uses the bot PAT, not OAuth |
| A secret leaks into git (public hackathon repo) | `.gitignore` first, secret scan before every push, fine-grained PAT limited to one repo, rotate all keys after the event |
| Atlas connection blocked (IP list, campus Wi-Fi, SRV DNS) | Open the access list for the event. If SRV DNS fails, use the non-SRV connection string. Keep `mongomock` as the local fallback so the UI still renders |
| Judges ask "do you need write access to my repo?" | Login asks for `read:user` only. Repo access in the product is a GitHub App installed per repo (roadmap slide, not built today) |
| Cookie not sent from the UI on a different origin | Same-site deploy, or a proxy from Next.js `/api/*` to FastAPI. Otherwise set `allow_credentials=True` and an exact `ui_origin` |
| Over-scoping auth delays the core pipeline | Auth is **last priority**. Steps 1–4 and 6 matter for the MongoDB prize; step 5 is a nice-to-have |

---

## Orchestration (`/orchestrate`-style workstreams)

This follows the runbook roles. Role C already owns "GitHub token, test repo, Atlas" and "Mongo logging".

| Order | Workstream | Owner | Depends on | Done when |
|---|---|---|---|---|
| 1 | Steps 1–3: secrets + config | C | none | `config --check` all ✓ on every laptop |
| 2a | Step 4: `db.py` | C | 1 | Smoke run visible in Atlas |
| 2b | `llm.py` provider switch | B | 1 | Luminal and fallback both answer a ping |
| 3 | Step 6: stages write to Mongo | C, with A and B adding `set_stage` calls in their modules | 2a | One full run linked in Atlas |
| 4 | Step 5: GitHub login | C, or D if C is behind | 1 | `/auth/me` works; `DEMO_MODE` tested |
| 5 | Step 7: UI login + history | D | 3, 4 | History page reads real runs |
| 6 | Step 8 + security pass | Whoever is free at bug bash | 3–5 | Tests green; secret scan clean; `.env` absent from `git log -p` |

Handoff chain per workstream (ECC `/orchestrate feature`): planner (this file) → tdd (write the step 8 test first) → implement → code-review → security-review (secrets, cookie flags, OAuth `state` check). Run the security review on `auth.py` and `config.py` before the 6:45 freeze.

### Next step
Review and adjust this plan, then implement workstreams 1 → 2a/2b in parallel → 3. Leave 4–5 until the core pipeline has passed the 3:30 checkpoint.
