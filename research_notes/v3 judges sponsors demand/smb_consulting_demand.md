# Demand evidence: "consulting-firm-grade capability as an AI product" for SMBs and small consultancies

Prepared 2026-10-11 for c0mpiled-15 (State College, PA). Method: WebSearch only. WebFetch failed with DNS errors (`ENOTFOUND`) for doc.toasttab.com and help.shopify.com, so every claim below comes from search-result extracts, not full-page reads. Treat figures as "as quoted in the search extract." Most price figures come from vendor blogs and marketplaces, not neutral surveys.

Legend: **[F]** fact quoted from a source extract. **[I]** inference or synthesis by me. **[K]** model knowledge that I could not verify this session. Confidence: H / M / L.

---

## TL;DR for the pitch
- **Human equivalent is expensive.** A local consultant costs about $75/hr, or $95-$1,500 for a one-time engagement (avg $399). A fractional CFO costs $175-$500/hr or $3k-$15k/mo. A buy-side QoE on a small deal costs $5k-$35k. **[F, M]** So a $49-$499 one-time AI diagnostic is credibly 10-100x cheaper. **[I]**
- **The pain is real and measured.** Uneven cash flow affects 51% of employer firms. Rising costs affect 75% (Fed SBCS 2025, secondhand). 40% of restaurants say profitability is their #1 goal. 48% plan to raise menu prices (Toast 2025). **[F, M]**
- **The incumbents are free but stay inside one data source.** Square AI, ToastIQ, Shopify Sidekick and Intuit's agents each answer questions about their own data. None, as described, produces a cross-source, consultant-style written diagnostic with cited numbers that you can hand to a lender, buyer or board. **[I, M]**
- **The consulting-firm buyer exists.** About 9,586 BizBuySell-reported small-business sales in 2025 (median $350k). About 7,000 SBA 7(a) acquisition loans in FY2025. Record search-fund launches. Several AI-QoE startups (Provafi, shepi, Finsider, QoEAgent) confirm that investors see a market. **[F, M]**

---

## 1. SMB consulting prices, data use, and pains

### 1a. What human advisors charge
| Advisor | Price | Source | Conf. |
|---|---|---|---|
| General small-business consultant | avg **$75/hr**, range $45-$150/hr; one-time engagement **$95-$1,500, avg $399** | Thumbtack https://Thumbtack.com/p/small-business-consulting-fees | M [F] |
| Freelance functional consultants (N. America) | marketing $25-100/hr; accounting/bookkeeping $30-100; HR $35-175; IT security $40-140 | Upwork https://www.upwork.com/hire/business-consultants/cost/ | M [F] |
| Business coach | $150-$500/hr; most owners pay **$1,000-$5,000/mo**; new coaches $75-200/hr, senior $500-1,000/hr | Talo https://talo.com/costs/business-coach-cost | M [F] |
| Fractional CFO, hourly | **$175-$500/hr**; about $300/hr for an industry-experienced CFO | Zeni https://zeni.ai/blog/part-time-cfo-cost ; https://www.zeni.ai/blog/how-much-does-a-fractional-cfo-cost | M [F] |
| Fractional CFO, monthly | $3k-$12k/mo (Pilot); $3.5k-$5k/mo for $0.5-2M revenue firms (10-20 hrs) and $5k-$10k/mo for $2-10M (20-40 hrs) | Pilot https://pilot.com/blog/fractional-cfo-cost-guide ; SDO CPA https://sdocpa.com/fractional-cfo-cost-roi | M [F] |
| Low-end CFO / bundled options | BELAY from $350/mo; Zeni from $1,149/mo (bundles bookkeeping) | https://blog.belaysolutions.com/how-much-does-a-fractional-cfo-cost ; Zeni | M [F] |
| One-off "AI/automation" diagnostics already sold | $29 self-serve AI strategy report; $250 automation roadmap; $999 45-min "AI tools assessment" | https://hunted.space/product/ai-strategy-reports ; https://aveille.gumroad.com/l/wvrbab ; https://www.ai.joaoqueiros.com/blog/ai-tools-assessment-solo-consulting-corey-ganim | L [F] |

