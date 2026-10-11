# AI-native products that can take money during c0mpiled-15 (Track 2) and still be a startup afterwards

Prepared 2026-10-11 for c0mpiled-15 at Penn State. Track 2 is judged on actual sales during the event.

**Method and limits (read first)**
- All evidence comes from WebSearch result extracts. I did not use WebFetch, so no page was read in full. Numbers are as the search snippets reported them.
- **Reddit is blocked.** WebSearch with `allowed_domains: reddit.com` returned a 400 error ("domains are not accessible to our user agent"), and open queries returned no Reddit threads. So this note has **no Reddit demand evidence**. The demand signals are surveys, vendor pricing, Product Hunt, TrustMRR, YC pages and press. That is a gap. If you can, have a teammate spend 15 minutes checking r/cscareerquestions, r/college and r/startups manually.
- Tags used: **[F]** = fact as reported by a source. **[I]** = my inference. Confidence is H/M/L.
- Several sources are vendors writing about competitors (Adzuna, Jobright, Scoutify, fincomparelab). They are flagged where used.

---

## 0. Market context

| Signal | Detail | Source | Conf |
|---|---|---|---|
| YC is mostly B2B and agent-heavy; consumer is thin | [F] Of 478 YC 2026 companies, only 20 (4%) are tagged Consumer. About 47% match an "agent" keyword screen. | https://dev.to/eliofbm/i-analyzed-all-478-yc-2026-startups-consumer-is-fading-half-the-batch-builds-ai-agents-hardware-51hi | M (third-party count) |
| W26 agent examples are vertical B2B | [F] Agents (37) are the largest category, e.g. Patientdesk.ai and Wayco. | https://www.extruct.ai/research/ycw26 | M |
| S26/P26 theme: infrastructure for agents (phone numbers, cards) | [F] AgentPhone (YC P2026) gives agents their own phone numbers. | https://timewell.jp/en/columns/yc-summer-2026-batch-analysis , https://www.ycombinator.com/companies/industry/call-center | M |
| F26 batch | [F] Mostly unpublished. Early lists show 10 to 19 companies. | https://nextbillion.net/business-development/y-combinator-fall-2026-batch/ | M |
| What this means for you | [I] Consumer "agent does the errand" products are underfunded by YC, so the space is not saturated. It is also less proven as fundable. Founder-ops ideas fit YC's B2B tilt better. | — | — |

---

## 1. Founder lead and investor research agent (best fit for selling at the event)

**What it is.** A founder pastes a one-liner and an ICP or round size. The agent browses and enriches, then returns either 50 qualified investors or customer leads. Each row has a reason-to-contact, a verified email or channel, and a personalized first-touch draft. Optionally it pushes rows into a CRM (Notion or Sheets) and queues sends.

**Evidence**
- [F] Clay hit **$100M ARR in Dec 2025** with about 14k customers and a $5B tender (Jan 2026). A later report says it raised $115M at $7.1B. Its research agent, Claygent, browses the web and writes structured results. https://hub.causo.ai/guides/clay-alternatives-2026 , https://thenextweb.com/news/clay-raises-115m-series-d-7-1bn-valuation-wellington (H that the category is fundable)
- [F] Clay's pain point for small teams: credit burn. One operator spent about **$700 in two weeks**. https://hub.causo.ai/guides/clay-alternatives-2026 (M, vendor framing)
- [F] **Fundraisly** launched on Product Hunt on 2 Jun 2026 with about 1k to 1.5k upvotes and claims Launch of the Month. Plans start at **$1,000/mo**. https://hunted.space/dashboard/fundraisly , https://theaiagentindex.com/agents/fundraisly (M, the two sources give conflicting upvote counts)
- [F] VentureStrat AI costs $69 to $149/mo. EasyVC has a 50k-contact database. Outreachr is free and open source. https://www.capterra.com/p/10045820/VentureStrat-AI/ , https://thedailyworkflow.com/service/EasyVC , https://www.everydev.ai/tools/outreachr
- [F] Human alternative: Fiverr B2B lead-list gigs cost **$50 to $400 per order**, delivered in 2 days to 2 weeks. https://fiverr.com/nurul_alam22/do-b2b-lead-generation-and-targeted-email-list-building (M)

