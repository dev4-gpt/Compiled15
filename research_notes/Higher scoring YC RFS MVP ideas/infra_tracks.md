# YC Fall 2026 RFS Infra Tracks: (4) AI-Native Compliance Infrastructure, (5) Self-Maintaining APIs, (6) Proving You're Human. Market Gaps and 8-Hour Demoable Product Reframes

Research date: 2026-10-11. Method: web search across vendor pages, IETF Datatracker, arXiv, trade press, and secondary RFS write-ups. Limits on this session (they affect how far to trust the notes):
- ycombinator.com, modelence.com, quasa.io and producthunt.com would not resolve from the sandbox (DNS failure). So the RFS wording below comes from search snippets and secondary write-ups, not the official page.
- GitHub code search and repo APIs were blocked: the session is bound to its configured repos. Live curl to the Federal Register, eCFR, CFPB and SEC also failed. **I could not live-verify any repo name or endpoint in this session.** Items marked "(training knowledge, verify)" come from my prior knowledge and should be checked before a hackathon depends on them.

---

## Q0. What the three RFS entries actually ask for

### Takeaway
All three entries exist on the Fall 2026 list of 13 ideas, each with a named YC author. Self-Maintaining APIs is the most concrete: agents that scan codebases and push fixes as PRs when a provider changes its API. Compliance is framed around fintech: tracking obligations, monitoring regulatory change, flagging anomalies and keeping audit trails.