**Pricing anchors [I]:**
- A same-day "consultant-grade diagnostic" at **$99-$399** sits at or below Thumbtack's average one-time engagement ($399).
- It replaces roughly 1-3 hours of fractional-CFO time ($175-$1,500).
- The comparable products found ($29-$999) rely on questionnaires, not the owner's actual sales and accounting data.

### 1b. Do SMBs use their own (POS) data for decisions?
- **[F, L]** 79% of small businesses said they use "small data" reporting for decisions. Only **48% use sales trends** and **43% use sales receipts**. This is a Constant Contact survey of 1,200 SMBs from **Oct 2014**, so it is old. https://news.constantcontact.com/press-release-holiday-season-approaches-small-businesses-report-putting-small-data-good-use
- **[F, L]** 60% of SMBs use a web/cloud analytics system (Onepath 2020, small sample). https://www.techrepublic.com/article/small-businesses-are-using-more-analytics-to-survive-covid-19/
- **[F, M]** Strawhecker/North survey of 600+ POS decision makers: inventory management (65%) and reporting/analysis (48%) are among the POS features they value most. https://partners.north.com/blog/survey-smbs-value-inventory-employee-and-reporting-management-most-in-pos-systems
- **[F, M]** AI adoption among SMBs is contested:
  - NFIB: **24%** of owners use AI tools, and 21% at firms with single-digit headcount (dated Aug 2026 per the extract). https://getcoai.com/news/only-24-of-small-businesses-are-using-ai-tools-like-chatgpt-says-survey/
  - Thryv (vendor): 55% in 2025, up from 39%. https://www.businesswire.com/news/home/20250717239434/en/AI-Adoption-Among-Small
  - Fed note: about 18% of firms (Census data) at end-2025. https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html
- **Gap:** I found no recent, neutral statistic for "% of SMBs that use POS data for decisions." In a pitch, say "roughly half use sales-trend data (2014 survey)" and flag the date. **[I]**

### 1c. Most-cited SMB pains
- **[F, M] Fed Small Business Credit Survey, 2025 report (2024 data), employer firms**, as quoted by the Coleman Report:
  - rising costs of goods/services/wages **75%**
  - paying operating expenses **56%**
  - **uneven cash flow 51%**
  - weak sales **48%**
  - about 1/3 report trouble making loan payments on time

  I could not confirm the 51% against the Fed PDF itself. https://colemanreport.com/33-of-small-businesses-say-paying-debt-is-a-challenge-51-concerned-about-uneven-cash-flow/ ; report: https://fedsmallbusiness.org/-/media/project/clevelandfedtenant/fsbsite/reports/2025/2025-report-on-employer-firms.pdf
