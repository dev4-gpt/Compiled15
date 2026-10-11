**c0mpiled-15 \| Track 1A**

Self-Improving Agent Team: Project Shortlist, Scoring & Build Plan

*Companion to the Competition Intelligence report. Event: October 11, 2026. Scores are analyst judgments using the same weights as the original report; they are not the organizers' rubric.*

1\. Executive Brief

- **Decision:** Go for Track 1A. It is scored on relative improvement and problem difficulty, with a baseline, a round-by-round curve and a held-out test, which rewards rigorous evaluation over polish.

- **Primary recommendation:** ScheduleEvolve, where agents write and evolve scheduling-solver code scored by a deterministic evaluator.

- **Luminal-flavored alternative:** BatchBrain, the same engine applied to an LLM-inference batching policy. It fits Luminal's business and the lead judge.

- **Hedge:** Build one problem-agnostic Evolve Engine first. If the first problem stalls, swap the problem module, not the whole project.

2\. Changes From the Original Report

| **Item**      | **Change and reason**                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Build window  | Luma lists 12:00 PM to 8:00 PM, judging 8:00, awards 8:45. The original report said 12 to 7. Plans below use 8 hours and freeze code at about 6:45 PM. Confirm with organizers.        |
| PatchForge    | Downgraded from 8.95 to 8.50. Fixtures are self-authored, so difficulty is hard to prove, and a pass-rate metric saturates quickly, giving a flat improvement curve.                   |
| ScheduleArena | Renamed ScheduleEvolve and reframed. Agents evolve solver code (propose, test, learn) instead of only swapping jobs. This better matches "optimizing code" and gives a smoother curve. |
| New concepts  | BatchBrain, HotLoop and BotLadder added. All have objective, deterministic or simulatable scoring and fresh held-out tests.                                                            |

3\. Weighted Ranking (Track 1A Candidates)

Weights: judging alignment 20%, novelty 20%, feasibility 20%, measurable demo 15%, YC opportunity 15%, commercial potential 10%.

| **\#** | **Concept**          | **J** | **N** | **F** | **D** | **Y** | **C** | **Weighted** |
|--------|----------------------|-------|-------|-------|-------|-------|-------|--------------|
| 1      | ScheduleEvolve       | 10    | 9     | 9     | 10    | 8     | 8     | 9.10         |
| 2      | BatchBrain           | 10    | 9     | 8     | 10    | 7     | 7     | 8.65         |
| 3      | PatchForge (revised) | 9     | 8     | 8     | 9     | 9     | 8     | 8.50         |
| 4      | SQLMedic             | 9     | 8     | 9     | 9     | 7     | 8     | 8.40         |
| 5      | HotLoop              | 10    | 8     | 8     | 10    | 6     | 7     | 8.30         |
| 6      | BotLadder            | 9     | 7     | 9     | 10    | 5     | 5     | 7.75         |

Top candidates: ScheduleEvolve, BatchBrain, PatchForge. Most reliable live demo: ScheduleEvolve. Scores are sensitive to team skills and API behavior.

4\. Shared Core: The Evolve Engine

One reusable loop makes every concept below a swap of the problem module:

- Problem interface: generate_instances(seed) and evaluate(code, instances) returning a score plus diagnostics.

- Proposers: N agents on Luminal-hosted DeepSeek or GLM Flash each emit a candidate (a full function or a patch to the current champion).

- Sandbox: subprocess with timeout and memory limit. Crashes, timeouts and infeasible outputs score as failures.

- Feedback: top and bottom candidates, per-instance diagnostics and the champion's weaknesses go into the next round's prompt.

- Splits: dev instances drive search, validation instances pick the champion, held-out instances are generated from fresh seeds and touched once at the end.

- Logging: every round writes score, tokens, latency and code to JSON for the results dashboard.

5\. Technical Deep Dives

5.1 ScheduleEvolve (Recommended)

*Agents iteratively write and improve field-service dispatch heuristics, scored on a deterministic cost and tested on unseen workloads.*

**Problem and MVP**

30 jobs, 5 technicians, skill requirements, time windows, travel times, overtime and priorities. Objective J = a\*travel + b\*lateness + c\*overtime + d\*unassigned work, with hard checks for skill eligibility and non-overlap. Infeasible schedules score as failures.

**Architecture**

Instance generator, greedy baseline, parallel proposer agents each producing solve(instance), sandboxed run on dev instances, feasibility checker and cost evaluator, diagnostics (worst jobs, violated constraints) back to proposers, champion promotion, frozen held-out evaluation. OR-Tools is run once as a reference ceiling.

