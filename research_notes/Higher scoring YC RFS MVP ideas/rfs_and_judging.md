# YC Fall 2026 RFS text (six requests) and what wins AI hackathons with YC-style judges

> **Important note on access (read first).** During this research session the egress proxy **blocked ycombinator.com and luma.com** (curl got HTTP 403 on CONNECT; WebFetch got DNS failures for ycombinator.com, luma.com, modelence.com, superframeworks.com and blog.jetbrains.com). So **I could not load the official RFS page or the c0mpiled-15 Luma page directly.** Every "quote" below comes from search-engine extracts of those pages (the search tool reads the page and returns excerpts) or from third-party write-ups. Confidence labels:
> - **HIGH (near-verbatim)**: a phrase came back in quotes from a search extract of ycombinator.com/rfs, and/or several independent secondary sources agree on it.
> - **MEDIUM**: a paraphrase of the official page, or an author name given only by secondary sites (several of which agree).
> - **LOW**: one secondary source only.
> Before quoting any of this on stage or in a submission, open https://www.ycombinator.com/rfs in a normal browser and check the wording.

## Q1. What does each of the six YC Fall 2026 RFS say, what examples, buyers or product shapes does each suggest, and who wrote each?

### Takeaway
The Fall 2026 RFS list has 13 requests, and all six target requests are on it. Secondary sources agree on the authors: Multiplayer AI (Aaron Epstein), AI-Powered Consumer Products for 1 Billion People (Raphael Schaad), AI for the Aging Population (Max Kolysh), AI-Native Compliance Infrastructure (Daivik Goel), Self-Maintaining APIs (Harsha Gaddipati) and Proving You're Human (Max Kolysh). Each one points at a concrete product shape: shared agent sessions; consumer agents that become cheap as token costs fall; voice, monitoring, robots and caregiver coordination for people over 65; a compliance system of record for regulated financial and licensed businesses; agents that open fix PRs when an API changes; and a privacy-preserving way to show a verified human is on the other end.

### Cited Findings

