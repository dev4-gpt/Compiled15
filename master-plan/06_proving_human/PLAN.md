# Track 6: Proving You're Human, MVP: HumanPass

**Score:** 7.80 weighted (fourth-highest of the six winners) but 6.04 risk-adjusted because p_success is only 0.55. Rank 6 of 6.
**One-liner:** Verify you are a real person once. After that, give any website an unlinkable "unique human" token that reveals nothing else about you, and hand your AI agents scoped, revocable tokens so a site can tell "a human's agent, within limits" from a bot farm.

## 1. Thesis

AI agents and generated media make CAPTCHAs and behavioral signals useless. Sites need to know two things: that a real, unique human is behind an account, and whether an agent is acting with a human's permission. The answer has to protect privacy. Sites should get a yes/no and a per-site pseudonym, never an identity. Everything needed exists separately: blind signatures and Privacy Pass, passkeys, liveness checks and zero-knowledge credentials. No consumer product combines them with delegation to agents.

## 2. Candidates considered

| Concept | Risk-adj | Verdict |
|---|---|---|
| **HumanPass**, unlinkable personhood tokens + agent delegation | 6.04 | **Chosen**: best RFS fit (10) and depth (9); hardest build |
| HumanProof, randomized liveness challenge | 5.07 | Arms race against deepfakes, and liveness alone doesn't prove uniqueness. Used inside HumanPass as the enrollment step |
| HumanMark, C2PA human-authored content | Gated out (G4) | No buyer today |

## 3. User, buyer, wedge

- **Buyer:** platforms losing to bots: ticketing, dating, marketplaces, social, free-trial abuse, airdrops. They pay per verification.
- **User:** anyone who wants to prove they're human without uploading an ID to every site.
- **Wedge vs World ID / ID verification vendors:** no special hardware or iris scan, and no identity documents shared with the site. The new part is first-class agent delegation: a human can say "this agent may buy 2 tickets on my behalf today".

## 4. MVP scope

- **In:** enrollment = passkey (WebAuthn) + randomized liveness challenge (MediaPipe face landmarks: follow a dot, turn head, read a random phrase); issuer signs a batch of blind tokens (RSA blind signatures, RFC 9474); per-site pseudonym = HMAC(user secret, site origin) so accounts can't be linked across sites; demo relying-party site with a "Verify human" button and a rate limit of one account per pseudonym; agent delegation token (scoped JWT signed by the user's passkey-bound key: site, actions, expiry, max uses), verified by the site; bot-farm simulator.
- **Out:** document-based uniqueness (passport NFC + ZK, e.g. anon-aadhaar or the Self/OpenPassport approach) is in the roadmap, not the MVP; production-grade anti-spoofing.

**Honest limit:** in the MVP, uniqueness only means one passkey and one live face per enrollment, plus device and rate signals. Say this on stage. Overclaiming security is this track's biggest risk.

## 5. End-to-end architecture

```
            ENROLL (once)                                   USE (every site)
User ──► Passkey create (WebAuthn) ─┐               Site "Verify human" ──► wallet page
     ──► Liveness challenge ────────┤                        │
          (MediaPipe, random steps) │                        ▼
                                    ▼               Present unblinded token + per-site pseudonym
                         Issuer: dedupe check ─►    Site verifies issuer signature (public key),
                         blind-sign N tokens        checks token not spent, pseudonym unique
                         (RFC 9474)                          │
                                    │                        ▼
                         Wallet (browser storage)    Account created ✓ / bot rejected ✗
                                    │
            DELEGATE                ▼
User ──► "Agent may buy ≤2 tickets on site X until 6pm" ──► delegation token signed by the user's key
Agent ──► presents delegation + human token ──► site enforces scope, logs "agent for human #pseudonym"
```

## 6. Data model

- Issuer: `enrollments {passkey_cred_id, liveness_score, device_signals, created_at}`; `issued {batch_id, count, ts}` (never stores which token went to whom)
- Site: `spent_tokens {token_hash}`, `accounts {pseudonym, created_at}`, `delegations {pseudonym, agent_id, scope, expires_at, uses}`
- Wallet (client): user secret, unblinded tokens, delegation keys

## 7. Stack and resources

| Need | Choice | Resource |
|---|---|---|
| Passkeys | SimpleWebAuthn (TS) or py_webauthn | `MasterKale/SimpleWebAuthn`, `duo-labs/py_webauthn` |
| Blind signatures | RFC 9474 RSA blind signatures | Cloudflare `blindrsa-ts`, Python `cryptography` primitives |
| Privacy Pass reference | Token issuance and redemption design | IETF Privacy Pass RFCs 9576-9578 |
| Liveness | MediaPipe Face Landmarker in browser | `google-ai-edge/mediapipe` |
| ZK roadmap | Semaphore, anon-aadhaar, Self | `semaphore-protocol/semaphore`, `privacy-scaling-explorations/anon-aadhaar`, `selfxyz/self` |
| Comparison points | World ID, Cloudflare Turnstile | `worldcoin/world-id-*` docs |
| Demo site + bot farm | Next.js + a Playwright script that spawns 50 sign-ups | Playwright preinstalled in this environment |

## 8. Eight-hour build plan

| Time | A (crypto) | B (enrollment) | C (relying party + agents) | D (UI, pitch, validation) | Done when |
|---|---|---|---|---|---|
| 12:00-1:00 | Blind sign/verify round-trip in tests | Passkey register/login | Demo ticketing site skeleton | Threat model page, pitch outline | Token verifies after unblinding |
| 1:00-2:30 | Issuer API, batch issuance, spent-token store | Liveness challenge (random steps) | "Verify human" flow + pseudonyms | Wallet UI | Human signs up with a token |
| 2:30-3:30 | Pseudonym derivation, unlinkability test | Dedupe + device signals | Bot-farm Playwright script | Talk to 3 people who run sign-ups | **Checkpoint:** 50 bots rejected, human accepted |
| 3:30-4:30 | Delegation token format + verify | Replay attack test (recorded video fails) | Agent buys 2 tickets within scope, 3rd refused | Live demo dashboard | Delegation works end-to-end |
| 4:30-5:30 | Security review of own claims | Hardening | Metrics | Deck incl. honest limits | Attack table |
| 5:30-6:45 | Bug bash, backup video | | | Rehearse | **Code freeze 6:45** |

**Fallback at 3:30:** drop liveness to a passkey-only enrollment and keep blind tokens + delegation. The privacy and agent story is still the novel part.

## 9. 90-second demo

A ticket drop opens and a bot farm script fires 50 sign-ups, all rejected. A judge enrolls with a passkey and a 5-second liveness check, then signs up. Show that two sites see two different pseudonyms for the same person. The judge tells their agent "buy 2 tickets". The agent's third purchase is refused because it is outside the delegated scope. End on the attack table: replayed video, token reuse, cross-site linking, scope escalation.

## 10. Metrics

- Bot rejection rate in the simulator (target 100% of naive bots) and human success rate (target 95%+ over 10 test users).
- Enrollment time (target under 30 s).
- Attack table: each attack attempted live, with result.

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Overclaimed security | State the limits on a slide; uniqueness via documents/ZK is roadmap |
| Crypto bugs under time pressure | Use RFC test vectors in the first hour; no custom primitives |
| Judges ask "why not World ID" | No hardware, no biometric template stored, agent delegation built in |

## 12. Validation and next 30 days

- **At the event:** organizers (they fight fake registrations), anyone running a marketplace or community.
- **Days 1-30:** add document-backed uniqueness via a ZK passport proof; pilot with a ticketing or community platform; SDK for the relying party.
