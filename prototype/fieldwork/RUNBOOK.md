# Fieldwork: build-day runbook (c0mpiled-15, Track 2)

**Goal by 7:00 PM:** at least one paid diagnostic delivered to a real organization, run on its own export. Better: three or more. Bring receipts, the buyer's quote, and the deck itself, shown with permission or redacted.

## Roles (works with 2 people; add people top to bottom)
| Role | 2 people | 3-5 people |
|---|---|---|
| **Seller** (lead): finds buyers, runs diagnostics on the spot, collects payment and quotes | Person 1 | Person 1 (+ person 4 as second seller) |
| **Builder**: deploys, sets up keys, fixes import problems on real files, polishes the deck | Person 2 | Person 2 |
| **Bloomerang and sponsors**: live API pull, MongoDB and AWS story, sponsor prize submissions | Person 2 | Person 3 |
| **Pitch**: slides, demo video, rehearsal | Both, from 5:30 | Person 5 |

## Schedule (6 hours)
| Time | Seller | Builder | Done when |
|---|---|---|---|
| H+0:00-0:30 | Ask Builder's Collective and organizers which local businesses and nonprofits are attending. Confirm whether selling to locals or attendees counts and which payment methods count | Deploy (AWS App Runner, or a laptop plus a tunnel). Set `LLM_*` (Luminal first, Groq fallback), `MONGODB_URI`, `PAYMENT_LINK` (Stripe live link, $49) and `ADMIN_TOKEN` | Public URL works; `/health` shows the store and LLM providers |
| 0:30-2:00 | **Sell.** Pitch below. Get a real export from each prospect (Square Item Sales CSV, Shopify Orders, Bloomerang export or Givebutter CSV). Run it in front of them | Watch the logs. Fix column aliases for any new export format within 10 minutes (`engine/ingest.py`). Add a test for each new format | First real run on a real file |
| 2:00-3:30 | Close the first sale. Record a 20-second quote | Bloomerang: ask staff for a demo key; show `POST /engagements/bloomerang` | **Checkpoint: one payment, or a written commitment** |
| 3:30-5:00 | Second and third buyers. Call or DM nonprofits from the CauseIQ State College list (290 under $250k revenue) and local shops near campus | Polish the deck wording on real outputs. Raise LLM quality and keep the validator at zero violations | Three or more engagements stored in Atlas |
| 5:00-5:45 | Collect receipts and quotes | Record the backup demo video. Freeze the code | Code freeze |
| 5:45-7:00 | Rehearse the 3-minute pitch. Submit to Track 2, the Bloomerang pool, MongoDB and AWS | | Submitted |

**If there is no sale by 3:30:** cut the price to $19, offer "pay what it was worth" after delivery, and pivot to student clubs and side businesses (any club with a dues or donation sheet). Do not change the product.

## Sales pitch (30 seconds)
> "Consultants charge about $75 an hour, and a one-off diagnostic averages around $400. Send me your Square / Shopify / Bloomerang export and in about a minute you get the same diagnostic: what's growing, what's slipping, the top three moves with owners and dates, and, for nonprofits, the list of lapsed donors to call first with the letters already drafted. Every number links to your own data. It's $49 today. If it doesn't tell you something you didn't know, don't pay."

**Exports to ask for:**
- Square: Reports → Item Sales → Export (item detail)
- Shopify: Orders → Export → CSV
- Bloomerang: Data Export, or an API key with read access
- Givebutter or a spreadsheet: any file with donor, date and amount

## Judge pitch (3 minutes)
1. **Receipts first.** Show the number of organizations, payments and a buyer quote.
2. **Live run.** Upload a real file (with permission) or a synthetic one, clearly labeled. Walk through the deck to the appendix: "every number has a formula; the AI can't invent one". Show `evidence.json`.
3. **Why now and who pays.** Show consultant pricing against a $49 price, and FEP donor retention data. For Bloomerang: we complement Penny, reach nonprofits not yet on Bloomerang, and every audit is a Bloomerang lead.
4. **Stack.**
   - MongoDB Atlas holds the audit trail.
   - The analyst runs on Luminal.
   - Deployed on AWS.
   - Optional: an AGI-0 agent pulls exports from back offices with no API.
5. **Ask and next step.** Pilot with Centre County nonprofits through the Chamber and SBDC.

## Fallbacks
| Failure | Fallback |
|---|---|
| LLM down or rate-limited | The template analyst runs automatically; reports stay fully grounded |
| MongoDB unreachable | In-memory store (automatic); say so |
| PDF rendering fails | Open the HTML deck and print to PDF from the browser |
| Unknown export format | Error lists the columns found. Add an alias in `engine/ingest.py`, plus a test |
| Stripe live mode not activated | Accept Venmo or Zelle and log it with `mark-paid`. Confirm with organizers that it counts |