### Cited Findings
- The Fall 2026 RFS has 13 ideas, and roughly 10 are software-first. The official list is at ycombinator.com/rfs. The apply deadline was reported as July 27, 2026, 8:00 p.m. PT. — [VCCafe](https://www.vccafe.com/requests-for-startups-fall-2026-edition/); [Superframeworks](https://superframeworks.com/articles/yc-fall-2026-rfs-indie-hacker-plays); [Mining Wells](https://miningwells.com/blog/yc-request-for-startups)
- **Self-Maintaining APIs** (author Harsha Gaddipati): AI agents that automatically scan codebases and push the fix as a pull request, so a developer's code updates itself when an API provider changes its interface. — [Medium summary](https://medium.com/@tanishshenoy/yc-has-dropped-its-2026-request-for-startup-wishlist-4313275d32fb); [Modelence mirror](https://modelence.com/yc-rfs-fall-2026)
- **Proving You're Human** (author Max Kolysh): the title appeared in the results, but I could not retrieve the full text. — [Modelence mirror](https://modelence.com/yc-rfs-fall-2026)
- **AI-Native Compliance Infrastructure** (author Daivik Goel): a production-ready platform for fintech and financial services that consolidates fragmented compliance tools. It tracks obligations, watches for regulatory changes, flags anomalies and generates audit trails, with an alerts feed that summarizes what changed and its impact. A secondary write-up dates it to July 23, 2026 and suggests regulatory-change monitoring tied to a company's products and locations as a wedge. — [Modelence compliance page](https://modelence.com/yc-rfs-fall-2026/ai-native-compliance-infrastructure); [Quasa](https://quasa.io/media/yc-fall-2026-rfs-how-to-build-ai-native-compliance-infrastructure)

### Inferences
- Judges scoring "literal RFS fit" will look for these exact phrases. For #5: "scan codebases" plus "push the fix as a PR" when "providers change interfaces". For #4: "obligations", "regulatory change", "anomalies", "audit trail", "fintech". The demo should show each verb happening.

### Gaps
- Full verbatim text of the "Proving You're Human" entry. Pull it from ycombinator.com/rfs directly.

---

## Q1. Self-Maintaining APIs: landscape, datasets, distribution, ideas

### Takeaway
The pieces exist but are not connected. Diff tools (oasdiff, pb33f openapi-changes) detect breaking spec changes. Codemod platforms (Moderne/OpenRewrite) rewrite code. Dependabot/Renovate bump versions but do not fix call sites. The SDK-generator market has consolidated sharply: Stainless went to Anthropic, Fern to Postman, and Speakeasy reportedly pivoted. No dominant product yet closes the loop "provider spec changed → find affected downstream repos → open a verified fix PR". An open-source project called "Patch" claims exactly this loop for TS/JS and is early, so it is the closest originality threat.

### Cited Findings
**Existing tools and players**
- **oasdiff**: a Go CLI and library that diffs OpenAPI specs and flags breaking changes. It separates errors (definite breaks) from warnings (possible breaks). Sources put the number of checks at 100+ or 250+, depending on version. — [oasdiff GitHub](https://www.github.com/Tufin/oasdiff); [BREAKING-CHANGES.md](https://github.com/tufin/oasdiff/blob/v1.10.16/BREAKING-CHANGES.md)
- **pb33f openapi-changes**: another OpenAPI change tool. — [gittrend](https://gittrend.io/repo/pb33f/openapi-changes)
- **Patch** (open source, on Product Hunt): an AI agent that detects breaking API changes and dependency updates and opens a PR with the fix. It runs the type checker and tests, retries on failure, and never auto-merges. TS/JS only and early-stage. — [Product Hunt](https://www.producthunt.com/p/patch-4/patch-6) (via search snippet; page not fetchable)
- **APIShift** (OpenEnv Hackathon India 2026): an RL environment where LLM agents learn to migrate code across API changes, trained on real Stripe, GitHub, Twilio, Slack and OpenAI version diffs. Its reward scores detection, patch correctness and backward compatibility. — [HF Space](https://yaswanth169-apishift-env.hf.space/)
- **Brex/Cursor migration case study**: a single large agent hallucinated library methods, missed obvious breaking changes and bypassed validation gates. Brex moved to orchestrated agent automations and reports a 32x speedup on framework upgrades. — [Brex Journal](https://www.brex.com/journal/agent-automations-for-big-migrations)
- **Moderne/OpenRewrite**: $30M Series B in Feb 2025 ($50M total). OpenRewrite came out of Netflix and is integrated into Amazon Q, Broadcom App Advisor and GitHub Copilot. Moderne launched "Mod Agent". — [TechCrunch](https://techcrunch.com/2025/02/11/moderne-raises-30m-to-solve-technical-debt-across-complex-codebases/); [Intel Capital](https://www.intelcapital.com/moderne-secures-30m-to-drive-billions-in-enterprise-code-modernization-savings-based-on-its-innovative-tech-used-by-aws-microsoft-and-broadcom-ai-assistants/)
- **SDK generator consolidation**: Anthropic reportedly acquired Stainless in May 2026 and is winding down its hosted SDK generator. Fern was acquired by Postman in Jan 2026 and keeps its brand, with generators under Apache-2.0. Speakeasy has reportedly pivoted away from SDKs. Most of these claims come from competitor-authored pages, so treat them with caution. — [Scalar: Stainless wind-down](https://scalar.com/resources/stainless-wind-down); [Fern: leave Stainless](https://buildwithfern.com/lp/leave-stainless); [WorkOS: Stainless alternatives](https://workos.com/blog/stainless-alternatives); [Speakeasy comparison (Feb 2026)](https://www.speakeasy.com/blog/comparison-sdk-generators-openapi)
- **Vercel AI SDK v6→v7**: a community "migrate-ai-sdk-v6-to-v7" agent skill exists, and the canonical version lives in vercel/ai. This is a live, real, recent migration target. — [Tessl registry](https://tessl.io/registry/skills/github/saif-shines/channel-watcher-agent/migrate-ai-sdk-v6-to-v7/review)

**Datasets of real breaking changes**
- An ICWE 2024 study of OpenAPI spec histories found only 517 APIs consistently ship major-version bumps with breaking changes. 1,970 APIs sometimes ship breaking changes in minor or patch releases, and 927 never break. — [USI paper (APIACE, ICWE 2024)](https://design.inf.usi.ch/sites/default/files/biblio/apiace-icwe2024.pdf)
- Public git-versioned OpenAPI specs (training knowledge, verify): [stripe/openapi](https://github.com/stripe/openapi), [github/rest-api-description](https://github.com/github/rest-api-description), [openai/openai-openapi](https://github.com/openai/openai-openapi), [twilio/twilio-oai](https://github.com/twilio/twilio-oai) and [APIs-guru/openapi-directory](https://github.com/APIs-guru/openapi-directory), a multi-thousand-API corpus. Running `oasdiff breaking <old> <new>` across consecutive commits of any of these produces a real, verifiable breaking-change history.

### Inferences
- **Best real-data demo target: SDK major-version migrations with huge public footprints.** Examples (training knowledge, verify): openai-python v0→v1 (`openai.ChatCompletion.create` → `client.chat.completions.create`), Stripe Charges → PaymentIntents, Vercel AI SDK v6→v7, LangChain import moves. A GitHub code search for the old call pattern should return thousands of public repos. I could not run code search in this session, so the hit counts are unverified.
- **Distribution (training knowledge, verify)**: a GitHub App with `contents:write` plus `pull_requests:write` installs per repo or org and opens PRs from a bot identity, the same pattern as Dependabot and Renovate. An MCP server exposing `scan_repo`, `diff_spec` and `propose_patch` lets Claude Code or Cursor users pull fixes locally. A GitHub Action that runs oasdiff on the provider side and publishes a machine-readable "migration recipe" is the provider-side wedge.
- **Etiquette and risk**: mass-opening PRs on strangers' repos counts as spam under GitHub's Acceptable Use policies and will annoy judges if it looks automated. For the demo, fork 3-5 real repos, open PRs against your forks with CI passing, and possibly open 1-2 genuine upstream PRs to repos that are clearly active.
- **Where the gap is**: (a) Provider-side: API vendors have no "publish a breaking change → auto-generate the codemod for every consumer" product, now that Stainless is out of the hosted SDK business. (b) Consumer-side: verification (tests plus type check plus record-replay against a sandbox API) is the moat, because Brex shows naive agents hallucinate. (c) Cross-language: Patch is TS-only.

**Ideas (ranked)**
1. **"Breakwatch": spec diff → blast radius → PR.** Pull two real commits of stripe/openapi or openai-openapi, run oasdiff, have an LLM turn each breaking change into a migration recipe, find public repos using the removed or renamed operation, and open a fix PR on a fork that passes its own tests. Verifiable outcome: a green CI PR on a real repo. RFS fit is very high: it literally scans codebases and pushes the fix. Originality threat: Patch (TS-only), APIShift (research only).
2. **Provider-side "Migration Recipe" GitHub Action.** On every spec PR in an API vendor's repo, it comments the oasdiff breaking list plus an auto-generated codemod and a list of N public dependents affected. Demo on github/rest-api-description history. Sells to API companies, which suits YC B2B.
3. **MCP server "api-upgrade"** for coding agents. `upgrade openai-python to v1` → it finds call sites, rewrites them, and runs tests. Low build cost, but weaker originality because Claude Code and Cursor can already do this ad hoc.
4. **Deprecation-sunset radar.** Monitor providers' `Deprecation` and `Sunset` HTTP headers (RFC 8594/9745, training knowledge, verify) plus changelogs, and alert repos before the date. A weaker demo, because there is no PR at the end.

### Gaps
- Live counts of public repos still calling deprecated endpoints. GitHub code search was blocked here; re-run `gh search code '"openai.ChatCompletion.create"'` from a normal environment.
- Whether Patch's repo is active, and its exact name. Product Hunt could not be fetched.
- I found nothing on 2025-2026 updates from Grit (acquired by Honeycomb? unverified), codemod.com or Optic (reported in prior coverage as acquired by Atlassian, not confirmed here).

---

## Q2. AI-Native Compliance Infrastructure: landscape, free data, ideas

### Takeaway
The top of the market is crowded and well funded: Norm Ai ($120M Series C, Jul 2026), Vanta (agentic platform, ~$300M ARR reported), Drata, Greenlite (fincrime), Cardamon (YC W25, regulatory applicability) and Complir (YC P26, product compliance). A hackathon team cannot out-platform them. The open angle is a narrow, real-data wedge with an auditable output, such as "this live fintech landing page violates these exact CFR sections, here is the trail", or a regulatory-change feed mapped to a specific company's products.

### Cited Findings
- **Norm Ai**: reported $120M Series C led by Khosla at a $1.2B valuation (Jul 2026), more than $260M raised in total. Earlier rounds were $48M in Mar 2025 (Coatue, Craft, Vanguard, Blackstone) and a $27M Series A. Its focus is regulatory AI agents and "supervisory agents". The Khosla and valuation details come from one source. — [AI2Work](https://ai2.work/blog/norm-ai-s-120m-round-turns-compliance-into-an-agent-workload); [PYMNTS](https://pymnts.com/news/investment-tracker/2025/norm-ai-raises-48-million-to-develop-regulatory-ai-agents); [FinTech Futures](https://www.fintechfutures.com/fintech-start-ups/us-regtech-start-up-norm-ai-raises-27m-series-a-funding)
- **Vanta**: AI Agent (Jun 2025) for end-to-end GRC workflows. The Agentic Trust Platform (Nov 2025) is reported in a third-party review at $300M+ ARR and 16k+ customers as of Apr 2026, citing Fortune; unverified. Vanta has also added privacy automation (ROPA, DPIA). — [Channel Insider](https://www.channelinsider.com/news-and-trends/vanta-agentic-ai-compliance-solution/); [SOC2Auditors review](https://soc2auditors.org/insights/vanta-review/); [Verdict](https://www.verdict.co.uk/?p=399979)
- **Greenlite**: AI agents for financial-crime compliance (AML/KYC). An aggregator reports $20M total and a Series A in May 2025 (low reliability). — [Extruct](https://www.extruct.ai/hub/greenlite-ai/); [NeuronFeed](https://neuronfeed.com/compare/greenlite-ai-vs-norm-ai)
- **YC companies**: Cardamon (W2025, London, ex-Revolut) works out which regulations apply to each financial firm. Complir (P2026, Copenhagen) handles product compliance and labels for cross-border retail. LogosGuard (2025) turns AI policies into executable controls. The YC Regtech and Compliance directories list more. — [YC Regtech directory](https://www.ycombinator.com/companies/industry/Regtech); [YC Compliance directory](https://www.ycombinator.com/companies/industry/Compliance); [Complir press](https://www.complir.io/resources/press)
- **Federal Register API**: free, no key, JSON or CSV, base `https://www.federalregister.gov/api/v1/` (e.g. `documents.json`, `agencies`). Pagination is capped at 2,000 results, so use date filters. — [Federal Register REST API docs](https://www.federalregister.gov/reader-aids/developer-resources/rest-api); [nokey client source](https://nokey.readthedocs.io/en/latest/_modules/nokey/government/federal_register.html)
- **eCFR API**: free, no key, with point-in-time historical versions and search. — [eCFR REST API docs](https://www.ecfr.gov/reader-aids/ecfr-developer-resources/rest-api-interactive-documentation)
- **Regulations.gov API**: dockets, documents and public comments. — [Vaquill guide](https://www.vaquill.ai/blog/regulations-gov-api-guide-rulemaking-data)
- **Context**: the EU AI Act sets the tone for risk-based AI regulation, and financial institutions name AI regulatory compliance as a 2026 priority. — [FinTech Global](https://fintech.global/2026/01/08/ai-regulatory-compliance-priorities-financial-institutions-face-in-2026)

**More free data sources (training knowledge, verify endpoints)**
- eCFR versioner: `https://www.ecfr.gov/api/versioner/v1/full/{date}/title-12.xml?part=1026` (Reg Z), plus `/api/versioner/v1/versions/title-12.json` for change dates. Point-in-time diffs make "what changed in Reg Z since date X" verifiable.
- CFPB Consumer Complaint Database API: `https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/` (filter by company or product, free text narratives).
- SEC EDGAR: `https://data.sec.gov/submissions/CIK##########.json` and full-text search `efts.sec.gov/LATEST/search-index` (requires a User-Agent header).
- FTC enforcement actions and press releases (RSS); FINRA Rule 2210 (communications) text; NMLS Consumer Access (state licensing lookup; no official API, scraping ToS risk).
- EU AI Act consolidated text on EUR-Lex (Regulation (EU) 2024/1689). GPAI obligations took effect 2 Aug 2025, and most high-risk obligations take effect Aug 2026, subject to the EU "digital omnibus" delay proposals. Verify the current dates.

### Inferences
- **Incumbent collision map**: SOC 2 and ISO evidence collection is owned by Vanta/Drata (avoid). Enterprise reg-to-policy agents are owned by Norm Ai (avoid head-on). AML transaction monitoring and KYC is owned by Greenlite, Sardine, ComplyAdvantage, Alloy and Unit21 (avoid). State licensing tracking is held by Harbor Compliance and incumbents. Regulatory applicability for fintech is Cardamon's turf. **Still open-ish**: fintech marketing and UDAAP review of live public pages (Hadrius and Saifr touch RIA and broker-dealer marketing review, so verify), and "compliance-as-code CI" that fails a PR when product copy, fee disclosures or app flows violate a mapped CFR citation.
- The most verifiable real-data demo is to take 10 real public fintech landing pages (neobanks, BNPL, crypto apps), check their claims against specific CFR sections (Reg Z §1026.24 advertising triggers, Reg DD §1030.8, the FDIC §328 misrepresentation-of-insurance rule, the FTC Act §5 substantiation standard), and output citation-anchored findings with the exact eCFR paragraph URL plus a screenshot. Then cross-reference CFPB complaint counts for the same company as an "anomaly" signal. Each finding can be checked by hand, which is what verifiable means here.

**Ideas (ranked)**
1. **"RegDiff → Impact PR."** Watch the Federal Register API for new CFPB/OCC/FDIC/FinCEN rules and diff eCFR point-in-time versions. Map each change to a fintech's repo (fee-disclosure templates, T&C markdown, onboarding copy) and open a PR with the redline plus citation, so the audit trail is the git history. This combines #4 and #5 and hits obligations, regulatory change, audit trail and fintech literally.
2. **"Ad-claim linter for fintech."** Crawl a real company's site, extract claims ("FDIC insured", "0% APR", "no fees", "guaranteed"), map each to a CFR or FTC rule, and flag it with a paragraph-level citation. Demo on 10 real sites with a hand-verifiable table. Watch for collisions with Hadrius, Saifr and Red Oak (marketing review for advisers; verify).
3. **Complaint-anomaly radar.** Use the CFPB complaints API to find week-over-week spikes per company or issue and auto-draft a root-cause memo tied to the relevant reg. This is a real "flags anomalies" demo on fully public data.
4. **EU AI Act obligation mapper for AI startups.** Read a real company's public product description or model card, classify its risk tier, and emit an article-by-article obligation checklist with EUR-Lex anchors. More crowded (many "AI Act checker" tools exist) and outside the fintech RFS focus.

### Gaps
- Hadrius, Saifr and Red Oak 2026 status and funding: none surfaced in this session's searches.
- Drata's 2026 AI agent launches: not found.
- Live verification of the CFPB, eCFR and EDGAR endpoints: curl was blocked here.

---

## Q3. Proving You're Human: landscape, unsolved problems, 8-hour browser demos

### Takeaway
The market has split into two layers. (1) **Agent authentication**: Web Bot Auth / HTTP Message Signatures, now an IETF WG draft co-authored by Cloudflare and Google, which Visa TAP, Mastercard Agent Pay and Amex build on. It proves which registered agent is calling, not whether a human is behind it. (2) **Unique-human proof**: World ID with AgentKit delegation (18M+ credentials, regulatory baggage), ZK passport proofs (Self, ZKPassport, Rarimo) and stamp aggregators (Human Passport). The unsolved middle is binding layer 1 to layer 2 in a privacy-preserving, non-crypto-native, non-biometric way that a normal website can verify with a few lines of code: "this signed agent acts for one real, unique human, rate-limited per human, without revealing who."

### Cited Findings
- **Web Bot Auth**: `draft-ietf-webbotauth-httpsig-protocol-00` (Sep 2026, Standards Track, Web Bot Auth WG), by Thibault Meunier (Cloudflare) and Sandor Major (Google). It defines a `Signature-Agent` header, a JWKS key directory, and a well-known URI. It expires 5 Mar 2027. — [IETF Datatracker](https://datatracker.ietf.org/doc/html/draft-ietf-webbotauth-httpsig-protocol-00)
- It is built on RFC 9421 HTTP Message Signatures. Bots publish an Ed25519 JWKS at `/.well-known/http-message-signatures-directory` and sign requests. Cloudflare's Verified Bots program has used it since 1 Jul 2025. A crawlbase post says it was still an individual draft (-02) as of Aug 2026, which conflicts with the Sep 2026 WG draft; the WG adoption is probably newer. — [Crawlbase](https://crawlbase.com/blog/web-bot-auth-signed-agents/); [earlier individual draft](https://www.ietf.org/archive/id/draft-meunier-webbotauth-httpsig-protocol-00.html); [architecture draft](https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture)
- Reported backers include Amazon, Cloudflare, Akamai and OpenAI, and AWS WAF supports it. Google is involved. — [TechWyse](https://www.techwyse.com/news/ai-search/google-web-bot-auth-ai-agent-cryptographic-verification)
- **Visa Trusted Agent Protocol + Mastercard Agent Pay** (announced with Cloudflare on 24 Oct 2025) both use Web Bot Auth as the agent-authentication layer, and Amex is also adopting it. Agent Pay does not remove a merchant's KYB, AML or age-check duties. "Know Your Agent" is an industry framing, not a standard. — [Cloudflare blog](https://blog.cloudflare.com/secure-agentic-commerce/); [Cloudflare press release](https://www.cloudflare.com/press/press-releases/2025/cloudflare-collaborates-with-leading-payments-companies-to-secure-and-enable-agentic-commerce/); [Kapronasia](https://kapronasia.com/insight/blogs/payments-research/visa-and-cloudflare-launch-trusted-agent-protocol); [Didit](https://updates.didit.me/blog/agentic-commerce-identity-layer/)
- **World ID / AgentKit**: launched Mar 2026 so a verified human can delegate their World ID to an AI agent, developed with Coinbase. In Jun 2026 it added support for Claude Code, Codex, Cursor and others, with integrations for Okta, Shopify, Vercel, Browserbase and Exa. It has issued 18M+ credentials. World has been banned or investigated in 10+ countries. One analysis argues that only World proves a unique human behind an agent, while AP2, Visa, Mastercard and Web Bot Auth prove registration or payment capability. — [HackerNoon](https://hackernoon.com/world-expands-agentkit-so-ai-agents-can-prove-a-unique-human-is-behind-them); [The Defiant](https://thedefiant.io/news/infrastructure/world-enters-phase-3-extends-proof-of-human-to-ai-agents); [BlockEden](https://blockeden.xyz/blog/2026/04/18/world-chain-proof-of-humanity-ai-agents-sybil-resistance/); [Quartz](https://qz.com/sam-altman-world-human-verification-ai-agents)
- **Human Passport** (human.tech): aggregates Web2 and Web3 "stamps" (GitHub, LinkedIn, ENS, BrightID). Its uniqueness is weaker than iris, but it carries less regulatory exposure. — [human.tech blog](https://passport.human.tech/blog/proof-of-personhood-explained-how-it-works-who-s-building-it-and-why-it-matters-now)
- **Self (self.xyz)**: ZK proofs over passport and ID NFC data, with npm packages `@selfxyz/qrcode` and `@selfxyz/core` and on-chain verification on Celo. It reportedly raised $9M in Nov 2025. **ZKPassport**: scans the NFC chip and MRZ and generates a ZK validity proof. Trade-offs versus Self, Rarimo and Privado ID include device limits, replay risk, and personhood versus identity. — [Safe Foundation research](https://safefoundation.org/blog/safe-research-zk-passport-where-are-we-now); [Devcon forum](https://forum.devcon.org/t/privacy-preserving-verification-for-ticketing-with-self-protocol/7682); [skills.sh self-xyz](https://www.skills.sh/openclaw/skills/self-xyz)
- **Personhood credentials paper**: arXiv 2408.07892 (Adler et al., more than 30 co-authors from OpenAI, Microsoft, MIT, Oxford and others; v4 Jan 2025). It argues CAPTCHAs fail against capable AI and strict ID checks are not private enough, and proposes personhood credentials. — [arXiv](https://arxiv.org/abs/2408.07892v3); [DIF blog](https://blog.identity.foundation/balancing-online-trustworthiness-and-anonymity-with-personhood-credentials/)

### Inferences
- **Unsolved problems**:
  - (a) Per-human rate limiting for agents. A site wants "max N free trials or votes per real human, across any agent", and Web Bot Auth alone cannot give that.
  - (b) A non-crypto, non-biometric issuer with broad coverage. World needs an Orb; Self and ZKPassport need an NFC passport and a native app.
  - (c) Revocation and accountability: who is liable when a delegated agent misbehaves.
  - (d) Verification that site owners can drop in. Most sites run Turnstile or reCAPTCHA, not any of these.
  - (e) Proving an agent is acting on fresh human intent (consent for a specific transaction), not just that a human exists.
- **What is demoable in a browser in 8 hours** (training knowledge for libraries, verify):
  - WebAuthn/passkeys via `@simplewebauthn/browser` and `@simplewebauthn/server`, a device-bound human-presence and user-verification signal.
  - Signing an agent's requests with Ed25519 per Web Bot Auth: Cloudflare publishes reference code at `cloudflare/web-bot-auth` (verify) and RFC 9421 libs exist.
  - Cloudflare Turnstile (free).
  - Privacy Pass / Private Access Tokens, which Safari issues automatically on Cloudflare-fronted sites.
  - Self's QR SDK for passport ZK proofs, if a team member has an NFC passport and the Self app.
- **The highest-leverage reframe** is a "human-bound agent token". A human does a passkey (UV=true) ceremony once, plus an optional Self or World proof. A server issues a short-lived delegation credential bound to the agent's Web Bot Auth key (JWKS thumbprint) with scope and per-human quotas. Sites verify `Signature-Agent` plus the delegation token. **Real verifiable outcome**: run real headless agents (Playwright, Browserbase, OpenAI or Claude computer-use) against a demo site and show that unbound agents are blocked or rate-limited while bound ones pass, with a live log. This is distinct from World AgentKit (no Orb, open standard) but near it conceptually: **flag World AgentKit as the originality threat**.

**Ideas (ranked)**
1. **"Human-bound agent pass"** (passkey plus Web Bot Auth delegation plus per-human quota middleware). It works as a drop-in Express or Cloudflare Worker middleware and an MCP or browser-agent client plugin. The demo: real agents hit a real deployed page, and the pass rate is shown live. Strong RFS fit. Watch for World AgentKit and Cloudflare signed agents.
2. **Agent-traffic auditor.** Deploy a free Cloudflare-fronted page (or analyze your own server logs), classify real incoming bot traffic by UA, ASN, reverse DNS and the presence of Web Bot Auth signatures, and report the share that is verifiably signed versus spoofed (e.g. fake "GPTBot" UAs from non-OpenAI IPs; OpenAI and Google publish crawler IP ranges). The verifiable result is real bot traffic. The startup is "Plausible for agents". Collides with Cloudflare Bot Management, DataDome and HUMAN Security for enterprises, but is open for small sites.
3. **Proof-of-human for reviews and comments.** Gate a comment or review form with Self ZK passport proof (uniqueness nullifier per site) or a passkey plus a human stamp. Demo: one person cannot post twice. Narrower; Self and World already pitch this.
4. **"Consent receipts" for agentic checkout.** A human approves a specific cart via passkey, producing a signed receipt the merchant verifies alongside a Visa TAP or Mastercard Agent Pay style agent signature. Collides with Visa Intelligent Commerce and Google AP2 mandates (verify AP2's "mandates" concept).

### Gaps
- Official current text of the YC "Proving You're Human" RFS.
- Current status of Cloudflare Privacy Pass, Turnstile and Private Access Tokens in 2026, and any evidence of mass CAPTCHA defeat by agents in 2026: not found in this session.
- Humanity Protocol (palm scan) 2026 status and Rarimo SDK status: not researched due to the tool budget.
- Whether Cloudflare's Agents SDK has shipped Visa or Mastercard protocol support (promised Oct 2025, unconfirmed).
- Google AP2 details beyond the name.