**Who pays and how much.** [I] Hackathon founders, judges' portfolio companies and online indie founders. A price of **$19 to $49 per run** undercuts Fiverr ($50+, days) and Fundraisly ($1k/mo). Upsell to $49/mo for a weekly refresh.

**Gap.** [I] Today the choice is a $1k/mo fundraising platform, a Clay setup with a learning curve, or a slow human list. There is no "pay once, get it in 15 minutes, with drafts" option aimed at pre-seed and student founders.

**6-hour MVP.** Form (startup URL, target type) → agent with web search and browser → scrape and enrich (portfolio pages, Crunchbase-like public data, recent tweets/posts) → score fit → draft emails → deliver a Google Sheet and Gmail drafts. The live demo runs on a judge's own startup.

**Selling it during the event.** Stripe Payment Link at $29. Walk the room. Every team at c0mpiled-15 is a founder who will want customers or investors on Monday. Offer a free 5-row preview, with full results behind payment.

**Startup potential.** M to H. The market is large (Clay). The risk is commoditization and data-provider costs.
**Overall confidence that it sells at the event:** H.

---

## 2. Quality-gated internship and job agent ("sniper, not spammer")

**What it is.** The agent watches fresh postings (GitHub internship lists, Greenhouse/Lever/Ashby boards). It applies only to roles above a fit threshold. It tailors the résumé per role, fills the ATS form in a browser, finds the recruiter or hiring manager, and drafts a short personal note. Its pitch is explicitly the opposite of auto-apply spam: 10 good applications a day, not 750.

**Evidence**
- [F] Greenhouse 2025 report: applications per job rose from **28 (2021) to 95 (2025)**. **More than 1 in 5 US candidates** have used AI agents to apply. Only 8% of job seekers call AI hiring fair. https://www.greenhouse.com/newsroom/an-ai-trust-crisis-70-of-hiring-managers-trust-ai-to-make-faster-and-better-hiring-decisions-only-8-of-job-seekers-call-it-fair (H)
- [F] Fortune, Jul 2026: about **254 applicants per job ad** on Greenhouse. The CEO calls it an "AI doom loop". https://fortune.com/2026/07/27/greenhouse-ceo-daniel-chait-ai-doom-loop-job-seekers-spam-interview-applications-unemployment/ (H)
- [F] A banking recruiter says early-careers application volume tripled in a year, driven by agentic AI. https://www.efinancialcareers.com/news/agentic-ai-for-banking-jobs (M)
- [F] LazyApply complaints: it applies to random jobs, achieves about 10/day rather than the advertised 750, and users report account flags. Pricing is $99 to $999/yr. https://ca.trustpilot.com/review/lazyapply.com?page=3 , https://scoutify.com/blog/lazyapply-review , https://www.adzuna.co.uk/blog/aiapply-review-what-works-what-doesnt-a-better-alternative (M; the reviewers are competitors)
- [F] Willingness to pay exists: AIApply made **$15K/mo (Apr 2024)** and later about $25K/mo. https://starterstory.com/stories/aiapply (M, self-reported). Jobright costs $29 to $59/mo. Simplify+ costs about $39.99/mo. scale.jobs charges $199 for 250 human-submitted applications. https://jobright.ai/blog/simplify-copilot-review-2026-features-pricing-and-top-alternatives/ , https://scale.jobs/blog/cheapest-ai-job-search-tools (M)
- [F] Student outreach tools are tiny: ReachOut has 4 users, ColdCraft is free, Inboxd is on Indie Hackers. https://chromeboard.com/extension/reachout-—-cold-email-lin-icddimbiggognaacbjfgkiahmaekofoh , https://peerpush.com/p/coldcraft , https://www.indiehackers.com/product/inboxd (M)

