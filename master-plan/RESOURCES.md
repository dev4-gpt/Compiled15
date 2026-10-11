# Resources: Repos, Tools, Skills, Connectors

Open-source repos and services each MVP builds on. Check the license and the last-commit date before adopting any repo.

## 1. Shared across all projects

| Need | Resource | Notes |
|---|---|---|
| LLM (sponsor) | Luminal OpenAI-compatible endpoint (DeepSeek, GLM Flash) | Swap endpoint via `LLM_BASE_URL` env var |
| LLM fallback | Claude API (`claude-api` skill in this session) | Structured outputs, tool use |
| Database (sponsor) | MongoDB Atlas, free cluster plus student credits; Atlas Vector Search | All six data models fit document collections |
| Alt DB / realtime / auth | Supabase (connector available in this session) | Realtime channels for WarRoom |
| UI scaffolding | Lovable (connector available) | Generate the first dashboard pass, then pull the code into the repo |
| Deploy | Vercel (connector available), AWS App Runner (sponsor story) | |
| Models and datasets | Hugging Face (connector available, user `dev4-gpt`) | Embeddings, ASR, OCR, VLMs |
| Notes and interviews | Notion (connector available) | Mirror `validation/interviews.md` if the team prefers |
| Team comms | Slack (connector available) | WarRoom can mirror timelines to Slack |
| Browser testing / bots | Playwright + Chromium (preinstalled here) | HumanPass bot farm, UI smoke tests |
| Code hosting | `dev4-gpt/Compiled15` (this repo) | Each MVP gets its own repo on build day |

## 2. Per track

### Track 1: WarRoom (Multiplayer AI)
- `yjs/yjs`: CRDT shared state
- `liveblocks/liveblocks`: presence, rooms, comments
- `cloudflare/partykit`: realtime rooms on the edge
- `tldraw/tldraw`: reference for multiplayer UX
- `vercel/ai`: streaming agent UI

### Track 2: DocSaathi (Consumer 1B)
- `PaddlePaddle/PaddleOCR`, `naptha/tesseract.js`: OCR
- `openai/whisper`, `SYSTRAN/faster-whisper`: ASR
- `rhasspy/piper`: offline TTS
- `ggml-org/llama.cpp`, `mlc-ai/web-llm`: on-device models
- Twilio WhatsApp Sandbox, Meta WhatsApp Cloud API

### Track 3: ScamShield (Aging)
- `pipecat-ai/pipecat`, `livekit/agents`: real-time voice agents
- Twilio Voice Media Streams: phone audio
- FTC Consumer Sentinel and FBI IC3 Elder Fraud reports: scam taxonomy and statistics
- AARP Fraud Watch Network: public scam scripts for the eval corpus

### Track 4: RegDiff + LicenseLoop (Compliance)
- `docling-project/docling`, `Unstructured-IO/unstructured`: document parsing
- Federal Register API, eCFR API: federal sources
- State regulator bulletin pages, CSBS, NMLS public resource center: licensing context
- `open-policy-agent/opa`: rules-as-code reference for the roadmap

### Track 5: DriftFix (Self-Maintaining APIs)
- `oasdiff/oasdiff`, `OpenAPITools/openapi-diff`: OpenAPI breaking-change detection
- `Instagram/LibCST`: Python codemods
- `ast-grep/ast-grep`, `semgrep/semgrep`: structural search across languages
- `stoplightio/prism`: mock server from an OpenAPI spec
- `PyGithub/PyGithub`: PR creation
- `stripe/openapi`, `twilio/twilio-oai`, `github/rest-api-description`: real spec histories to replay
- `renovatebot/renovate`, `dependabot/dependabot-core`: the comparison point in the pitch

### Track 6: HumanPass (Proving Human)
- `MasterKale/SimpleWebAuthn`, `duo-labs/py_webauthn`: passkeys
- RFC 9474 (RSA blind signatures), RFC 9576-9578 (Privacy Pass)
- `google-ai-edge/mediapipe`: face landmarks for liveness
- `semaphore-protocol/semaphore`, `privacy-scaling-explorations/anon-aadhaar`, `selfxyz/self`: ZK personhood roadmap
- World ID docs, Cloudflare Turnstile: comparison points

## 3. Skills and process tools

- `python3 master-plan/scoring/score.py`: re-score after any evidence change.
- `validation/interviews.md`: one row per conversation; feeds the C and M scores.
- Claude Code skills available here: `claude-api` (LLM integration), `run` (launch and screenshot the app), `code-review` / `security-review` (pre-freeze review), `dataviz` (metrics charts for the demo).
