# Track 2: AI Consumer Products for 1B People, MVP: DocSaathi

**Score:** 7.52 weighted, 6.39 risk-adjusted, rank 5 of 6.
**One-liner:** A WhatsApp assistant you send a photo or voice note to. It explains any bill, government letter, form or prescription label in your language, by voice, and then does the next step: a reminder, a reply draft or filling in the form.

## 1. Thesis

The next billion AI users will not install an AI app or type prompts. They are on low-end Android phones, use WhatsApp, prefer voice, often read their own language better than English, and deal with paperwork written in formal English or bureaucratic language. Reaching a billion people means meeting them in the app they already use, with voice in and voice out, and making the AI do something useful, not just chat.

## 2. Candidates considered

| Concept | Risk-adj | Verdict |
|---|---|---|
| **DocSaathi**, document explainer and doer on WhatsApp | 6.39 | **Chosen**: universal pain, voice-first, clear action loop |
| VoiceLedger, shopkeeper voice bookkeeping | 5.82 | Strong market but hard to validate at a US event; keep as a vertical expansion |
| LabelLens, label photo to explanation | Gated out (G2, G4) | Medical-label advice is a regulated claim; its OCR-to-explanation pipeline is reused here |

## 3. User, buyer, wedge

- **User:** adults in India, Indonesia, Nigeria, Brazil, plus immigrants in the US who get letters in a language they don't read well.
- **Who pays:** freemium consumer (₹49-99/month premium for form filling), plus B2B2C: fintechs, telcos and NGOs that pay to reduce support calls. In the US, immigrant-serving nonprofits, which fits the Bloomerang nonprofit prize.
- **Wedge:** general chatbots answer questions; DocSaathi takes a document and returns a decision and an action (due date, amount, what to sign, what to reply), in voice, in your language, inside WhatsApp.

## 4. MVP scope

- **In:** WhatsApp sandbox (Twilio or Meta Cloud API) or a WhatsApp-styled web fallback; image in, voice note in; OCR + LLM structured extraction (type, issuer, amount, due date, required action); voice answer in 4 languages (Hindi, Spanish, English, plus one more); reminder scheduling; reply-letter draft.
- **Out:** payments, government portal submission, identity documents.

## 5. End-to-end architecture

```
WhatsApp user ──photo / voice note──► Webhook (FastAPI)
                                         │
                ┌────────────────────────┼─────────────────────────┐
                ▼                        ▼                         ▼
        OCR (PaddleOCR /         ASR (Whisper /              Language ID
        Tesseract / VLM)         faster-whisper)
                └──────────────┬─────────┴─────────────────────────┘
                               ▼
                 LLM structured extraction (JSON schema:
                 doc_type, issuer, amount, due_date, action, risk_flags)
                               ▼
                 Action engine: reminder │ reply draft │ checklist
                               ▼
                 Answer composer (simple language, user's language)
                               ▼
                 TTS (Piper / cloud TTS) ──voice note + text──► WhatsApp
                               │
                       MongoDB: users, documents, actions
```

## 6. Data model

- `users {wa_id, language, created_at}`
- `documents {user, media_url, ocr_text, doc_type, fields{}, confidence, created_at}`
- `actions {document_id, type: reminder|reply|checklist, due_at, status}`
- `messages {user, direction, modality, text, audio_url, ts}`

## 7. Stack and resources

| Need | Choice | Resource |
|---|---|---|
| Messaging | Twilio WhatsApp Sandbox (fastest) or Meta WhatsApp Cloud API | Twilio docs; web fallback built in Lovable |
| OCR | PaddleOCR or a vision-language model | `PaddlePaddle/PaddleOCR`, `naptha/tesseract.js`; Hugging Face connector to pick a VLM |
| ASR | Whisper / faster-whisper | `openai/whisper`, `SYSTRAN/faster-whisper` |
| TTS | Piper (offline) or cloud TTS | `rhasspy/piper` |
| LLM | Luminal-hosted open model; small on-device model for the on-device AI prize | `ggml-org/llama.cpp`, `mlc-ai/web-llm` |
| Storage | MongoDB Atlas | sponsor |
| Test docs | 12 synthetic documents: utility bill, tax notice, school letter, bank SMS, rental notice, benefits form | Created tonight, 4 kept as held-out |

## 8. Eight-hour build plan

| Time | A (channel) | B (understanding) | C (actions + voice) | D (UI, validation) | Done when |
|---|---|---|---|---|---|
| 12:00-1:00 | Twilio sandbox webhook echo | OCR on 3 docs | TTS + ASR smoke test | Doc set, pitch outline | Photo in, text out on WhatsApp |
| 1:00-2:30 | Media download, session state | JSON extraction schema + prompt | Answer composer, 2 languages | Web fallback chat UI | Bill explained correctly |
| 2:30-3:30 | Voice-note in/out loop | Accuracy script over 8 dev docs | Reminder + reply draft | Interview 3 non-native speakers | **Checkpoint:** voice question about a photo gets a voice answer |
| 3:30-4:30 | Language auto-detect | Risk flags (scam letter, late fee) | 4 languages | Before/after demo docs | Full loop in 4 languages |
| 4:30-5:30 | Hardening | Held-out docs run once | Dashboard of extracted fields | Deck | Field accuracy table |
| 5:30-6:45 | Bug bash, backup video | | | Rehearse | **Code freeze 6:45** |

**Fallback:** if WhatsApp sandbox approval or media fails, run the same backend behind the WhatsApp-styled web UI and say so.

## 9. 90-second demo

Teammate photographs a confusing utility shut-off notice and sends a Hindi voice note: "What is this, what do I do?" A voice note answers in Hindi with the amount, the deadline and what happens if unpaid, then offers a reminder and a reply draft. Switch to a Spanish school letter. End on the field-accuracy table on held-out documents.

## 10. Metrics

- Field extraction accuracy (amount, due date, action) on 4 held-out docs.
- End-to-end latency from photo to voice answer (target under 15 s).
- Comprehension check: user correctly states amount and deadline after hearing the answer (test with 3 people at the event).

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Wrong amount or date said confidently | Show the source crop; low-confidence fields are read back as questions |
| Legal or medical advice | Scope to explaining and organizing; no advice on prescriptions; banner "not legal advice" |
| Hard to validate with US judges | Frame the US immigrant use case; interview non-native speakers on site |

## 12. Validation and next 30 days

- **At the event:** 5 conversations with people whose parents receive letters in English; 1 nonprofit contact.
- **Days 1-30:** pilot with one immigrant-services nonprofit and one Indian WhatsApp community of 200 users; track weekly active senders and documents per user.
