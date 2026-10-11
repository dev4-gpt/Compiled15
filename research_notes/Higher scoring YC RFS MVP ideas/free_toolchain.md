# The free leverage stack for an 8-hour student hackathon (as of October 2026)

**Method note:** Direct page fetches (WebFetch/curl) were blocked in this environment (DNS failure / proxy 403). All findings come from web-search result summaries, mostly third-party roundups dated Jan–Sep 2026. Free-tier numbers change often and sources disagree. Treat every number as "check the console on the morning of the hackathon". Conflicts are flagged inline.

## 1. Free / free-tier LLM APIs and inference

### Takeaway
A team can run an entire hackathon on free hosted inference without paying. Groq and Cerebras give very fast open-weight models (roughly 1–2k tok/s on Cerebras). Gemini's free tier covers Flash/Flash-Lite plus multimodal input. OpenRouter `:free` models are a fallback, capped at 50 requests/day unless the account has ever bought $10 of credits. The binding limits are usually daily token or request caps, not speed, so build a provider fallback chain.

### Cited Findings
- **Groq:** free tier needs no credit card. It is governed by rate limits, not a monthly token budget, and limits apply per organization, not per API key — [eesel](https://eesel.ai/blog/groq-pricing); [costbench](https://costbench.com/software/llm-api-providers/groq/free-plan/)
- **Groq** (Aug 2026 table reproduced by a third party): about 30 RPM for most chat models. llama-3.1-8b-instant gets 14,400 RPD / 500K tokens/day. llama-3.3-70b-versatile gets 1,000 RPD / 100K tokens/day. Whisper audio gets about 2,000 requests/day. The daily token ceiling binds before the request count — [localaimaster](https://localaimaster.com/blog/groq-api-free-guide); [OpenRouter blog comparison](https://openrouter.ai/blog/tutorials/free-llm-apis-compared/). One costbench page wrongly says "no free tier" — [costbench](https://www.costbench.com/software/llm-api-providers/groq/)
- **Gemini API free tier:** sources conflict heavily.
  - A Sep 30 2026 guide says Flash, Flash-Lite and 2.5 Pro are free in the API, but image and video generation models are not. Limits apply per Google Cloud project and reset at midnight Pacific — [yingtu](https://yingtu.ai/en/blog/google-gemini-api-free-tier-limits-2026)
  - Apr 2026 sources say Pro was removed from the free tier ("Free tier Flash-only, Pro paid-only", effective Apr 1 2026) — [agentdeals](https://agentdeals.dev/gemini-api-pricing-changes)
  - Quoted Flash limits range from 5 RPM / ~100 RPD, to 10 RPM / 250K TPM / 250 RPD (Jan 2026), to 15 RPM / 1,500 RPD (May 2026) — [tinkerllm](https://tinkerllm.com/blog/gemini-api-free-tier-limits-rate-quotas/); [costbench](https://www.costbench.com/software/llm-api-providers/google-gemini-api/free-plan/)
  - Google's own page says limits depend on tier, model and account, and should be viewed in AI Studio — [yingtu](https://yingtu.ai/en/blog/google-gemini-api-free-tier)
- **OpenRouter `:free` models:** 20 RPM. 50 requests/day until the account has bought $10 of credits in its lifetime, then 1,000/day. The upgrade persists even at a zero balance. Limits are per account across all keys, and the set of free models rotates — [truefoundry](https://www.truefoundry.com/de/blog/openrouter-rate-limits-your-free-tier-depends-on-what-youve-already-paid); [pinggy](https://pinggy.io/blog/free_ai_model_apis_unlimited_tokens_openrouter/); [benchlm](https://benchlm.ai/md/free-tier/openrouter.md)
- **Cerebras:** free trial of about 1M tokens/day (some sources also list 1M tokens/hour) on gpt-oss-120b and qwen-3.8-27b. Request limits conflict: 5 RPM / 30K uncached TPM (Sep 2026 summary) versus 30 RPM in older summaries. Sources also disagree on whether a card is needed ($5 credits after adding a payment method, versus no card) — [fast.io](https://fast.io/resources/cerebras-rate-limit/); [benchlm](https://benchlm.ai/md/free-tier/cerebras.md); [costbench](https://costbench.com/software/llm-api-providers/cerebras-inference/free-plan/)
- **Cerebras speed:** marketed at about 2,000 tok/s — [morphllm](https://www.morphllm.com/cerebras-pricing)
- **Hugging Face Inference Providers:** free users get about $0.10/month of credits with no pay-as-you-go option. PRO gets $2/month and can continue pay-as-you-go. HF charges provider rates with no markup — [HF docs](https://huggingface.co/docs/inference-providers/pricing); [HF blog](https://huggingface.co/blog/inference-providers)
- **Cloudflare Workers AI:** 10,000 Neurons/day free, shared across all models (big models drain it faster). After that it needs Workers Paid at $0.011 per 1,000 Neurons. Limits reset at 00:00 UTC — [Cloudflare plans](https://www.cloudflare.com/plans.md); [pricepertoken](https://pricepertoken.com/endpoints/cloudflare/free); [dev.to](https://dev.to/yimtheppariyapol/cloudflare-workers-ai-add-a-free-llm-to-a-static-site-no-backend-needed-37ab)

### Inferences
- For an 8-hour demo, plan for these daily caps:
  - Groq 70B: about 100K tokens/day, which runs out quickly with RAG prompts.
  - Groq 8B: 500K tokens/day.
  - Cerebras: about 1M tokens/day.
  - Each teammate can create their own account or org (the limits are per org) to multiply quota. This works legitimately for a team of 3–4.
- Use an OpenAI-compatible client with a fallback list (Cerebras → Groq → Gemini Flash → OpenRouter free). Groq and Cerebras speed makes "instant" UX cheap to demo.
- The cheapest free multimodal input (images, PDFs, audio) is likely Gemini Flash. Groq Whisper (about 2,000 requests/day) is the cheapest fast hosted speech-to-text.

### Gaps
- Could not verify official rate-limit pages for Groq, Gemini, Cerebras or Cloudflare (fetch blocked).
- No data found on "Luminal" as a free inference provider.
- GitHub Models and Mistral free tiers were not researched.

## 2. On-device and in-browser models

### Takeaway
On a 16 GB Apple Silicon laptop:
- 7–14B models run at about 25–60 tok/s via Ollama/llama.cpp.
- In-browser WebGPU (WebLLM, Transformers.js v4) reaches about 60 tok/s on high-end Macs, less on typical laptops.
- Kokoro TTS (82M) runs faster than real time in the browser.
- Chrome's Gemini Nano APIs (Prompt and Summarizer) work, but they need large disk space and a capable GPU, so they make a risky demo dependency on a borrowed laptop.

### Cited Findings
- **Transformers.js v4:** release notes report GPT-OSS 20B (q4f16) at about 60 tok/s on an M4 Pro Max via WebGPU. A commentator notes that "your average laptop isn't doing that" — [transformers.js releases](https://github.com/huggingface/transformers.js/releases); [aihola](https://aihola.com/article/transformers-js-v4-browser-ai)
- **In-browser LLM:** one anecdotal run hit 66.8 tok/s on an M3 Pro (engine unclear) — [pinggy](https://pinggy.io/blog/run_llm_in_browser_webgpu/)
- **Unverified viral claim:** "Gemma 4 at 255 tok/s in browser". Treat as unreliable — [pasqualepillitteri](https://pasqualepillitteri.it/en/news/7149/gemma-4-255-tok-browser-webgpu-fable-5)
- **Ollama on laptops:** 3–4B models fit on 8 GB machines. 7–14B is the sweet spot on 16 GB unified memory, at about 25–60 tok/s on Apple Silicon. Common picks are llama3.2 3B, llama3.1 8B and qwen2.5-coder 7B. These are SEO-style guides, so the numbers are directional — [itsourcecode](https://itsourcecode.com/ai-framework/ollama-run-local-llms-2026-complete-guide/); [davidsblueprint](https://www.davidsblueprint.com/articles/best-laptops-for-ollama-2026)
- **Kokoro TTS 82M:**
  - Runs fully client-side via kokoro-js / Transformers.js, using WebGPU or a WASM fallback — [kokoro-js README](https://cdn.jsdelivr.net/npm/kokoro-js@1.2.0/README.md); [dev.to](https://dev.to/emojiiii/running-kokoro-82m-onnx-tts-model-in-the-browser-eeh)
  - Real-time factor (RTF) of 0.2–0.4 on an M2 Air with WebGPU; about 1.1 on a mid-range x86 laptop with WASM. Firefox issues were reported — [voicechanger benchmarks](https://voicechanger.live/text-to-speech/benchmarks)
- **Whisper large-v3-turbo:** about 809M parameters (decoder pruned to 4 layers). A vendor reports about 5x faster than large-v3 on an M2 MacBook Pro (10 min of audio in 63 s, using CoreML, not whisper.cpp). Independent GPU numbers show about 2.7x — [whispernotes](https://whispernotes.app/en/blog/introducing-whisper-large-v3-turbo); [classmethod](https://dev.classmethod.jp/articles/openai-whisper-large-v3-turbo-faster-whisper/)
- **Chrome built-in AI (Gemini Nano):**
  - Official docs (Sep 2025): Prompt API stable in Chrome 138 for extensions only; Summarizer shipping from 138; Writer/Rewriter in origin trial — [Chrome built-in APIs](https://developer.chrome.com/docs/ai/built-in-apis)
  - Newer reports say the Prompt API became stable for any website from Chrome 148 — [Tom's Hardware IT](https://www.tomshw.it/business/chrome-148-gemini-nano-prompt-api-stabile-runtime-browser-locale); [noqta](https://noqta.tn/en/tutorials/chrome-built-in-ai-prompt-api-gemini-nano-2026)
  - Requirements: Windows 10/11, macOS 13+, Linux or ChromeOS (Chromebook Plus); no Android or iOS. At least 22 GB free disk and more than 4 GB VRAM — [Summarizer API docs](https://developer.chrome.com/docs/ai/summarizer-api)

### Inferences
- "Private, offline, in-browser" is now a cheap, credible demo angle. Example stack: Transformers.js or WebLLM with a 1–4B model plus Kokoro TTS plus Whisper (tiny/base in the browser, turbo locally).
- Download size (hundreds of MB to GBs) is the practical risk on venue Wi-Fi. Pre-cache the models.
- Gemini Nano is a "nice if available" path. Always feature-detect with `LanguageModel.availability()` and fall back to a hosted model.

### Gaps
- No sourced figures found for MediaPipe LLM Inference, Piper TTS, Apple Foundation Models framework (on-device ~3B), Web Speech API quality, or phone-side inference. Prior knowledge suggests the Web Speech API (`SpeechRecognition`) works in Chrome but sends audio to Google servers, and that Apple's Foundation Models framework needs iOS/macOS 26 and Swift. Both are unverified here.
- No controlled WebLLM vs Transformers.js comparison on the same hardware.

## 3. Free realtime voice, telephony and WhatsApp

### Takeaway
A live voice agent is feasible in 8 hours by combining:
- a framework: Pipecat for phone/own transport, LiveKit Agents for WebRTC rooms
- either a speech-to-speech model (Gemini Live, which has a free tier) or a cascade of Groq Whisper → fast LLM → TTS

Free phone numbers come from the Twilio trial (about $15 credit plus one number, unverified) or LiveKit Cloud's free Build plan (1,000 agent-minutes/month plus one US number).

### Cited Findings
- **Choosing a framework:** Pipecat for phone or your own transport; LiveKit Agents for WebRTC, multi-party or video. Some teams run Pipecat logic on LiveKit transport — [forasoft](https://www.forasoft.com/blog/article/pipecat-vs-livekit-agents)
- **Latency:**
  - A speech-to-speech model takes about 300 ms. An STT+LLM+TTS cascade adds 300–800 ms — [forasoft](https://www.forasoft.com/blog/article/pipecat-vs-livekit-agents)
  - Production target is 450–600 ms end to end — [cekura](https://www.cekura.ai/blogs/livekit-agents)
  - A Twilio call can reach about 500 ms with parts of the pipeline running locally — [cerebrium](https://cerebrium.ai/docs/v4/examples/twilio-voice-agent)
- **LiveKit Cloud Build (free):** 1,000 agent-session minutes/month, LiveKit Inference credits, and one US local phone number — [futureagi](https://futureagi.com/blog/livekit-alternatives-2026/)
- **Twilio trial:** one free number plus $15 credit for new accounts. This comes from a hackathon resource page and is unverified against Twilio — [mintlify hackathon resources](https://www.mintlify.com/azlan18/Hackathon-Resources/resources/voice-comms)
- **Gemini Live API:**
  - Has a free tier with prototyping-level rate limits. Paid 3.1 Flash Live costs about $0.005/min of audio input and $0.018/min of audio output — [makerstack](https://makerstack.co/reviews/gemini-flash-live-review/); [rywalker](https://rywalker.com/research/gemini-live-api)
  - One source mentions a shared allowance of 5,000 Search-grounding requests/month, unverified — [tokenkarma](https://tokenkarma.app/blog/gemini-live-api-pricing-voice-agents-2026/)
  - Some articles name unverified model versions ("3.8 Live") — [apidog](https://apidog.com/blog/gemini-3-8-live-api/)
- **WhatsApp voice:** voice calls via Pipecat need a WhatsApp Cloud API number with calls enabled (example uses Kapso) — [kapso docs](https://docs.kapso.ai/docs/build-voice-agents/quickstart)

### Inferences
- The most impressive cheap demo is a judge calling a real number from their own phone. A free path: LiveKit Cloud phone number, or Twilio trial plus Pipecat, with Gemini Live (free) or Groq Whisper + Cerebras/Groq LLM + Kokoro/Cartesia TTS.
- Twilio trial accounts usually can only call verified numbers and play a trial message (prior knowledge, unverified). Pre-verify the judges' or demo phones, or use LiveKit's number.

### Gaps
- Could not confirm Meta WhatsApp Cloud API test-number terms (historically a free test number that can message up to 5 verified recipients; unverified here).
- OpenAI Realtime API pricing and any free tier were not found.

## 4. Free infrastructure (database, hosting, realtime/multiplayer)

### Takeaway
Free tiers are far more generous than a one-day demo needs:
- **Supabase:** Postgres, auth, storage and realtime.
- **Cloudflare:** Workers, D1 and Durable Objects. Durable Objects are now on the free plan with SQLite storage, which makes them ideal for multiplayer rooms.
- **Liveblocks:** drop-in CRDT multiplayer.

The main gotchas are Supabase pausing after one week of inactivity and Cloudflare's 10 ms CPU limit per request on the free plan.

### Cited Findings
- **Supabase free:**
  - 2 projects per organization, 500 MB Postgres per project, 50K monthly active users (auth). Projects pause after one week of inactivity — [jetadmin](https://www.jetadmin.io/blog/supabase-pricing-2026-guide-to-plans-limits-and-real-world-costs/); [automationatlas](https://automationatlas.io/answers/supabase-free-tier-limits-2026/)
  - Storage and egress figures conflict (500 MB–1 GB storage; 5 GB bandwidth) — [activepieces](https://www.activepieces.com/blog/supabase-pricing-free-tier-limits-pro-costs-egress.md)
- **Cloudflare Workers free:** 100,000 requests/day at 10 ms CPU per invocation — [Cloudflare Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)
- **Durable Objects free:** 100K requests/day, 13,000 GB-s/day, 50M SQL rows read/day, 100K rows written/day, 5 GB stored. Exceeding a limit causes errors until the 00:00 UTC reset — [Cloudflare plans](https://www.cloudflare.com/plans.md)
- **D1 free:** 5 GB storage, 5M rows read/day, 100K rows written/day — [Cloudflare plans](https://www.cloudflare.com/plans.md)
- **Liveblocks Free:** 500 monthly active rooms, unlimited MAU, 10 simultaneous connections per room, 256 MB realtime storage (10 MB per room), 512 MB file storage, hard caps. Some older pages show a 100-MAU Starter plan, which looks outdated — [Liveblocks limits](https://liveblocks.io/docs/pricing/limits); [Liveblocks Free plan](https://liveblocks.io/docs/pricing/plans/free)

### Inferences
- Multiplayer state is cheap: use Yjs plus Liveblocks, or Durable Objects with WebSockets (PartyKit is now part of Cloudflare). The 10-connections-per-room cap on Liveblocks is fine for a live demo but not for "everyone in the audience joins".
- Create the Supabase project on the day, or ping it, to avoid the pause.

### Gaps
- MongoDB Atlas M0, Vercel Hobby and GitHub Actions free minutes were not verified. Prior knowledge (unverified): Atlas M0 = 512 MB; Vercel Hobby is non-commercial; GitHub Actions is unlimited on public repos and about 2,000 min/month on private repos.
- PartyKit's current standalone status was not verified.

## 5. AI coding and app-building tools

### Takeaway
Hard evidence on speedups is mixed:
- METR's 2025 RCT found experienced developers 19% slower on mature codebases, while they believed they were 20% faster.
- A 2026 follow-up leans toward a speedup but is statistically inconclusive.

For greenfield hackathon code (the case those studies didn't measure), agentic tools such as Claude Code, Cursor, Lovable and v0 likely compress scaffolding and UI a lot. But free tiers of app builders are tiny (Lovable 5 credits/day, v0 $5/month), so teams should not rely on them as the main engine.

### Cited Findings
- **METR 2025 RCT:** 16 experienced open-source developers, 246 tasks, mature repositories, Feb–Jun 2025 tools. They were 19% slower with AI yet self-estimated 20% faster — [scienceblog](https://scienceblog.com/t-a-randomized-trial-by-metr-found-that-experienced-developers-completed-real-coding-tasks-19-slower-when-allowed-to-use-ai-tools-yet-afterwards-they-estimated-on-average-that-ai-had-made-them-20-fast/); [eWeek](https://eweek.com/news/news-ai-tools-slow-developer-productivity-study)
- **2026 follow-up** (secondary sources): 57 developers, 143 repos, more than 800 tasks.
  - Returning developers: estimated -18% (CI -38% to +9%), which likely means less time taken, i.e. a speedup. New developers: -4% (CI -15% to +9%).
  - METR flagged selection bias and labels the original result "historical" — [codercops](https://blog.codercops.com/blog/ai-coding-productivity-2x-not-10x-metr-2026); [urandom](https://urandom.io/blog/2026-03-01-ai-made-developers-slower-then-december-happened)
- **App-builder free tiers:**
  - Lovable: 5 credits/day, about 30/month — [dupple](https://dupple.com/learn/best-free-vibe-coding-tools); [dotsquares](https://dotsquares.com/press-and-events/tech/lovable-pricing-guide-pros-cons-alternatives)
  - v0: $5/month of credits (one source says about 7 messages/day) — [toolhalla](https://toolhalla.ai/blog/bolt-new-vs-lovable-vs-replit-vs-v0-2026)
  - Bolt: 150K–300K tokens/day, conflicting, with a 1M/month ceiling — [hostadvice](https://hostadvice.com/ai-app-builders/lovable-vs-bolt-vs-replit/)
  - Replit Starter: "daily Agent credits", effort-based, no fixed number found — [create.xyz](https://www.create.xyz/blog/lovable-vs-bolt-vs-v0-vs-replit)
- **Claude Code GitHub Actions:**
  - Setup: run `/install-github-app` from the CLI; needs repo admin; the app gets read/write on Contents, Issues and PRs. An `@claude` mention on an issue or PR then implements changes and opens PRs — [Claude Code docs](https://code.claude.com/docs/en/github-actions)
  - Gotchas: fork PRs can't read secrets; bot comments don't re-trigger workflows — [ocdevel](https://ocdevel.com/podcaster/claude-code/f9b6bfe0-a75a-4dc7-8270-97d741fe192e)

### Inferences
- Realistic 8-hour pattern: one person uses Lovable or v0 for the UI shell (burning free credits early), while the others drive Claude Code or Cursor on the backend. Use the fast free LLM APIs for the product's own inference.
- AI tools are weakest at debugging integrations (OAuth, webhooks, telephony, WebRTC, CORS). Budget human time there.

### Gaps
- Claude Code / Cursor student or free plan terms were not verified.
- No rigorous hackathon-specific speedup data was found.

## 6. Browser agents, computer use, and MCP as distribution

### Takeaway
Use plain Playwright for known paths (most reliable), Stagehand for mixed deterministic and natural-language steps, and Browser Use for open-ended goals (most impressive, least predictable). MCP is now a real distribution channel:
- Claude's directory lists more than 950 MCP servers.
- MCP Apps (in-chat interactive UI) are supported by both Claude and ChatGPT.

So "ship the product as an MCP server or app" is a cheap and credible go-to-market story.

### Cited Findings
- **Layers:** Stagehand is for code-owned AI actions, Playwright for deterministic automation, and Playwright MCP gives an existing agent browser tools. (Author Skyvern is a competing vendor.) — [skyvern](https://www.skyvern.com/blog/browser-use-vs-stagehand-which-is-better/)
- **Reliability:**
  - Browser Use's observe-act loop is flexible but unpredictable. Stagehand v3 (early 2026) is described as "significantly more reliable" (author opinion) — [alexcloudstar](https://alexcloudstar.com/blog/ai-browser-agent-stagehand-browser-use-playwright/)
  - Unsourced figure: AI automation 85–95% reliable vs 99%+ for Playwright selectors — [pkgpulse](https://www.pkgpulse.com/guides/stagehand-vs-playwright-ai-vs-browser-use-ai-web-2026)
  - Browser Use scores 89.1% on WebVoyager, but on a 586-task subset, so it is not directly comparable to other tools — [skyvern alternatives](https://www.skyvern.com/blog/browser-use-alternatives/)
- **Claude connectors directory:** more than 950 MCP servers. MCP Apps (charts, maps, forms in chat) and Tasks ship under a versioned extensions framework (MCP spec 2026-07-28). The directory is vetted by Anthropic — [Claude blog](https://claude.com/de/blog/bringing-mcp-2026-07-28-to-claude); [Claude connectors docs](https://claude.com/docs/connectors/overview)
- **Local servers:** servers on npm/PyPI can't be listed in the directory directly. Package them as MCPB (Desktop Extensions) or inside a plugin — [Claude connectors docs](https://claude.com/docs/connectors/overview)
- **Cross-platform:** Anthropic and OpenAI both announced MCP Apps support (reported as Jan 26 2026, secondary source). One MCP codebase can target both ChatGPT's app directory and Claude — [workos](https://workos.com/blog/building-mcp-apps-inside-claude-chatgpt); [manufact](https://manufact.com/blog/distribute-mcp-server-across-directories)

### Inferences
- An MCP server is about 100–300 lines with the official SDKs and can be demoed inside Claude or ChatGPT in minutes. That makes the "agent-native product" pitch cheap.
- For live demos, script the browser agent's path with Playwright or Stagehand plus a recorded fallback video. Fully autonomous Browser Use runs can fail on stage.

### Gaps
- Directory review timelines (getting listed within a hackathon is unlikely; local or custom connectors work immediately) were not verified.
- No sourced data on Anthropic or OpenAI computer-use API free access.

## 7. Capability combinations that are cheap to demo but impressive

### Takeaway
Each of these combinations is now mostly glue code on free tiers:
- **Agent opens a real PR:** Claude Code GitHub App, `@claude` on an issue.
- **Live phone-call voice agent:** LiveKit or Twilio trial plus Gemini Live or a Groq/Cerebras cascade.
- **Private in-browser inference:** Transformers.js/WebLLM plus Kokoro plus Whisper.
- **Multiplayer state:** Liveblocks or Durable Objects plus Yjs.
- **Product delivered as an MCP App** inside Claude or ChatGPT.
- **Near-instant LLM UX:** Cerebras or Groq at very high tok/s.

### Cited Findings
- **PR agent:** the `@claude` mention creates PRs and implements features once the GitHub app is installed — [Claude Code docs](https://code.claude.com/docs/en/github-actions)
- **Phone voice agent:** LiveKit free plan includes a phone number and 1,000 agent-minutes — [futureagi](https://futureagi.com/blog/livekit-alternatives-2026/). Cascade latency is about 500 ms achievable — [cerebrium](https://cerebrium.ai/docs/v4/examples/twilio-voice-agent)
- **In-browser stack:** about 60 tok/s for a 20B model on a high-end Mac; Kokoro faster than real time — [transformers.js releases](https://github.com/huggingface/transformers.js/releases); [voicechanger](https://voicechanger.live/text-to-speech/benchmarks)
- **Multiplayer:** Liveblocks 500 rooms free; Durable Objects 100K requests/day free — [Liveblocks](https://liveblocks.io/docs/pricing/limits); [Cloudflare plans](https://www.cloudflare.com/plans.md)
- **MCP Apps:** in-chat UI in Claude and ChatGPT — [Claude blog](https://claude.com/de/blog/bringing-mcp-2026-07-28-to-claude)
- **Speed:** Cerebras about 2,000 tok/s — [morphllm](https://www.morphllm.com/cerebras-pricing)

### Inferences
- Since capabilities are cheap, the differentiator is the specific workflow or vertical plus a real user story, not the tech. Design around one "magic moment" that uses one or two of the combinations above. Avoid things that are still hard in 8 hours: custom model training, reliable autonomous web agents on arbitrary sites, production telephony compliance, and payments or KYC.
- The demo risks are rate limits, venue Wi-Fi and model downloads. Mitigate with multi-provider fallback, per-teammate API keys, pre-cached models and a recorded backup video.

### Gaps
- No 2025–2026 hackathon post-mortems with quantified build-time data were found within the search budget.
