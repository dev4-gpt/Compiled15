# Bloomerang + nonprofit fundraising demand — research note (c0mpiled-15, Penn State, Oct 11 2026)

**Method caveat:** I did this research only with WebSearch on 2026-10-11. WebFetch failed with DNS errors (`ENOTFOUND bloomerang.com / bloomerang.co`), so I never opened a primary page. Every claim below comes from search-engine extracts of the cited URL. Exact numbers should be re-checked on the page before anyone puts them on a slide.
Confidence: **H** = an official or primary source's extract states it clearly. **M** = a single credible secondary source, or extracts that agree. **L** = third-party aggregators that disagree, or a source with unclear provenance. **INF** = my inference, not a sourced fact.

---

## 1. Bloomerang: product, customers, pricing, AI strategy

### Facts
- **What it sells:** A donor-management CRM plus a "Giving Platform" for small and mid-sized nonprofits. The modules are Bloomerang CRM, Bloomerang Fundraising (online giving, from the Qgiv acquisition) and Bloomerang Volunteer (from InitLive). **M**: https://bloomerang.com/about , https://www.capterra.com/p/131207/Bloomerang/pricing
- **Acquisitions:** InitLive in 2023, which became Volunteer Management. Qgiv in 2024, which expanded the giving platform. **M**: https://bloomerang.com/about
- **Customer count:** More than 10,000 customers in 2021 and more than 13,000 in 2022, from the company timeline (**M**, https://bloomerang.com/about). Dataro's July 2026 post says the integration reaches "more than 24,000 nonprofits" (**M**, https://dataro.io/blog/dataro-bloomerang-integration). That figure likely includes Qgiv customers (**INF**).
- **Pricing (L, aggregators disagree):**
  - CRM from about $125/mo billed annually. Fundraising add-on from about $40/mo, which must be bundled with CRM. Volunteer from about $119/mo.
  - Price scales with the number of constituent records, and every plan includes unlimited users.
  - Some listings show a $79 or $99 "Starter" tier, and one example runs from $99/mo at 500 donors to $299/mo at 10k.
  - A CostBench changelog says the top plan dropped from $300 to $125/mo on Feb 4, 2026.
  - Sources: https://www.capterra.com/p/131207/Bloomerang/pricing , https://costbench.com/changelog/bloomerang-price-decrease-2026-02/ , https://erpresearch.com/erp-add-ons/nonprofit/bloomerang/pricing , https://toolradar.com/tools/bloomerang/pricing
  - I found no "Standard Plus" tier in any source.
- **Engagement Level (built in):**
  - Uses a proprietary formula developed with Dr. Adrian Sargeant.
  - Positive inputs: consecutive-year giving, year-over-year increases, membership, events, volunteering, and email opens and clicks.
  - Negative inputs: lapsed status, year-over-year decreases, and email unsubscribes.
  - Levels: Cold, Cool, Warm, Hot, On Fire.
  - **H**: https://help.bloomerang.com/en/articles/12632614-how-is-engagement-level-calculated-and-what-does-it-tell-me
- **Generosity Score:**
  - A DonorSearch wealth and philanthropy rating (wealth markers, real estate, philanthropic history), given free on every constituent.
  - Bloomerang does not compute it from its own data.
  - **H**: https://bloomerang.com/news/generosity-score , https://help.bloomerang.com/en/articles/12632736-about-the-constituent-summary

### AI timeline, 2025–2026
| Date | Item | What it does | Source | Conf |
|---|---|---|---|---|
| Mar 31, 2026 | **Penny**, "AI fundraising strategist" (beta) | Answers natural-language questions over the org's full donor history, e.g. "Who gave last year but not this year?". Recommends strategy and drafts campaign content. Tagline: "Penny suggests. Your team decides." Available in beta to all Giving Platform customers. | https://bloomerang.com/news/bloomerang-penny-ai-fundraising-strategist-nonprofits , https://thenonprofittimes.com/npt_articles/bloomerang-launches-ai-strategist-penny/ , https://bloomerang.com/ai | H |
| May 18 / Jun 10, 2026 (GiveCon) | **Dataro partnership**, not an acquisition. Terms undisclosed. | Predictive donor scores on each record, daily recommended actions, and on-demand AI prospect research. Dataro says it went live **Jul 1, 2026** on "select plans". | https://bloomerang.com/blog/dataro-partners-with-bloomerang , https://dataro.io/blog/dataro-bloomerang-integration , https://thenonprofittimes.com/npt_articles/bloomerang-adds-dataro-predictive-ability-to-giving-platform/ , https://aijourn.com/?p=541952 | H/M |
| 2026 | Conversational reporting | Natural-language report generation. A roundup said it was in alpha with GA "this summer". I could not confirm that it shipped. | https://www.cuspera.com/products/bloomerang-x-883/news | L |
| ongoing | AI Content Assistant in the email editor | Writing help at no extra cost. Reportedly it does not read CRM data, only the text the user types. | https://www.usecarly.com/blog/bloomerang-ai/ | M |
| policy | "Never uses customer data to train models" | — | https://bloomerang.com/features/ai/ | H |

- **Marketing claims about Penny:** Up to 47% cumulative revenue growth and retention 2.5x the industry average. One testimonial: the Joe Nuxhall Miracle League raised $2.25M. These are vendor claims and are not verified (**M**, see the Penny news link above).
- **"Bloomerang Intelligence":** No source uses this name (**gap**). The AI brand names that do exist are **Penny** and the Dataro-powered predictive scores.
- **"Bloomerang Labs":** No public page found (**gap**). **INF:** It is probably an internal R&D or innovation group that has not been publicly branded.

### What Bloomerang says the hard problem is
- **Donor retention is the core brand thesis.** Bloomerang's long-running pitch, quoting Sargeant: "Improving donor retention by just 10% can double the lifetime value of your donor database." Some Bloomerang material instead says 10 points of retention raises LTV by "150–200%". **H**, but these are vendor numbers: https://bloomerang.com/blog/donor-retention-math-made-simple , https://bloomerang.co/results/eaf/
  - The worked example assumes 5,000 donors, a $200 average gift, and retention moving from 41% to 51%.
  - A third party re-ran the same example and got +56% total dollars, not 200%: https://nonprofithub.org/fundraising/donor-retention-math-made-simple/ (**M**)
- **Staff turnover:** Bloomerang has run webinars on it, e.g. "Employee turnover: the one thing keeping your nonprofit stuck" (https://bloomerang.com/webinar/video-employee-turnover-the-one-thing-keeping-your-nonprofit-stuck , **M**). Its Sustainable Giving Report with Qgiv (290+ nonprofits, 2,000 donors) frames the issue as burnout (https://bloomerang.com/?p=114873 , **M**).
- **Giving Signals Report 2026** (May 19, 2026; 1,000+ donors, 405 fundraisers). **M**: https://bloomerang.com/resources/giving-signals-report-2026
  - 97% of donors give because they care about their community.
  - 79% are motivated when contacted through their preferred channel.
  - 75% of Millennials expect to give more this year.
  - The report's six "signals" are trust, motivation, Millennials, need, friction, and proof.
- **INF:** For a pitch, the Bloomerang-native framing is "retention, made actionable by a lean or turning-over staff." Penny already answers the "who lapsed" question, so a team should differentiate on *action plus outcome* rather than on querying alone.

---

## 2. Bloomerang REST API v2

| Item | Finding | Source | Conf |
|---|---|---|---|
| Base URL | `https://api.bloomerang.co/v2` | https://jentic.com/apis/bloomerang | M |
| Auth (private key) | Header **`X-API-KEY: <key>`**. Keys are generated under user menu → Edit My User → "API Key v2.0" → Generate. A private key gives full read/write access and is for server-to-server use only, never in browser forms. | https://docs.nexla.com/user-guides/connectors/bloomerang_api/bloomerang_api_data_source , https://help.bloomerang.com/en/articles/12632849-generate-and-deactivate-private-api-keys , https://lp.datablend.com/knowledge/bloomerang-credentials , https://bloomerang.com/developers | M (the header name comes only from Nexla) |
| Auth (OAuth) | Authorization-code flow. Token endpoint `https://api.bloomerang.com/v2/oauth/token`. `token_type` is "Bearer". | https://bloomerang.com/api/oauth-reference-guide | H |
| v1 | Deprecated. It used the key as a Basic-auth-style username. | https://bloomerang.com/api/rest-api-v1 | M |
| Endpoints | `GET /constituents`, `GET /constituents/search`, `POST /constituent` (singular for create), `POST /transaction`, plus transactions, interactions, funds, campaigns, appeals, households, notes, and others. The chiperific gem says it covers "most" endpoints except processor, user, and wallet item. | https://docs.nexla.com/user-guides/connectors/bloomerang_api/bloomerang_api_data_source , https://jentic.com/apis/bloomerang , https://github.com/chiperific/bloomerang , https://www.cozyroc.com/node/9925 | M |
| Interactions | Pipedream has "new interaction" triggers and "add interaction" actions, so the API supports both reading and writing interactions. | https://pipedream.com/apps/bloomerang/integrations/oto | M |
| Engagement or Generosity via API | **Gap.** I found no confirmation that the API returns engagement level or generosity score. The CSV export explicitly *excludes* engagement scores. | https://help.bloomerang.com/en/articles/12632641-export-bloomerang-data | M |
| Pagination | `skip` / `take`, with `take` defaulting to 50 | https://apis.io/rate-limits/bloomerang/bloomerang-rate-limits/ | M |
| Rate limits | No published numeric limits. Back off and retry on HTTP 429. | same as above | L-M |
| Sandbox | **None.** The gem README says Bloomerang has no sandbox and that POST, PUT and DELETE calls hit live production data. | https://github.com/chiperific/bloomerang | M |
| Swagger | v2 docs and Swagger UI are linked from bloomerang.co/features/integrations/api/rest-api | https://rollout.com/integration-guides/bloomerang/api-essentials | M |

- **CSV export:**
  - Run from Organization settings. It produces a ZIP with one CSV per entity: Constituents, Transactions, Donations, Addresses, Emails, Phones, Households.
  - The export *excludes* Groups, engagement scores, and email or letter templates.
  - **H**: https://help.bloomerang.com/en/articles/12632641-export-bloomerang-data
- **Column names: GAP.** No extract listed the exact headers. What the import docs say:
  - Donation imports require **Date (MM/DD/YY or MM/DD/YYYY), Amount, Fund**.
  - Campaign and Appeal are optional and must already exist in the database.
  - Matching uses **Account Number**, or else name plus email or address.
  - Files must be CSV, at most 10,000 rows or 2 MB.
  - **H**: https://bloomerang.co/wp-content/uploads/2025/01/Import-Basics-1_14_25.pdf , https://help.bloomerang.com/en/articles/12632768-what-are-the-required-fields-for-an-import
- **INF:** A demo should accept flexible headers such as `Account Number`, `First Name`, `Last Name`, `Email`, `Date`, `Amount`, `Fund`, `Campaign`, `Appeal`, and map them with fuzzy matching. With no sandbox, use a read-only key against a demo account, or CSV upload. Because engagement scores are not in the export, a team would need to recompute its own engagement or retention score, which is an opening for the product.

---

## 3. Demand evidence

### Donor retention (Fundraising Effectiveness Project, AFP)
| Period | Key numbers | Source | Conf |
|---|---|---|---|
| FY2025 (Q4 2025 report) | Overall retention **43.3%** (up from 43.1%). Donor count **down 3.6%** in 2025, continuing a decline since 2021. Dollars **up about 5.0%**, with most of the growth in Q4. New-donor retention roughly flat. | https://afpglobal.org/news/fundraising-effectiveness-project-reports-strongest-revenue-growth-five-years-even-fewer | H |
| Q1 2026 (year-to-date) | 3.2M donors, $3.5B, 15,700 orgs. Dollars **up 4.3%** YoY, donors **down 0.8%**. Year-to-date retention about **18%**, with **new-donor retention 7.1%** and **repeat 25.8%**. Retention fell in the Small, Midsize, Major and Supersize segments; micro donors were lowest at 10.0%. AFP: "retention tells a more cautionary story." | https://afpglobal.org/news/fundraising-effectiveness-project-reports-easing-donor-losses-q1-2026-new-data-shows-growth , https://www.nonprofitpro.com/article/repeat-and-recaptured-donors-power-growth-on-a-shrinking-donor-base-new-data-shows/ | H |
| Q2 2026 | **Not found** (gap). FEP also changed its methodology in 2026: https://ministrywatch.com/fewer-donors-more-dollars-and-methodology-changes-at-fep/ | — | — |

Note that the Q1 retention figures are year-to-date and cannot be compared with the full-year 43%.

### Cost of losing donors
- Acquiring a donor costs about **7x** as much as retaining one. This is a Blackbaud analyst figure cited in an Academic Impressions paper. **M**: https://www.academicimpressions.com/wp-content/uploads/2017/07/4-Pillars-of-Donor-Relations-Sample.pdf
- New-donor acquisition costs **50–100% more than the dollars it raises**. **M**: https://prizmah.org/sites/default/files/2021-03/Donor%20retention%20toolkit-compressed.pdf
- Charities lost 103 donors for every 100 they gained (2014 FEP). **H**, but old: https://www.philanthropy.com/news/charities-lost-103-donors-for-every-100-they-gained-in-2014-says-study/
- Retention +10 points doubles database LTV. This is Bloomerang/Sargeant marketing, covered in section 1. **M**

### Fundraiser tenure and turnover
- **16 months:** average fundraiser tenure. Replacement costs **$127,650** direct plus indirect. Source is a Chronicle of Philanthropy article from April 2012, cited secondhand. **M** (old, and I did not see the original): https://www.philanthropy.com/news/revolving-door-dilemma/ , https://philanthropydaily.com/shutting-door-development-turnover/
- Replacement costs **65–83% of salary**, from Penelope Burk's research. Losing one high performer costs about **$952K** over 3 years. **M**: https://www.philanthropy.com/news/how-charities-can-curb-turnover-among-fund-raisers/
- DickersonBakker: **63%** of orgs had turnover in the last 2–3 years, with the highest rates at small orgs, and **85%** struggle to hire. **M**, date unclear: https://ministrywatch.com/lack-of-qualified-fundraiser-staff-could-threaten-u-s-nonprofits-new-report-warns/
- **Gap:** No source found for "16–18 months" specifically for *development directors*. The 16-month figure covers fundraisers in general.

### Consultant pricing (anchor for a "sell during hackathon" price)
- **Hourly rates:**
  - $100–$300/hr. **M**: https://callhub.io/blog/fundraising/fundraising-consultant-advantages/
  - $75–$250/hr. **M**: https://givebutter.com/blog/nonprofit-consulting
  - $125–$250/hr for experienced independents. **L-M**: https://financialmodelslab.com/blogs/business-insights/nonprofit-fundraising-consultancy
- **Project fees:** $5k–$50k for plans, campaigns, or donor research. **M**: callhub link above
- **Gap:** I found no published price for a "donor data audit" or "retention audit" specifically.
- **INF:** A $99–$499 self-serve retention audit, or a $50–$150/mo tool, sits far below consultant pricing and around Bloomerang's own $125/mo CRM entry price.

### Market size
- About **1.5M** US nonprofits, with about 1.3M of them charitable. **M**: https://thenonprofittimes.com/?p=57957
- **Most nonprofits are very small.** **M**
  - Most 501(c)(3)s have budgets under $50k: https://candid.org/blogs/data-insights-very-small-nonprofits-make-up-majority-us-nonprofits/
  - 88% have budgets under $500k (National Council of Nonprofits, 2019). One source says 66.9% excluding organizations under the filing threshold.
- **State College metro (about Centre County):** About **1,160** organizations, with **290** reporting revenue under $250k. These are CauseIQ figures and may include non-501(c)(3)s. **L-M**: https://causeiq.com/directory/state-college-pa-metro/
  - Local anchors: Centre County Community Foundation, Centre County United Way, Centre County PAWS: https://nonprofitscan.com/org/251215290/centre-county-united-way
- **AI adoption among nonprofits:** **M**
  - Virtuous 2026 report (346 orgs): 92% use AI, but only 7% report major mission gains. https://virtuous.org/blog/the-2026-nonprofit-ai-adoption-report-blog/
  - Another report: 76% use AI, only 9% feel ready, and small orgs lack data infrastructure. https://faunalytics.org/bridging-the-gap-between-ai-interest-and-readiness/
  - UK: about 80% of small charities do not use AI, and 56% cite a lack of skills. https://www.thirdsector.co.uk/nearly-80-per-cent-small-charities-not-using-ai-research-finds/digital/article/1917640

---

## 4. Competitive landscape: AI donor analytics

| Product | What it does | Price signal | Gap for small nonprofits | Source | Conf |
|---|---|---|---|---|---|
| **Bloomerang (Penny + Dataro)** | Natural-language Q&A over donor data, strategy recommendations, predictive scores, daily actions, prospect research | Penny is beta for all Giving Platform customers. Dataro is on "select plans". | Requires being a Bloomerang customer. Dataro features are tier-gated. | see section 1 | H/M |
| **Dataro** (standalone) | ML propensity scores (likelihood to give, upgrade, or lapse) and next-best-action | Vendor pricing: platform fee plus about $0.12–$0.14 per active donor. Mid tier from about **$25k/yr**. Essentials targets **10k–250k active donors**. Some directories list $250/mo, which I could not verify. | Built for orgs with 10k+ donors, so out of reach for orgs with <1k donors | https://dataro.io/pricing/ , https://us.fitgap.com/products/033403/dataro | M |
| **DonorSearch** (incl. AI) | Wealth and philanthropy screening and prospect scoring from public records, real estate, SEC filings | Contact sales | Answers "who could give", not "who is about to lapse". It already powers Bloomerang's Generosity Score. | https://toolradar.com/tools/donorsearch/alternatives | M |
| **Gravyty (Raise)** | AI-drafted outreach and stewardship for gift officers, mainly in higher ed and advancement | Contact sales | Built for major-gift officer teams | https://gravyty.com/using-ai-to-find-reach-steward-donors-in-a-meaningful-way , https://gravyty.com/blog/raise-gravyty-vs-momentum-donor-engagement-software/ | M |
| **Momentum** (givemomentum; may now be connected to Virtuous) | Daily inbox shortlist of donors to contact, AI drafts in the org's own voice, and recommended channel and message | Sales call only. Virtuous CRM starts at **$199/mo**. | Price and onboarding effort | https://givemomentum.com/ , https://givemomentum.com/sign-up , https://aitoolsbakery.com/blog/virtuous-crm-review/ | M/L (the Virtuous relationship is unconfirmed) |
| **Fundraise Up** | AI optimization of donation forms (amounts, frequency, real-time testing) | **4%** platform fee per transaction on self-managed accounts, with no subscription | Focused on conversion, not CRM-side retention analytics | https://fundraiseup.com/docs/platform-basics/ , https://techcrunch.com/2025/01/23/fundraise-up-claims-its-ai-can-boost-nonprofit-donations | H |
| **Givebutter** | Free fundraising and CRM with segments (New, Recurring, Retained) and a paid "Plus" tier for automation and reporting | Free plus tips, or Plus | No predictive or AI retention scoring found | https://givebutter.com/blog/can-givebutter-replace-my-crm | M |

**INF: what small nonprofits still lack.**
1. **Predictive retention at small scale.** Dataro's models target orgs with 10k+ donors. Orgs with 200–2,000 donors are poorly served.
2. **Explainable, action-ready output.** Teams need a plain-English *why* plus a drafted ask, not just a score.
3. **Continuity when staff turn over.** Institutional knowledge leaves with a 16-month-tenure development director.
4. **Data hygiene before AI.** Duplicates, missing emails, lapsed fields, and unknown gift dates.
5. **Proof of ROI.** "These 37 lapsing donors equal $X at risk."

Bloomerang's Penny covers some of #1 and #2 inside Bloomerang. A tool that sits *on top of* a Bloomerang export or API and outputs "$ at risk, with drafted outreach" complements it rather than competing with it.

---

## 5. Het Sheth
- Het Sheth organized **"c0mpiled-6/pennstate"**, a sprint hackathon on Feb 27, 2026, 4–11 pm, in the Engineering Design and Innovation Building. **H**: https://news.engr.psu.edu/2026/sheth-het-eship-hackathon.aspx , https://www.psu.edu/news/engineering/story/engineering-entrepreneurship-program-host-sprint-hackathon-feb-27
  - Run by Penn State's Engineering Entrepreneurship (E-SHIP) program in SEDI, with Transpose Platform, a San Francisco VC firm.
  - Co-organized with Ishaan Narang, with support from professors Ted Graef and Brad Groznik.
  - Theme: "AI for Productivity and Research."
  - Het was a **CS senior**, a **3-time hackathon winner** (including Cal Hacks and c0mpiled-1), and was forming the **"Builders Collective at Penn State."**
- **c0mpiled series context:** Transpose runs numbered c0mpiled hackathons tied to YC Request for Startups themes. c0mpiled-11 and c0mpiled-13 were held in SF in July 2026, and there were Tokyo and Osaka editions. **M**: https://luma.com/olys436o , https://resemom.jp/release/prtimes/20260806/202927.html
- **Gaps:**
  - No public source links Het Sheth to Bloomerang or "Bloomerang Labs" (searches for "Het Sheth" Bloomerang returned nothing).
  - No public page for c0mpiled-15 or for Bloomerang's Track 2. The user's brief is the only source for "Labs @ Bloomerang".
- **INF:**
  - He values hands-on shipping and AI-for-productivity, with a builder and hackathon-winner orientation.
  - In a "sell during the hackathon" track, expect him to reward real users or LOIs and a live demo on real-looking Bloomerang data over slides.

---

## Gaps and next checks
1. FEP Q2 2026 numbers. Check https://afpglobal.org/fep or the FEP dashboard directly.
2. Exact Bloomerang CSV export column headers. Get them from a demo export or the import templates.
3. Whether the API exposes engagement level or generosity score.
4. Official current Bloomerang pricing page, since the aggregators conflict.
5. Whether conversational reporting has reached GA.
6. Any "Bloomerang Intelligence" or "Bloomerang Labs" branding.
7. Het Sheth's role at Bloomerang.
8. A sourced "development director tenure 16–18 months" figure. Current evidence is the 2012 figure of 16 months for fundraisers in general.
9. Published pricing for a donor-data or retention audit.
10. An IRS BMF count of 501(c)(3)s for Centre County. The EO BMF CSV for PA can be filtered by ZIP 168xx.
