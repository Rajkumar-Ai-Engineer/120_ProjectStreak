# Data Analytics Folder — Visual and PDF Source Audit

**Repository:** `Rajkumar-Ai-Engineer/120_ProjectStreak`  
**Branch:** `master`  
**Path:** `da/`  
**Date:** 2026-11-05  
**Method:** GitHub tree inspection, PNG retrieval and visual review, PDF artifact inventory

## 1. Executive result

The folder contains 21 files: five PDFs and 16 PNG screenshots. The screenshot review yielded 15 identifiable dashboard/notebook artifacts and one image that the connector could not retrieve. The PDF files were inventoried, but their page content could not be rendered or extracted using the available GitHub connector in this pass. Consequently, the PDF-specific documents record evidence and gaps rather than fabricate report content.

## 2. Visual evidence findings

The inspected screenshots show these topics:

| Screenshot | Identified topic | Visible evidence |
|---|---|---|
| 183035 | IPL Analysis 2025 | Match summary KPIs, winner/toss comparisons, toss decision split |
| 183112 | House Price Analysis | Sale price by locality/year, room count, carpet area, property tax rate |
| 183120 | Restaurant Food Sales | Sales/profit KPIs, item type, item profit, month/year and time of sale |
| 183130 | India Crime Analysis | Victim gender, case closure, crime year, weapon, age and police deployment |
| 183138 | COVID-19 Analysis | Total cases/deaths, yearly charts, country maps |
| 183159 | Healthcare Patient and Billing | Patient count, average billing, admissions, insurance and medical-condition billing |
| 183211 | Financial Portfolio Growth | Normalized stock growth lines for AAPL, AMZN, GOOGL and MSFT |
| 183222 | Project 112/120 Financial Portfolio Analysis | Social post gives period, ticker set, weights and claimed annual returns |
| 183235 | Unknown | GitHub connector returned an empty image payload; visual content not reviewed |
| 183253 | Reddit Sentiment Distribution | 46 positive, 20 negative, 134 neutral posts; Python visualization context |
| 183324 | HR Attrition | Employee counts, attrition split, gender, satisfaction and education views |
| 183354 | Employee Performance | Employee count, gender, hire year, job title, department and performance score |
| 183400 | Movie Ratings | 504 films, average rating 3.376, votes and film ranking |
| 183424 | Product Sales 2010–2024 | Sales/revenue KPIs, yearly comparisons and year filters |
| 183429 | Sales Dashboard | Profit/sales KPIs, Madrid top-profit city, country/product-line/deal-size views |
| 183459 | Online Retail Customer Segmentation | `Online Retail.xlsx`, notebook, duplicate removal and numeric feature selection |

Project-level documentation is in `da/projects/`. The full index is [da/README.md](README.md).

## 3. PDF evidence findings

| PDF | What the filename supports | Review status |
|---|---|---|
| `118-world wildlife.pdf` | World Wildlife-themed source; filename label 118 | Page content pending |
| `120-job.pdf` | Job-themed source; filename label 120 | Page content pending |
| `churn-analysis.pdf` | Churn-analysis-themed source | Page content pending |
| `geospatial-coffee-sales.pdf` | Geospatial coffee-sales-themed source | Page content pending |
| `retail-sales.pdf` | Retail-sales-themed source | Page content pending |

The connector returned base64 for several PDF files, but the page streams are compressed and the available file-inspection path did not provide page rendering or text extraction. The large churn PDF also exceeded the connector's ordinary content retrieval. The PDF documents under `da/source-pdfs/` preserve these limitations and specify what must be extracted next.

**No claim is made that these PDFs correspond to the screenshot projects.** That relationship must be established from their contents.

## 4. Data and interpretation risks visible from the screenshots

- **IPL:** the player-level values are not labelled clearly; match and toss counts need reconciliation.
- **House prices:** currency and the PriceRealityCheck definition are absent; outliers and locality imbalance require review.
- **Restaurant sales:** currency, time range, profit formula and time-of-day boundaries are absent.
- **Crime:** source/jurisdiction and definitions for police deployment, case closure and age bins are absent; do not represent as official national statistics without provenance.
- **COVID-19:** source timestamp, cumulative/daily definitions and reporting revisions are absent.
- **Healthcare:** patient privacy, billing period/currency and billed-versus-paid definitions need clarification; billing is not a clinical outcome.
- **Portfolio:** the accompanying post reports 35.4% and 20.24% annual returns, but the optimization method and calculation are not reproduced.
- **Reddit sentiment:** classifier/annotation provenance and validation are absent; counts alone do not establish model quality.
- **HR attrition:** attrition denominator, observation period and salary period are absent; descriptive splits are not causal evidence.
- **Employee performance:** performance rubric and whether records are real or synthetic are unknown.
- **Movie ratings:** rating provider/scale and vote aggregation need documentation; popularity is not equivalent to quality.
- **Product sales:** KPI units and currency are absent; title and visible year filter ranges should be reconciled.
- **Sales dashboard:** total-sales number formatting is ambiguous and should be validated against the underlying data.
- **Online retail:** customer-level feature engineering, returns/cancellations, missing CustomerID handling, scaling and cluster validation are not visible.

## 5. Implementation evidence

The folder tree contains no visible source code, SQL, notebook, dashboard project file, or dependency manifest. Two screenshots expose partial Python notebook/editor context: Reddit sentiment visualization and Online Retail preprocessing. A social post explicitly names Python and Matplotlib for the portfolio analysis. These are limited clues, not a complete source-code audit.

Dashboard appearance alone is not sufficient to identify Power BI, Tableau, Excel or another BI authoring platform. Tool names remain unconfirmed unless shown explicitly.

## 6. Canonical inventory handling

No new canonical project IDs were assigned. The filename labels 118 and 120 are preserved, but they are not independently reconciled with the master project catalogue. Screenshot topics are documented as evidence-based project candidates, not automatically counted as separate implementations. Some screenshots may be outputs or evidence for projects already indexed elsewhere.

## 7. Verification boundary

This pass confirms repository file presence and visually documents 15 screenshots. It does not validate raw datasets, reproduce any KPI, execute notebooks, test dashboards, or verify model quality. PDF page contents and one screenshot remain unreviewed. Any future technical report must be grounded in the actual PDF pages and underlying source artifacts.

## 8. Required next steps

1. Upload the five PDF files directly or provide page-rendered copies so their contents can be reviewed.
2. Re-upload `Screenshot 2026-11-03 183235.png` or provide a smaller copy.
3. Inspect original notebooks/dashboard files and trace the calculations behind each visual.
4. Map the PDF reports to screenshot evidence only after matching titles/content.
5. Reconcile project candidates with the 120-project catalogue before changing the canonical inventory.
