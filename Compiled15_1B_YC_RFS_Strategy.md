**c0mpiled-15 \| Track 1B**

YC Requests for Startups (Fall 2026): One Project per Request, Scored, With a Full Build Plan

*Prepared October 10, 2026 for the October 11 event. Scores are analyst judgments, not the organizers' rubric. RFS summaries were checked against the official text of ycombinator.com/rfs (Fall 2026).*

1\. Executive Brief

- **Recommendation:** Build DriftFix for the Self-Maintaining APIs request. It scores 9.00, the highest of 13. YC's request says that when Stripe ships a breaking change, "an agent should scan customer codebases, identify affected usages, and open a PR with the fix", which is exactly the demo.

- **Backups:** CareCircle (AI for the Aging Population, 8.20) if the team prefers consumer/health; Huddle (Multiplayer AI, 8.05) if the team is strongest at real-time front-end.

- **Winning principle:** An MVP that ends in a real, verifiable artifact (a GitHub PR with green tests) beats a polished dashboard. Freeze code at 6:45 PM.

- **Schedule note:** Build window 12:00 to 8:00 PM per the Luma page; the original report said 12 to 7. Confirm with organizers.

2\. Scoring Rubric

The original rubric was replaced because it had no term for on-stage demo risk or for stacking sponsor prizes.

| **Code** | **Dimension**         | **Weight** | **What it measures**                                               |
|----------|-----------------------|------------|--------------------------------------------------------------------|
| J        | Judge appeal          | 20%        | Fit with the YC founders and engineers on the panel                |
| F        | 8-hour feasibility    | 20%        | Real end-to-end MVP by 6:45 PM with 3-4 people                     |
| R        | RFS fit / fundability | 15%        | How literally it answers the YC request                            |
| D        | Demo impact           | 15%        | Visible result in 90 seconds with low failure risk                 |
| N        | Novelty / wedge       | 10%        | Sharp wedge versus incumbents                                      |
| C        | Commercial validation | 10%        | Can you get a real "I would use this" during the event             |
| S        | Sponsor stacking      | 10%        | Luminal models, MongoDB, AWS, AGI on-device, Bloomerang nonprofits |

Weighted = 0.2J + 0.2F + 0.15R + 0.15D + 0.1N + 0.1C + 0.1S.

3\. One Project per YC Request

| **\#** | **YC request**                      | **Project** | **J** | **F** | **R** | **D** | **N** | **C** | **S** | **Score** |
|--------|-------------------------------------|-------------|-------|-------|-------|-------|-------|-------|-------|-----------|
| 1      | Self-Maintaining APIs               | DriftFix    | 10    | 8     | 10    | 10    | 8     | 8     | 8     | 9.00      |
| 2      | AI for the Aging Population         | CareCircle  | 8     | 8     | 9     | 9     | 7     | 8     | 8     | 8.20      |
| 3      | Multiplayer AI                      | Huddle      | 8     | 7     | 10    | 9     | 7     | 7     | 8     | 8.05      |
| 4      | New OS for the Physical World       | CrewOS      | 8     | 7     | 10    | 8     | 8     | 7     | 7     | 7.90      |
| 5      | AI-Native Compliance Infrastructure | LicenseLoop | 8     | 7     | 10    | 8     | 7     | 7     | 7     | 7.80      |
| 6      | The Primer                          | PhonicsPal  | 6     | 7     | 9     | 8     | 6     | 6     | 6     | 6.95      |
| 7      | AI Consumer Products for 1B People  | LabelLens   | 6     | 8     | 7     | 8     | 5     | 6     | 8     | 6.95      |
| 8      | Data for the Real World             | FieldLens   | 7     | 7     | 8     | 7     | 6     | 6     | 7     | 6.95      |
| 9      | A Cloud for Small Software          | Shipyard    | 7     | 6     | 9     | 7     | 6     | 6     | 7     | 6.90      |
| 10     | Proving You're Human                | HumanProof  | 6     | 6     | 8     | 7     | 7     | 5     | 6     | 6.45      |
| 11     | Best Time to Build in Crypto        | AgentEscrow | 6     | 6     | 8     | 7     | 6     | 5     | 4     | 6.15      |
| 12     | Future of American Defense          | PartsTrace  | 5     | 5     | 7     | 5     | 6     | 4     | 3     | 5.10      |
| 13     | Compute at Sea                      | SeaSite     | 4     | 5     | 8     | 5     | 7     | 3     | 3     | 5.05      |

Project descriptions

**1. DriftFix (Self-Maintaining APIs), 9.00**

Detects a vendor's breaking API change, finds affected code in a customer repo, opens a tested PR with the fix.

MVP: OpenAPI v1/v2 diff, 5 change types, Python client repo, pytest against mock v2, real GitHub PR. Demo: tests red, click Run, PR opens with green tests. Risk: flaky LLM patches; mitigated by test gating and deterministic rules.

