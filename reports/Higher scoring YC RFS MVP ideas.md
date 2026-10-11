# Score the proof, not the pitch

**Build MigrateLoop: a team of parallel agents on Luminal that learns to migrate real public Python code across a real breaking API change (openai-python v0 to v1 is the leading candidate). Enter it in c0mpiled-15 Track 1 and in the MongoDB and Luminal sponsor prizes.** Under a rescoring method built around what this event appears to judge, it scores **6.72**, first of 18 new ideas. Keep **AskBeforeYouPay** as the backup: a scam-check line for parents and grandparents that students can pre-buy for their family, entered in Track 2. It scores **6.23**, or **6.35** for its free funnel alone. The earlier plan's ideas scored low for two reasons, and generic framing was only part of it. The plan was tuned to a "YC partner reads the RFS" rubric, while the event, judging from search extracts of its Luma page, has two tracks with objective metrics. **Track 1** is judged on **relative improvement on fresh held-out tests** from a self-improving agent team running on Luminal. **Track 2** is judged on **actual sales during the event** ([Luma](https://luma.com/compiled-jjvw)). The old rubric also gave top demo marks to fixtures the team wrote itself. Rescored under the new method, the old winner DriftFix drops from 7.94 to **5.68**, and every old track winner fails at least one new gate. These results depend on event rules that came from search snippets. **Confirm at check-in that Track 1 exists as described.** If it does not, the ranking flips to the real-user consumer and aging projects (see the switch rules below).

## c0mpiled-15 rewards a number on screen, not an RFS essay

The event runs Sunday, October 11, 2026, from noon to 9 PM at Penn State's Engineering Design and Innovation Building, with **more than $10K in prizes**, YC founders judging, **judging at 7:00 PM** and awards at 8:15 PM ([Luma](https://luma.com/compiled-jjvw)). That leaves about **seven build hours, not eight**. Two tracks appear in the page extracts.

- **Track 1 (Transpose Platform):** build a self-improving agent team on **Luminal (YC S25)** using DeepSeek or GLM Flash. Agents run in parallel and refine a solution over rounds on a problem with a measurable outcome. Teams show a baseline, then improvement, then results on fresh tests not used during optimization. Judging is on "**relative improvement and problem difficulty**". Prizes are **$3,000 plus a session with Luminal's founder**, $1,500 and $500.
- **Track 2 (Engineering Entrepreneurship):** winners "successfully build and validate their product by getting **actual sales during the event**". Pools come from AWS (up to $5,000), Engineering Entrepreneurship and Bloomerang.
- **Sponsor prizes:** MongoDB ($1,000 credits, swag, an article) and Luminal ($1,000 inference credits).

