# c0mpiled-15 (Penn State, Sun Oct 11 2026): judges, sponsors, and demand they publicly state

**Method and limits.** Everything below comes from WebSearch result extracts. WebFetch and curl were blocked (DNS failure or proxy 403 on news.engr.psu.edu, luminal.com and docs.agi.tech), so no primary page was read in full. Each claim is tagged:
- **[F]** is a fact as reported in a search extract, with its URL.
- **[I]** is my inference.
- **Conf** gives confidence as H, M or L.

Four judges' companies could not be identified at all: Unseen AI, Raya, Cara and Starborn (see Gaps).

---

## 0. Event rules: read these first

- **Event.** [F] Sun Oct 11 2026, 12:00 to 21:00, at the EDI Building. Prize money is ">$10,000", and "YC founders" are there to judge and mentor. Greg Woodman (Adjunct Prof, Engineering Entrepreneurship) is the only judge named in the extract. Open to all. Conf H. https://luma.com/compiled-jjvw
- **Track 1 (Transpose Platform).**
  - [F] Teams use DeepSeek or GLM Flash models hosted on Luminal Cloud to explore competing approaches, evaluate them, and feed the results into the next round.
  - [F] Entries must show a working demo and a baseline. The final solution is scored on fresh tests that were not used during optimization.
  - [F] Judging weighs relative improvement and problem difficulty, not raw scores.
  - [F] Prizes: 1st $3000 plus a 1:1 with Joe Fioti, 2nd $1500, 3rd $500.
  - Conf M-H. https://luma.com/compiled-jjvw
- **Track 2 (Engineering Entrepreneurship).** [F] "Sell your product DURING the hackathon!" Winners are the teams that "successfully build and validate their product by getting actual sales during the event". The organizers will "bring in local business connections to help teams find problems and validate ideas". Prize pool: "various prizes up to $3000". Conf M-H. https://luma.com/compiled-jjvw
- **Sponsor prizes and credits.** [F] Best use of AGI: $500. Best use of MongoDB: $1000 in credits, swag and an article. Luminal Cloud: $1,000 of free inference. Conf M-H. https://luma.com/compiled-jjvw
- **Organizer.** [F] Het Sheth is listed as host ("PSU Alum, Labs @ Bloomerang"). Conf M. https://luma.com/compiled-jjvw
- **What this implies for scoring.**
  - [I] Track 2 is scored on revenue evidence, such as Stripe receipts, signed LOIs or paid pilots.
  - [I] Track 1 is effectively an "AutoML / evolutionary search over prompts or programs on cheap open models" contest that rewards held-out generalization.
  - [I] One project can target both tracks plus the AGI and MongoDB prizes if it runs inference on Luminal, uses AGI's agent and stores data in Atlas.

### 0a. Precedent: c0mpiled-6/pennstate (Feb 27 2026), Het Sheth's "sprint hackathon"

- **Format.** [F] Run by PSU Engineering Entrepreneurship with Transpose Platform, Fri Feb 27, 4 to 11 pm, EDI Building. Organized by Het Sheth (then a CS senior) and Ishaan Narang, with faculty support. Theme: "AI for Productivity and Research" (generative AI for scientific discovery, workflow automation, research, education and productivity). Prize pool $7,500+. Conf H.
  - https://news.engr.psu.edu/2026/sheth-het-eship-hackathon.aspx
  - https://www.psu.edu/news/engineering/story/engineering-entrepreneurship-program-host-sprint-hackathon-feb-27
- **Sheth's background.** [F] Sheth had won prizes at earlier Transpose c0mpiled events in California. Conf M. https://news.engr.psu.edu/2026/sheth-het-eship-hackathon.aspx
- **Speakers.** [F] The c0mpiled-6 Luma page lists Henry Kwon, Abejith Murali and Shaurya Pednekar plus PSU faculty. Conf M. https://luma.com/xgtu3nbn
- **Gaps.**
  - **Winners and detailed rules for c0mpiled-6: NOT FOUND.** The PSU article is a pre-event announcement, and no recap or compiled.sh post-mortem surfaced. The page itself could not be fetched (DNS blocked).
  - No "sales during the event" rule was found for c0mpiled-6. That rule appears only for c0mpiled-15.
