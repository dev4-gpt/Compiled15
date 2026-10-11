# Scoring Framework

The method used to compare 18 concepts (3 per YC request) and pick one project. The data is in `scoring/scores.yaml`, the math is in `scoring/score.py`, and the output is in `scoring/RESULTS.md`.

## 1. Pipeline

```
18 concepts ──► Gates (pass/fail) ──► Weighted score (10 criteria) ──► Risk adjustment (p_success)
                                                                              │
             Final pick ◄── Evidence re-score (Phase 1) ◄── Sensitivity (Monte Carlo) ◄── Best per track (6 MVPs)
```

## 2. Gates (all four must pass)

| Gate | Rule | Why |
|---|---|---|
| G1 | Ends in a verifiable artifact: a PR, a fired alert, a signed token, a cited report | Judges trust what they can check |
| G2 | The demo needs no regulated claim (medical device, legal advice, certified KYC) | Avoids a disqualifying Q&A moment |
| G3 | All demo data can be made or obtained before code freeze | No dependency on partners saying yes today |
| G4 | A named buyer already spends money on this problem | Separates startups from features |

Gate failures in this round: CareCircle and MedMinder (G2, their core output is a medication or cognition signal), LabelLens (G2, G4), PlanParty (G4, no buyer), HumanMark (G4). Useful parts carry over. CareCircle's family-circle alerts are built into ScamShield, and LabelLens's photo-to-explanation pipeline is built into DocSaathi.

## 3. Criteria, weights and anchors

| Code | Criterion | Weight | 2 | 5 | 8 | 10 |
|---|---|---|---|---|---|---|
| R | RFS fit | 12% | Tangential | Adjacent to the request | Clearly answers it | Literally the example in the RFS text |
| J | Judge appeal (YC founders, engineers) | 12% | Niche, unfamiliar | Interesting | Judges have felt this pain | Judges would use it themselves |
| F | 8-hour feasibility (3-4 people) | 15% | Needs partners or data we lack | Core works, demo is rough | End-to-end with fallbacks | Comfortably done by 4:30 PM |
| D | Demo impact and verifiability | 12% | Slides only | Dashboard with mocked data | Live run with a visible result | Live before/after the audience can verify (red to green, scam blocked) |
| T | Technical depth and defensibility | 8% | Prompt wrapper | Pipeline with some logic | Deterministic verification plus an agent | Novel method or a data flywheel |
| N | Novelty and wedge | 8% | Crowded with free tools | Incumbents do it partly | Clear wedge incumbents ignore | New category |
| M | Market size and urgency | 8% | Nice-to-have | Real but small | Large, budgeted | Huge and getting worse now |
| C | Validation possible at the event | 8% | Users not present | Could email some | Can interview 5+ on site | Can get a live "I'll try it" on site |
| S | Sponsor stacking | 7% | No sponsor fit | One sponsor | Two sponsors | Three or more sponsor prizes |
| P | Post-event startup potential | 10% | Hobby | Small business | Venture-scale with a known GTM | Team could raise on it |

Weights sum to 100. Feasibility gets the most weight because an unfinished MVP scores zero on demo.

## 4. Formulas

- **Weighted** = Σ(weight × score) / 100, on a 0-10 scale.
- **Risk-adjusted** = Weighted × (0.5 + 0.5 × p_success). `p_success` is the estimated chance that the full demo runs live by code freeze. The penalty is capped at 50% because a failed live run still has the recorded backup, the code and the pitch.
- **Track winner** = the highest risk-adjusted score in each of the 6 tracks.
- **Sensitivity**: 20,000 runs with weights redrawn from Dirichlet(α = base weight) and each score jittered by -1, 0 or +1. Reported as P(#1) and mean rank.
- **Break-even**: the p_success at which the leader loses first place.

## 5. Evidence re-score (Phase 1)

The starting scores are desk judgments. Before committing, each finalist runs a 45-minute spike and 3+ user conversations, then these updates apply:

| Evidence | Update |
|---|---|
| Spike produced the core artifact end-to-end (PR, alert, token) | F +1, p_success +0.10 |
| Spike blocked on an external dependency | F −2, p_success −0.20 |
| 3+ target users describe the pain unprompted | C +1, M +1 |
| A user commits ("run it on my repo", "I'd install it for my mom") | C +2, P +1 |
| Sponsor engineer confirms a prize fit | S +1 |
| Judge or mentor says "this already exists": name it, and if it really does | N −2 |

Update `scores.yaml`, re-run `python3 master-plan/scoring/score.py`, and commit the new `RESULTS.md`. The decision rule in `FINAL_DECISION.md` is applied to the re-run output, not to the starting scores.

## 6. Known biases in this scoring

- The team's stated strength is developer tools, which favors tracks 4 and 5 on F and J.
- R scores rely on the Fall 2026 RFS text summarized in `Compiled15_1B_YC_RFS_Strategy.docx`. Re-read the official page before Phase 1.
- Sponsor stacking (S) assumes the prizes listed for c0mpiled-15 (Luminal, MongoDB, AWS, on-device AI, Bloomerang nonprofits). Confirm them at check-in.
