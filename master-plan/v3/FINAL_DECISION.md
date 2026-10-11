# Final decision (v3)

**Build and sell Fieldwork in Track 2.** Fieldwork produces a consultant-grade diagnostic from a donor export or a sales export.
- Stack these prizes on it: **Bloomerang** (DonorPulse practice and API), **MongoDB** (Atlas store) and **AWS** (deploy).
- Run the analyst on **Luminal** if the endpoint works.
- **Backup:** MigrateLoop in Track 1. Switch only if the team ends up with no seller, or if check-in shows that Track 2 sales can't count.

## Honest score
- **Today: 7.92 weighted, 6.02 final. This does not meet the 8.0 bar, and we are not rounding it up.**
- No idea in the list reaches 8.0 on current evidence (`v3/scoring/RESULTS.md`).
- Fieldwork ranks first in 81.7% of the 20,000 runs with shifted weights.
- Fieldwork loses first place only if its chance of making a sale falls below 0.51.

What would honestly lift it above 8: proof captured at the event, and nothing else.

| Evidence captured at the event | Criteria change | New weighted |
|---|---|---|
| First paid diagnostic from a real organization, on its own export | E 8→9, V 8→9 | 8.26 |
| ...plus 3+ organizations in the room booked or paid | U 7→8 | **8.36** |
| ...plus a Bloomerang customer connected through the API live | S 8→9 | 8.46 |

So the bar is crossed by **selling**, which is also how Track 2 is judged. After each change, re-run `python3 master-plan/scoring/score.py --config master-plan/v3/scoring/scores_v3.yaml` with the new scores and their evidence, such as receipt IDs.

## Why Fieldwork
1. **Track 2 offers about twice Track 1's money** ($5k AWS + $3k Engineering Entrepreneurship + $2k Bloomerang, vs $3k/$1.5k/$500), and it rewards selling, which is the team's strength.
2. **It is consulting capability as a product.** A small-business consultant charges about $75/hr, and a one-time engagement averages about $399. A fractional development director costs thousands a month. Fieldwork delivers the same diagnostic in about a minute for $49, with every number traceable. Consulting firms can also buy it to run their own client diagnostics.
3. **It closes a gap Bloomerang has publicly signaled.** Retention is Bloomerang's core message. Its AI (Penny, in beta) serves only its own customers, and Dataro starts around $25k/yr for 10k+ donor files. Fieldwork serves the 200-2,000-donor nonprofit with any CRM, and makes non-customers a Bloomerang lead.
4. **It is already built.**
   - The prototype passes 10 tests and runs end to end: upload, metrics, grounded report, deck and PDF.
   - The validator blocks any number that isn't in the evidence, which is the answer to "isn't this just a wrapper?".
5. **Two kinds of buyer** (nonprofits and small businesses) raise the chance of at least one sale before 7 PM.

## Switch rules
| At check-in | Do |
|---|---|
| Track 2 confirmed; selling to local organizations counts | Go: Fieldwork (follow `prototype/fieldwork/RUNBOOK.md`) |
| Track 2 counts attendees only | Sell the $5 "Fieldwork for your club or side business" tier to student orgs (clubs export their donor or sales sheets); same code |
| Track 2 doesn't exist, or sales don't count | MigrateLoop in Track 1 (v2 plan) |
| Bloomerang staff offer a demo API key | Show the live API pull; add evidence to criterion S |

## Not verified
The event rules, prize pools and judge affiliations come from search extracts and the user's list. The Bloomerang API details come from third-party write-ups, and there is no sandbox. The FEP benchmark is from an extract. Confirm all of these before putting them on a slide.