**Who pays.** Students at Penn State and at the event. [I] Pricing could be **$9 for 10 tailored applications plus 10 recruiter notes**, or $19/mo. Timing helps: Oct to Jan is peak posting season for summer internships (https://www.mintlify.com/vanshb03/Summer2026-Internships/seasons/summer-internships, M).

**Competitors.** Simplify, Jobright, LazyApply, AIApply, JobCopilot, Careerflow, scale.jobs.
**Gap.** [I] The volume tools are distrusted. The quality tools (Simplify) only autofill. Nobody combines "agent applies end-to-end" with a hard quality gate plus a human-contact note.

**6-hour MVP.** Upload résumé → agent pulls 30 new SWE internship postings from the GitHub list → scores fit → tailors 10 → uses Playwright/browser-use to fill 2 to 3 Greenhouse forms live, pausing for the user to approve submit → finds the recruiter on LinkedIn or the company site → drafts a note.

**Selling it.** $9 Stripe link on a QR code at a table. Pitch it in the student Discord or GroupMe. The demo is a real application submitted on stage.

**Startup potential.** M. The market is huge but crowded, there is ToS and ban risk on LinkedIn, and ATSs are adding bot defenses (inferred from the Greenhouse "doom loop" framing).
**Confidence it sells at the event:** H for $5 to $10 price points.

---

## 3. "Money-back agent": calls, emails and fills forms to cancel, refund or dispute

**What it is.** The user forwards a receipt or names a charge. The agent cancels the subscription, requests the refund, or files the dispute. It works through email, web chat or form, or a voice call that waits on hold and talks to the rep. Pricing is pay-per-task or a share of what it recovers.

**Evidence**
- [F] **Pine AI** calls, emails and operates software to negotiate bills, cancel subscriptions and file refunds and disputes. It claims a 93% negotiation success rate and **$3M+ saved** (BusinessWire, Dec 2025). Third-party listings put pricing from **$150/mo** (unconfirmed). https://www.businesswire.com/news/home/20251203384902/en , https://catalog.thesys.dev/ai-agents/pine-ai (M)
- [F] **pap! (YC S24)** scans inbox e-receipts and automatically claims price-drop refunds by contacting customer service through email, phone, forms or chat. It charges commission only and has expanded to flight delays and class actions. The launch page reported $6,650 secured, growing 233% MoM. https://www.ycombinator.com/launches/LoC-pap-automatic-refunds-for-consumers , https://www.ycombinator.com/companies/pap (H)
- [F] Rocket Money charges **35 to 60% of first-year savings** for bill negotiation and $7 to $14/mo for Premium, which includes a cancellation concierge. https://www.fincomparelab.com/reviews/rocket-money-review/ (M, third-party)
- [F] Hold-time pain: about **41 min/month on hold** per person, or 2.8B hours/yr in the US. This is a 2025 survey commissioned by a vendor. https://answeringservicecare.com/insights/please-hold-america-the-national-hold-music-report/ (M). 22% of Americans would rather spend a night in jail than contact customer service (2022). https://www.kptv.com/2022/09/28/22-americans-would-rather-spend-night-jail-than-contact-customer-service-survey-finds/ (M)
- [F] **Threat:** iOS 26 **Hold Assist** waits on hold for you natively. https://www.igeeksblog.com/iphone-hold-assist-in-ios-26/ (H). [I] Waiting on hold alone is now a feature. The product has to do the conversation and the follow-through.
- [F] **Regulatory warning:** DoNotPay settled with the FTC ($193k) over overstated "robot lawyer" claims. https://www.abajournal.com/news/article/robot-lawyer-website-donotpay-settles-ftc-claims-it-couldnt-deliver-on-promises (H). Moffatt v. Air Canada shows that chatbot statements bind the company that deploys them. https://www.manatt.com/insights/newsletters/advertising-law/ai-gone-wild-airline-has-to-honor-a-refund-policy (H)
- [F] US DOT automatic refund rule: airlines must refund cards within 7 business days of a cancelled or significantly changed flight. https://www.usefini.com/guides/ai-airline-cancellation-refund-automation (M, vendor)

**Who pays.** [I] Students with forgotten subscriptions, gym contracts, airline credits or Amazon price drops. Pricing could be **$5 per completed task, or 25% of the amount recovered**.
**Competitors.** Pine, pap!, Rocket Money, Billshark, Trim. DoNotPay is damaged.
**Gap.** [I] Pine is expensive. Rocket Money is limited to supported providers. pap! covers only receipt-driven claims. A student-priced, pay-per-task agent that also does voice is open.

**6-hour MVP.** Chat intake → agent picks a channel → (a) drafts and sends the cancellation or refund email from the user's Gmail via OAuth, or (b) places a Vapi/Retell/Twilio voice call with a script and live transcript → logs the outcome. The demo is a live call on stage to a real customer-service line, or to a teammate playing the rep.

**Selling it.** "Tell us one charge you hate. $5 if we kill it today." Outcomes are visible within hours, so revenue can be counted.

**Startup potential.** M to H. The consumer financial pain is broad. Unit economics depend on voice cost. Liability needs careful claims (no "lawyer" language).
**Confidence it sells at the event:** M. Some calls will not resolve within event hours.

---

## 4. Accelerator / YC application agent for founders

**What it is.** The agent reads your repo, site and deck. It drafts YC/accelerator answers, critiques them against public YC advice, finds 10 matching accelerators and grants with deadlines, and pre-fills the forms.

**Evidence**
- [F] Human review sells: HireCade charges **$499** for a live YC-application review session. https://www.hirecade.com/learning/yc-application-review (M). Lobster Capital's YC Roaster is free, with reviews by YC founders. https://lobstercap.substack.com/p/announcing-yc-roaster-free-brutally (H)
- [F] The YC deal is $125k for 7% plus $375k on an uncapped MFN SAFE, so the outcome is worth a lot to applicants. https://www.rebelfund.vc/blog-posts/y-combinator-winter-2026-batch-true-costs-breakdown (H)

**Who pays.** Hackathon teams, who are a perfect audience on the day. [I] Price **$15 to $29**.
**Gap.** [I] There is the free human roaster and the $499 human session, and almost nothing agentic that also finds and pre-fills the other 20 accelerators and grants.
**6-hour MVP.** GitHub URL + site → draft answers → critique → output a list of 10 programs with deadlines and pre-filled text.
**Selling it.** Every team at the event is a buyer, and the pitch is "apply to YC with what you built today."
**Startup potential.** L to M. It is seasonal with a small TAM. It could serve as a wedge into idea #1 (founder ops).
**Confidence it sells at the event:** H. **As a long-term startup:** L.

---

## 5. Class-action settlement filing agent

**What it is.** The agent scans the inbox or purchase history, matches it against open settlements, pre-fills the claim forms, and the user signs the attestation.

**Evidence**
- [F] At least 7 or more iOS/Android "settlement finder" apps exist (Claimly, TapClaim, ClaimBack, ClassyAction, Settlement Finder, ClaimWise, Settlemate). Many **do not file for you**: ClaimBack says explicitly that it does not file. Others gate auto-fill behind a subscription. https://apps.apple.com/us/app/-/id6755294155 , https://apps.appfollow.io/ios/claimback-settlemate-cash/6757753865?country=mr , https://appgoblin.info/apps/6760950821 (M)
- [F] Live example: the Apple Siri AI settlement pays **up to $95** to iPhone 15 Pro / 16 buyers (Jun 2024 to Mar 2025). https://www.kold.com/2026/09/22/some-iphone-users-could-get-up-95-apple-settlement-heres-how-file-claim/ (H). [I] Most students qualify, which makes it a perfect live hook.
- [F] pap! (YC) has expanded into class actions. https://www.ycombinator.com/companies/pap (H)

**Who pays.** [I] Students. Price **$3 per filed claim** or 15% of the payout. Payouts arrive months later, so charge upfront.
**Gap.** [I] Finder apps are commoditized. Actually filing end to end from receipts in your inbox is rare.
**MVP.** Gmail OAuth → find Apple/Google/Amazon receipts → match against 5 hand-curated open settlements → browser agent fills the form, then stops for user attestation.
**Risks.** Fraud and attestation rules apply. The user must personally attest.
**Startup potential.** M. It is a natural feature of a broader "money-back agent" (#3).
**Confidence it sells at the event:** M to H. The Siri hook is timely.

---

## 6. Financial-aid appeal agent

**What it is.** Intake (income change, competing offers) → the agent finds the school's specific appeal or professional-judgment form and process → drafts the letter with documentation → compares competing offers → emails the aid office.

**Evidence**
- [F] Secondhand citation of College Aid Pro (Mar 2025): **75% of private-college and 25% of public-college appellants succeed**, with typical gains of **$3k to $5k/yr**. https://dev4.ngpf.org/blog/question-of-the-day/question-of-the-day-if-a-student-successfully-appeals-their-college-financial-aid-offer-how-much-additional-aid-do-they-typically-receive-per-year/ (L to M, the original study was not located)
- [F] The incumbent, SwiftStudent, offers **free templates, not an agent** (2020, built with FormSwift). https://www.bestcolleges.com/news/swiftstudent-helps-students-ask-for-financial-aid-fixes/ (H)
- [F] Consumer Reports: appeals succeed when circumstances change or when a school matches a comparable offer. https://www.consumerreports.org/paying-for-college/how-to-ask-for-more-college-financial-aid (H)

**Who pays.** [I] Families of incoming students. Price **$29 to $49**, or a success fee. The return is high: $29 for a possible $3k+.
**Gap.** [I] Only free static templates exist, with no school-specific agent.
**Event timing problem.** [I] Award letters and appeals cluster in spring. In October, current students appeal mainly for mid-year changes. Penn State is mostly public, where success rates are lower. **A sale at the event is unlikely.** This is a better startup than a hackathon sale.
**Startup potential.** M (B2C, seasonal; could go B2B2C through counselors).

---

## 7. Security-deposit recovery agent

**Evidence**
- [F] Depositron (NYC) generates demand letters. Nearly 5,000 complaints about withheld deposits have been filed with the NY AG since 2023. https://www.thomsonreuters.com/en-us/posts/ai-in-courts/security-deposit-crisis (H)
- [F] Juris (LA) DepositLetter is an AI service for renters. https://socaltech.com/juris_launches_ai_powered_service_to_help_renters_get_their_deposits_back/s-0079417.html (M)
- [F] Caution: AI letters tend to overstate claims and misread local law. https://terms.law/2025/02/24/why-ai-generated-security-deposit-demand-letters-can-backfire/ (M). Property managers are noticing renters using AI. https://www.getaptly.com/blog/your-renters-are-using-ai-to-fight-deposit-deductions-heres-what-i-learned-from-a-manager-with-1-250-doors (M)

**Assessment.** [I] The agent would read the lease and move-out photos, compute state-statute deadlines, send a certified-mail demand (via the Lob API) and file small claims. The pain is real for students, but **October is off-season** (move-outs happen May and August), and the rules are jurisdiction-heavy. Low chance of a sale at the event. M as a startup.

---

## 8. Health-insurance denial appeal agent (consumer)

**Evidence**
- [F] **Claimable** charges about **$50/case**, claims about 75% overturn, and raised **$10M** (Mark Cuban among investors) according to Bloomberg via PYMNTS. It has deals with 4 drugmakers. https://www.pymnts.com/artificial-intelligence-2/2026/insurance-denials-meet-their-match-in-ai-powered-appeals/ , https://corridorbusiness.com/ai-meets-advocacy-how-claimable-is-helping-patients-fight-denied-insurance-claims/ (M to H)
- [F] Counterforce Health is free (nonprofit) and claims about 70%. https://www.axios.com/local/raleigh/2025/08/20/using-ai-to-fight-back-against-insurance-denials-counteforce (H). Sheer Health has a free tier and paid appeals. https://lailluminator.com/2025/11/20/repub/health-insurance-bots/ (H)

**Assessment.** [I] Proven and fundable, but the buyers are not students at a hackathon. It needs PHI handling (HIPAA). A free nonprofit already exists. **Do not pick this for Track 2.**

---

## 9. Scholarship apply agent (deprioritize)

- [F] PRSPCT AI (scholarship matches and essays, $9.99/wk or $24.99/mo) shows **no active subscriptions on TrustMRR**. https://trustmrr.com/startup/prspct-ai (M). [I] This is a negative willingness-to-pay signal.
- [F] ScholarPath AI is a solo-developer Product Hunt launch with 5 agents. https://www.producthunt.com/p/scholarpath-ai/scholarpath-ai (M). Most tools find and draft but do not submit.
- [I] Students expect scholarship help to be free (school portals, Fastweb), so selling it at the event is unlikely.

---

## Indie / MRR benchmarks

- [F] AgentGPT has about **$9K MRR** with 215 subscriptions on TrustMRR (Jan 2026). Most agent-tagged TrustMRR startups are at $0 to $100 MRR. https://trustmrr.com/startup/agentgpt (M). [I] Being "an agent" is not enough. Specific, painful jobs are what sell.
- [F] Turbo AI (study notes) reports eight-figure ARR, 5M users and about $20/mo pricing. https://www.techcrunch.com/2025/10/23/20-year-old-dropouts-built-ai-notetaker-turbo-ai-to-5-million-users (H). [I] Students will pay $20/mo, but the study category is saturated and not agentic, so it is excluded.
- [F] Consumer browser-agent launches are mostly dev infrastructure (BrowserAct was #1 on Product Hunt on 25 Jun 2026). https://www.onenewspage.com/n/Press+Releases/1ztfzbohwh/BrowserAct-Reaches-No-on-Product-Hunt-Highlighting.htm (M). [I] Build on that infrastructure (BrowserAct, browser-use) rather than competing with it.

---

## Ranking for c0mpiled-15 Track 2 [I]

| # | Idea | Sale during event | Startup | Main risk |
|---|---|---|---|---|
| 1 | Founder lead/investor agent ($29) | H | M to H | Data costs; Clay commoditization |
| 2 | Quality-gated internship agent ($9) | H | M | ATS/LinkedIn bot blocks; crowded |
| 4 | YC/accelerator app agent ($19) | H | L to M | Small TAM; seasonal |
| 3 | Money-back agent (cancel/refund/dispute, $5/task) | M | M to H | Calls may not resolve during event; FTC claims |
| 5 | Settlement filing agent ($3/claim) | M to H | M | Attestation/fraud; slow payouts |
| 6 | Financial-aid appeal agent | L | M | Wrong season; public-school odds |
| 7 | Deposit recovery agent | L | M | Off-season; jurisdiction law |
| 8 | Insurance denial agent | L | M to H | PHI; buyer not present |
| 9 | Scholarship agent | L | L | No WTP evidence |

**Suggested combination [I].** Build #1 as the core. Bundle #4 as a $19 "founder pack" upsell aimed at the room. Or, for a student-facing angle, combine #2 and #5 into a "student money and career agent" with several cheap SKUs. Several low price points ($5 to $29) on Stripe Payment Links increase the number of transactions, which is presumably what "actual sales" counts. Confirm with organizers whether they score on revenue or on transaction count.

## Gaps and next checks
- No Reddit threads (domain blocked). Verify demand quickly by asking 10 attendees on site.
- Pine's pricing, Simplify+ pricing and AIApply's 2025/26 MRR are unconfirmed or third-party only.
- The 75%/25% financial-aid appeal statistic is secondhand.
- The F26 YC list is incomplete. Re-check the YC directory filtered to Fall 2026 for competitors in each idea.
- c0mpiled-15 Track 2 rules: whether sales to other participants or judges count was not verified here.
