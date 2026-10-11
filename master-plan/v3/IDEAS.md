# Every idea so far

Scores come from three rubrics, so compare them **only within the same column**:
- **v1** (desk rubric, `master-plan/scoring/RESULTS.md`): risk-adjusted score.
- **v2** (event-metric rubric, `reports/Higher scoring YC RFS MVP ideas.md`): final score.
- **v3** (this rubric, `v3/scoring/RESULTS.md`): weighted / final, with the evidence rule and the 8.0 bar.

"Gated" means the idea failed a pass/fail rule in that version.

## v3: current candidates (sales-first, consulting-grade, sponsor-aligned)

| Rank | Idea | Lane | v3 weighted | p | v3 final | Status |
|---|---|---|---|---|---|---|
| 1 | **Fieldwork** (donor + sales practices) | Track 2 + Bloomerang + MongoDB + AWS | **7.92** | 0.60 | **6.02** | **Pick**. Prototype built. Below the 8.0 bar until a sale lands (see FINAL_DECISION.md) |
| 2 | ForwardCheck | Sponsor prizes only | 6.16 | 0.85 | 5.61 | Free top of a funnel; no track metric |
| 3 | Fieldwork Sales (SMB-only) | Track 2 | 7.44 | 0.55 | 5.43 | Subset of #1 |
| 4 | DonorPulse (nonprofit-only) | Track 2 + Bloomerang | 7.82 | 0.45 | 5.24 | Subset of #1 |
| 5 | MigrateLoop | Track 1 | 6.74 | 0.60 | 5.12 | Track 1 fallback |
| 6 | AskBeforeYouPay | Track 2 | 6.94 | 0.50 | 4.86 | Strongest demand stat; weak consulting fit |
| 7 | TenX | Track 1 | 6.24 | 0.60 | 4.74 | |
| 8 | ComplaintRadar | Track 1 | 6.28 | 0.55 | 4.58 | |
| 9 | SteerSwarm | Track 1 | 6.18 | 0.45 | 4.14 | |
| 10 | DiligenceDesk | Track 2 | 6.12 | 0.25 | 3.37 | Buyers not in the room; AI QoE tools exist |
| — | VetFollow | Track 2 | 6.06 | 0.25 | — | Gated: no clinic data or API on the day (G1, G3) |
| — | GiftSync | Sponsor prizes only | 5.64 | 0.30 | — | Gated: Bloomerang has no sandbox; needs live data (G1, G3) |
| — | ScaleMap (menu pricing teardown) | Track 2 | — | — | — | Merged into Fieldwork Sales |

## v2: rescoring around the event metric (18 ideas)

| Area | Ideas (v2 final) |
|---|---|
| Self-maintaining APIs | MigrateLoop 6.72 · Breakwatch 5.53 · FixMyRepo 5.28 · (DriftFix rescored 5.68, gated) |
| Multiplayer AI | SteerSwarm 5.92 · RoomAgent 5.47 · QuorumBot 5.12 · (WarRoom 4.67, gated) |
| Consumer for 1B people | ForwardCheck 6.35 · TenX 6.11 · DocSnap 5.01 · (DocSaathi 4.66, gated) |
| Aging | AskBeforeYouPay 6.23 · ScamEvolve 5.87 · SafeWord 4.13 · (ScamShield 4.52, gated) |
| Compliance | ComplaintRadar 5.87 · ClaimCheck 5.04 · RegDiff-PR 4.81 · (RegDiff 4.37, gated) |
| Proving you're human | OneVote 5.07 · AgentPass 4.40 · BotLedger 4.38 · (HumanPass 3.76, gated) |

## v1: desk scoring (18 ideas)

| Area | Ideas (v1 risk-adjusted) |
|---|---|
| Self-maintaining APIs | DriftFix 7.94 · SchemaSentinel 6.22 · SDKSmith 5.76 |
| Aging | ScamShield 7.15 · CareCircle (gated) · MedMinder (gated) |
| Multiplayer AI | WarRoom 6.98 · Huddle 6.48 · PlanParty (gated) |
| Compliance | RegDiff 6.58 · LicenseLoop 6.54 · EvidenceBot 6.02 |
| Consumer for 1B people | DocSaathi 6.39 · VoiceLedger 5.82 · LabelLens (gated) |
| Proving you're human | HumanPass 6.04 · HumanProof 5.07 · HumanMark (gated) |

Earlier Track 1A concepts (from `Compiled15_1A_Project_Strategy.docx`): ScheduleEvolve, BatchBrain, PatchForge, SQLMedic, HotLoop, BotLadder.

## Why the scores changed
- **v1** rewarded what an imagined YC partner would like, and accepted fixtures the team wrote itself.
- **v2** rewarded the event's own metrics: held-out improvement and real sales.
- **v3** adds what the user asked for:
  - consulting-grade output;
  - demand evidence from public sources;
  - closing a gap for a sponsor using its own API;
  - fit with a team that sells;
  - a hard rule that every score of 8 or more must cite evidence.

  Fieldwork rises to the top because it is the only idea that is already built and tested, and it targets the track with the most prize money with a buyer-facing product.