**2. CareCircle (AI for the Aging Population), 8.20**

Daily voice check-in agent for elders that flags missed meds or confusion to a family and caregiver group.

MVP: elder profile, browser voice check-in, structured signal extraction, alert rules, family timeline. Demo: teammate role-plays the elder live. Risk: medical claims and telephony setup.

**3. Huddle (Multiplayer AI), 8.05**

One live AI agent session a whole team co-steers in real time with roles, votes and handoff.

MVP: shared room, live agent plan and tool calls, comment/redirect, driver approval, provenance log. Demo: judges join by QR and steer. Risk: reads as "just a UI" without one sharp workflow.

**4. CrewOS (New OS for the Physical World), 7.90**

Operating system that routes each field job to an AI agent, a robot or a human crew, and records the work as it happens.

MVP: job intake, AI quoting agent, router that assigns sub-tasks to agent / simulated robot / human, tech mobile view with photo proof-of-work, safety and reliability log. Demo: a new job is split three ways live. Risk: robots are simulated. (Updated to match YC's "three kinds of workers" framing.)

**5. LicenseLoop (AI-Native Compliance Infrastructure), 7.80**

Real-time view of a fintech's state-by-state licenses: renewal deadlines, regulatory changes mapped to affected licenses, and an audit trail.

MVP: 10-state license register, deadline engine, LLM summaries of regulator notices mapped to affected licenses with citations, finance-team dashboard. Demo: a new state rule arrives and the affected licenses and tasks light up. Risk: legal accuracy; label output as review-required. (Reworked: YC's text is about financial compliance and state licensing, not SOC 2.)

**6. PhonicsPal (The Primer), 6.95**

Voice phonics tutor for ages 5-7 with mastery tracking.

MVP: word lists, speech recognition, per-phoneme mastery model, adaptive next word. Demo: live reading session. Risk: ASR accuracy on child speech; weak learning evidence in a day.

**7. LabelLens (AI Consumer Products for 1B People), 6.95**

Photo of any medicine or food label to a plain-language answer in your language, on-device.

MVP: camera capture, OCR, on-device or small-model explanation, translation. Demo: scan a real label. Risk: thin wedge; safety of medical advice.

**8. FieldLens (Data for the Real World), 6.95**

Phone-based structured capture of infrastructure or crop defects with geotagged labels.

MVP: capture app, vision auto-labeling, map view, dataset export. Demo: photograph campus defects live. Risk: data volume too small to impress.

**9. Shipyard (A Cloud for Small Software), 6.90**

One-click sandboxed hosting for agent-built micro-apps with auto permission manifests.

MVP: upload app, static analysis to permission manifest, sandboxed deploy, share link. Demo: deploy a generated app in 30 s. Risk: security depth in a day.

**10. HumanProof (Proving You're Human), 6.45**

Replay-resistant liveness challenge for sign-ups.

MVP: randomized gesture/voice challenge, replay detection, signed attestation. Demo: real user passes, replayed video fails. Risk: overclaimed security.

**11. AgentEscrow (Best Time to Build in Crypto), 6.15**

Stablecoin escrow on testnet so agents can pay agents on verified delivery.

MVP: testnet contract, two agents negotiate, verifier releases funds. Demo: agent buys a dataset. Risk: few judges value crypto; contract bugs.

**12. PartsTrace (Future of American Defense), 5.10**

Readiness logistics: spare-part substitution finder from maintenance records.

MVP: synthetic parts catalog, substitution graph, LLM rationale. Demo: grounded aircraft gets a substitute part. Risk: no real data; weak judge fit.

**13. SeaSite (Compute at Sea), 5.05**

Site, cooling and power planner for offshore compute.

MVP: cost/cooling model over ocean sites, map. Demo: choose a site. Risk: no validation possible at the event.

How these map to the original report

Names differ from the original 15-project report. About half the ideas are the same or closely related; scores differ because this report uses a different rubric.

| **This report**                             | **Original report**                                              | **Relationship**                                                                                                                                            |
|---------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DriftFix                                    | PatchForge                                                       | Same idea: fix code after a breaking API change, verified by tests. DriftFix adds the real GitHub PR. Not DocDrift, which only detects doc/code mismatches. |
| CareCircle                                  | CareRelay                                                        | Same space: caregiver coordination. CareCircle adds daily voice check-ins with the elder.                                                                   |
| Huddle                                      | TeamAgent                                                        | Same idea: shared multi-user agent workspace.                                                                                                               |
| CrewOS                                      | FieldRoute + ScheduleArena                                       | Same core: field dispatch and scheduling. CrewOS adds agent/robot/human routing from the RFS.                                                               |
| LicenseLoop                                 | ComplianceDiff                                                   | Related: both trace changes to obligations. LicenseLoop focuses on financial state licensing, per the RFS.                                                  |
| PhonicsPal                                  | TutorLoop                                                        | Same category, narrower (early reading).                                                                                                                    |
| Shipyard                                    | TinyDeploy                                                       | Same idea.                                                                                                                                                  |
| HumanProof                                  | ProofOfHuman                                                     | Same idea.                                                                                                                                                  |
| FieldLens                                   | SensorGap                                                        | Loosely related: SensorGap optimized sensor placement; FieldLens captures data by phone.                                                                    |
| LabelLens, AgentEscrow, PartsTrace, SeaSite | None                                                             | New in this report.                                                                                                                                         |
| None                                        | SQLMedic, AgentReplay, DocDrift, NonprofitClose, InferenceRouter | Not carried over: not tied to a YC request, or better suited to Track 1A.                                                                                   |

4\. DriftFix: Technical Deep Dive (Recommended)

*When a vendor ships a breaking API change, DriftFix finds the affected code in a customer repo and opens a pull request with a tested fix.*

**Problem and buyer**

*From the RFS author (Harsha Gaddipati): at AWS, over 30% of service downtime came from external API or package changes going unnoticed. YC suggests two shapes: per-provider agents ("Install Stripe's update agent") or a neutral third-party service, "like Dependabot but for APIs". DriftFix starts as per-provider agents sold to API vendors.*

Breaking API changes (renamed fields, moved endpoints, new required params, changed enums, re-nested responses) silently break downstream integrations. Customers find out from production errors. Wedge buyer: API-first vendors who want to auto-open migration PRs for their customers to cut churn and support load. Second buyer: platform teams consuming many APIs.

**MVP scope**

- **In:** OpenAPI v1 to v2 diff, 5 breaking-change types, Python client code using requests, pytest against a v2 mock server, one real GitHub PR.

- **Out:** Arbitrary languages, SDK regeneration, private-repo auth flows, non-OpenAPI APIs.

**Architecture**

- **Detect:** Diff and classify spec changes. Deterministic Python, no LLM.

- **Impact:** Find call sites with ripgrep, then Python ast for function and line.

- **Fix:** Luminal-hosted DeepSeek (GLM Flash fallback) returns a unified diff per finding; 2-3 candidates in parallel.

- **Verify:** Apply each candidate in a temp copy, run pytest against the v2 mock, keep the first that passes.

- **Ship:** Branch, commit and open a PR via the GitHub API with explanations, test evidence and "needs human" items.

- **Record:** Runs, changes, findings and candidates stored in MongoDB Atlas for the dashboard and history.

**Data model (MongoDB)**

| **Collection** | **Fields**                                                |
|----------------|-----------------------------------------------------------|
| specs          | api, version, raw, fetched_at                             |
| changes        | api, from, to, type, path, field, breaking                |
| repos          | url, branch                                               |
| findings       | change_id, file, line, snippet, confidence                |
| candidates     | finding_id, model, diff, passed, test_log                 |
| runs           | repo, changes, fixed, flagged, pr_url, duration_s, tokens |

**Stack**

Python 3.11, FastAPI, openai client pointed at Luminal, pytest, PyGithub, pymongo. Mock servers as FastAPI apps for v1 and v2. UI in Next.js or Streamlit with live stage status. Optional AWS App Runner deploy for the AWS story.

**Demo fixtures (choose tonight, build after noon)**

- customer_name moves to recipient.name (re-nesting).

- /v1/labels moves to /v2/shipments/{id}/label.

- New required service_level parameter.

- Enum value "express" renamed to "priority".

- Error code 400 becomes 422 with a new body.

Customer repo "shopfront-integration": about 8 Python files, 10 call sites, 12 tests passing on v1 and failing on v2. Held-out proof: a second repo plus a sixth change, run once at the end and never used for prompt tuning.

**Metrics shown on stage**

Breaking changes detected (5/5); call-site precision and recall; auto-fixed with passing tests (target 8/10); flagged for humans; time to PR (target under 2 minutes); held-out repo result.

**Team roles**

| **Role** | **Responsibility**                                                                          |
|----------|---------------------------------------------------------------------------------------------|
| A        | Spec differ, mock servers, fixtures, held-out set                                           |
| B        | Fix agent: Luminal prompts, parallel candidates, diff application, retry with test feedback |
| C        | Impact scanner, verify loop, GitHub PR, MongoDB logging, orchestration API                  |
| D        | UI, pitch deck, customer validation (5+ developer interviews, quotes)                       |

**Hour-by-hour plan**

| **Time**    | **A**                            | **B**                    | **C**                          | **D**                    | **Done when**                    |
|-------------|----------------------------------|--------------------------|--------------------------------|--------------------------|----------------------------------|
| 12:00-12:30 | Repo skeleton, specs v1/v2       | Luminal smoke test       | GitHub token, test repo, Atlas | Wireframe, pitch outline | All can call Luminal             |
| 12:30-1:30  | Spec differ + classifier         | Fix prompt v1            | Customer repo + tests on v1    | UI shell                 | 5 typed changes printed          |
| 1:30-2:30   | Mock servers v1/v2               | Diff output + apply      | Impact scanner                 | 3 dev interviews         | Tests red on v2; findings listed |
| 2:30-3:30   | Prompt hints per type            | 3 parallel candidates    | Verify loop                    | Wire UI to API           | CHECKPOINT: 1 fix end-to-end     |
| 3:30-4:30   | Enum + error edge cases          | Retry with test feedback | PR creation + body             | Live pipeline view       | Full run opens real PR           |
| 4:30-5:30   | Held-out repo (no tuning)        | Prompt hardening         | Mongo logging, history         | Metrics panel            | 8/10 fixed on dev repo           |
| 5:30-6:15   | Bug bash                         | Bug bash                 | Deploy or local fallback       | 5-slide deck             | Two clean runs                   |
| 6:15-6:45   | Held-out run once                | Record backup video      | Freeze, tag v-demo             | Rehearse                 | CODE FREEZE 6:45                 |
| 6:45-8:00   | Video, submission, Q&A rehearsal |                          |                                |                          | Submitted by 7:45                |

**Fallbacks (decide at checkpoints)**

- If LLM fixes are flaky at 3:30, use deterministic rewrite rules for renames and path moves and keep the LLM for required params and error changes.

- If the GitHub API fails, produce a local branch and .patch file shown in the UI; keep a recorded run as backup.

- If Luminal is slow, switch to any OpenAI-compatible endpoint via an environment variable and say so.

**90-second demo narrative**

0-10s: APIs change and integrations rot; YC asked for agents that open the PR. 10-25s: v2 spec ships, customer tests go red. 25-55s: Run; stages light up through changes, call sites, candidates and green tests. 55-70s: open the real GitHub PR. 70-85s: metrics and the held-out result, with "needs human" items shown honestly. 85-90s: API vendors pay to cut churn.

**Judge questions to prepare**

- **Versus Dependabot?** YC itself frames this as "Dependabot but for APIs". Dependabot bumps package versions; DriftFix rewrites your code to a changed API contract and proves it with tests.

- **Versus Claude Code or Copilot?** Those are general agents a human drives. DriftFix triggers on the spec change, runs across many repos and verifies against the vendor contract.

- **Hallucinated fixes?** Nothing ships without passing tests; unverified items are flagged, never auto-merged.

- **Who pays?** API vendors, priced per connected customer repo. Show event quotes.

- **Moat?** A corpus of real migrations, change-type playbooks and vendor distribution.

**Validation at the event**

Role D collects 5+ developer interviews and at least one "I would try this on my repo" commitment, plus sponsor reactions. Quotes go on slide 4.

5\. Backup Deep Dives

5.1 CareCircle (AI for the Aging Population)

- **MVP:** Caregiver sets up an elder profile; the agent runs a daily voice check-in; the LLM extracts meds taken, mood, pain and confusion cues; rules raise alerts to the family; the timeline lives in MongoDB.

- **Demo:** A teammate role-plays the elder live and the family dashboard shows an alert.

- **Validation:** Contact a State College senior center or Meals on Wheels chapter, which also fits the Bloomerang nonprofit prize.

- **Risks:** Medical claims (state "not a medical device") and telephony setup time.

- **Timeline:** Profile and script by 1:30, voice loop by 3:00, extraction and alerts by 4:30, dashboard by 5:30, freeze 6:45.

5.2 Huddle (Multiplayer AI)

- **MVP:** Shared room where 3 users see one agent's live plan and tool calls; anyone can comment or redirect; a driver approves steps; provenance shows who changed what.

- **Stack:** Next.js with websockets or MongoDB change streams, plus a Luminal model.

- **Demo:** Judges join from phones by QR code and co-steer live.

- **Risks:** Can read as "just a UI"; anchor it on one workflow such as incident response.

6\. Checklist

- Tonight: Luminal account with psu.edu email and a tested key; GitHub test account and token; MongoDB Atlas student credits and a free cluster; optional AWS account.

- Tonight: agree on the 5 breaking changes, repo layout and roles on paper. No code before noon.

- At check-in: confirm team-size cap, build end time and submission format.

- During the build: hit the 3:30 PM checkpoint or switch to the fallback immediately.

- End: run the held-out repo once, report honestly, record the video, submit by 7:45 PM.

**Sources**

- ycombinator.com/rfs, Fall 2026 (official text, provided by the team)