- **Other c0mpiled results.** [F] c0mpiled-2 (Abu Dhabi, agentic systems) was won by a project on human fatigue in industrial workflows. Conf M. https://www.compiled.sh/articles/c0mpiled-2-the-adaptive-city-post-mortem
- **Tokyo winner.** [F] c0mpiled Tokyo (Mar 2026) was won by "Engram", an AI memory assistant. Conf M. https://prtimes.jp/main/html/rd/p/000000015.000172016.html
- **YC RFS themes.** [F] c0mpiled events generally use YC Request-for-Startups themes. Conf M. https://luma.com/compiled-cp9o and https://melts.notion.site/Transpose-The-University-of-Tokyo-IPC-Mori-Building-YC-Collaboration-Hackathon-Part-2-306903bd64b88027a9c2de6110dcc01b

### 0b. What Engineering Entrepreneurship judges value

- **Ted Graef.** [F] Directs PSU E-SHIP (since Jan 2020). He co-founded All Traffic Solutions, a State College hardware company, and his bio stresses rapid product development and startup operations. He created the ENtern startup internship. Conf H.
  - https://news.engr.psu.edu/2020/graef-ted-engineering-e-ship-appointment.aspx
  - https://www.sedi.psu.edu/eship/faculty.aspx
- **Greg Woodman.** [F] Frames his teaching around the entrepreneurial mindset and explicitly lists customer discovery. Conf M. https://www.sedi.psu.edu/eship/faculty.aspx
- **PSU programs.** [F] PSU I-Corps and Happy Valley LaunchBox teach lean startup and customer discovery. Conf M. https://invent.psu.edu/hubs/happy-valley-launchbox-powered-by-pnc-bank/
- **Inferred priorities** [I], conf M:
  - A real paying customer beats a polished demo.
  - Judges will ask who paid, how much, and why.
  - Evidence of customer discovery (interviews, the local business's own words) and a repeatable sales motion matter.
  - Physical or operational businesses fit Graef's background.
  - A $5 to $50 paid pilot from a real local business, or a Stripe payment link with real receipts, is probably the strongest proof possible in 9 hours.

---

## 1. Judges' companies

### Luminal (Joe Fioti, CEO, PSU alum): YC S25

- **What they sell.** [F] An open-source Rust ML compiler that integrates with PyTorch (a torch.compile backend). It compiles models ahead of time into fast GPU and ASIC kernels. Luminal Cloud is serverless inference with automatic batching, scale-to-zero and pay-per-use. Licensed on-prem deployment is also offered. Conf H.
  - https://www.luminal.com/
  - https://github.com/luminal-ai/luminal
  - https://www.ycombinator.com/companies/luminal
- **Performance claims.** [F] Vendor claims "2-3x" over existing engines, for example GPT-OSS 120B on 8xH100 at 36k tok/s vs 28k for TensorRT-LLM and 26k for vLLM. YC's profile says "10x". Unverified. Conf M. https://www.luminal.com/
- **Funding.** [F] $5.3M seed led by Felicis (Nov 2025). Conf H.
  - https://techcrunch.com/2025/11/17/luminal-raises-5-3-million-to-build-a-better-gpu-code-framework/
  - https://www.felicis.com/blog/luminal-announcement
- **Joe Fioti.** [F] PSU alum, ex-Intel. Conf M. https://luma.com/compiled-jjvw
- **Pain points and asks** (from hiring) [F], conf M:
  - Cloud Inference Engineer work on KV caching, paged attention, sequence packing, and the scheduler, batcher and autoscaling. https://zerogtalent.com/space-jobs/luminal/cloud-inference-engineer
  - A torch.compile frontend that handles framework edge cases. https://www.ycombinator.com/companies/luminal/jobs/yfZYkvH-ml-framework-frontend-engineer
  - Rust codegen for NVIDIA, Trainium, AMD and TPU targets. https://www.ycombinator.com/companies/luminal/jobs/7Bgke65-senior-compiler-engineer
  - "Closed multiple contracts with non-Nvidia hardware platforms" (customers not named).
- **Blog.** [F] "Compiling Models to Megakernels". Conf M. https://blog.luminal.com/p/compiling-models-to-megakernels
- **Third-party caveat.** [F] Long compile phases suit stable, high-volume models but are less suited to fast-changing models and short-lived serverless instances, so check cold starts. Conf M. https://www.itechguides.com/luminal-raises-5-3-million-to-build-a-better-gpu-code-framework-what-it-actually-does/
- **API access.**
  - [F] $1,000 of free Luminal Cloud inference is given at this event. Conf H.
  - [F] One aggregator says the cloud was early-access or invite only. Conf L.
  - [F] An LLM-gateway directory lists Luminal serving "DeepSeek v4.1 Flash". Conf L. https://llmgateway.io/providers
- **OpenAI-compatible? UNCONFIRMED.**
  - No Luminal API docs surfaced.
  - [I] Because Track 1 uses DeepSeek and GLM, and LLM gateways list Luminal as a provider, an OpenAI-style /v1/chat/completions endpoint is likely. Conf L-M.
  - Ask organizers for the base URL and key at check-in, and keep the OpenAI SDK with a swappable `base_url`.
- **Hackathon idea (Track 1 plus sales).** "Evolve-and-verify optimizer for one local business's real task."
  - Example tasks: classifying a vet clinic's call transcripts, or extracting fields from a restaurant's supplier invoices.
  - Run an evolutionary prompt and program search on DeepSeek or GLM Flash on Luminal. Report the baseline against held-out accuracy, plus cost per 1k calls on Luminal against GPT-class APIs.
  - Sell the resulting tuned pipeline to the business as a $X/month pilot.
  - [I] This hits Luminal's pitch (cheap, fast open-model inference), Track 1's held-out rule and Track 2's sales rule at once.

### AGI, Inc. (Vivek Patel; CEO Div Garg, ex-MultiOn)

- **What they sell.** [F] Computer-use agents. The flagship AGI-0 handles clicks, form filling, navigation and multi-step workflows across browser, Android/iOS and desktop OSes. The company claims #1 on OSWorld, AndroidWorld and its own REAL Bench (vendor-reported). There is an embedded Agent SDK for devices, with demos with Lenovo and Qualcomm. Backers include Menlo and Point72; funding figures conflict ($10M vs a $20M seed). Conf M.
  - https://www.theagi.company/agent
  - https://ai.theagi.company/products-agi-0-agi-api-and-sdk-offerings
  - https://www.unite.ai/?p=441825
- **Developer API** [F], conf M-H:
  - Get a key at **platform.agi.tech**.
  - REST base `https://api.agi.tech/v1` with a Bearer key.
  - Calls: `POST /sessions {agent_name:"agi-0"}`, then `POST /sessions/{id}/message {message:"..."}`, then poll `GET /sessions/{id}/status`.
  - The docs also mention a live VNC "screencast" view, persistent login and browser state between tasks, and SSE streaming.
  - Agents: agi-0, agi-0-fast, agi-1. There is a Node SDK. The open-source `agisdk` (pip, Apache-2.0) is a separate benchmark and eval toolkit.
  - https://agiinc.mintlify.app/
  - https://github.com/agi-inc/agi-node
  - https://github.com/agi-inc/agisdk
- **OpenAI-compatible?** [I] No. It is a session or task API, not chat completions. Conf M.
- **Pricing.** [F] Starter $19/mo with 1,000 "thinking" steps (~50 tasks), then pay-as-you-go at $0.02 per step. Third-party only, not confirmed. Conf L-M. https://ai.theagi.company/products-agi-0-agi-api-and-sdk-offerings
- **Cloudflare listing.** [F] Cloudflare lists "AGI Agent" as a verified bot that "takes actions and makes purchases on behalf of users". Conf M. https://radar.cloudflare.com/bots/directory/agi-agent-2
- **Pain and ask** [I], conf M:
  - They need real-world, reliable, revenue-generating workflows to prove the "99.9% reliability on custom workflows" claim.
  - The $500 "Best use of AGI" prize signals they want showcase use cases.
- **Hackathon idea.** "Legacy-portal agent for local SMBs."
  - AGI-0 logs into the web portals a small business already uses, such as a vet's PIMS, a restaurant's supplier ordering site, or the Centre County permit or licensing portals, and does the repetitive task: reorders, reconciling invoices, posting hours to Google Business Profile.
  - Show the live VNC view during the demo. Charge the business for setup on the spot.

### VetRec (Kevin Cohen, co-founder and CEO): YC S23

- **What they sell.** [F] A HIPAA-compliant, SOC 2 Type II AI scribe for veterinarians. It writes SOAP notes, discharge notes and rDVM letters, and summarizes patient-history PDFs of 150+ pages. Company claim: saves ~2 hours a day per doctor. It is in Cornell CVM's program. Seattle-based. Conf H.
  - https://www.ycombinator.com/companies/vetrec
  - https://dvm360.com/view/cornell-college-of-veterinary-medicine-partners-with-ai-powered-scribe
  - https://ycombinator.com/companies/vetrec/jobs/ztggLLC-software-engineer
- **PIMS integration.** [F] Pushes notes into ezyVet through the Partner API (vendor claim: 10-15 minutes down to ~60 seconds per consult). No Cornerstone integration was found. Conf M. https://www.ezyvet.com/integration/vetrec
- **Newest launch.** [F] **AI Receptionist** (Jul 15 2026): answers calls 24/7, books appointments, takes messages, routes urgent cases and logs to the PIMS. Coming next: online booking, outbound follow-ups and Rx refill reminders. Pricing is sales-led. Scribe is reportedly priced per DVM per month. Conf M-H.
  - https://www.streetinsider.com/PRNewswire/VetRec+Launches+AI+Receptionist+to+Ensure+Clinics+Never+Miss+a+Call/26772597.html
  - https://www.puppilot.co/phone-systems/vetrec
- **Industry pain.** [F] Vets spend 1-2 hours after close on records ("pajama time"); data is siloed across PIMS, causing double entry and callbacks. Burnout stats (70-84%) are unsourced. Conf M.
  - https://www.puppilot.co/blog/the-moral-injury-of-pajama-time-is-administrative-burden-a-deeper-more-solvable-driver-of-vet-burnout
  - https://otto.vet/the-definitive-guide-to-veterinary-pims-integration-automation/
- **API.** [I] No public developer API was found, so do not build on VetRec directly. Conf M.
- **Hackathon idea.** Build what VetRec says is "coming next" (outbound follow-ups and refill reminders) for a **State College vet clinic**:
  - Ingest the clinic's discharge notes.
  - Generate and send personalized recheck and refill SMS or email.
  - Track bookings.
  - Sell a month's pilot to a local clinic during the event.
  - [I] Vet clinics are a dense SMB category locally, and Karbasi (Moichor) is also vet-adjacent, so this idea appeals to two judges.

### NPU Ventures (Shevy Karbasi): founder of Moichor, YC W21

- **Background.** [F] Karbasi co-founded Moichor, a YC W21 AI veterinary diagnostics company (computer-vision CBC for birds and reptiles; in-clinic Pathview device with results in ~15 minutes; 60k+ tests in 2022; 200+ clinics). He then launched **NPU Ventures, a pre-seed fund focused on AI and national-security startups**. This comes from one PSU Startup Week listing, so treat it as single-sourced. Conf M.
  - https://pennstatestartupweek2026.sched.com/event/2H9xL/build-break-pivot-a-y-combinator-founders-journey-to-vc
  - https://www.dvm360.com/view/exclusive-moichor-opens-preorders-for-image-based-cbc-point-of-care-device
  - https://pet-insight.com/?p=19118
- **API.** None (a VC fund).
- **Judging lens** [I], conf M: fundable pre-seed wedge, defensibility, and dual-use or national-security angles. He also knows vet clinics as a sales channel.
- **Idea fit.** Any team that shows "paid by a real customer today, plus a path to a large market" fits.
  - [I] A dual-use framing, such as an agent that automates government or regulatory portals, may resonate.

### Dropbox (Ajay Narayanan Sridhar)

- **Product and API.** [F] Dropbox runs a remote MCP server (beta) with 23 file tools: list, search, extract content, sharing links, file requests, revisions. Team admin, webhooks and large uploads are available only in the v2 API. There is no machine-to-machine auth, so headless agents need offline refresh tokens. Conf M. https://www.scalekit.com/blog/dropbox-mcp-vs-api
- **Engineering blog.** [F] Dropbox Tech posts in 2026 cover Dash (AI universal search) and MCP, for example "How Dropbox uses MCP and Dash to close the design-to-code security gap" (Jun 2026) and "Dash's relevance judge with DSPy" (Mar 2026). Conf M. https://dropbox.tech/tag-results
- **Free tier.** [I] The Dropbox API is free with an app key (developer console). Not verified in this pass.
- **Idea.** "Shoebox to books":
  - A local SMB drops receipt and invoice photos into a Dropbox file request.
  - An agent extracts and categorizes them and returns a monthly spreadsheet.
  - Sell it as a bookkeeping pre-processor.

### Fanatics (Krushil Amrutiya)

- **Business and AI work.** [F] Licensed sports merchandise, collectibles (Fanatics Collectibles/Topps) and betting. With Google Cloud it runs AI product discovery across 100M+ fans. Its CPO says product discovery ranked #1 in its research into shopping friction (~2,400 new SKUs during March Madness). It is hiring for Applied AI recommendations and autonomous agents. Conf M.
  - https://www.pymnts.com/news/retail/2026/how-fanatics-turns-2-billion-daily-fan-signals-into-sales/
  - https://swooped.co/job-postings/ai-engineer-new-york-fanatics-inc-9222c
- **API.** None public. [I]
- **Idea.** A game-day merch and inventory assistant for downtown State College shops that sell PSU gear around home games. It forecasts demand from the football schedule and opponent, and drafts restock orders and social posts. [I] Local apparel shops depend heavily on Beaver Stadium weekends.

### Unseen AI (Amanda Lind, SPC), Raya (Kanika Gupta, HF0 W26), Cara (Kartikey Pandey), Starborn (Rushi Patel)

- **Not identified** after 2-3 searches each. Conf: gap.
  - No SPC company named "Unseen" surfaced. Unrelated hits included Unseen Security (NL), Unseen (Australian real-estate data) and Unseenlabs (FR).
  - No HF0 "Raya" surfaced. A "Raya" voice-AI company exists (LitWiz Labs; Indian-language voice agents), but nothing links it to Kanika Gupta or HF0. https://huggingface.co/RayaVoiceAI
  - Nothing came up for Cara or Starborn. A Rushi Patel co-founded Homebase (SMB hourly-team software), but that link is unverified and probably a different person.
- **Action.** Ask the judges in person, or check their LinkedIn profiles, before pitching.
- **Safe framing** [I]: SPC and HF0 judges tend to reward technical depth and strong founder-market fit.

---

## 2. Sponsors and partners

### Transpose Platform

- [F] A Houston-listed investment firm (~$2.65B AUM per an aggregator). It describes itself as a "significant investor" in YC through YC-fund vehicles (Transpose Platform BOV II) and runs the c0mpiled hackathon series on YC RFS themes. Conf M.
  - https://yespress.io/transpose-platform.md
  - https://my.motherbase.ai/company/178896-transpose-platform
- [F] Track 1 sponsor ($3000 first prize). [I] They want to see YC-grade founders.

### AWS

- [F] Not verified: the $200 new-account credit search returned nothing for AWS.
- [I] Bedrock, Lambda and Amplify are typical. No AWS-specific prize appeared in the extracts.

### MongoDB

- [F] Atlas M0 is free forever (512 MB, shared resources) on AWS, GCP or Azure. Prize: $1000 in credits, swag and an article. Conf H.
  - https://www.mongodb.com/cloud/pricing
  - https://luma.com/compiled-jjvw
- [I] Use Atlas plus Vector Search as the system of record to qualify.

### Engineering Entrepreneurship (Ted Graef, Greg Woodman)

- See §0b. They fund the Track 2 pool (up to $3000).

### Red Bull

- No product or API relevance. [I] An in-kind sponsor.

### Connect Happy Valley

- **Correction to the brief.** [F] It is **not** a business network. It is "the local guide and community utility that makes it easier for people to find their people, discover welcoming places", linking residents and newcomers with clubs, nonprofits, cultural experiences and third places. It runs "Connect Happy Valley Social" mixers (Sep 20 2026, Pine Grove Hall, $6). Conf M-H.
  - https://connecthappyvalley.com/
  - https://www.statecollege.com/event/connect-happy-valley-social-2/
- [I] Its "customers" are local clubs, nonprofits, venues and third places: cafes, breweries, studios, gyms and event spaces. Organizers said they would bring "local business connections" to Track 2.
- **Related local business bodies** [F]:
  - Centre County Chamber (CBICC) member directory: https://business.cbicc.org/activememberdirectory/FindStartsWith?term=H
  - Happy Valley Networking (HVN) group: https://www.statecollege.com/business-directory/category/network-marketing/
  - Downtown State College Improvement District (DSCID): going through 2026 reauthorization, struggling to fill vacancies, and running a Calder Way pop-up incubator. Conf M. https://www.psucollegian.com/news/borough/business-owners-community-members-express-support-for-dscid-reauthorization-plan-during-public-hearing/article_9c9998cb-0a8b-4a37-a6a9-e022bd844584.html
  - Happy Valley LaunchBox: https://invent.psu.edu/hubs/happy-valley-launchbox-powered-by-pnc-bank/
- **Idea fit** [I]:
  - An "events and listings autopilot" for clubs, nonprofits and venues: turn a flyer photo or Instagram post into structured events pushed to the Connect Happy Valley calendar, Google Business Profile and Facebook.
  - Or a membership and RSVP tool. Sell at $10-25/month to venues met at the event.

### co.space

- [F] Spun out of the New Leaf Initiative (2014) as an off-campus "educational living space for young entrepreneurs" (a house). New Leaf's coworking space has since closed. Current status unclear. Conf L-M.
  - https://sites.psu.edu/engineering/2014/01
  - https://www.statecollege.com/articles/community/new-leaf-initiative-closes-downtown-state-college-coworking-space/

### Nittany AI (Nittany AI Alliance)

- [F] PSU program with a multi-phase AI Challenge: customer discovery, then prototype, then MVP, then pitch.
- [F] The 2026 winner was CrashAI (PennDOT crash-data analysis; $5.5k plus awards).
- [F] The 2026-27 cycle opened Sep 1 2026; prototypes are due Jan 25 2027.
- Conf H.
  - https://www.psu.edu/news/academics/story/student-teams-win-cash-awards-their-ai-solutions-nittany-ai-challenge
  - https://www.nittanyai.psu.edu/challenge
- [I] A hackathon project can roll into the Nittany AI Challenge.

### MICS

- **Not identified.** No PSU club named "MICS" surfaced. Gap.

---

## 3. Best "close the gap and sell today" plays (all [I])

1. **Vet-clinic follow-up and refill agent.** Builds VetRec's stated roadmap gap. Uses Luminal for inference, AGI-0 to log into the PIMS or portal, and Atlas for storage. Buyer: a State College or Centre County vet clinic. Price: $49-99 for a 1-month pilot. Appeals to Cohen, Karbasi, Fioti and AGI.
2. **Venue and club events autopilot for the Connect Happy Valley ecosystem.** Turns flyers and Instagram posts into events on GBP, Facebook and the community calendar. Buyer: cafes, breweries, nonprofits. Price: $10-25/month. Easy to close live.
3. **Game-day merch and staffing forecaster for downtown shops.** Fits Fanatics (Amrutiya) and DSCID.
4. **Track 1 entry.** Evolutionary prompt and program search on Luminal-hosted DeepSeek or GLM for a real SMB classification or extraction task, with a held-out test set and a cost comparison. The tuned pipeline doubles as the Track 2 product.

**Sales proof tips** [I]: use a Stripe payment link or a PSU-friendly Venmo/PayPal invoice, get the buyer on video or on a signed one-page pilot agreement, and show screenshots of the receipt.

---

## 4. Gaps and next steps

- Unseen AI, Raya, Cara, Starborn and MICS are unidentified. Ask in person or check LinkedIn.
- Luminal API docs (base URL, OpenAI compatibility, key issuance) were not found. Ask organizers or the Luminal team at check-in.
- c0mpiled-6 winners and recap were not found. The PSU news page was unreachable (DNS); only search snippets were used.
- AGI pricing is from a third party only. Base URL is consistent (api.agi.tech/v1), but there is a docs.agi.tech vs mintlify discrepancy.
- AWS credit terms and the AWS prize are not verified.
- Vivek Patel's role at AGI Inc is not verified.
