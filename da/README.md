# Data Analytics (DA)

This folder contains five PDF source documents and 16 PNG screenshot assets. This index separates **visual evidence that could be inspected** from **PDF source content that still requires page-level extraction**. Do not treat a screenshot-derived observation as proof of the underlying dataset or code.

## Audit summary

| Evidence | Count | Review result |
|---|---:|---|
| PDF files | 5 | All inventoried; page content not extractable in the connected GitHub reader during this pass |
| PNG screenshots | 16 | 15 visually inspected; `183235.png` could not be retrieved by the connector |
| Screenshot-based project notes | 16 | 15 substantive notes plus one explicit retrieval-pending note |
| PDF source audit notes | 5 | One note per PDF; content review remains pending |
| Executable source files visible in `da/` | 0 | No Python, SQL, notebook, dashboard project or dependency files appeared in the directory tree |

## Screenshot-based project documentation

Each page records what is visible, what remains unknown, technology evidence where present, and recommended validation. No screenshot-derived result has been independently reproduced.

1. [IPL Analysis 2025](projects/01-ipl-analysis-2025.md) — 74 matches, no-result count, title winner and team/toss comparisons.
2. [House Price Analysis](projects/02-house-price-analysis.md) — sale price by locality/year and property feature comparisons.
3. [Restaurant Food Sales](projects/03-restaurant-food-sales.md) — sales, profit, item type, month/year and time-of-day views.
4. [India Crime Analysis](projects/04-india-crime-analysis.md) — victim demographics, case closure, year, weapon and police-deployment views.
5. [COVID-19 Analysis](projects/05-covid-19-analysis.md) — country-level cases/deaths, yearly trends and maps.
6. [Healthcare Patient and Billing](projects/06-healthcare-patient-billing.md) — admissions, insurance provider, gender and billing by condition.
7. [Financial Portfolio Growth](projects/07-financial-portfolio-growth-python.md) — normalized growth chart for AAPL, AMZN, GOOGL and MSFT.
8. [Project 112/120 — Financial Portfolio Analysis](projects/08-financial-portfolio-analysis-project-112.md) — source-post details including date range, weights and claimed returns.
9. [Reddit Sentiment Distribution](projects/09-reddit-sentiment-distribution.md) — visible positive/negative/neutral counts and code context.
10. [HR Attrition Dashboard](projects/10-hr-attrition-dashboard.md) — employee counts, attrition, gender, satisfaction and education.
11. [Employee Performance Dashboard](projects/11-employee-performance-dashboard.md) — employee counts, hire year, job title, department and performance score.
12. [Movie Ratings Analysis](projects/12-movie-ratings-analysis.md) — film count, average rating, votes and film ranking.
13. [Product Sales 2010–2024](projects/13-product-sales-2010-2024.md) — product-sales and revenue KPIs with yearly comparisons.
14. [Sales Dashboard — City/Country](projects/14-sales-dashboard-city-country.md) — sales/profit KPIs, top-profit city, product line, deal size and country.
15. [Online Retail Customer Segmentation](projects/15-online-retail-customer-segmentation.md) — notebook screenshot showing duplicate removal and numeric-column selection.
16. [Unidentified Screenshot 183235](projects/16-unidentified-screenshot-183235.md) — connector returned an empty payload; visual review pending.

## PDF source documents

These are source-artifact records, not invented project summaries. The PDF bytes exist in the repository, but page-level text/images were not accessible through the current GitHub file connector workflow. Upload the PDFs directly in chat or provide an accessible extracted copy to complete the technical write-ups.

- [118 — World Wildlife](source-pdfs/118-world-wildlife.md) — [PDF](118-world%20wildlife.pdf)
- [120 — Job](source-pdfs/120-job.md) — [PDF](120-job.pdf)
- [Churn Analysis](source-pdfs/churn-analysis.md) — [PDF](churn-analysis.pdf)
- [Geospatial Coffee Sales](source-pdfs/geospatial-coffee-sales.md) — [PDF](geospatial-coffee-sales.pdf)
- [Retail Sales](source-pdfs/retail-sales.md) — [PDF](retail-sales.pdf)

## Screenshot asset list

- `Screenshot 2026-11-03 183035.png` — IPL Analysis 2025
- `Screenshot 2026-11-03 183112.png` — House Price Analysis
- `Screenshot 2026-11-03 183120.png` — Restaurant Food Sales
- `Screenshot 2026-11-03 183130.png` — India Crime Analysis
- `Screenshot 2026-11-03 183138.png` — COVID-19 Analysis
- `Screenshot 2026-11-03 183159.png` — Healthcare Patient and Billing
- `Screenshot 2026-11-03 183211.png` — Financial Portfolio Growth
- `Screenshot 2026-11-03 183222.png` — Financial Portfolio Analysis post
- `Screenshot 2026-11-03 183235.png` — retrieval pending
- `Screenshot 2026-11-03 183253.png` — Reddit Sentiment Distribution
- `Screenshot 2026-11-03 183324.png` — HR Attrition
- `Screenshot 2026-11-03 183354.png` — Employee Performance
- `Screenshot 2026-11-03 183400.png` — Movie Ratings
- `Screenshot 2026-11-03 183424.png` — Product Sales
- `Screenshot 2026-11-03 183429.png` — Sales Dashboard
- `Screenshot 2026-11-03 183459.png` — Online Retail notebook

## Quality and interpretation rules

- Values shown in screenshots are transcribed as visible and remain unverified against raw data.
- Currency, units, dataset provenance, date coverage and metric definitions are marked unknown whenever not visible.
- Dashboard tool names are not inferred from appearance alone.
- The financial portfolio post's reported returns are treated as author claims, not reproduced results.
- The healthcare and crime dashboards are descriptive artifacts; they do not establish causal or clinical conclusions.
- No projects are assigned new canonical IDs based only on screenshot filenames.
- No code, notebook, dashboard or model was executed during this pass.

## Completion needed

1. Extract and inspect all pages of the five PDFs.
2. Re-fetch or re-upload screenshot `183235.png`.
3. Match PDF contents to screenshot projects only when the evidence supports the relationship.
4. Locate the underlying source notebooks/dashboards and inspect code, transformations and calculations.
5. Reconcile project names and IDs against the repository's canonical inventory before adding them to the 120-project count.
