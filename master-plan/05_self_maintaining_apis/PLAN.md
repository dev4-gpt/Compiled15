# Track 5: Self-Maintaining APIs, MVP: DriftFix (FINAL PICK)

**Score:** 8.82 weighted, 7.94 risk-adjusted, **rank 1 of 6**. First in 98.4% of 20,000 sensitivity runs.
**One-liner:** When a vendor ships a breaking API change, DriftFix finds the affected code in customer repos and opens a pull request with a fix verified by tests.

The minute-by-minute build runbook already exists: **[`../../BUILD_PLAN_DriftFix.md`](../../BUILD_PLAN_DriftFix.md)**. This file is the strategy layer and records what the master plan adds.

## 1. Thesis

APIs change constantly and integrations break without warning. The YC RFS for this request says an agent should scan customer codebases, identify affected usages and open a PR with the fix, either as per-provider agents or as "Dependabot for APIs". The RFS author's own statistic: at AWS, over 30% of service downtime came from external API or package changes nobody noticed. The task is concrete, and a PR with green tests is the strongest proof any of the six projects can show.

## 2. Candidates considered

| Concept | Risk-adj | Verdict |
|---|---|---|
| **DriftFix**, spec diff → impact → fix → verify → PR | 7.94 | **Chosen** |
| SchemaSentinel, learn contracts from traffic | 6.22 | Good v2 input: catches undocumented changes DriftFix can then fix |
| SDKSmith, regenerate SDKs | 5.76 | Commodity (Stainless, Speakeasy, Fern) |

## 3. User, buyer, wedge

- **Buyer 1 (wedge):** API-first vendors (payments, logistics, comms). They run DriftFix to auto-open migration PRs in their customers' repos, which cuts churn, support tickets and the long tail of old versions.
- **Buyer 2:** platform teams that consume 20+ external APIs.
- **Wedge vs Dependabot/Renovate:** they bump version numbers; DriftFix rewrites call sites to the new contract and proves it with tests. **Vs Copilot/Claude Code:** those need a human to start them. DriftFix starts on the spec change, runs across many repos and checks against the vendor's contract.

## 4. MVP scope

- **In:** OpenAPI v1→v2 diff; 5 breaking-change types (re-nesting, path move, new required param, enum rename, error code change); Python `requests` client code; impact scan (ripgrep + `ast`); LLM fix candidates in parallel; pytest against a v2 mock server; real GitHub PR; run history in MongoDB.
- **Out:** other languages, SDK regeneration, private-repo OAuth app, non-OpenAPI APIs.

## 5. End-to-end architecture

```
Spec v1 ─┐
         ├─► DETECT: oasdiff-style diff + classifier (deterministic) ──► typed changes
Spec v2 ─┘                                                                  │
                                                                            ▼
Customer repo ─────────────► IMPACT: ripgrep + Python ast (+ LibCST) ──► findings {file, line, change, confidence}
                                                                            │
                                                                            ▼
                         FIX: deterministic codemods for renames/moves; LLM for the rest
                              (2-3 candidates in parallel, unified diffs)
                                                                            │
                                                                            ▼
                         VERIFY: apply in temp worktree ─► pytest vs mock v2 ─► lint
                              (one retry with test-failure feedback)
                                                                            │
                                     pass ─────────────────┬────────── fail
                                                           ▼                │
                         SHIP: branch + commit + PR (explanations, evidence)   ▼
                                                           │        "needs human" section
                                                           ▼
                         RECORD: specs, changes, findings, candidates, runs ─► MongoDB ─► dashboard
```

**Master-plan upgrade over the runbook:** use deterministic codemods (LibCST) for field renames and path moves from the start rather than only as the 3:30 fallback. That raises p_success (the variable the decision is most sensitive to, see `FINAL_DECISION.md` §3) and puts the LLM on the cases that need judgment.

## 6. Data model

Unchanged from the runbook: `specs`, `changes`, `repos`, `findings`, `candidates`, `runs` (MongoDB Atlas).

## 7. Stack and resources

| Need | Choice | Resource |
|---|---|---|
| Spec diff reference | oasdiff (Go CLI, breaking-change rules) as a cross-check for our Python differ | `oasdiff/oasdiff`; `OpenAPITools/openapi-diff` |
| Code search and rewrite | ripgrep, Python `ast`, LibCST codemods, ast-grep for cross-language later | `Instagram/LibCST`, `ast-grep/ast-grep` |
| Mock server | FastAPI v1/v2 apps, or Prism from the spec | `stoplightio/prism` |
| LLM | Luminal (DeepSeek / GLM Flash), OpenAI-compatible; fallback via env var | `claude-api` skill if falling back to Claude |
| GitHub | REST via PyGithub; GitHub MCP connector in this session for checks | `PyGithub/PyGithub` |
| Real-world corpus (post-event) | Stripe's public OpenAPI spec history, Twilio and GitHub REST spec repos | `stripe/openapi`, `twilio/twilio-oai`, `github/rest-api-description` |
| UI | Next.js or Streamlit pipeline view | Lovable/Vercel connectors |

## 8. Eight-hour build plan

See the hour-by-hour table in `BUILD_PLAN_DriftFix.md` (roles A-D, checkpoint at 3:30 PM, code freeze at 6:45 PM). The master plan changes three things:
1. **12:30-1:30, Role B:** write the LibCST rename and path-move codemods before the LLM prompt (about 40 minutes).
2. **4:30-5:30, Role A:** run the held-out repo against both the codemod path and the LLM path, and report each.
3. **All day, Role D:** log every interview in `validation/interviews.md`, which feeds the Phase 1 re-score.

## 9. 90-second demo

From the runbook: v2 ships, the customer's tests go red, click Run, the stages light up, a real GitHub PR opens with green tests and explanations, the metrics and held-out result appear, and the "needs human" items are shown honestly.

## 10. Metrics

5/5 changes detected; call-site precision and recall; at least 8/10 auto-fixed with passing tests; time to PR under 2 minutes; held-out repo result; codemod vs LLM share of fixes.

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Flaky LLM patches | Test gate; codemods for mechanical changes; retry with feedback |
| GitHub API failure | Local branch + `.patch` shown in UI; recorded backup |
| "Fixtures are self-authored" | Held-out repo + 6th change never tuned on; post-event, replay real Stripe spec versions |

## 12. Validation and next 30 days

- **At the event:** 5+ developer interviews, 1 "run it on my repo" commitment, sponsor reactions (Luminal, MongoDB).
- **Days 1-7:** replay 3 real historical breaking changes from public specs (Stripe, Twilio, GitHub) on open-source client repos and open real PRs upstream where appropriate.
- **Days 8-30:** GitHub App install flow; TypeScript support via ast-grep; 3 API-vendor design partners; pricing per connected customer repo.