- **[F, H]** On FRED, **94-96%** of employer firms report at least one financial challenge (SBCS 2025, convenience sample). https://fred.stlouisfed.org/series/SBCSS10B2V1FRB
- **[F, M] NFIB "single most important problem"** (https://nfib.com/sbet):
  - taxes 18% (May 2025)
  - labor quality 21% (Aug 2025)
  - taxes 20% and inflation 12% (Dec 2025)
  - labor quality 19% and inflation 16% (Feb 2026, via Statista: https://www.statista.com/statistics/220371/single-most-important-problem-for-small-%20businesses-in-the-us/)
- **[F, M] Toast 2025 Voice of the Restaurant Industry** (712 operators, Apr-May 2025):
  - top pain points: inflation 20%, marketing 16%, sourcing/hiring 16%
  - 41% face moderate or extreme hiring challenges
  - responses: staff efficiency 47%, retention strategies 42%, **optimizing shift scheduling 39%**
  - **48% plan to raise menu prices**, 38% doing profit analysis, 31% changing suppliers
  - **40% say improving profitability is their top goal**

  https://pos.toasttab.com/blog/data/2025-voice-of-restaurant-industry-survey ; https://www.businesswire.com/news/home/20251009135658/en
- **[F, M] SCORE (value of advice):**
  - 55% of in-business mentoring clients reported revenue increases (PwC census survey of 15,282 clients, 2022). https://centralny.score.org/sites/default/files/2023-04/SCORE_Fact_Sheet_National-2022-FINAL%20%281%29.pdf
  - Growth rises with the number of mentor interactions: 30% after one interaction, 43% after five or more (2018). https://www.cpapracticeadvisor.com/small-business/news/12415443/business-mentoring-increases-small-business-survival-rates
- **Gap:** I found no strong quantitative source for "customer retention" as a ranked SMB pain. The closest are Toast's "marketing" at 16% and its retention-strategy figure (which refers to *staff* retention). **[I]**

**[I] Mapping pains to diagnostic modules:**

| Pain | Module | Evidence |
|---|---|---|
| Rising costs / inflation | Item margin and price-increase simulator | Toast 48% raising prices; SBCS 75% |
| Uneven cash flow | Daily/weekly revenue volatility and cash runway from POS + P&L | SBCS 51% |
| Labor | Sales-per-labor-hour by daypart; scheduling suggestions | Toast 39% optimizing schedules; NFIB labor quality ~20% |
| Weak sales | Item mix, dead SKUs, top-customer concentration | SBCS 48% |

---

## 2. Existing AI analytics for SMBs (so the pitch is not "Square AI again")

| Product | What it does (per sources) | Limits / gap (mostly [I]) |
|---|---|---|
| **Square AI** (US open beta mid-2025, free in Dashboard; AU and UK in 2026) | Natural-language Q&A over the seller's own Square sales, customers, staff and transactions. Answers questions like best sellers, voids, YoY, peak hours, with AI-generated charts. Oct 2025 update added web context (weather, events, news, reviews). "Tens of thousands" of sellers used it in the first 2 months. [F, H] https://squareup.com/us/en/press/square-ai-open-beta ; https://squareup.com/us/en/press/square-ai-beta-insights ; https://squareup.com/us/en/press/square-releases-ai ; https://www.pymnts.com/artificial-intelligence-2/2025/square-adds-conversational-ai-assistant-to-business-technology-platform/ | Data is Square-only (a beta tester called its focus "very specific and limited": https://community.squareup.com/t5/Reports-Setup-Management/Have-you-tried-Square-AI-yet/m-p/813237). It does not ingest QuickBooks P&L, rent or labor cost. It is reactive Q&A, not a written diagnostic. |
| **ToastIQ** (launched May 2025) | Server upsell prompts, guest "Digital Chits", "Shift at a Glance", AI marketing assistant, ad attribution. The current product page says it gets answers, uncovers insights and takes action. Draws on 130k+ locations. [F, H] https://www.businesswire.com/news/home/20250501039656/en/toast-launches-toastiq-to-superpower-the-future-of-restaurants ; https://pos.toasttab.com/au/products/toast-iq | Restaurant- and Toast-only. Operational nudges rather than a P&L-level strategy report. |
| **Shopify Sidekick** (free) | Natural-language analytics ("which 3 products have highest sales?"), content, and admin actions. Runs on Claude Sonnet via Google Cloud. Nearly 100M merchant conversations since Jan 2025. A reported "Pulse" feature surfaces up to 5 proactive recommendations (secondary source, unverified). [F, M] https://cloud.google.com/customers/shopify ; https://www.shopify.com/solutions/ai/enterprise ; https://www.chattergo.com/blog/shopify-sidekick-deep-dive-from-chatbot-to-agentic-copilot | Shopify-only. E-commerce focus, so no in-store POS or accounting cross-reference. |
| **Intuit Assist / QuickBooks AI agents** | Assist launched Sept 2023. Agents in 2025: Accounting, Payments, Customer, and a **Finance Agent** (KPI tracking, benchmarking, forecasting, scenario modeling, P&L / cash flow / balance-sheet summaries). Global rollout Nov 2025. [F, M] https://www.businesswire.com/news/home/20251114912265/en ; https://report.woodard.com/articles/intuit-launches-ai-agent-team-in-quickbooks-fpwr | Accounting-ledger view. It does not see item-level POS mix or daypart labor. **This is the closest threat**; differentiate on POS × P&L joins and on a one-time, consultant-style deliverable. |
| **Clover** | Built-in reporting (busiest times, best sellers). AI predictions come from third-party apps (Analytics BusinessQ, CorralData "chat with Clover data"). [F, M] https://www.clover.com/ca/pos-systems/business-tracking-reporting ; https://corraldata.com/integrations/clover | Fragmented across add-on apps. |
| **Fathom** (advisor tool) | Reporting and forecasting on top of Xero/QBO/MYOB. 50+ KPIs, from about $50/mo. Sold to accountants as a "client advisory" toolkit. Claims 80k+ businesses. [F, M] https://www.softwareadvice.com/product/456607-Fathom | Dashboards for accountants, not POS-aware. Shows that **accountants pay for advisory tooling**, which is a channel. |
| **Autymate** | QuickBooks analysis over 24+ months with peer comparison and dollar-amount fixes, aimed at accounting firms. [F, L] https://www.autymate.com/accounting-firm | Closest in concept, but QBO-only. |
| **Fiscal.ai** | Search shows an **equity investment research** platform (Trustpilot 4.5/24 reviews), **not** an SMB tool. [F, M] https://trustpilot.com/review/fiscal.ai | Not a competitor. Do not cite it as SMB analytics. |

**[I] White space to claim:**
1. **Cross-source joins.** Combine POS item sales (Square/Toast/Shopify) with the QuickBooks P&L. Examples: item gross margin after COGS, labor % by daypart, the dollar impact of a price change.
2. **Consultant output format.** Executive summary, 3-5 ranked recommendations, each with a **cited number from the uploaded file** (row and column provenance) and a dollar impact estimate.
3. **One-time, no-integration.** Upload CSVs and get a report in minutes. No subscription, no OAuth, and it works across POS vendors.
4. **Shareable artifact.** The report goes to a lender, a buyer, a partner or an advisor. The incumbents' chat answers are ephemeral and stay inside their own dashboards.

---

## 3. Export formats (for ingestion)

**Caveat:** Official doc pages could not be fetched. The lists below are partly confirmed by search extracts **[F]** and otherwise come from model knowledge **[K]**. The parser must be header-tolerant: match columns by fuzzy name, and fill down blank order-level fields.

### Square
- **Transactions CSV** (Sales > Transactions > Export > Transaction CSV). Confirmed [F, M] that it contains Date, Time, Gross Sales, Fees, Net Total, Transaction ID, Payment ID, Card Brand, PAN Suffix, Device Name, Staff Name, Event Type and Customer ID. https://sellercommunity.com/t5/General-Discussion/Exporting-ALL-data-from-reports/m-p/651847
  - [K] Other columns: Time Zone, Discounts, Service Charges, Net Sales, Gift Card Sales, Tax, Tip, Partial Refunds, Total Collected, Source, Card, Cash, Other Tender, Location, Dining Option, Customer Name, Description, Details, Channel.
- **Item Sales detail CSV** [K, M]: Date, Time, Time Zone, Category, Item, Qty, Price Point Name, SKU, Modifiers Applied, Gross Sales, Discounts, Net Sales, Tax, Transaction ID, Payment ID, Device Name, Notes, Details, Event Type, Location, Dining Option, Customer ID, Customer Name, Customer Reference ID, Unit, Count, Itemization Type, Channel.
  - The search confirmed that the item-detail file includes Gross Sales, Device Name, Event Type and Customer ID but lacks Net Total, Card Brand and PAN Suffix [F].
- **Item Sales summary (custom report)** [F, M]: Item Name, Item Variation, SKU, Category, Items Sold, Gross Sales, Items Refunded, Refunds, Discounts & Comps, Net Sales, Tax, Unit. https://community.squareup.com/t5/Square-Point-of-Sale/Exporting-only-selected-columns-in-a-custom-report/m-p/751939
- Note [F]: users merge the Transactions and Items CSVs themselves for QuickBooks import. https://community.squareup.com/t5/Payments-Troubleshooting/export-sales-report-as-a-excel-or-numbers-file/td-p/761161

### Shopify (Orders > Export, CSV)
- [F, H] Shopify defines these columns: **Financial Status, Paid at, Lineitem quantity, Lineitem price**, Payment References, Refunded Amount, Vendor, Outstanding Balance, Employee, Shipping Province / Shipping Province Name. https://help.shopify.com/en/manual/orders/export-orders
- [F, H] **Multi-item orders produce one row per line item, with order-level fields blank on the extra rows.** The parser must forward-fill by `Name`. Exports of 50 or fewer orders download directly; larger exports are emailed. The default CSV cannot be customized.
- [K, M] Full default header, approximately in order:
  - Order fields: Name, Email, Financial Status, Paid at, Fulfillment Status, Fulfilled at, Accepts Marketing, Currency, Subtotal, Shipping, Taxes, Total, Discount Code, Discount Amount, Shipping Method, Created at
  - Line-item fields: Lineitem quantity, Lineitem name, Lineitem price, Lineitem compare at price, Lineitem sku, Lineitem requires shipping, Lineitem taxable, Lineitem fulfillment status
  - Billing fields: Billing Name, Street, Address1, Address2, Company, City, Zip, Province, Country, Phone
  - Shipping fields: the same set as billing
  - Other fields: Notes, Note Attributes, Cancelled at, Payment Method, Payment Reference, Refunded Amount, Vendor, Outstanding Balance, Employee, Location, Device ID, Id, Tags, Risk Level, Source, Lineitem discount, Tax 1-5 Name/Value, Phone, Receipt Number, Duties, Billing Province Name, Shipping Province Name, Payment ID, Payment Terms Name, Next Payment Due At, Payment References

### Toast (Toast Web reports or automated nightly SFTP export)
- [F, H] Export types include OrderDetails, ItemSelectionDetails, ModifiersSelectionDetails and others. Nightly exports are generated after closeout (default 4:00 AM) for the previous business day. Columns are configurable, so the column order follows the Toast Web settings. https://support.toasttab.com/en/article/Automated-Nightly-Data-Export-1492723819691?lang=en_US ; field reference: https://doc.toasttab.com/doc/platformguide/adminDataExportFieldReference.html
- [F, M] ItemSelectionDetails includes order number, order-open timestamp, check ID and server. ModifiersSelectionDetails includes Location, Order Id, Order #, Sent Date and Void Reason ID.
- [K, M] **ItemSelectionDetails.csv**: Location, Order Id, Order #, Sent Date, Order Date, Check Id, Server, Table, Dining Area, Service, Dining Option, Item Selection Id, Item Id, Master Id, SKU, PLU, Menu Item, Menu Subgroup(s), Menu Group, Menu, Sales Category, Gross Price, Discount, Net Price, Qty, Tax, Void?, Deferred, Tax Exempt, Tax Inclusion Option, Dining Option Tax, Tab Name.
- [K, M] **OrderDetails.csv**: Location, Order Id, Order #, Checks, Opened, # of Guests, Tab Names, Server, Table, Revenue Center, Dining Area, Service, Dining Options, Discount Amount, Amount, Tax, Tip, Gratuity, Total, Voided, Paid, Closed, Duration (Opened to Paid), Order Source.
- Toast also has a TimeEntries export (labor hours and wages) [K]. It is useful for labor-% analysis.

### QuickBooks Online Profit & Loss
- [F, M] There is **no native CSV export of the P&L**. Export to Excel, then Save As CSV (Intuit community moderator). https://quickbooks.intuit.com/learn-support/en-us/reports-and-accounting/export-reports/00/1277391
- [K, M] Layout of the .xlsx (a report, not a flat table):
  - Header rows: company name, "Profit and Loss", date range, blank.
  - Column header: blank account column, then "Total" (or one column per month for "P&L by Month").
  - Body rows in order: **Income** → account lines → **Total Income** → **Cost of Goods Sold** → lines → **Total Cost of Goods Sold** → **Gross Profit** → **Expenses** → lines (sub-accounts are indented, with "Total X" subtotals) → **Total Expenses** → **Net Operating Income** → **Other Income** / **Other Expenses** → **Net Other Income** → **Net Income**.
  - Footer: basis (Cash/Accrual) and timestamp.
  - Parser rule [I]: locate rows by label text, strip "$" and ",", and treat "(x)" as a negative number.

---

## 4. Consulting firms, brokers, lenders and searchers as buyers

### Market size signals
- **[F, M] BizBuySell 2025:** **9,586** small-business transactions (+0.4% YoY), $7.95B total enterprise value, **median sale price $350k**, sold at 94% of asking. Q1 had 2,368 sales and Q2 had 2,342. https://bizbuysell.com/blog/2025-year-in-review/ ; https://www.bizbuysell.com/insight-report/
  - BizBuySell captures only a subset of the market [I].
- **[F, M] SBA 7(a), FY2025** (secondary sources; SBA report not fetched):
  - about **78,078 loans / $37.3B**, a record (FY2024: 70,242 / $31.1B)
  - acquisition segment **about 7,003 deals / $8.29B** (+34.6%), or 23.6% of dollars (>$9B) by another estimate
  - SOP 50 10 8, effective 6/1/2025, requires a 10% equity injection for change of ownership

  https://ctacquisitions.com/?p=57466 ; https://www.whitefordlaw.com/news-events/client-alert-sba-issues-sop-50-10-8-key-changes-impacting-sba-7a-lending
- **[F, M] Search funds / ETA:**
  - Stanford 2024 study: 681 funds through 2023; **record 94 launches in 2023**; IRR 35.1%, 4.5x
  - Later Stanford update: launches stay at historic highs in 2024-25, but only about half of the 2021-24 cohort acquired a company; about 20 months to acquire; median price $16M (2024-25)

  https://searchfunder.com/post/stanford-2024-search-fund-study-highlights ; https://www.gsb.stanford.edu/index.php/insights/search-funds-keep-offering-proven-path-ownership
  - [I] The bigger volume is in **self-funded searchers and first-time Main Street buyers**. IBBA/CT Acquisitions puts first-time buyers at 46% of Main Street deals in 2025 (unverified). https://ctacquisitions.com/?p=57467
- **[F, L-M] "Silver tsunami":**
  - 2.3M (Project Equity) to 2.9M boomer/55+-owned businesses, employing about 32M people
  - less than a third to about half of owners have a succession plan

  https://smb.co/blog/silver-tsunami-millions-of-small-businesses-need-new-owners ; https://www.fastcompany.com/90908597/
- **[F, M] IBBA Market Pulse:** deals under $2M are priced on SDE and remain a buyer's market. In Q2 2026, 255 brokers/advisors completed 181 deals that quarter. https://www.ibba.org/wp-content/uploads/2026/08/mp-highlights-q2-2026.pdf ; https://www.ibba.org/wp-content/uploads/2026/02/market-pulse-highlights-q4-2025.pdf

### What diligence costs today
- **[F, M] QoE report:**
  - $5k-$15k for businesses under $5M at boutique firms
  - $10k-$35k for deals of $100k-$10M
  - $25k+ at large firms; $25k-$50k for $5-15M EV
  - sell-side runs 10-30% higher
  - **not required by the SBA**, but lenders often ask for one; most searchers buy one above a few hundred thousand dollars

  https://webacquisition.com/quality-of-earnings-qoe-report-cost/ ; https://www.bdemerson.com/article/quality-of-earnings-report-cost ; https://searchfunder.com/post/is-a-qoe-always-necessary
- **[I]** On a median $350k BizBuySell deal, a $10k-$15k QoE equals 3-4% of the price. That is why many small buyers skip it, and it is the opening for a **$500-$2,000 AI "pre-QoE" screen**.

### Competitors already validating the AI-QoE niche [F, M]
- **Provafi**, launched Oct 2025 on Product Hunt: a cheap "Phase 1" AI QoE pitched as an alternative to paying "$30k+". https://www.producthunt.com/@mstroube
- **shepi**, an AI QoE tool for searchers, brokers and accounting firms. https://www.caplight.com/company/shepi
- **Finsider**, AI QoE automation for CFOs/CPAs, seed round Mar 2025. https://www.barchart.com/story/news/35038707/quality-of-earnings-software-launched-by-finsider-ai-ai-powered-qoe-reports-automation-platform-targets-60-faster-due-diligence-for-ma-deals
- **QoEAgent**, a CU Boulder venture doing proof-of-cash and TTM views. https://www.colorado.edu/venturepartners/startup-portfolio/qoeagent-inc
- **Audit Sight**, an AI QoE-prep module (Jul 2025). https://my-cpe.com/insights/accounting-industry/people-updates/audit-sight-debuts-ai-module-to-streamline-quality-of-earnings-prep
- A Columbia team polled Searchfunder users about a cheaper AI QoE, and some said they would try it. https://www.searchfunder.com/post/columbia-team-working-on-cheaper-quality-of-earnings-reports

[I] **Implication:** "AI QoE" is getting crowded. The hackathon angle should be **POS-level operating diligence**: item mix, revenue concentration, daypart and labor, and the reconciliation of POS sales to P&L revenue. A ledger-based QoE does not cover these well.

### Small consultancies adopting AI
- **[F, L]** BizCover (Australia, 196 consulting firms): 90% use AI or plan to within 2 years, and 59% would consider AI tools instead of hiring or outsourcing. https://www.bizcover.com.au/how-consulting-businesses-are-adapting-to-ai-in-2025/
- **[F, L]** Smokeball (an adjacent sector, small law firms): 53% have integrated AI, up from 27% in 2023. https://legaltechnology.com/smokeballs-state-of-law-report-suggests-ai-adoption-has-soared-in-small-firms/
- **[F, M]** Fathom's existence and its advisor certification program show that accountants buy tools to sell "advisory." https://www.fathomhq.com/lp/financial-performance
- **Gap:** I found no US survey of independent consultants or fractional CFOs on AI-tool spending.

### Migration consulting (for a "migration consultancy" angle)
- **[F, M] Restaurant POS switch:**
  - vendor implementation $500-$5k, plus internal time worth 2-3x that
  - total direct cost $7k-$25k, plus $5k-$20k soft cost, for an independent restaurant
  - termination, data-export and re-integration fees add 15-25%
  - flat migration fees seen: $3,000 (retail POS) and $500 (data to Shopify POS, up to 10 locations)
  - multi-location loyalty/data migrations: $75k-$200k

  https://gosnappy.io/blog/cost-of-switching-pos-systems-for-restaurants/ ; https://adorapos.com/blog/pos-system-switching-checklist ; https://sales.websell.io/POS-Migration-pos-migration-63511/ ; https://geekyants.com/blog/loyalty-program-software-cost-guide-for-us-restaurants-2026-edition
- **[F, M] QuickBooks Desktop to Online:**
  - Intuit offers free assisted migration for accountants
  - a third-party flat fee of **$395** was found
  - memorized reports do not migrate; payroll and history integrity is a known concern

  https://quickbooks.intuit.com/accountants/resources/move-to-online/migration-toolkit/ ; https://quickbooksmadeeasy.com/?p=1085487 ; https://unclekam.com/tax-pro-tools/accounting-software/qbo-desktop-migration-guide/
- **[I]** Pitch angle: a "before/after-you-switch" report that normalizes Square, Toast and Shopify exports into one schema. It lets an owner or migration consultant compare vendors on real data and verify that history migrated correctly. The normalizer is the same code needed for Section 3.

---

## 5. Nonprofit-adjacent (brief)
- **[F, L]** Fractional Chief Development Officer: **$6k-$18k/mo** (citing Pavilion 2025, via a vendor page). https://stealthagents.com/research/cost-of-hiring-a-chief-development-officer
- **[F, L]** Fractional nonprofit revenue lead: $3k-$12k/mo for 2-8 days/month. One guide says nonprofits that are 80%+ grant- or donor-funded should hire a fractional development officer instead. https://pulserevops.com/knowledge/tl16322
- **Gap:** I found no AFP-sourced hourly rate for fundraising consultants. [K, L] The commonly cited range is about $75-$250/hr, and AFP ethics prohibit commission-based fundraising fees. That is a useful talking point for flat-fee AI products, but verify it.

---

## Gaps and next steps
1. Official column lists for Square, Toast and Shopify were not fetched because WebFetch DNS failed. **Ask a local merchant for a sample export** at the event, or download our own sandbox export. Build fuzzy header matching.
2. The Fed SBCS 51% cash-flow figure is secondhand. Verify it in the PDF before putting it on a slide.
3. No neutral recent "% of SMBs using POS data" statistic exists in the results. Use the 2014 figure (48% use sales trends) with its date.
4. SBA FY2025 acquisition counts come from secondary compilers.
5. Nothing local to State College or Centre County was researched (e.g., Penn State SBDC, local SCORE chapter). Those are likely the fastest warm channels for consultants. [I]
