# Sponsor-wow x YC-RFS fit: "only possible now" live-agent demos for c0mpiled-15 (Penn State, Oct 11 2026)

**How this was researched.** Almost everything comes from WebSearch result extracts. WebFetch to docs.agi.tech failed with a DNS error (`ENOTFOUND`). Earlier sessions also had ycombinator.com and luma.com blocked (see `../Higher scoring YC RFS MVP ideas/rfs_and_judging.md`). The one exception is the AGI Inc API section: I cloned the public SDK repo `github.com/agi-inc/agi-node` (last commit 2026-02-16) and read its source directly, so that section is primary.

**Confidence tags:**
- [F] a fact taken from a source extract
- [P] read in primary source code
- [I] my own inference
- [U] unverified, or only one weak secondary source

Earlier notes already cover the RFS wording, judge profiles and sponsor prizes: `rfs_and_judging.md`, `judges_sponsors.md`.

---

## 0. TL;DR ranking (for a 1-day build with a live agent on stage)

| # | Idea (working name) | RFS hit | AGI-0 wow | Live reliability | Legal risk | Startup potential | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | **Countersign**: a family-approved agent that acts for an elderly parent and pauses for a verified-human co-sign before anything irreversible | Aging + Proving You're Human + Multiplayer | High: live VNC, plus the agent's `QUESTION` → phone approval → resume | Med-High if the irreversible step runs on our own replica merchant | Low-Med | High (gap between Rocket Money/Pine and World/Auth0) | **Build this** |
| 2 | **Integration Medic**: an agent that fixes a broken API integration by actually using the vendor dashboard, then opens the PR | Self-Maintaining APIs | High: the agent drives the Stripe test-mode dashboard, then a GitHub PR appears | Med (dashboards have 2FA and change often; test mode helps) | Low | Med-High (SelfHeal, OpsLevel exist; dashboard-side repair is open) | Strong #2 / fallback |
| 3 | **Huddle**: a multiplayer co-steered browser agent (watch, redirect, hand off) | Multiplayer AI (near-verbatim RFS) | Med-High: 3 phones in the audience steer one agent | High (the multiplayer layer is our code) | Low | Med (Mosaic S26, Browser Use takeover, Cloudflare HITL, YC's open-source QM) | Use as a *feature* of #1, not standalone |
| 4 | **LicenseGuard**: a compliance agent that checks and renews state licenses on government portals | AI-Native Compliance Infra | Med (read-only lookups are safe; renewals need real credentials) | Med-Low on live government sites | Med | High market, crowded with consultancies | Good pitch, weak demo |
| 5 | **Benefits co-pilot**: an agent that fills government forms (SNAP/Medicaid/LIHEAP) | Aging + Consumer-1B | High emotional pull | **Low**: Propel found agents "presumptuous, entered incorrect information, agreed to legal terms on behalf of the user" | **High** (false statements on government applications) | Med (Propel, DUOS, Advocate) | Avoid as primary |
| 6 | **Bill-fighter / subscription canceller** on its own | Consumer-1B / Aging | High | Med | Med (DoNotPay precedent) | **Low differentiation**: Rocket Money Rowan (Aug 2026), Pine ($25M A) | Only as the "task" inside #1 |

[I] The winning framing is #1. The agent does a real errand for Grandma, such as cancelling a charge or disputing a bill. Before the irreversible click it stops, and two family members on their phones watch the live VNC and co-sign with a passkey or liveness check. The agent then presents a signed, scoped mandate to the merchant. That covers three RFS in one story, gives AGI a showcase for its Visa/agentic-commerce narrative, and keeps the risky step on a site we control.

---

## 1. AGI Inc API: what we can actually call ([P] from agi-node source unless noted)

- **Setup.** Get a key at `platform.agi.tech/api-keys` and set `AGI_API_KEY`. Install with `npm install agi`. There is also an official C#/NuGet `Agi` package [F] ([NuGet](https://www.nuget.org/packages/Agi)). Docs live at `docs.agi.tech`, which was unreachable from here. Older notes cite a mintlify mirror.
- **Base URL.** `https://api.agi.tech`. Endpoints:
  - `POST /v1/sessions` takes agent name, `webhookUrl`, `maxSteps` and `restoreFromEnvironmentId`, and returns `sessionId`, `vncUrl`, `environmentId` and `agentUrl`.
  - Per-session paths, all under `/v1/sessions/{id}/`:
    - `message` (POST)
    - `status` (GET)
    - `messages` (GET)
    - `events` (SSE)
    - `pause`, `resume`, `cancel` (POST)
    - `navigate` (POST)
    - `screenshot` (GET)
  - `DELETE /v1/sessions/{id}` takes an optional `'filesystem'` argument, which saves the environment.
  - `DELETE /v1/sessions` deletes all sessions.
- **Agents.** `agi-0` (general), `agi-0-fast`, `agi-1` (advanced). Client-driven `agi-2-claude` runs desktop/mobile through `AgentLoop`, but **desktop mode is feature-gated** (contact partner@theagi.company).
- **Built-in human-in-the-loop hooks (key for ideas #1 and #3):**
  - Session status includes `waiting_for_input`.
  - Message types are `THOUGHT | QUESTION | USER | DONE | ERROR | LOG`.
  - The action schema includes `ask_question`, and the loop result has `askUser`.
  - [I] So the agent can natively stop and ask a human. We route that question to the family's phones (multiplayer) and gate the answer on verified-human proof.
- **Live VNC.** `vncUrl` is returned on the session, so it can be embedded on the projector as the "wow" screen.
- **Persistent logins.** End a session with `delete('filesystem')`, then create a new one with `restoreFromEnvironmentId`, and cookies/auth survive. [I] This is the main demo de-risker: log in, clear 2FA and dismiss cookie banners *before* going on stage.
- **Webhooks.** A `done` event is POSTed to `webhookUrl`.
- **SDK extras.** A multimodal driver supports audio-in, TTS out, turn detection, camera, MCP servers and an `agent_identity` field (default "agi-2-claude by AGI Company"). [I] That `agent_identity` field fits idea #1's "who is this agent acting for" story.
- **Pricing** [F/U], third-party only, no official page found:
  - Starter: $19/mo with 1,000 "thinking" steps (~50 tasks).
  - Pay-as-you-go: $0.02/step.
  - Enterprise: custom.
  - Source: [ai.theagi.company products page](https://ai.theagi.company/products-agi-0-agi-api-and-sdk-offerings).
  - [I] A 30–60-step errand costs about $0.60–1.20 in agent steps, so unit economics work at $10–15/mo consumer pricing with a few tasks a month.
  - `TaskMetadata.cost` is "not yet provided by API" [P].
- **Vendor claims** [F, vendor-reported]:
  - #1 on OSWorld ([AGI blog](https://www.theagi.company/blog/osworld)).
  - "99.9% reliability on your custom workflows", with replicas of 10 popular sites ([AGI-0 page](https://theagi.company/agent)).
  - Visa partnership targeting "near-100% reliability" for agent-led transactions ([AGI x Visa](https://www.theagi.company/blog/agi-inc-visa)).
  - REAL Bench is a replica-internet eval.
  - Cloudflare lists "AGI Agent" as a verified bot that "takes actions and makes purchases on behalf of users" ([Cloudflare Radar](https://radar.cloudflare.com/bots/directory/agi-agent-2)).
- **What AGI Inc wants to see** [I]:
  - Commerce or transaction workflows (the Visa tie-in).
  - Reliability stories.
  - The live VNC and session APIs used beyond a toy "find flights" task.
  - **Use `waiting_for_input`/`QUESTION` + `restoreFromEnvironmentId` + `vncUrl` explicitly and name them in the pitch.** Judges from the sponsor reward deep API use.

**Fallbacks if the AGI key or quota fails:**
- Browser Use Cloud has a documented **human takeover**: a keep-alive session plus a live URL with full mouse/keyboard control ([docs](https://docs.cloud.browser-use.com/tips/live-view/human-takeover)).
- Cloudflare Browser Run has structured **human-in-the-loop** handoff, with a Live View URL that expires after 5 min by default (1 hr max). Changelog dated 2026-07-28 ([CF](https://developers.cloudflare.com/changelog/post/2026-07-28-human-in-the-loop/)).
- Stagehand/Browserbase: Free / $20 / $99 per month, with overage around $0.10–0.12/hr [U] ([usagepricing](https://usagepricing.com/tools/pricing-calculator/browserbase)).
- Browser Use plans: $29 / $299 / $999 per month [U] ([costbench](https://costbench.com/software/browser-automation/browser-use/)).
- Plain Playwright against our own replica site is the last-resort deterministic path.

---

## 2. Reliability reality check (2026)

**Benchmark numbers:**
- **OSWorld(-Verified).** The human baseline is about 72.4%. Simular Agent S hit 72.6% in Dec 2025. GPT-5.4 is reported at 75.0%. Claims of 85%+ exist [U] ([buildmvpfast](https://www.buildmvpfast.com/blog/osworld-benchmark-ai-agents-passed-human-baseline-2026), [ai2.work](https://ai2.work/blog/gpt-5-4-beats-humans-at-computer-use-what-it-means-for-ai-agents)).
- **Claude.** Sonnet 4.6 scored 72.5% and Opus 4.6 72.7%. Sonnet 5 is reported at 81.2%. All three figures are secondary sources ([conversion.com.br](https://www.conversion.com.br/blog/claude-sonnet-4-6), [vellum](https://www.vellum.ai/blog/claude-sonnet-5-benchmarks-explained)).
- **Stanford AI Index 2026.** OSWorld went from about 12% to 66.3% ([arahi](https://bump.arahi.ai/blog/stanford-ai-index-2026-ai-agents-task-success)).
- **Live web is harder.** On Online-Mind2Web (300 tasks, 136 real sites), the best agent completed 61.3% and most agents were near 30% ([TestMu, Jul 2026](https://www.testmuai.com/blog/state-of-ai-browser-agents-2026/)).
- **WebArena.** Went from 14.4% (2023) to 61.7% for one specialized scaffold ([arXiv 2607.05775](https://arxiv.org/pdf/2607.05775)).
- **Efficiency.** Agents take 2.7–4.3x more steps than needed ([OSWorld-Human](https://arxiv.org/pdf/2506.16042)).
- **Domain-specific.** Propel tested ChatGPT Agent and Claude Cowork on SNAP applications. The agents navigated sites and uploaded documents, but entered wrong information and **agreed to legal terms on the user's behalf** ([Propel pt1](https://www.propel.app/insights/can-ai-agents-help-people-apply-for-snap-part-1/), [pt2](https://www.propel.app/insights/how-should-ai-agents-help-people-manage-benefits/)).

[I] **On-stage implication.** Expect roughly a 1-in-3 failure risk per *novel* multi-step task on a real site. The specific failure points are CAPTCHAs, 2FA, cookie walls, A/B layout changes, and the conference Wi-Fi.

**Mitigations** (all [I]):
1. Run the irreversible step on **our own replica site**. AGI itself evaluates on replicas, so this is on-brand.
2. Pre-auth with `restoreFromEnvironmentId`.
3. Use `agi-0-fast` with a tight `maxSteps` and a very specific prompt.
4. Run 10 rehearsals and record a backup video.
5. Show the *pause-for-human* step as a feature, so a stall reads as "safety working".
6. Use a phone hotspot.

---

## 3. Idea-by-idea evaluation

### Idea 1: Countersign (Aging + Proving You're Human + Multiplayer). RECOMMENDED

**Pitch.** Grandma says (voice or SMS), "I keep getting charged $14.99 by something I didn't sign up for." The agent finds the charge, goes to the merchant, and gets to the cancel/refund button. It then **pauses**. Daughter and son receive a push notification showing the live VNC and the exact action ("Cancel StreamPlus, request $44.97 refund"). Each approves with a passkey/WebAuthn plus a liveness check. The agent resumes and presents a **signed delegation mandate** (who the human is, which agent, what scope, expiry). The merchant-side verifier shows "verified human principal, 2-of-2 family co-sign", and the action completes. An audit trail goes to MongoDB.

**What AGI-0 does live:**
1. Session restored from the pre-authenticated environment.
2. It reads the (demo) bank/email to find the charge.
3. It navigates the cancel flow on a replica merchant we build. Optionally it also does a real read-only lookup on a live site.
4. It emits `QUESTION`, and the status goes to `waiting_for_input`.
5. Our backend fans the question out to the family and collects the co-signs.
6. `POST /message` sends the approval token, and the agent finishes.
7. The `done` webhook fires.

**"Only possible now" because:**
- Agents now beat the human OSWorld baseline.
- Web Bot Auth is in production at Cloudflare. Since Jul 1 2025, RFC 9421 HTTP Message Signatures are part of Verified Bots, with keys at `/.well-known/http-message-signatures-directory`. A signature *authenticates the operator, not authorization* ([IETF draft](https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture-03), [crawlbase](https://crawlbase.com/blog/web-bot-auth-signed-agents/)).
- Card networks now ship agent tokens: Mastercard Agent Pay (Apr 2025) and Visa Trusted Agent Protocol (Oct 2025, now Visa Intelligent Commerce). Both use Web Bot Auth, and the Visa approach may shift chargeback liability [U] ([eco.com](https://eco.com/support/en/articles/15192003-mastercard-agent-pay-vs-visa-trusted-agent-2026-compared)).
- [I] **The gap.** All of these prove *which agent/operator* is acting. World AgentKit proves *a unique human* is behind it. None of them gives the **family/caregiver delegation + per-action human co-sign** layer for vulnerable users.

**Who pays** [I]:
- (a) Adult children ($10–20/mo, the "sandwich generation"). Rocket Money Premium+ with Rowan costs $15/mo ([fintech.global](https://fintech.global/2026/09/03/rocket-money-launches-ai-agent-to-manage-finances/)), which anchors willingness to pay.
- (b) Banks and credit unions, as an elder-fraud control. Over-60s reported **$7.75B in losses in 2025, up 59% YoY** (FBI IC3) ([AARP](https://www.aarp.org/money/scams-fraud/fbi-ftc-report-2025-losses), [HousingWire](https://www.housingwire.com/articles/fbi-seniors-cybercrime-2025/)).
- (c) Merchants and agent platforms, as a verifier API.

**Competitors:**
- Consumer agents:
  - **Rocket Money Rowan** (launched Aug 25 2026, built with Anthropic). It cancels trials by SMS reply and negotiates bills, and says it has "human oversight where required" ([PYMNTS](https://www.pymnts.com/?p=4123012)).
  - Rocket Money bill negotiation takes 35–60% of first-year savings ([fincomparelab](https://www.fincomparelab.com/reviews/rocket-money-review/)).
  - **Pine AI** has a $25M Series A (Dec 2025), claims a 93% negotiation success rate, and charges success-based or per task ([fintech.global](https://fintech.global/2025/12/03/pine-launches-ai-agent-as-it-secures-25m-series-a/), [19pine](https://www.19pine.ai/fr/ai-information-page)).
  - Trim: [I], from memory, not re-checked.
- Identity:
  - **World AgentKit**: beta Mar 17 2026, expanded Jun 24 2026 with Okta, Shopify, Vercel, Browserbase and Exa. It needs an Orb-verified World ID, which matters for elderly users ([HackerNoon](https://hackernoon.com/lite/world-expands-agentkit-so-ai-agents-can-prove-a-unique-human-is-behind-them)).
  - **Auth0 for AI Agents**: CIBA + RAR async approval ("Approve payment of $50.00 to ExampleCorp") ([Auth0](https://auth0.com/ai/docs/intro-asynchronous-authorization)).
  - Incode "agentic identity" re-verifies at high-risk actions ([Incode](https://incode.com/use-cases/agentic-identity/)).
  - YC **Proof of Human** / Roundtable ([YC](https://www.ycombinator.com/companies/proof-of-human)).
- General agents:
  - ChatGPT agent. Atlas reportedly deprecated Aug 9 2026 and folded into ChatGPT [U].
  - **Google Project Mariner was shut down May 4 2026**, with its technology moved into Gemini Agent and AI Mode ([Wikipedia](https://en.wikipedia.org/wiki/Project_Mariner)).
  - Perplexity Comet is free, with Max at $200/mo ([eesel](https://www.eesel.ai/fr/blog/tarifs-perplexity-comet)).
  - Anthropic computer use.
- [I] **Differentiation.** Rowan and Pine are single-player and autonomous. World and Auth0 are infrastructure. Countersign is the **multi-party caregiver approval layer + agent mandate**, which fits a world where elderly users are the main scam target.

**Legal risk (Low-Med):**
- **CFAA/ToS.** In *Amazon v. Perplexity*, an N.D. Cal. preliminary injunction (Mar 2026) found Comet accessed the site "with the user's permission but without authorization by Amazon". The **Ninth Circuit vacated it on Aug 4 2026**: the user is the one accessing, and Amazon is unlikely to win under CFAA/CDAFA. The merits are still pending ([Northeast Times](https://northeasttimes.com/2026/08/06/appeals-court-sides-with-perplexity-ai-in-amazon-shopping-dispute/), [Bloomberg Law](https://news.bloomberglaw.com/ip-law/amazon-wins-court-order-blocking-perplexitys-ai-shopping-bots)).
- **Authority to act for a parent.** [I] Bank and health portals may need a POA or an authorized-representative designation, so position the product as the parent's own account with consented delegation.
- **Overclaiming.** DoNotPay paid $193K under a final FTC order (5-0, Jan 16 2025) and is barred from claiming it equals a lawyer without evidence ([FTC](https://www.ftc.gov/node/87474)). Don't claim "legal", and don't overstate success rates.
- **Voice.** If the agent *phones* merchants, the FCC Feb 2024 ruling treats AI voices as "artificial" under the TCPA. Its application to consumer-initiated calls to customer service is unclear ([Perkins Coie](https://perkinscoie.com/insights/update/fcc-declares-ai-generated-robocalls-unlawful)).
- **Cancellation law.** The FTC click-to-cancel rule was **vacated by the 8th Cir. Jul 8 2025** on procedural grounds, but state auto-renewal laws still apply ([Greenberg Traurig](https://www.gtlaw.com/en/insights/2025/7/eighth-circuit-vacates-ftcs-click-to-cancel-rule)). [I] Pitch line: "the federal rule died, so cancelling is still hard; agents fix it."

**Startup potential:** High. It is a wedge into elder-finance safety, which banks pay for, and later into an agent-delegation standard.

**Judge fit:**
- Patel/AGI: commerce + HITL + VNC.
- Karbasi (NPU Ventures): consumer/fintech [I].
- Bloomerang: the nonprofit angle ("Area Agency on Aging" volunteers as co-signers) [I].
- MongoDB: audit log / mandate store.
- AWS: Cognito/passkeys or Rekognition liveness [I].

### Idea 2: Integration Medic (Self-Maintaining APIs)

**Pitch.** A Stripe webhook breaks because of a rotated secret, a deprecated API version, or a moved field. A monitor detects 4xx/5xx errors and contract drift. Then:
- AGI-0 **logs into the vendor dashboard** (Stripe test mode). It reads the changelog or upgrade notice, rolls the webhook signing secret or bumps the pinned API version, and runs a test event.
- A coding agent opens a GitHub PR that updates the code and config, with the dashboard evidence (screenshots) attached.
- The judges see the red dashboard turn green.

**Why the dashboard matters** [I]: the RFS frames this as an agent opening a fix PR in the customer's codebase ("Dependabot for API contracts"). Many fixes, though, require **dashboard-only actions** (keys, webhook endpoints, version pins, OAuth redirect URIs) that no API or PR can reach. That gives a computer-use agent a clear role.

**Reliability.** Medium. Dashboards have 2FA, so pre-authenticate with an env snapshot. Stripe test mode is a safe sandbox. Keep the "break" scripted.

**Competitors:**
- **SelfHeal** (Product Hunt): "rewrite the connector code, test it against the live API, and redeploy", free pilot ([PH](https://www.producthunt.com/p/selfheal/selfheal)).
- **OpsLevel Maintenance Agent** opens PRs ([OpsLevel](https://opslevel.com/use-cases/maintenance-agent)).
- **Integuru** (YC W24) reverse-engineers internal APIs, which is adjacent ([yespress](https://yespress.io/integuru-yc-w24)).
- Dependabot/Renovate.
- SDK generators (Stainless, Speakeasy, Fern): [I], not re-verified.
- An MSR 2026 study reports agent chore PRs break things at 2–3x the human rate, so review gates are a selling point ([codex.danielvaughan](https://codex.danielvaughan.com/2026/06/17/safer-builders-risky-maintainers-msr-2026-breaking-changes-codex-cli-refactoring-maintenance-configuration/)).

**Who pays.** Engineering teams with many integrations (per-integration SaaS, $50–500/mo [I]), and API vendors as a DX add-on. RFS author anecdote: "over 30% of our service downtime was due to external api/package changes".

**Legal risk.** Low. It runs on the customer's own accounts, but credential custody is a security-review hurdle.

**Startup potential.** Med-High. Developer tools buyers are clear, but the field is crowding.

**Judge fit:**
- Fioti/Luminal (infra) and the Engineering Entrepreneurship faculty.
- AGI: less consumer-flashy, but it shows "agent does what APIs can't".

### Idea 3: Huddle, a multiplayer co-steered browser agent (Multiplayer AI)

**Pitch.** One AGI session's `vncUrl` goes up on the projector. A web app shows presence/cursors for N people. Any member can send `POST /message` to redirect, `pause`/`resume`, or "take the wheel". `QUESTION` events go to the group and are resolved by vote or by a role. This matches the RFS nearly verbatim: anyone can "drop into the same live agent session to watch it work, redirect it, and hand it off" (see `rfs_and_judging.md`).

**Reliability.** High, because the novelty is our coordination layer, not the agent.

**Competitors:**
- **Mosaic (YC S26)**, shared memory for coding-agent sessions ([wavect](https://wavect.io/blog/mosaic-yc-s26-shared-agent-sessions-review.md)).
- YC's open-sourced **QM** multiplayer harness (MIT, Jul 2026) ([valueaddvc](https://valueaddvc.com/pulse/yc-qm-multiplayer-agent-tooling-analysis-2026)).
- Oryxa ("rooms" for agent CLIs).
- Browser Use takeover and Cloudflare HITL handoff (see §1).
- HeyClicky (YC Spring 2026, Epstein's company).

**Verdict** [I]: as a generic tool it is thin and duplicates YC's own QM. **Fold it into Countersign**, where the "team" is a family and the multiplayer step is approval.

### Idea 4: LicenseGuard (AI-Native Compliance Infrastructure)

**Pitch.** An obligations register of state licenses (money transmitter, vet/DEA, contractor). The agent runs **read-only public license lookups** on state portals each night (e.g., Pennsylvania's public license verification [I]). It flags expirations, drafts the renewal, and pauses for a human to sign.

**Background** [F]:
- Money transmitter licensing covers 49 states + DC, with no reciprocity.
- Annual renewals cost about $250–1,000 per state, plus exams ([Buckingham](https://www.buckinghamcapitalconsulting.com/post/how-to-get-a-money-transmitter-license-in-the-us), [zenind](https://www.zenind.com/help/post/money-transmitter-licensing-in-the-united-states-requirements-registration-and-compliance)).

**Reliability.** Government portals are slow, old and CAPTCHA-prone. Read-only lookups are the feasible demo.

**Competitors:**
- Licensing consultancies (Labyrinth, InnReg, Faisal Khan).
- YC ComplyDo and Arden (per `rfs_and_judging.md`).
- Vanta/Drata for SOC 2.

**VetRec tie-in** [I]: Kevin Cohen's clinics have DVM licenses, DEA registrations and CE deadlines.

**Verdict.** Credible business, but a quieter demo.

### Idea 5: Government-form filler (Aging/Consumer)

**Evidence against it as the main demo:**
- Propel's own testing (above).
- Intuit's earlier SNAP feature produced applications "filled with nothing but special characters" ([Propel](https://www.propel.app/insights/how-should-ai-agents-help-people-manage-benefits/)).

**Legal.** Submitting false information on benefit applications is serious [I]. **Never submit live.** At most, fill and stop before submit.

**Competitors.** Propel, DUOS (50-state benefit enrollment), Advocate, Hyperscience Hypercell for SNAP (agency side) ([DUOS](https://www.silicon.co.uk/press-release/duos-introduces-new-capabilities-to-enable-one-click-enrollment-in-government-benefits-nationwide), [TechCrunch](https://techcrunch.com/2024/03/05/ai-could-be-the-solution-for-bureaucracy-with-emilie-poteat-from-advocate/)).

**Verdict.** Mention it as a future Countersign task ("form filled, family reviews before submit"), not as the headline.

### Idea 6: Bill fighter / subscription canceller (standalone)

[I] The incumbents (Rocket Money + Rowan, Pine, Trim) and the DoNotPay cautionary tale make this read as unoriginal on its own. It works as the *errand* inside Countersign, where the novelty is the verified, multi-party, scoped delegation.

---

## 4. Recent YC companies near these spaces (to avoid looking unoriginal)

**Confirmed or likely YC** (batch per source):
- **Multiplayer:** Mosaic (S26; shared coding-agent sessions); HeyClicky (Spring 2026); YC QM (YC's own open source).
- **Proving human / agent trust:**
  - Proof of Human (no batch shown).
  - Roundtable (see `rfs_and_judging.md`).
  - Salus (W26; runtime action checks for agents) ([YC API list](https://www.ycombinator.com/companies/industry/API)).
- **Browser/computer-use infra** (these are tools for us, not competitors):
  - Browser Use (W25).
  - Kernel (S25; managed headful browsers).
  - Skyvern (S23; vision browser workflows, used by gov/insurance ops) ([YC](https://ycombinator.com/companies/skyvern)).
  - StableBrowse (Spring 2026).
  - Coasty (S26 listing; computer-use API).
  - RamAIn (W26).
  - Integuru (W24).
  - Source: [extruct S26](https://www.extruct.ai/data-room/ycombinator-companies-s26/).
- **Aging:** Kaigo Health (voice check-ins), Twolabs (caregiving humanoids), GoGoGrandparent (per `rfs_and_judging.md`). I found no 2026-batch eldercare agent company in searches. The S26 healthcare share is about 8.5% ([TIMEWELL](https://timewell.jp/en/columns/yc-summer-2026-batch-analysis)).
- **Compliance:** ComplyDo, Arden.

**Not YC (or unverified) but direct competitors:**
- Pine AI, Rocket Money Rowan, World AgentKit, Auth0 for AI Agents, Incode, SelfHeal, OpsLevel, Propel, DUOS.
- Visa TAP / Mastercard Agent Pay.
- Perplexity Comet, ChatGPT agent, Gemini Agent.

**Whitespace** [I]: none of the searches surfaced a YC company doing **caregiver multi-party co-sign for agent actions taken for older adults**, or **dashboard-side (not code-side) API integration repair**. That absence comes from limited search, not proof. Check the YC directory with "caregiver", "delegation" and "agent approval" before the pitch.

---

## 5. Demo script sketch for Countersign (3 min)

1. **0:00 Problem.** "$7.75B stolen from over-60s last year (FBI IC3). Agents can now do Grandma's errands, so who makes sure the agent, and the person instructing it, is legit?"
2. **0:30 Ask.** Grandma's voice note goes in. AGI-0 starts, and the `vncUrl` goes full-screen on the projector.
3. **1:00 Errand.** The agent finds the charge and navigates the cancel flow on the replica merchant. Narrate the agent's `THOUGHT` stream.
4. **1:40 Pause.** `QUESTION` fires and the status goes to `waiting_for_input`. Two judges' or teammates' phones buzz, showing the live view and the exact action. Each does passkey + liveness: 2-of-2.
5. **2:10 Resume.** The agent presents the signed mandate (Web Bot Auth-style headers + scoped JWT). The merchant verifier shows "human-backed, family-approved, expires 10 min". The action completes.
6. **2:40 Audit trail** in MongoDB Atlas, then the business model: families pay $12/mo, plus a credit-union pilot.

**Stack** [I]:
- AGI API: sessions, SSE events, `vncUrl`, `restoreFromEnvironmentId`.
- WebAuthn passkeys, plus optional AWS Rekognition Face Liveness.
- MongoDB Atlas for the mandate and audit store.
- Luminal-hosted open model for intent parsing and risk scoring (Luminal $1k inference prize).
- Next.js PWA for push notifications.

---

## 6. Open questions / verify before stage

- Official AGI pricing and hackathon credits. Ask Vivek on site. Confirm `vncUrl` is populated for `agi-0` web sessions and whether it is embeddable (iframe/CORS).
- Whether AGI-0 supports custom request headers or signing, so the agent can send Web Bot Auth signatures. If not, sign at our replica merchant's gateway or proxy [I].
- Exact YC RFS wording (ycombinator.com/rfs was blocked; see `rfs_and_judging.md`).
- Atlas deprecation, Sonnet 5 OSWorld figures and Pine pricing are single-source.
