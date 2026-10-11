# Compiled15 Master Plan: Six YC Requests, Six MVPs, One Final Build

A structured plan for six Fall 2026 YC Requests for Startups. Each request gets 3 candidate concepts, a gated and weighted score, an end-to-end MVP plan, a resource map and a final decision. It extends the earlier Track 1B strategy doc and the DriftFix runbook at the repo root.

> **Superseded.** The current decision is in [`v3/FINAL_DECISION.md`](v3/FINAL_DECISION.md): **Fieldwork in Track 2**, prototype in [`../prototype/fieldwork`](../prototype/fieldwork). Every idea and its score is listed in [`v3/IDEAS.md`](v3/IDEAS.md). This v1 plan is kept for history.

## 1. Structure

```
master-plan/
├── README.md                     ← this file: process, timeline, how to use
├── 00_SCORING_FRAMEWORK.md       ← gates, 10 weighted criteria with anchors, formulas, evidence re-score rules
├── scoring/
│   ├── scores.yaml               ← all 18 candidates × 10 criteria + p_success (the only place scores live)
│   ├── score.py                  ← gates → weighted → risk-adjusted → Monte Carlo sensitivity
│   └── RESULTS.md                ← generated output (do not edit by hand)
├── 01_multiplayer_ai/PLAN.md     ← WarRoom
├── 02_consumer_1b/PLAN.md        ← DocSaathi
├── 03_aging_population/PLAN.md   ← ScamShield (backup)
├── 04_compliance_infra/PLAN.md   ← RegDiff engine + LicenseLoop vertical
├── 05_self_maintaining_apis/PLAN.md ← DriftFix (final pick) → links to ../BUILD_PLAN_DriftFix.md
├── 06_proving_human/PLAN.md      ← HumanPass
├── RESOURCES.md                  ← repos, APIs, connectors and skills per track
├── FINAL_DECISION.md             ← ranking, robustness, switch rules
└── validation/interviews.md      ← interview log feeding the re-score
```

Every `PLAN.md` uses the same 12 sections: thesis · candidates considered · user/buyer/wedge · MVP scope · end-to-end architecture · data model · stack and resources · 8-hour build plan · 90-second demo · metrics · risks · validation and next 30 days.

## 2. Scoreboard

| Rank | Track | MVP | One-liner | Risk-adj |
|---|---|---|---|---|
| **1** | Self-maintaining APIs | **DriftFix** | Breaking API change → PR with green tests in customer repos | **7.94** |
| 2 | Aging population | ScamShield | Live scam-call detection, whisper intervention, family alert | 7.15 |
| 3 | Multiplayer AI | WarRoom | One incident agent co-steered by the whole on-call team | 6.98 |
| 4 | Compliance infra | RegDiff + LicenseLoop | New regulation → cited diff of affected licenses, policies, tasks | 6.58 |
| 5 | Consumer for 1B | DocSaathi | WhatsApp voice assistant that explains and acts on any document | 6.39 |
| 6 | Proving you're human | HumanPass | Unlinkable personhood tokens + scoped agent delegation | 6.04 |

Full table with all 18 candidates and the sensitivity analysis: [`scoring/RESULTS.md`](scoring/RESULTS.md).

## 3. Process (phases)

| Phase | What | Output | Exit criterion |
|---|---|---|---|
| **0. Desk research** (done) | 3 concepts per request, gates, scoring | `scores.yaml`, 6 plans, `RESULTS.md` | One leader with P(#1) > 70% |
| **1. Evidence re-score** (before noon) | 45-min spike on DriftFix (and ScamShield if time allows); 3+ user conversations each | Updated `scores.yaml`, interview log | Re-run `score.py`; apply the switch rules in `FINAL_DECISION.md` §4 |
| **2. Build** (12:00-6:45 PM) | Follow `BUILD_PLAN_DriftFix.md` with the master-plan changes in `05_.../PLAN.md` §8 | Working MVP, real PR, metrics, held-out result | 3:30 PM checkpoint; code freeze 6:45 PM |
| **3. Ship** (6:45-8:00 PM) | Video, submission form, Q&A rehearsal | Submission by 7:45 PM | Submitted |
| **4. After the event** (days 1-30) | Real spec replays, GitHub App, design partners | 3 design partners | Decide whether to keep going as a company |

Phase 1 spikes must follow the event rules: if no code is allowed before noon, the spike is a paper walkthrough plus manual API calls. Declare anything pre-existing on the submission form.

## 4. How to use

```bash
# Re-score after editing master-plan/scoring/scores.yaml
python3 master-plan/scoring/score.py            # writes scoring/RESULTS.md
python3 master-plan/scoring/score.py --runs 50000 --seed 7   # tighter sensitivity estimate
```

Requires Python 3.9+ and PyYAML.

## 5. Ground rules carried over from the earlier docs

- An MVP that ends in a real, verifiable artifact beats a polished dashboard.
- Get the evaluator and baseline working before the UI.
- Keep a held-out test set, run it once at the end and report it honestly.
- Decide fallbacks at checkpoints, never at 6:30 PM.
- Scores here are analyst judgments, not the organizers' rubric. Evidence from Phase 1 overrides them.
