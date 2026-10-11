# v4: ranked ideas (including your four)

Scores come from `scoring/scores_v4.yaml`, run through `master-plan/scoring/score.py`. Full tables are in `scoring/RESULTS.md`.

How to read the columns:
- **Weighted** is the score out of 10 if the demo works.
- **p** is the chance the live proof lands by 7 PM.
- **Final** = Weighted × (0.4 + 0.6p).
- **Growth** (P) is startup potential after the event. **Wow** (W) is how much the agent does live. **Feasibility** (F) is how buildable it is in about 6 hours.

**No idea reaches 8.0 honestly.** The best ones sit between 7.0 and 7.6 weighted.

| Rank | Idea | Track | Weighted | p | Final | Wow | Growth | Feasibility | #1 in sims |
|---|---|---|---|---|---|---|---|---|---|
| 1 | AlgoTune Evolve | 1 | 7.00 | 0.70 | **5.74** | 6 | 7 | 8 | 47% |
| 2 | **DispatchIQ (Track 1)** (yours) | 1 | 7.22 | 0.65 | **5.70** | 8 | 6 | 8 | 38% |
| 3 | MigrateLoop | 1 | 7.18 | 0.60 | 5.46 | 7 | 8 | 6 | 8% |
| 4 | LeadAgent | 2 | 7.36 | 0.55 | 5.37 | 7 | 6 | 8 | 6% |
| 5 | ApplyGate | 2 | **7.56** | 0.45 | 5.07 | 8 | 7 | 6 | <1% |
| 6 | KernelForge | 1 | 7.20 | 0.50 | 5.04 | 7 | 8 | 6 | <1% |
| 7 | Fieldwork (built) | 2 | 7.06 | 0.50 | 4.94 | 4 | 6 | 9 | 0% |
| 8 | Countersign | 2 | 7.40 | 0.40 | 4.74 | **9** | 8 | 6 | 0% |
| 9 | AskBeforeYouPay | 2 | 6.70 | 0.50 | 4.69 | 5 | 6 | 6 | 0% |
| 10 | SettlementBot | 2 | 6.56 | 0.45 | 4.40 | 7 | 5 | 6 | 0% |
| 11 | Integration Medic | Sponsor | 6.22 | 0.35 | 3.79 | 8 | 7 | 5 | 0% |
| 12 | AgentRoom (yours) | Sponsor | 5.18 | 0.45 | 3.47 | 7 | 5 | 5 | 0% |
| — | PatchPilot (yours) | — | gated | | | | | | Sample repo is test data we'd write ourselves (G1) |
| — | AuditFlow (yours) | — | gated | | | | | | Made-up transactions, no buyer (G1) |
| — | DispatchIQ sold to HVAC shops | — | gated | | | | | | No buyers at the event; simulated data |

## The ideas in plain words

- **AlgoTune Evolve (Track 1):** a team of AI agents keeps rewriting slow scientific Python code (NumPy/SciPy tasks from a public benchmark) to make it faster, round after round. It is tested on new inputs it never saw. Safest Track 1 result, but the least visual.
- **DispatchIQ (Track 1):** agents write and keep improving the code that assigns technicians to jobs. A rule checker rejects illegal schedules. Shown on unseen days with a sick technician and a 2 PM emergency: schedule chart before and after, travel time saved, jobs on time. Most visual Track 1 option. Fits YC's "New OS for the Physical World".
- **MigrateLoop (Track 1):** agents learn to fix real open-source code broken by an API change. Strongest growth story (a YC request, "Self-Maintaining APIs"), but collecting real code is a build risk.
- **LeadAgent (Track 2):** a founder types "seed investors in climate" or "HVAC companies in PA". In minutes the agent returns 50 researched contacts with sources and draft emails, for $29. Easiest to sell to attendees, but Clay and Apollo are big incumbents.
- **ApplyGate (Track 2):** an internship agent that rejects poor fits and submits 10 strong, tailored applications for $9. Huge student pain: about 254 applicants per job in 2026. But submitting through real job sites is fragile.
- **KernelForge (Track 1):** agents make math kernels faster on CPU. Exactly the judge's field, but the test harness is ours to build and agents can cheat the timer.
- **Countersign (Track 2 + AGI prize):** an AGI agent runs a money errand for an elderly parent and stops for family to approve on their phones. The biggest wow and novelty, but the least reliable live.

## Recommendation
**Build DispatchIQ in Track 1.** It is statistically tied with AlgoTune (5.70 vs 5.74), and it beats it on wow (8 vs 6) and on fit with a YC request. It's also your idea, and it has a ready plan (ScheduleEvolve in `Compiled15_1A_Project_Strategy.docx`).

**Fallback inside the same engine:** if dispatch scores don't improve by 3:30, swap the problem module to AlgoTune tasks and keep the agent loop.

**Track 2 alternative if you'd rather sell:** LeadAgent.