Technology: Python, OR-Tools (reference only), subprocess sandbox, Luminal OpenAI-compatible API, Streamlit and matplotlib for the score-vs-round curve and Gantt before/after.

**Evaluation**

Compare greedy, single-agent, N-agent at equal token budget, and OR-Tools on 50 held-out instances. Report mean cost, percent improvement over greedy, percent of the greedy-to-OR-Tools gap closed, infeasible-output rate, tokens and time.

**Eight-hour delivery plan**

| **Time**   | **Output**                                                                      |
|------------|---------------------------------------------------------------------------------|
| 12:00-1:00 | Instance generator, greedy baseline, feasibility checker, cost function         |
| 1:00-2:00  | Evolve Engine loop and sandbox                                                  |
| 2:00-3:30  | Parallel proposers and diagnostics feedback                                     |
| 3:30-4:30  | First full runs. Checkpoint: curve must trend down, else switch to the fallback |
| 4:30-5:30  | Ablation: 1 agent vs N agents, same budget                                      |
| 5:30-6:15  | Dashboard, Gantt visualization, run logs                                        |
| 6:15-6:45  | Frozen held-out evaluation                                                      |
| 6:45-8:00  | 90-second video, submission form, buffer                                        |

Fallback: agents propose structured swaps and reassignments; the deterministic engine validates and applies only legal moves.

90-second demo narrative: 0-15s greedy schedule with late jobs. 15-40s rounds running, competing agents, cost curve falling. 40-65s Gantt before/after. 65-85s held-out table with improvement and OR-Tools gap closed. 85-90s dispatch vertical.

**Judge questions to prepare**

- Why not just OR-Tools? We search for heuristics and show OR-Tools as an honest ceiling. Value is adapting to custom constraints that generic solvers model poorly.

- How is overfitting prevented? Separate dev, validation and frozen held-out sets on fresh seeds.

- Why multiple agents? Show the 1-agent vs N-agent ablation.

- Who buys it? One field-service vertical, with integration burden acknowledged.

After the event: pilot with one service vertical and learn which live constraints break generic routing software.

5.2 BatchBrain

*Agents evolve the batching and scheduling policy of an LLM-inference server, scored on a simulator.*

- **Problem:** Simulated GPU with bursty request traces, mixed prompt lengths, batch-size and memory limits. The policy decides batch composition and ordering.

- **Architecture:** Trace generator, static FIFO batching baseline, proposers write policy(state), simulator reports p95 latency, throughput and SLO violations, feedback, held-out traces with unseen burst patterns.

- **Evaluation:** FIFO baseline, a continuous-batching reference, and the evolved policy. Report p95 latency reduction on held-out traces.

- **Risk:** Simulator realism. Label it clearly as a simulator and set constants from public numbers. Timeline mirrors ScheduleEvolve.

- **Judge questions:** Is the sim realistic? Why not vLLM's scheduler? We compare against it as a reference; the pitch is automated per-workload policy search.

5.3 PatchForge (Revised)

Keep the original architecture with three changes: use three real-library breaking-change fixtures alongside synthetic ones, score on mutated held-out contract tests, and report valid patches per round so the curve is not flat. Weighted 8.50.

6\. Other Candidates (Brief)

| **Concept** | **Description**                                                                                                                              | **Key risk**                                   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| SQLMedic    | Agents rewrite slow SQL. Verified by result equivalence on random data; timed on DuckDB or SQLite with held-out data sizes. Metric: speedup. | Easy queries saturate. Use 10-15 hard queries. |
| HotLoop     | Agents optimize slow Python/numpy functions. Property tests for correctness; geometric-mean speedup on held-out functions and inputs.        | Timing noise. Use median of 5 runs.            |
| BotLadder   | Agents evolve a bot for a small game. Win rate against a fixed held-out opponent pool; Elo-style curve.                                      | Low YC and commercial relevance.               |

7\. Competition-Day Checklist

- Tonight: create a Luminal account at dash.luminal.com with a psu.edu email, confirm the OpenAI-compatible endpoint works, and note rate limits.

- Tonight: agree on objective, constraints, dev/validation/held-out split and roles on paper. Do not write code before noon.

- At registration: confirm team-size cap, build window end time and submission mechanics.

- Hour 1 to 2: get the evaluator working before any UI. Baseline numbers must exist before agents run.

- By 3:30 PM: if the cost curve is not falling, switch to the fallback or swap the problem module.

- Last phase: run the frozen held-out evaluation once, report it honestly, then record the video.

- Avoid: unmeasured multi-agent demos, tuning on the held-out set, hiding failures, and claiming beating OR-Tools unless the data shows it.

*Evidence note: all scores and plans are analyst judgments. Judge preferences are inferred from roles, not verified.*
