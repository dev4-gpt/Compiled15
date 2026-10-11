# Track 3: AI for the Aging Population, MVP: ScamShield

**Score:** 8.17 weighted, 7.15 risk-adjusted, **rank 2 of 6 (backup project)**.
**One-liner:** A guard for older adults' calls and messages. It recognizes scam scripts as they happen (fake grandchild, IRS, tech support, romance, gift cards), steps in with a calm voice prompt, and alerts a trusted family circle before any money moves.

## 1. Thesis

Older adults lose billions of dollars a year to fraud, according to the FBI IC3 Elder Fraud reports; check the latest figure before quoting it. Losses keep rising as AI voice cloning makes scams more convincing. Existing protection works at the network level (carrier spam labels) or after the fact (bank fraud teams). Nothing listens to the conversation itself, with consent, and steps in at the moment of persuasion. Seniors also get the most from a family circle that hears about trouble without taking away their independence. That is the useful part of CareCircle.

## 2. Candidates considered

| Concept | Risk-adj | Verdict |
|---|---|---|
| **ScamShield**, live scam interception + family circle | 7.15 | **Chosen**: most visceral demo of all 18, clear buyers (banks, carriers, families), no medical claims |
| CareCircle, daily voice check-in | Gated out (G2) | Med and confusion flags drift into medical territory. Its family-circle alert UI is reused here |
| MedMinder, medication reminder calls | Gated out (G2) | Crowded and regulated |

## 3. User, buyer, wedge

- **User:** adults 70+, living independently.
- **Payer:** adult children (consumer subscription, $10-15/month); later banks and credit unions (cutting fraud reimbursements) and carriers (bundled add-on).
- **Wedge:** spam filters judge the caller ID. ScamShield judges what is being said, the script, and responds the way a trusted grandchild would.

## 4. MVP scope

- **In:** live call simulation over WebRTC (or a Twilio number); streaming transcription; a scam-pattern detector (LLM + rule features: urgency, secrecy, payment method, authority claim, unusual payment rails); risk score over time; in-call whisper intervention ("This sounds like a known scam. Hang up and call Sarah."); SMS screening; family-circle alert with transcript snippet; senior-friendly UI.
- **Out:** carrier integration, recording without consent (always announce), automatic call blocking.

## 5. End-to-end architecture

```
 Senior's phone / browser call
      │ audio stream (consented, announced)
      ▼
 Streaming ASR (Deepgram / faster-whisper) ──► rolling transcript
                                                   │
                     ┌─────────────────────────────┼────────────────────────┐
                     ▼                             ▼                        ▼
         Rule features (gift card,      LLM scam classifier         Known-script similarity
         wire, crypto, secrecy,         (tactic labels + why)        (embeddings vs scam corpus)
         urgency, authority)
                     └──────────────┬──────────────┴────────────────────────┘
                                    ▼
                        Risk score (0-100) with hysteresis
                     ┌──────────────┼──────────────────┐
                 > 60 ▼          > 80 ▼                  ▼ always
         Gentle whisper to      Family alert (SMS /     Timeline + evidence
         senior (TTS)           push) with transcript    (MongoDB)
```

## 6. Data model

- `seniors {id, name, trusted_contacts[], consent_at, language}`
- `calls {senior_id, started_at, transcript[], risk_series[], tactics[], outcome}`
- `alerts {call_id, level, sent_to[], snippet, acknowledged_by, ts}`
- `scam_corpus {script_id, type, text, embedding}` (built from FTC/AARP public scam descriptions and role-play scripts)

## 7. Stack and resources

| Need | Choice | Resource |
|---|---|---|
| Real-time voice pipeline | Pipecat or LiveKit Agents | `pipecat-ai/pipecat`, `livekit/agents` |
| Telephony (optional) | Twilio Voice + Media Streams | Twilio docs |
| ASR | Deepgram streaming or faster-whisper | `SYSTRAN/faster-whisper` |
| Classifier | Luminal LLM + rule features + embeddings | Hugging Face connector for a sentence-embedding model |
| Family app | Next.js PWA, big-type senior view + family view | Lovable for the first UI pass, Vercel deploy |
| Storage | MongoDB Atlas | sponsor |
| Eval set | 20 scripted calls (12 scam types + 8 benign look-alikes: real bank call, pharmacy refill, grandchild asking for a ride) | Written tonight; 6 held out |

## 8. Eight-hour build plan

| Time | A (voice) | B (detection) | C (alerts + data) | D (UI, pitch, validation) | Done when |
|---|---|---|---|---|---|
| 12:00-1:00 | Browser call + streaming ASR | Tactic taxonomy + rule features | Mongo schema, alert sender (SMS) | Script set, wireframes | Live transcript on screen |
| 1:00-2:30 | TTS whisper injection | LLM classifier with reasons | Family timeline API | Senior + family views | Classifier labels 8 dev scripts |
| 2:30-3:30 | Latency tuning | Risk score with hysteresis | Alert levels and dedupe | Call senior centers / AARP chapter | **Checkpoint:** scam call triggers whisper + family SMS |
| 3:30-4:30 | Twilio phone number (stretch) | Embedding similarity to corpus | False-positive dashboard | Live risk meter UI | Benign calls stay green |
| 4:30-5:30 | Hardening | Held-out 6 scripts run once | Metrics table | Deck | Precision/recall table |
| 5:30-6:45 | Bug bash, backup video | | | Rehearse | **Code freeze 6:45** |

**Fallback:** if streaming voice is unreliable, analyze transcribed chunks every 5 s. The live risk meter and family alert still work.

## 9. 90-second demo

A teammate plays "grandson in jail, need $2,000 in gift cards, don't tell mom". The risk meter climbs as each tactic is labeled (urgency → secrecy → gift card). At 80, a calm voice whispers to the "grandmother" and a judge's phone (the family member) gets an SMS with the snippet. Then a benign pharmacy call stays green. End on held-out precision and recall and time-to-alert.

## 10. Metrics

- Detection recall on held-out scam scripts, false-positive rate on benign look-alikes.
- Time from first scam tactic to alert (target under 20 s).
- Senior comprehension of the whisper (tested with 2-3 older adults if reachable).

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Privacy and wiretap laws | Opt-in by the senior, announced on every call, on-device ASR on the roadmap; demo uses consented role-play |
| False positives annoy seniors | Hysteresis, two-level response (whisper before alert), benign look-alike eval |
| "Carriers already do this" | Carriers label numbers; we read the script, which catches spoofed and new numbers |

## 12. Validation and next 30 days

- **At the event:** ask judges and attendees "has a parent or grandparent been targeted?" (most say yes); 1 commitment to install for a parent; contact a State College senior center (the Bloomerang nonprofit angle).
- **Days 1-30:** 10 families in a beta, using the app for SMS and email screening first (lower legal risk than calls); talk to 2 credit unions about co-marketing.