**General context**
- The Fall 2026 RFS has 13 ideas. Inc. and VCCafe covered its release. One summary says the application deadline was July 27 (2026) — [Inc.](https://www.inc.com/lucia-auerbach/y-combinator-requests-for-startups-fall-2026/91379840); [VCCafe](https://www.vccafe.com/requests-for-startups-fall-2026-edition/); [Modelence summary page](https://modelence.com/yc-rfs-fall-2026/multiplayer-ai)
- The official page is https://www.ycombinator.com/rfs. A Threads post from a YC-adjacent account sums up the batch as including "AI built to care for older people… and rebuilding the trust layer of the internet" — [Threads](https://www.threads.com/@startingupgoodorg/post/DbdZfpUIAgD/y-cs-fall-requests-for-startups-includes-ideas-spanning-education-one-to-one-ai/)

**1. Multiplayer AI, by Aaron Epstein (author: HIGH; text: MEDIUM-HIGH)**
- Author: Aaron Epstein, YC General Partner and co-founder of Creative Market — [YC RFS page via search extract](https://www.ycombinator.com/rfs); [YC people page](https://www.ycombinator.com/people/aaron-epstein); [usepoly explainer](https://usepoly.co/yc-multiplayer-ai)
- Core argument (near-verbatim from page extracts): the best work tools of the last two decades went multiplayer (Google Docs, Figma), but "AI hasn't had its multiplayer moment yet". Agents are "the most powerful new tool a team has, yet people still use them alone" — [YC RFS](https://www.ycombinator.com/rfs)
- Product shape (near-verbatim): anyone on a team "could drop into the same live agent session to watch it work, redirect it, and hand it off." Third-party summaries add humans and AI passing responsibility back and forth (human↔AI handoff) — [YC RFS](https://www.ycombinator.com/rfs); [myideacheck](https://myideacheck.com/blog/yc-fall-2026-rfs/multiplayer-ai)
- Examples named: engineers coding together in real time, sales teams working a deal, support teams resolving a ticket, and (per secondary summaries) lawyers drafting a contract — [YC RFS](https://www.ycombinator.com/rfs); [explainx](https://explainx.ai/blog/yc-requests-for-startups-fall-2026)
- Related: Epstein is primary partner for HeyClicky (YC Spring 2026), described as "the simplest interface in the world to talk AI models + spawn agents" — [YC company page](https://www.ycombinator.com/companies/heyclicky)

**2. AI-Powered Consumer Products for 1 Billion People, by Raphael Schaad (title and author: HIGH; key quotes: HIGH)**
- Exact title as reported: "AI-Powered Consumer Products for 1 Billion People". Author: Raphael Schaad (YC General Partner) — [YC RFS via search extract](https://www.ycombinator.com/rfs); [WorthvieW](https://www.worthview.com/y-combinators-fall-2026-request-for-startups-all-13-ideas-explained/); [LinkedIn](https://www.linkedin.com/in/raphaelschaad/)
- Near-verbatim quotes from page extracts: "three years in, the only new icon on your home screen is ChatGPT", and "today, the magic can run $1,000 a month in tokens for each user, but that is falling 10x a year." The page ends by inviting founders building for a billion people to get in touch — [YC RFS](https://www.ycombinator.com/rfs)
- The $1,000/month and 10x/year figures are YC's own estimate, not an independently measured statistic — [superframeworks analysis](https://superframeworks.com/articles/yc-fall-2026-rfs-indie-hacker-plays)
- Categories cited by secondary sources: getting things done, mobility, learning, health, money, social — [cipherprojects](https://www.cipherprojects.com/blog/posts/what-solo-founders-should-build-yc-rfs-fall-2026/) (LOW-MEDIUM; I could not confirm these are in the official text)
- Schaad's related public views on X: "a left-hand list of Chats was a 18mo experiment that has reached 100M users but won't be the thing that will scale to 1B" (he expects messaging with a bot or bots instead), and there is "no *AI-native distribution channel* for new consumer apps" — [X post 1](https://x.com/raphaelschaad/status/2104906896788353399); [X post 2](https://x.com/raphaelschaad/status/2089399226824634634)

**3. AI for the Aging Population, by Max Kolysh (author: MEDIUM, secondary only; content: MEDIUM-HIGH)**
- Author: Max Kolysh. Several secondary sources say this, and note he wrote two entries (this one and Proving You're Human) — [superframeworks](https://superframeworks.com/articles/yc-fall-2026-rfs-indie-hacker-plays); [modelence](https://modelence.com/yc-rfs-fall-2026)
- Content, paraphrased from page extracts: caregiver demand far exceeds supply, and few products are built for older people. The page names four product types: (1) conversational voice interfaces, (2) monitoring for safety and independence, (3) home-assistance robots, (4) software to help family caregivers coordinate care. It says voice assistants like Alexa and Google Home frustrate most seniors, that one in five Americans will be over 65 by 2030, and that millions of caregiving jobs will go unfilled within the decade — [YC RFS](https://www.ycombinator.com/rfs); [digg](https://digg.com/tech/379cgr5u)
- YC companies already in this space (useful for showing differentiation): Kaigo Health (voice-agent phone check-ins for older adults), Twolabs (humanoid caregiving robots), GoGoGrandparent (phone line for rides and deliveries without a smartphone) — [Kaigo](https://www.ycombinator.com/launches/OnW-kaigo-health-the-ai-care-workforce-that-looks-after-grandma-grandpa); [Twolabs](https://www.ycombinator.com/launches/QWa-twolabs-humanoid-robots-for-caregiving); [GoGoGrandparent](https://www.ycombinator.com/blog/gogograndparent/)

**4. AI-Native Compliance Infrastructure, by Daivik Goel (author: MEDIUM, secondary only; key quotes: HIGH)**
- Author: Daivik Goel, according to several secondary sources — [modelence](https://modelence.com/yc-rfs-fall-2026/ai-native-compliance-infrastructure); [cipherprojects](https://www.cipherprojects.com/blog/posts/what-solo-founders-should-build-yc-rfs-fall-2026/)
- Near-verbatim quotes from page extracts: "Financial compliance is still stitched together with spreadsheets, siloed tools, and expensive headcount." "Most compliance work is monitoring regulatory changes, flagging anomalies, generating reports, and keeping audit trails." "The pain is especially acute for businesses navigating state-by-state licensing, renewal cycles, audits, and regulatory patchwork." — [YC RFS](https://www.ycombinator.com/rfs)
- Implied buyers: financial businesses and licensed businesses operating in many states (fintechs, lenders, money transmitters, insurance and similar; this is my inference from the "state-by-state licensing" wording) — [YC RFS](https://www.ycombinator.com/rfs)
- Secondary readings: "YC is pointing toward infrastructure, not a single-purpose document generator", and a suggested build of a single register of obligations and controls, mapped to owners, with gap analysis and automatic audit trails — [quasa](https://quasa.io/media/yc-fall-2026-rfs-how-to-build-ai-native-compliance-infrastructure); [modelence](https://modelence.com/yc-rfs-fall-2026/ai-native-compliance-infrastructure) (interpretation, not RFS text)
- YC companies nearby: ComplyDo, Arden ("AI-native internal audit firm"), plus Vanta as the established reference point — [ComplyDo](https://www.ycombinator.com/companies/complydo); [Arden](https://www.ycombinator.com/companies/arden)

**5. Self-Maintaining APIs, by Harsha Gaddipati (author: MEDIUM-HIGH; content: MEDIUM-HIGH)**
- Author: Harsha Gaddipati, according to several secondary sources. The search tool also tied his name to the YC page — [modelence](https://modelence.com/yc-rfs-fall-2026); [YC RFS](https://ycombinator.com/rfs)
- Anecdote (near-verbatim, from his time at AWS): "over 30% of our service downtime was due to external api/package changes going unnoticed." This is the author's own experience, not a study — [YC RFS](https://www.ycombinator.com/rfs); [Medium summary](https://medium.com/@tanishshenoy/yc-has-dropped-its-2026-request-for-startup-wishlist-4313275d32fb)
- Argument (paraphrased from the page): agentic coding tools have removed the old friction, because developers now routinely give outside tools access to their codebase. API vendors should therefore push fixes into customer codebases instead of only announcing changes. An agent scans the customer's code for affected usages and opens a pull request with the fix. This could be agents built by each provider, or a neutral third-party service ("Dependabot, but for API contracts" is the secondary sources' shorthand) — [YC RFS](https://www.ycombinator.com/rfs); [explainx](https://explainx.ai/blog/yc-requests-for-startups-fall-2026); [whatfinger](https://startup.whatfinger.com/2026/07/26/self-maintaining-apis/)
- Implied buyers: (a) API providers, who sell this as part of their developer experience, and (b) engineering teams that consume many APIs (inference from the text above).

**6. Proving You're Human, by Max Kolysh (author: MEDIUM, secondary only; key quotes: HIGH)**
- Author: Max Kolysh, according to secondary sources — [explainx](https://explainx.ai/blog/yc-requests-for-startups-fall-2026); [superframeworks](https://superframeworks.com/articles/yc-fall-2026-rfs-indie-hacker-plays)
- Near-verbatim quotes from page extracts: the opening story, "A finance worker joined a video call with his CFO and several colleagues, and wired out $25 million. Every other person on that call turned out to be a deepfake." The ask is to rebuild the internet's trust layer so people can know there is a verified human on the other end of "a call, message, or transaction", "ideally… one that doesn't make everyone give up their privacy." — [YC RFS](https://www.ycombinator.com/rfs)
- Secondary framing: "trust infrastructure against deepfakes, voice clones, bot fraud — without destroying privacy" — [explainx](https://explainx.ai/blog/yc-requests-for-startups-fall-2026)
- Existing YC player: Roundtable "Proof of Human", "an API that invisibly detects bots and verifies human identity". Others in the space: FaceSign, World or Worldcoin-style proof of personhood — [YC Roundtable](https://www.ycombinator.com/companies/roundtable); [FaceSign](https://www.facesign.ai/proofofhuman)

### Inferences
- In every one of these RFS, the hackathon-sized wedge is a **workflow with one buyer and one moment**: one shared agent session, one caregiver check-in loop, one obligations register for one license type, one API breaking change turned into one merged PR, one call or transaction verified as human. Judges who know the RFS will reward wording that echoes the RFS's own nouns ("drop into the same live agent session", "watch, redirect, hand off", "open a PR in the customer's codebase", "verified human on the other end… without giving up privacy").
- Self-Maintaining APIs and Multiplayer AI are the easiest to **prove live** in a 9-hour event: a real merged PR, or two people steering one agent on stage. Consumer-1B and Aging are the hardest to show with real users in a day, unless the team recruits real seniors or caregivers to try it during the event.
- Proving You're Human is crowded with funded companies (Roundtable, World, FaceSign). A hackathon entry needs a sharp, narrow angle, for example verifying a human on a single channel, to avoid "already exists".

### Gaps
- I could not retrieve the **full verbatim text** of any RFS, because ycombinator.com is blocked from this environment. Only excerpts are captured.
- **Author attribution for Aging, Compliance and Proving You're Human** rests on secondary sites. The extracts I saw from the official page did not show bylines for those sections.
- I could not confirm whether the official Consumer-1B text lists specific categories (mobility, health and so on), or whether the Multiplayer text mentions lawyers.

## Q2. What did winners of major 2025-2026 AI hackathons build, and why did they win?

### Takeaway
Recent winners at top hackathons share a pattern: **one vivid, working, demoable artifact with a clear user and a "wow" moment**. Examples are a computer-vision smart cane (TreeHacks 2026), a computer-use agent you control through FaceTime (Cal Hacks 12.0), and a 3D historical reconstruction where every part traces to a source, checked by verifier sub-agents (Claude Opus 4.8 Build Day). Organizers rarely publish why a project won. Where judging guidance exists, it stresses a specific problem, a working live demo and technical depth.

### Cited Findings
- **TreeHacks 2026 (Stanford, Feb 2026):** The grand prize went to "Shepherd", a motorized smart cane for visually impaired people that detects obstacles and steers its user using computer vision. More than $500K in prizes across 14 categories — [Stanford Daily](https://stanforddaily.com/2026/02/15/12th-annual-treehacks/); [Stanford OSE](https://ose.stanford.edu/news/treehacks-12-sam-altman-and-llamas) (spelled "Shephard" there). Devpost lists $12K for first place — [Devpost](https://treehacks-2026.devpost.com/)
- **Cal Hacks 12.0 (Oct 2025, co-hosted by Claude, Fetch.ai, AppLovin, Annapurna Labs):** 1st Overall out of 695 projects and more than 3,000 hackers went to FaceTimeOS, a multimodal computer-use agent you see, talk to and control over FaceTime on your own Mac. The only source is the winner's blog; I found no official list — [Dylan Lu blog](https://blog.dylanlu.com/cal-hacks-12/). The Claude track judged "technical complexity… innovative use of Claude Code beyond basic features" — [Devpost](https://cal-hacks-12-0.devpost.com/)
- **Claude Opus 4.8 Build Day (Anthropic, June 2026):** 1st was Tekton, a 3D reconstruction of Tang Dynasty architecture and Notre-Dame's spire in 339 construction stages, with each part linked to a historical source and placements checked by verifier sub-agents. 2nd was Sim Francisco, 10,000 synthetic residents seeded from the Census; its forecasts for the 2024 presidential vote and Prop A came close to the real results, and grouping residents into about 300 personas cut inference costs 10 to 100 times. 3rd was Custom Universe, which turns a phone photo into an editable 3D object, aimed at robotics labs that need synthetic data. The post does not give judging reasons — [Claude blog](https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon)
- **YC × Supabase AI hackathon (at YC; older, around 2024):** 47 projects demoed. Ten finalists were judged by YC partner Jared Friedman and others. The winner was a Twitter assistant that browses and drafts replies for your niche — [Supabase blog](https://supabase.com/blog/ai-hackathon-at-y-combinator)
- **OpenAI × YC o1 hackathon (Oct 2024):** Winners were Proxis, Vera Health and Camfer, all of which later appeared as real companies. No rationale was published — [YC on X](https://x.com/ycombinator/status/1844522539214832042)
- **YC Agents Hackathon ($65K)** and the YC AI Coding Agents hackathon, whose first prize included a guaranteed YC interview, show YC uses hackathons as a sourcing funnel — [Luma](https://luma.com/pz27h0xy); [Luma](https://luma.com/hzwlapu0)
- **Earlier c0mpiled events:** judges were YC-company founders (Crustdata, Channel 3, Random Labs, Allus AI, Cactus, SF Tensor at c0mpiled-13), and teams pick a YC RFS as their track — [Luma c0mpiled-13](https://luma.com/olys436o); [Luma c0mpiled-7](https://luma.com/rhi9rha9)

### Inferences
- Winners tend to have (1) a demo that is physical or visceral (a cane steering a person, an agent working over FaceTime), (2) built-in verification or a credibility mechanism (source tracing, verifier agents, forecasts checked against real outcomes), and (3) a concrete technical trick they can quantify (10 to 100 times cheaper inference).
- "Validated against ground truth" (Sim Francisco vs. real election results) is a strong pattern. It matches what c0mpiled-15 Track 1 asks for: a baseline, improvement over rounds, then evaluation on held-out tests.

### Gaps
- I found no official judge commentary on why the TreeHacks, Cal Hacks, PennApps, HackMIT, AGI House or Cerebral Valley 2025-26 winners won. a16z hackathon winners were not found.

## Q3. What do YC partners say makes a strong early product or demo?

### Takeaway
YC's guidance is consistent: build something people want, get real users by hand (do things that don't scale), and show a raw, working demo instead of a polished pitch. At YC hackathons, partners have explicitly asked for a live demo and a short plain-language description.

### Cited Findings
- At a YC hackathon, partners wanted to hear about projects "in a more raw, un-filtered way". They asked for a live demo and a two-sentence description from each team member. The writeup gives YC's top guidance as "build something people want" — [Princeton ODUS writeup](https://odus.princeton.edu/news/student-organization-spotlight-practical-hacking-yc-hackathon)
- YC Hacks' Devpost tagline: "Make something people want." — [Devpost](https://ychacks.devpost.com/)
- Paul Graham: "One of the most common types of advice we give at Y Combinator is to do things that don't scale". The most common example is recruiting users by hand. Stripe is "famous within YC for aggressive early user acquisition" ("Collison installation"). His weekly growth framing: with 100 users, get 10 more next week to grow 10% a week — [paulgraham.com/ds.htm](https://www.paulgraham.com/ds.htm); [Indie Hackers summary](https://www.indiehackers.com/post/summary-do-things-that-don-t-scale-by-paul-graham-bdcb54215a)
- Evidence of demand counts: one team's path into YC was a landing page with a paid early-access button that drew 150 users from several countries in four days — [Product Hunt forum](https://www.producthunt.com/p/april/from-hackathon-to-yc) (anecdote)
- A Hacker News commenter: ideas matter less than showing "you're thinking hard about solving a real problem", and you want a working demo — [HN](https://news.ycombinator.com/item?id=6262364) (anecdotal)

### Inferences
- For a YC-judged hackathon, the evidence that scores best is, in order: real external usage during the event (sales, signups, merged PRs) > a live working demo on a fresh input > a polished video or slides.

### Gaps
- I could not retrieve Startup School or Lightcone transcripts that address hackathons, demos or a "narrow wedge" directly, because ycombinator.com is blocked. Standard YC talks ("How to Get and Evaluate Startup Ideas", "How to Get Your First Customers") exist but I could not pull quotes from them.

## Q4. Are there hackathon formats where real usage or revenue during the event dominates judging?

### Takeaway
Yes, and **c0mpiled-15 itself has one**: its Track 2 (Engineering Entrepreneurship) is reportedly judged on **actual sales made during the event**. Outside c0mpiled, RevenueCat Shipaton, Polar × Lovable and the XPRIZE Build with Gemini hackathon judge on real revenue and users, usually over a longer window than one day.

### Cited Findings
- **c0mpiled-15 Track 2:** "winners are those who successfully build and validate their product by getting actual sales during the event". AWS prize pool of up to $5,000 for Track 2. Track 2 prize pools also come from Engineering Entrepreneurship and Bloomerang — [Luma c0mpiled-15 via search extract](https://luma.com/compiled-jjvw) (MEDIUM: two search extracts agree; a third search extract did not surface Track 2 at all)
- **RevenueCat Shipaton 2025:** a "Help Apps Make Money" award. The first-place team reached $1,100 MRR in ten days, and another winner had more than 1,000 installs and $2,000 revenue. Judging includes downloads, revenue, paying customers and conversion — [RevenueCat](https://www.revenuecat.com/blog/company/shipaton-2025-winners); [App Launchpad](https://theapplaunchpad.com/blog/revenuecat-shipaton-2026/)
- **Polar × Lovable "Prompt a Startup":** the highest MRR after 30 days wins — [X article on vibe-coder hackathons](https://x.com/meta_alchemist/article/2049846781576622570?lang=en) (secondary)
- **XPRIZE Build with Gemini:** three equally weighted criteria (business viability, AI-native operations, category impact). Teams must launch a real business with real users and revenue within 90 days — [XPRIZE](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google)

### Inferences
- In a sales-judged track, a cheap and immediately purchasable offer (a $1 to $20 Stripe link, a pre-order or a paid pilot sold to someone at the event or a reachable local business) beats a technically impressive product with no checkout. Plan distribution (who you will sell to in the room or by DM) before writing code.

### Gaps
- No public results from any c0mpiled sales track, so I don't know what amount of revenue has won before. I don't know whether sales to other hackathon participants count.

## Q5. Common failure modes of hackathon projects

### Takeaway
Projects lose to scope too large to finish (leading to a broken demo), "just a wrapper" with no real inference or evaluation, a confusing presentation, and demos judges can't access. A simple project that fully works consistently beats an ambitious one that half works.

### Cited Findings
- "A simple, fully working project consistently scores higher than an ambitious, overscoped one with a broken demo". Scope too large to finish is a common cause of a broken final demo — [HackerEarth via search summary](https://www.hackerearth.com/blog/hackathon-ideas)
- Judges "have seen a hundred GPT wrappers". They favor agentic, RAG or multimodal work aimed at a specific problem — [HackerEarth](https://www.hackerearth.com/blog/hackathon-ideas)
- How a judge spots a wrapper: give the team an input they didn't prepare (hard-coded output won't adapt), ask to see the live request and what context the model received, ask for a test set behind any accuracy claim, and ask what happens when the model is wrong, slow or down ("The AI handles it" doesn't count; fallbacks, thresholds and human hand-off do) — [DEV: judging AI hackathon projects](https://dev.to/pranjulrathour/judging-ai-hackathon-projects-what-to-check-when-every-team-says-we-used-ai-19mb)
- A demo judges can't access scores as if it doesn't work — [lablab.ai guide](https://lablab.ai/guide/how-to-win-an-ai-hackathon)
- JetBrains × Codex judges (June 2026): what decided most winners was "the few minutes they spent presenting it". Their advice: start with the problem (Jono Bacon, Avi Press), pick a specific workflow over the newest tool (Bonnie Xu, OpenAI), build one thing that works rather than five that don't, treat the demo as the pitch, and show it working quickly. "A strong project with a confusing demo loses to a simpler project that the judges understand." — [JetBrains blog](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)
- Judging is noisy: one judging-platform write-up found agreement between judges "no better than chance" — [DEV](https://dev.to/techtush/the-judges-agreed-no-better-than-chance-4-lessons-from-building-a-hackathon-judging-platform-3apn)
- Sponsor incentives shape what wins. An analysis of 8,200 ETHGlobal projects found theme spikes lined up with sponsored events. AI agents grew from about 1% to over 20% of submissions — [Medium (simbro)](https://simbro.medium.com/what-8-200-hackathon-projects-reveal-about-what-actually-wins-f105346ec97c)
- An example 2026 AI hackathon rubric: technical implementation about 25%, problem-solving about 25%, innovation about 20%. You.com's 2025 agentic hackathon used innovation, technical implementation, impact, UX, and presentation/docs — [lablab/masai summary](https://www.masaischool.com/blog/how-to-win-an-ai-hackathon-in-2026-full-guide/); [You.com](https://you.com/resources/the-winners-of-the-you-com-agentic-hackathon-2025)

### Inferences
- Because judging is noisy, make the decisive evidence **objective and undeniable**: a number on screen (a sale, a merged PR, a before/after metric on held-out tests). That reduces how much the result depends on which judge you get.
- Sponsor prizes (MongoDB "best use", Luminal credits) are cheap wins if the core build already uses them in a real way.

### Gaps
- No systematic dataset on failure modes for AI hackathons specifically. The evidence is mostly judge blogs.

## Q6. c0mpiled-15 (Oct 11, 2026, Penn State) judging criteria

### Takeaway
c0mpiled-15 runs **Sunday, October 11, 2026, noon to 9pm** at Penn State's Engineering Design and Innovation Building (State College, PA). It is hosted by c0mpiled (Transpose Platform) and Builder's Collective, with more than $10K in prizes and **YC founders judging**. It has (at least) two tracks. **Track 1** is a self-improving parallel agent team on **Luminal Cloud** (DeepSeek or GLM Flash), judged on relative improvement and problem difficulty with a held-out evaluation. **Track 2** is judged on **actual sales during the event**. Judging starts at 7:00 PM and awards are at 8:15 PM.

### Cited Findings (all from search-engine extracts of the Luma page, which I could not open directly; MEDIUM confidence, and one extract warned the page text was "jumbled")
- Logistics: Sunday Oct 11, 2026, 12 to 9 pm, Engineering Design and Innovation Building, State College PA. Hosts are c0mpiled (by Transpose Platform) and Builder's Collective. More than $10,000 in prizes; YC founders judging and mentoring; dinner provided — [Luma](https://luma.com/compiled-jjvw)
- **Track 1 (Transpose Platform):** "build a self-improving agent team" using **Luminal (YC S25)**, with agents running in parallel and refining a solution over repeated rounds. Use DeepSeek or GLM Flash models hosted on Luminal Cloud. Pick a problem with a measurable outcome (e.g., code optimization, a game-playing bot, a scheduling problem). Show a working demo, the starting baseline and the improvement over rounds, then evaluate on **fresh tests not used during optimization**. Judged on **relative improvement and problem difficulty, not raw scores across unrelated problems** — [Luma](https://luma.com/compiled-jjvw)
- Track 1 prizes: $3,000 for 1st plus a session with Luminal's founder, $1,500 for 2nd, $500 for 3rd — [Luma](https://luma.com/compiled-jjvw)
- **Track 2 (Engineering Entrepreneurship):** winners are those who "successfully build and validate their product by getting actual sales during the event". Prize pools from AWS (up to $5,000), Engineering Entrepreneurship and Bloomerang — [Luma](https://luma.com/compiled-jjvw)
- Sponsor prizes: **MongoDB**, best use of MongoDB, with $1,000 in credits, swag and an article. **Luminal**, $1,000 free inference credits. One extract also mentions a "best use of AGI" side prize — [Luma](https://luma.com/compiled-jjvw)
- Judges named include Greg Woodman and Joe Fioti (Joe Fioti is Luminal's founder, per general knowledge; not verified here) — [Luma](https://luma.com/compiled-jjvw)
- Schedule: judging 7:00 PM, awards 8:15 PM — [Luma](https://luma.com/compiled-jjvw)
- Earlier c0mpiled events used YC RFS lists as tracks (c0mpiled-7: Spring 2026 RFS; c0mpiled-13: Summer 2026 RFS), with YC-founder judges. A previous Penn State edition (c0mpiled-6) exists — [Luma c0mpiled-13](https://luma.com/olys436o); [Luma c0mpiled-7](https://luma.com/rhi9rha9); [Luma c0mpiled-6](https://luma.com/xgtu3nbn)

### Inferences
- **The c0mpiled-15 brief, as found, does not obviously contain a "YC Fall 2026 RFS" track.** Track 1 is a Luminal self-improving-agent challenge and Track 2 is a sales challenge. A YC-RFS idea most likely scores by entering **Track 2** (sell it during the event) and/or by being framed so it also fits Track 1, e.g., Self-Maintaining APIs as an agent team that improves its fix rate on held-out API breaking changes over rounds. Verify on the Luma page whether an RFS track, or a Track 1 "option B", exists. One extract labeled the Luminal brief "option A", which suggests there are other options.
- A scoring methodology for this event should weight: (1) **objective, measurable evidence**, meaning a baseline-to-improved metric on held-out tests (Track 1) or real paid sales (Track 2); (2) a working live demo; (3) fit with a named YC RFS and its exact language, which YC-founder judges will recognize; (4) sponsor-tech usage (Luminal, MongoDB, AWS) for side prizes; (5) a narrow scope that can be finished in about 7 hours of build time (noon start, judging at 7pm).

### Gaps
- I could not confirm the exact Luma wording, whether Track 2 requires a minimum number or amount of sales, whether sales to other attendees count, team-size rules, or whether an "option B" or RFS track exists.
- I found no public results or winners from earlier c0mpiled events to calibrate against.