All of this is from [Luma](https://luma.com/compiled-jjvw). None of the extracts showed a track judged on fit with the YC Fall 2026 RFS, even though earlier c0mpiled editions used RFS lists as tracks ([c0mpiled-13](https://luma.com/olys436o)). The six RFS areas are therefore best treated as the problem source and the pitch language, and the two tracks as the scoreboard.

Evidence from outside the event points the same way. YC's own guidance is "make something people want" and "do things that don't scale", with recruiting users by hand as the canonical move ([Paul Graham](https://www.paulgraham.com/ds.htm)). At a YC-run hackathon, partners asked for a raw live demo and a two-sentence description from each team member ([Princeton ODUS](https://odus.princeton.edu/news/student-organization-spotlight-practical-hacking-yc-hackathon)). Recent winners show the same pattern of **built-in verification**:

- First place at Anthropic's Opus 4.8 Build Day traced every reconstructed part to a historical source and used verifier sub-agents.
- Second place, Sim Francisco, checked its synthetic-population forecasts against the real 2024 election and Prop A results ([Claude blog](https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon)).

Revenue-judged hackathons exist and reward real money. The RevenueCat Shipaton winner reached **$1,100 MRR in ten days**, though over a far longer window than one afternoon ([RevenueCat](https://www.revenuecat.com/blog/company/shipaton-2025-winners)).

The failure modes are just as consistent. Judges "have seen a hundred GPT wrappers" ([HackerEarth](https://www.hackerearth.com/blog/hackathon-ideas)). Experienced judges probe with inputs the team did not prepare, and they ask for the test set behind any accuracy claim ([DEV](https://dev.to/pranjulrathour/judging-ai-hackathon-projects-what-to-check-when-every-team-says-we-used-ai-19mb)). JetBrains judges add that "a strong project with a confusing demo loses to a simpler project that the judges understand" ([JetBrains](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)). One judging-platform study found agreement between judges "**no better than chance**" ([DEV](https://dev.to/techtush/the-judges-agreed-no-better-than-chance-4-lessons-from-building-a-hackathon-judging-platform-3apn)). That is the strongest argument for this whole report: **an objective number (a held-out delta, a Stripe payment, a merged PR) is the only evidence that holds up regardless of which judge you get.**

The free stack makes that kind of proof cheap. The team's own scaffolding can be built on:

- **Inference:** Groq (llama-3.1-8b at 14,400 requests/day; 70B at about 100K tokens/day), Cerebras (about 1M tokens/day) and OpenRouter free models (50 requests/day until $10 has ever been spent) ([localaimaster](https://localaimaster.com/blog/groq-api-free-guide); [fast.io](https://fast.io/resources/cerebras-rate-limit/); [TrueFoundry](https://www.truefoundry.com/de/blog/openrouter-rate-limits-your-free-tier-depends-on-what-youve-already-paid)).
- **Data and realtime:** Supabase or MongoDB for data, and Cloudflare Durable Objects or Liveblocks (500 rooms, 10 connections per room) for multiplayer state ([Cloudflare](https://www.cloudflare.com/plans.md); [Liveblocks](https://liveblocks.io/docs/pricing/limits)).
- **Telephony:** LiveKit's free plan includes a US phone number and 1,000 agent-minutes ([FutureAGI](https://futureagi.com/blog/livekit-alternatives-2026/)).
- **PR bot:** the Claude Code GitHub app opens real PRs from an `@claude` mention ([Claude Code docs](https://code.claude.com/docs/en/github-actions)).

Evidence on AI coding speedups is mixed. METR's RCT found experienced developers 19% slower on mature codebases ([ScienceBlog](https://scienceblog.com/t-a-randomized-trial-by-metr-found-that-experienced-developers-completed-real-coding-tasks-19-slower-when-allowed-to-use-ai-tools-yet-afterwards-they-estimated-on-average-that-ai-had-made-them-20-fast/)). Greenfield hackathon glue code is a different case from mature codebases, but integration debugging (OAuth, webhooks, telephony) remains where hours disappear. **Capabilities are no longer the differentiator. The proof mechanism is.**

## The v1 rubric measured an imagined judge and self-authored evidence

The earlier plan in `master-plan/` scored 18 concepts on ten criteria and picked DriftFix with a reported 98.4% probability of ranking first. Six structural problems make that confidence misleading.

1. **It had no criterion for the event's actual scoring.** RFS fit and judge appeal together took 24%, both modelling a YC partner reading the RFS. Nothing scored "produces a held-out improvement curve" or "makes a sale today", even though those appear to be the only two track metrics.
2. **It rewarded synthetic evidence.** Gate G3 explicitly allowed demo data to be "made" before code freeze. DriftFix earned **D = 10** on OpenAPI v1-to-v2 fixtures the team wrote itself, even though its own risk table lists "Fixtures are self-authored" as a risk and defers real Stripe spec replays to after the event (`master-plan/05_self_maintaining_apis/PLAN.md`).
3. **Validation counted interviews, not usage.** Criterion C rewarded the chance to "interview 5+ on site". Nothing rewarded users acting, paying or merging during the event, which is the evidence Track 2 and YC culture both prize.
4. **The risk discount was too gentle.** Final = Weighted × (0.5 + 0.5p) keeps half the score when the live demo fails. In a sales track or a held-out track, a proof that does not land is worth close to nothing.
5. **The 98.4% robustness figure is circular.** The Monte Carlo jittered the analyst's own scores by ±1 and resampled weights around the analyst's own priors. It could never test the structural question of whether the rubric matches the judges. In this setting, structural error dominates numeric noise.
6. **Sponsor credit was assumed, and free-stack leverage was not scored.** Criterion S assumed on-device AI and Bloomerang-nonprofit prizes that the extracts do not confirm. Nothing scored whether an idea is built around something that only just became cheap, which is the core of Raphael Schaad's consumer RFS argument that agent cost "can run $1,000 a month in tokens… but that is falling 10x a year" ([YC RFS](https://www.ycombinator.com/rfs)).

## Scoring v2: four gates, ten criteria, a 60% failure penalty

The new method keeps the old pipeline (gates, weighted score, risk adjustment, Monte Carlo) so the team's `score.py` can be adapted. It changes what is measured.

**Gates (all must pass):**

| Gate | Rule |
|---|---|
| G1 | The proof uses inputs the team did not author: real repos, live sites, public datasets, real users or real payments |
| G2 | No regulated claim, and consent-safe (no unannounced recording of a third party) |
| G3 | Free stack on laptops, with no same-day third-party approval (for example, WhatsApp Business verification) |
| G4 | Lands in at least one confirmed track or sponsor prize |

**Criteria and weights:**

| Code | Criterion | Weight | Anchor at 2 | Anchor at 10 |
|---|---|---|---|---|
| E | Event-track scorability | 20 | No confirmed track judges what it produces | Produces the track metric (held-out delta or a sale) on a hard, real problem with a clean baseline |
| V | Verifiable real-world proof | 18 | Self-authored fixtures (4 = replay of public data; 6 = real third-party artifacts; 8 = 10+ real users or real PRs) | Paid sales, a merged upstream PR, or strangers' usage logged live |
| F | Feasibility in ~7 hours on free tiers | 14 | Needs approvals or paid APIs | Done by 4 PM with fallbacks |
| R | RFS literal fit | 10 | Tangential | Demo uses the RFS text's own nouns and verbs |
| U | Users reachable in the room | 10 | Users absent | Everyone present can act live in 30 seconds |
| D | Demo clarity | 8 | Needs explanation | Judge takes part and sees the result change |
| N | Novelty vs named incumbents | 6 | Shipped by a big incumbent | New category |
| L | Free-stack leverage | 5 | Fights free tiers | The cheapness is the product insight |
| S | Prize stacking | 5 | One prize at most | Two tracks plus sponsors |
| P | Post-event potential | 4 | Hobby | Fundable |

**Formulas:**

- Weighted = Σ(weight × score) / 100, on a 0-10 scale.
- **Final = Weighted × (0.4 + 0.6 × p)**, where p is the probability that *the live proof* lands by 7 PM: a held-out delta for Track 1, at least one real sale for Track 2, or roughly 10 real users or real PRs otherwise. It is not the probability that the code runs. The penalty for failure rises from 50% to 60% because a failed proof zeroes most of E and V (38% of weight) and dents D.
- **Weighted is also the score's ceiling** (Final at p = 1), so every idea has an explicit highest achievable score.
- Sensitivity: 20,000 runs with Dirichlet-resampled weights, ±1 score jitter and ±0.1 jitter on p.
- Scenario re-runs model the structural uncertainty about event rules directly: Track 1 absent, Track 2 absent, or track rules ignored.

Machine-readable scores, anchors, gates and per-idea proof mechanisms are in `research_notes/Higher scoring YC RFS MVP ideas/scores_v2.yaml`. It uses the same keys as `master-plan/scoring/scores.yaml`. To reproduce the numbers below, `score.py` needs one change: `risk_adjusted` should return `w * (0.4 + 0.6 * p)`. Legacy candidates fail the new gates and are dropped by the script's gate filter, so read their comparison scores from this report or disable the filter.

## Eighteen reframed ideas, three per RFS area

Each idea below is designed backwards from a proof mechanism. Scores are Final (Weighted ceiling in brackets). The comparison is the old track winner rescored under v2.

### Self-maintaining APIs: turn DriftFix into a learning loop on real code

The RFS describes agents that scan codebases and push the fix as a PR when a provider changes its interface. Its author cites his AWS experience that "over 30% of our service downtime was due to external api/package changes going unnoticed" ([YC RFS](https://www.ycombinator.com/rfs)). The pieces exist but are not connected:

- **Detecting breaking spec changes:** oasdiff ([oasdiff](https://www.github.com/Tufin/oasdiff)).
- **SDK generation is in flux:** Stainless is winding down its hosted generator after its reported acquisition by Anthropic ([Scalar](https://scalar.com/resources/stainless-wind-down)).
- **Closest open-source rival:** "Patch", which is TS-only and early ([Product Hunt](https://www.producthunt.com/p/patch-4/patch-6)).
- **Research-only version of the loop:** APIShift, an RL environment trained on real Stripe, GitHub and OpenAI version diffs ([APIShift](https://yaswanth169-apishift-env.hf.space/)).
- **Why verification is the moat:** Brex found a single large migration agent hallucinated methods and bypassed validation gates, and moved to orchestrated automations for a 32x speedup ([Brex](https://www.brex.com/journal/agent-automations-for-big-migrations)).

That is exactly the shape Track 1 rewards: parallel agents, an objective evaluator, improvement over rounds.

| Idea | Free tools | 7-hour sketch | Live proof | v2 Final [ceiling] |
|---|---|---|---|---|
| **MigrateLoop** (T1 + MongoDB + Luminal) | Luminal DeepSeek/GLM Flash; `gh search code`; pyright; pytest with a mocked HTTP transport; LibCST; MongoDB Atlas free tier; Claude Code for dev | Harvest 40-60 real files using openai<1 calls and split them by repo into train and held-out (12:00-12:45). Build the evaluator: type check against the v1 SDK, mocked call execution, no old symbols left (by 2:00). Run 8 parallel workers per round while a critic agent rewrites a shared migration playbook stored in MongoDB (rounds 0-N by 4:30). Freeze, then run held-out once (5:30) | Held-out pass@1 at round 0 vs round N; 2-3 green PRs on forks of real repos; one polite upstream PR to an active repo | **6.72** [8.20] |
| FixMyRepo (T2) | Same engine via the Claude Code GitHub app or an MCP server; Stripe payment link | Package the engine as "pay $5, get a verified PR off deprecated SDK calls" and sell it to attendees | Payments plus PRs on buyers' repos | 5.28 [7.55] |
| Breakwatch (sponsor only) | oasdiff on consecutive commits of stripe/openapi or github/rest-api-description | A provider-side GitHub Action posts the breaking list, a generated migration recipe and affected public dependents | Real historical breaking changes, hand-checkable | 5.53 [6.28] |
| *DriftFix, v1 plan* | — | Self-authored v1-to-v2 fixtures, one pass | PR on its own repo | *5.68 (v1: 7.94); fails G1* |

MigrateLoop answers both of the old plan's weaknesses at once. The fixtures become real public code, and the single pass becomes a measured improvement curve with a held-out split. Publish a hash of the held-out list in a public commit before optimization starts, so judges can verify the split was not tuned on. An ICWE 2024 study of OpenAPI histories found 1,970 APIs that sometimes ship breaking changes in minor or patch releases, which shows the problem is pervasive ([USI](https://design.inf.usi.ch/sites/default/files/biblio/apiace-icwe2024.pdf)). The specific migration target and its public hit count are training-knowledge assumptions. Run the code search before noon (see caveats).

### Multiplayer AI: make the agent team itself the multiplayer session

Aaron Epstein's RFS wants anyone on a team to "drop into the same live agent session to watch it work, redirect it, and hand it off" ([YC RFS](https://www.ycombinator.com/rfs)). The obvious pitches are taken:

- **Multiplayer coding sessions:** covered by Mosaic, Glen, Superconductor and Conductor ([YC: Mosaic](https://www.ycombinator.com/companies/mosaic-inc); [usepoly](https://usepoly.co/yc-multiplayer-ai)).
- **AI in group chat:** ChatGPT shipped group chats for up to 20 people in November 2025 ([iPhone in Canada](https://www.iphoneincanada.ca/2025/11/21/openai-chatgpt-group-chat)).

The open question in the space is who may approve what a shared agent does, and who gets credit ([softworker](https://softworker.ai/blog/ai-agent-collaboration-platform)).

| Idea | Free tools | 7-hour sketch | Live proof | v2 Final [ceiling] |
|---|---|---|---|---|
| **SteerSwarm** (T1 + sponsors) | Luminal; Durable Objects or Liveblocks; Next.js | Wrap any Track 1 optimization loop in a QR-joinable live console where people watch rounds, inject hints and take the wheel. Run an autonomous arm and a human-steered arm | Held-out improvement for both arms, plus the count of distinct live steerers | **5.92** [7.79] |
| RoomAgent | Liveblocks; Playwright/Stagehand; Groq | Judges scan a QR and co-steer one browser agent doing a real group task (the team's dinner order) with vote and veto | Steerers, interventions, task done | 5.47 [6.67] |
| QuorumBot (T2) | Telegram Bot API; Cerebras/Groq | A group-chat agent proposes actions, executes on quorum and logs who approved what; sold as a $3 team pass | Groups added, approvals, passes sold | 5.12 [6.74] |
| *WarRoom, v1 plan* | — | Simulated incident | — | *4.67 (v1: 6.98); fails G1* |

SteerSwarm is the only way to put the Multiplayer RFS into a scored track. Its ablation (does human steering beat autonomy on held-out cases?) is a real research finding, not a staged demo. It carries the most build risk, which is why its p is 0.60.

### Consumer products for 1B people: prove the cost curve, or put real phones in the loop

Schaad's RFS argues that per-user agent cost, not demand, blocks the next billion-user product ([YC RFS](https://www.ycombinator.com/rfs)). On X he has also said there is "no AI-native distribution channel for new consumer apps" ([X](https://x.com/raphaelschaad/status/2089399226824634634)). WhatsApp reaches more than 3B users, with about 535-550M in India ([Hyperleap](https://hyperleap.ai/blog/whatsapp-statistics-india-2026)). But Meta AI already sits inside WhatsApp, and Business API verification fails gate G3 on the day. Telegram is the honest zero-install channel for an afternoon.

| Idea | Free tools | 7-hour sketch | Live proof | v2 Final [ceiling] |
|---|---|---|---|---|
| **ForwardCheck** (sponsor; feeds the backup) | Telegram Bot API; Gemini Flash for images; Groq Whisper for voice notes; URL reputation check | Forward any suspicious text, screenshot or voice note and get a verdict in your language plus a share-to-family card | Attendees' own spam, with unique users logged live | **6.35** [6.98] |
| TenX (T1 + sponsors) | Luminal GLM Flash; public multilingual receipt/document datasets (verify availability); MongoDB | An agent team evolves prompts and routing until the cheap model matches a frontier reference on held-out real documents. Report cost per user per month against YC's $1,000 | Held-out accuracy at round 0 vs N; cost per user | 6.11 [7.45] |
| DocSnap (T2) | Telegram; Gemini Flash; Stripe link | Photo of a lease or bill gets an explanation and a drafted next action; $3 per document to students | Paid uses | 5.01 [7.16] |
| *DocSaathi, v1 plan* | — | WhatsApp onboarding | — | *4.66 (v1: 6.39); fails G3* |

ForwardCheck ranks second overall almost entirely on reachability and certainty (U = 9, p = 0.85). It lands only a sponsor prize, though, so its best use is as the free top of AskBeforeYouPay's funnel. TenX is the purest expression of Schaad's cost thesis and a strong second Track 1 choice.

### Aging population: sell to the grandchild, not the grandparent

Elder fraud is the most quantifiable pain in any of the six areas:

- **Losses:** the FBI IC3 2025 report puts losses for people 60+ at about **$7.7B, up roughly 59%**, with an average loss near $38,500 ([AARP](https://www.aarp.org/money/scams-fraud/fbi-ftc-report-2025-losses); [HousingWire](https://www.housingwire.com/articles/fbi-seniors-cybercrime-2025/)).
- **Scam types:** investment and tech-support scams dominate, and both persuade victims over days, not in a single call.
- **Caregivers:** there are **63M US family caregivers** ([AARP](https://www.aarp.org/press/releases/2025-07-24-new-report-reveals-crisis-point-for-americas-63-million-family-caregivers.html)).
- **Crowded segments:** AI companion calls (Meela, ElliQ) and call blocking ([BusinessWire](https://www.businesswire.com/news/home/20250911525548/en/Meela-Launches-Personalized-AI-Companion-to-Combat-Loneliness-Epidemic-Among-Seniors)).
- **Legal limit:** all-party-consent recording laws in states including CA, FL, IL and PA (the event is in Pennsylvania) make the old ScamShield's live call interception a G2 failure ([Dialzara](https://dialzara.com/blog/call-recording-laws-ai-agents-by-state)).

| Idea | Free tools | 7-hour sketch | Live proof | v2 Final [ceiling] |
|---|---|---|---|---|
| **AskBeforeYouPay** (T2 + MongoDB) | Telegram bot plus a LiveKit or Twilio-trial number; Groq/Cerebras; IC3 typology prompts; Stripe payment link; MongoDB | The senior forwards a message, or reads it to the line, and gets a risk verdict. The family approver is pinged with Approve or Stop. A landing page sells a "$5 family setup", and buyers enroll a parent's number on the spot | Real Stripe payments; real scam texts forwarded by attendees, logged live | **6.23** [8.20] |
| ScamEvolve (T1) | Luminal; public scam/spam corpora | An agent team evolves the detector over rounds and is tested on held-out real scam texts | Held-out precision/recall delta | 5.87 [6.67] |
| SafeWord | LiveKit number; announced bot | The senior conferences a suspicious "grandchild" call into a bot that calls the real relative's known number and checks the family safe word | Live call with a judge's phone | 4.13 [5.90] |
| *ScamShield, v1 plan* | — | Staged call interception | — | *4.52 (v1: 7.15); fails G1, G2* |

AskBeforeYouPay has the best buyer story at the event. Every student in the room has a parent or grandparent, and most have scam texts on their own phones right now. Because the senior starts every check, the flow is consent-safe. Its weighted ceiling ties MigrateLoop at 8.20. Only its lower chance of an actual sale (p = 0.60) puts it second.

### Compliance infrastructure: use free federal data that is checkable to the paragraph

The RFS says compliance work is "monitoring regulatory changes, flagging anomalies, generating reports, and keeping audit trails" ([YC RFS](https://www.ycombinator.com/rfs)). The platform layer is funded beyond a hackathon's reach: Norm Ai reportedly raised $120M at a $1.2B valuation ([AI2Work](https://ai2.work/blog/norm-ai-s-120m-round-turns-compliance-into-an-agent-workload)), and Cardamon works on regulatory applicability ([YC Regtech](https://www.ycombinator.com/companies/industry/Regtech)). Free, keyless federal data gives hand-checkable outputs:

- **Federal Register API** ([docs](https://www.federalregister.gov/reader-aids/developer-resources/rest-api)).
- **eCFR**, which offers point-in-time versions ([docs](https://www.ecfr.gov/reader-aids/ecfr-developer-resources/rest-api-interactive-documentation)).
- **CFPB complaint database API** (endpoint unverified this session).

| Idea | Free tools | 7-hour sketch | Live proof | v2 Final [ceiling] |
|---|---|---|---|---|
| **ComplaintRadar** (T1 + sponsors) | CFPB complaints API; eCFR; Luminal; MongoDB | An agent team learns features and hypotheses that forecast week-over-week complaint spikes per company or product. It is backtested on held-out future weeks, and each flag ships with an eCFR-cited memo | Held-out backtest delta on real public data; paragraph-linked memos | **5.87** [7.43] |
| ClaimCheck (T2) | Playwright; eCFR; Groq | Crawl 10 real fintech or startup landing pages, map claims ("FDIC insured", "0% APR") to eCFR/FTC paragraphs, and sell a $10 page check to founders in the room | A hand-verifiable table of 10 real sites; paid checks | 5.04 [6.91] |
| RegDiff-PR | Federal Register + eCFR diffs | A real rule change becomes a redline PR on disclosure templates, with the git history as the audit trail | Real rules; a self-built target repo | 4.81 [5.86] |
| *RegDiff, v1 plan* | — | Self-written internal policies | — | *4.37 (v1: 6.58); fails G1* |

ComplaintRadar turns "flag anomalies" into a forecasting problem with a held-out future, the same ground-truth pattern that won Sim Francisco its place.

### Proving you're human: the weakest fit for a seven-hour, scored event

The RFS opens with the $25 million deepfake CFO call and asks for verified humans "without making everyone give up their privacy" ([YC RFS](https://www.ycombinator.com/rfs)). The infrastructure layers are moving fast:

- **Agent authentication:** Web Bot Auth is now an IETF working-group draft by Cloudflare and Google ([IETF](https://datatracker.ietf.org/doc/html/draft-ietf-webbotauth-httpsig-protocol-00)).
- **Unique human behind an agent:** World's AgentKit delegates a verified human's World ID to an agent ([HackerNoon](https://hackernoon.com/world-expands-agentkit-so-ai-agents-can-prove-a-unique-human-is-behind-them)).
- **Bot detection:** Roundtable already sells invisible bot detection inside YC ([YC: Roundtable](https://www.ycombinator.com/companies/roundtable)).

| Idea | Free tools | 7-hour sketch | Live proof | v2 Final [ceiling] |
|---|---|---|---|---|
| **OneVote** (sponsor) | `@simplewebauthn`; Cloudflare Turnstile; Workers/D1 | A passkey-gated one-human-one-vote audience poll for the room; headless agents and duplicate voters are blocked and shown live | Real attendees voting; logged block events | **5.07** [6.95] |
| AgentPass | Passkeys + Web Bot Auth signing (cloudflare/web-bot-auth, verify) | A delegation token binds an agent key to one human with per-human quotas | Real headless agents vs a deployed page | 4.40 [6.28] |
| BotLedger | Published crawler IP ranges; server logs | Classify real bot traffic and flag spoofed GPTBot/Googlebot | Real logs from team members' sites | 4.38 [5.54] |
| *HumanPass, v1 plan* | — | Simulated issuer | — | *3.76 (v1: 6.04); fails G1* |

No idea in this area reaches a scored track. Pursue it only if the organizers confirm a prize for it.

## MigrateLoop leads at 6.72, and one check-in question can flip it

| Rank | RFS area | Idea | Lane | Weighted (ceiling) | p | **Final** |
|---|---|---|---|---|---|---|
| 1 | Self-maintaining APIs | **MigrateLoop** | T1 + MongoDB + Luminal | 8.20 | 0.70 | **6.72** |
| 2 | Consumer 1B | ForwardCheck | MongoDB | 6.98 | 0.85 | 6.35 |
| 3 | Aging | **AskBeforeYouPay** | T2 + MongoDB | 8.20 | 0.60 | 6.23 |
| 4 | Consumer 1B | TenX | T1 + sponsors | 7.45 | 0.70 | 6.11 |
| 5 | Multiplayer | SteerSwarm | T1 + sponsors | 7.79 | 0.60 | 5.92 |
| 6 | Compliance | ComplaintRadar | T1 + sponsors | 7.43 | 0.65 | 5.87 |
| 7 | Aging | ScamEvolve | T1 + sponsors | 6.67 | 0.80 | 5.87 |
| 8 | Self-maintaining APIs | Breakwatch | MongoDB | 6.28 | 0.80 | 5.53 |
| 9 | Multiplayer | RoomAgent | MongoDB | 6.67 | 0.70 | 5.47 |
| 10 | Self-maintaining APIs | FixMyRepo | T2 | 7.55 | 0.50 | 5.28 |
| 11 | Multiplayer | QuorumBot | T2 | 6.74 | 0.60 | 5.12 |
| 12 | Proving human | OneVote | MongoDB | 6.95 | 0.55 | 5.07 |
| 13 | Compliance | ClaimCheck | T2 | 6.91 | 0.55 | 5.04 |
| 14 | Consumer 1B | DocSnap | T2 | 7.16 | 0.50 | 5.01 |
| 15 | Compliance | RegDiff-PR | MongoDB | 5.86 | 0.70 | 4.81 |
| 16 | Proving human | AgentPass | MongoDB | 6.28 | 0.50 | 4.40 |
| 17 | Proving human | BotLedger | MongoDB | 5.54 | 0.65 | 4.38 |
| 18 | Aging | SafeWord | MongoDB | 5.90 | 0.50 | 4.13 |
| — | (v1 winners rescored) | DriftFix 5.68 · WarRoom 4.67 · DocSaathi 4.66 · ScamShield 4.52 · RegDiff 4.37 · HumanPass 3.76 | all fail ≥1 gate | | | |

Every reframed track leader beats its v1 counterpart under the same rubric, by **1.0 to 1.7 points**. The v1 and v2 numbers sit on different scales, so the comparison is within v2 only.

The sensitivity analysis is honest about uncertainty where v1 was not. In 20,000 perturbed runs, MigrateLoop finishes first **45%** of the time (mean rank 2.3), against 21.5% for ForwardCheck and 15% for AskBeforeYouPay. MigrateLoop loses first place if its p falls below **0.62**. The scenario runs matter more than the noise:

- **Track 1 absent:** ForwardCheck (6.35) and AskBeforeYouPay (6.23) overtake MigrateLoop (5.74).
- **Track rules ignored entirely:** ForwardCheck leads at 7.03.
- **Track 2 absent:** the order does not change.

**Recommendation.** Build **MigrateLoop**. Enter Track 1, then MongoDB (store playbook versions, runs and cases in Atlas, and show playbook diffs per round) and the Luminal credits prize (all agent inference on Luminal, as Track 1 requires). Pitch it in the Self-Maintaining APIs RFS's own words: it "scans codebases" and "pushes the fix as a PR". Present it as the first proof that a cheap open-weight model team can *learn* a migration and then apply it to code it has never seen.

Stack prizes only if the core is green at the 3:30 PM checkpoint and the rules allow entering two tracks. In that case, one teammate sells FixMyRepo to attendees from the same engine for a Track 2 entry. The ceiling move is to get one upstream PR merged during the event. That lifts V to 10 and the ceiling to about 8.56.

Role split for four people:

- **Role A:** agent loop on Luminal.
- **Role B:** evaluator and held-out harness. Build this first.
- **Role C:** MongoDB and the round-chart UI.
- **Role D:** corpus harvest, fork PRs, rules check and pitch.

Freeze the playbook at 5:30 PM, run the held-out set exactly once, and record a backup video by 6:30 PM.

**Switch rules.**

1. If check-in shows **no Track 1** as described, or Luminal access is unavailable, switch before noon to **AskBeforeYouPay with ForwardCheck as its free funnel**. Enter Track 2 and MongoDB.
2. If the code search before noon finds fewer than about 30 real candidate files for any migration target, switch the Track 1 problem to **TenX** or **ComplaintRadar**. Both run on public datasets with a clean held-out split.
3. After noon, switch only within the project. Fall back to deterministic LibCST codemods plus LLM residuals, which the old DriftFix plan already specified.

## What is still unverified

**The event rules, the RFS wording and several endpoints come from search snippets, not pages read directly.** Here is what needs checking:

- **Access was blocked.** Both research sessions behind this report were blocked from ycombinator.com and luma.com. Every RFS quotation is a search-engine extract or a secondary summary.
- **Author bylines are secondary.** The bylines for the Aging, Compliance and Proving-Human requests come only from secondary sites.
- **Track details may be incomplete.** The track descriptions came from extracts, one of which warned the page text was "jumbled" and another of which did not show Track 2 at all. One extract labelled the Luminal brief "option A", hinting at other options, possibly including an RFS track ([Luma](https://luma.com/compiled-jjvw)).
- **Questions for check-in:**
  - Does Track 1 exist exactly as described?
  - Can one team enter both tracks?
  - Do sales to fellow attendees count, and is there a minimum?
  - Is code written before noon allowed? (Corpus harvesting before noon may be data preparation, not code. Declare it either way.)
  - Is the AWS pool cash or credits?
- **Tool details are unverified.** The MigrateLoop corpus (the openai v0-to-v1 hit counts), the CFPB API endpoint, the cloudflare/web-bot-auth repo and the public receipt datasets for TenX are training-knowledge items that need a live check.
- **Free-tier limits move.** The numbers conflict across sources: Gemini's free tier ranges from 100 to 1,500 requests/day depending on the source. Check every console the morning of the event and give each teammate their own keys.
- **Mass PRs are spam.** Opening PRs on strangers' repos at scale violates GitHub norms. Keep real PRs on forks, plus at most one or two polite upstream PRs to clearly active projects.
- **All scores are analyst judgments.** They are tied to explicit anchors, and the method's worth lies in making the assumptions editable in `scores_v2.yaml`, not in the decimals.

## Conclusion

The bigger change is not swapping ideas but changing what counts as evidence. v1 asked "which concept would a YC partner like?" and answered it with fixtures the team controlled. v2 asks "what objective number will exist on screen at 7 PM that no judge can dispute?", and that question reshapes every RFS area. Self-Maintaining APIs becomes a learning curve on real code. Aging becomes a sale to the grandchild. Compliance becomes a backtest on federal data. Multiplayer becomes an ablation of human steering.

The decisive input is no longer any score. It is whether Track 1 exists as reported, which no amount of desk scoring can settle. Answer that question before noon and the decision follows.
