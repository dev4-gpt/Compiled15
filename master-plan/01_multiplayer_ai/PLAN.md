# Track 1: Multiplayer AI, MVP: WarRoom

**Score:** 8.21 weighted, 6.98 risk-adjusted, rank 3 of 6 (see `../scoring/RESULTS.md`).
**One-liner:** One AI incident-response agent that a whole on-call team co-steers live. It proposes hypotheses, the team votes and approves, it runs the checks, and it writes the postmortem from the shared session.

## 1. Thesis

Today's AI tools are single-player: one person, one chat. Real work like incidents, launches and deal reviews happens in groups, under time pressure, with split authority. A multiplayer agent needs shared context, turn-taking, permissions, attribution and conflict resolution. Incident response is the sharpest wedge: everyone is in one channel anyway, minutes cost money, and the record (postmortem) is a required artifact.

## 2. Candidates considered

| Concept | Risk-adj | Verdict |
|---|---|---|
| **WarRoom**, multiplayer incident agent | 6.98 | **Chosen**: sharp workflow, measurable (time to root cause), clear buyer |
| Huddle, generic shared agent room | 6.48 | Same core, but reads as "just a UI" without a job to be done. WarRoom is Huddle with a wedge |
| PlanParty, group-chat trip planner | Gated out (G4) | No buyer; consumer group chats monetize poorly |

## 3. User, buyer, wedge

- **Users:** on-call engineers, incident commander, support lead (3-6 people per incident).
- **Buyer:** VP Eng / SRE lead at 50-500 engineer companies; budget line is already incident tooling (PagerDuty, incident.io, FireHydrant, Rootly).
- **Wedge vs incumbents:** incumbents add a single-user AI summary bot. WarRoom makes the agent a participant that several humans steer together, with an approval and voting model and full provenance (who asked it to do what).
- **Why now:** agents can now run real diagnostic tools; the bottleneck has moved from "can AI do it" to "how does a team safely direct it together".

## 4. MVP scope

- **In:** shared room (web), live agent plan, 3+ simultaneous users with roles (Commander, Responder, Observer), hypothesis cards with votes, approval gate for any tool call, read-only diagnostic tools against a seeded demo system (logs, metrics, recent deploys), timeline with attribution, one-click postmortem.
- **Out:** real PagerDuty/Slack integration (Slack mirror is a stretch), write actions in production, auth beyond magic links.

## 5. End-to-end architecture

```
 Phones/laptops (QR join)
        │  WebSocket (presence, cursors, votes)
        ▼
 ┌───────────────┐   events   ┌──────────────────┐   tool calls (approved only)   ┌───────────────────┐
 │ Room server   │◄──────────►│ Agent orchestrator│──────────────────────────────►│ Demo "Checkout"   │
 │ (Next.js +    │            │ plan / hypotheses │◄──────────────────────────────│ service: logs,    │
 │ Liveblocks or │            │ arbitration       │       results                 │ metrics, deploys  │
 │ Supabase RT)  │            └────────┬─────────┘                                └───────────────────┘
 └──────┬────────┘                     │ LLM (Luminal / Claude)
        │ append-only event log         ▼
        ▼                       Postmortem generator
   MongoDB / Postgres  ───────► timeline + attribution + action items
```

**Arbitration model (the core IP):**
1. Any member can submit an instruction ("check DB connections").
2. The agent turns instructions into hypothesis cards with an expected check and a cost.
3. Members vote; the Commander's approval is needed for any tool call; Observers can only comment.
4. Conflicting instructions are merged or ranked by votes × evidence; the agent explains why it picked one.
5. Every event (instruction, vote, tool call, result) is attributed and timestamped.

## 6. Data model

- `rooms {id, incident_title, severity, status, created_at}`
- `members {room_id, user, role, joined_at}`
- `events {room_id, ts, actor, type: instruction|vote|approval|tool_call|result|note, payload}`
- `hypotheses {room_id, text, proposed_by, votes[], status: open|confirmed|rejected, evidence[]}`
- `postmortems {room_id, summary, timeline[], root_cause, action_items[], generated_at}`

## 7. Stack and resources

| Need | Choice | Resource |
|---|---|---|
| Realtime presence and state | Liveblocks or Supabase Realtime (Yjs as fallback) | `yjs/yjs`, `liveblocks/liveblocks`, Supabase connector in this session |
| Front end | Next.js + Tailwind + shadcn/ui | Lovable connector for the first UI pass, Vercel connector to deploy |
| Agent | Tool-calling loop over an OpenAI-compatible endpoint | Luminal endpoint (sponsor); Claude API as fallback (`claude-api` skill) |
| Demo system | FastAPI "checkout" service with an injected fault (connection pool exhaustion after a deploy) | Seeded logs and metrics JSON |
| Storage | MongoDB Atlas (sponsor) or Supabase Postgres | `events` append-only collection |
| Optional chat mirror | Slack connector | Post the timeline into a channel |

## 8. Eight-hour build plan

| Time | A (realtime) | B (agent) | C (demo system + data) | D (UI, pitch, validation) | Done when |
|---|---|---|---|---|---|
| 12:00-1:00 | Room server, presence, QR join | LLM smoke test, tool schema | Fault-injected checkout service, logs/metrics endpoints | Wireframe, pitch outline | 3 phones in one room |
| 1:00-2:30 | Event log, votes, roles | Hypothesis generation from instructions | Deploy history + 3 tools (logs, metrics, deploys) | Room UI: timeline + cards | Agent proposes 3 hypotheses from a page |
| 2:30-3:30 | Approval gate wiring | Tool-calling loop behind approval | Ground-truth root cause + scoring script | Talk to 3 on-call engineers | **Checkpoint:** one approved tool call returns real data |
| 3:30-4:30 | Conflict merge view | Arbitration + explanations | Second scenario (held out) | Live agent stream UI | Full incident resolved in-room |
| 4:30-5:30 | Hardening, reconnects | Postmortem generator | Metrics: time to root cause, # tool calls | Postmortem view | Postmortem with attribution generated |
| 5:30-6:45 | Bug bash, deploy | Held-out scenario run once | Record backup video | 5-slide deck, rehearse | **Code freeze 6:45** |

**Fallback at 3:30:** if live tool calling is unreliable, the agent picks from a fixed menu of 6 diagnostic queries; the multiplayer arbitration stays real.

## 9. 90-second demo

0-10s: "Incidents are team sports; AI tools are single-player." 10-30s: judges scan a QR and join the room; a page fires. 30-60s: three people give conflicting instructions; the agent merges them into hypothesis cards; votes; Commander approves; logs show the bad deploy. 60-80s: postmortem appears with who-did-what. 80-90s: buyer and metric (time to root cause vs. a solo baseline).

## 10. Metrics

- Time to root cause: WarRoom team vs. one person with a chat assistant (same scenario, rehearsed).
- % of agent tool calls approved, and % rejected by vote (proves human control).
- Postmortem completeness vs. a template checklist (timeline, cause, impact, action items).
- Held-out scenario solved: yes/no.

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Looks like a chat UI | Lead with the arbitration and approval moment, not the chat |
| Conference Wi-Fi breaks realtime | Local hotspot; Supabase/Liveblocks reconnect; backup video |
| Agent picks the wrong tool | Approval gate means a wrong pick is just a rejected card, which is a feature to show |

## 12. Validation and next 30 days

- **At the event:** 5 engineers who have been on call; ask "walk me through your last incident"; get 1 "I'd try it on our next game day".
- **Days 1-30:** run 3 game days with design partners using their staging logs; integrate Slack and PagerDuty webhooks; price per seat for responders.
