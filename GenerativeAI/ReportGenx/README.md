# ReportGenX — Weekly Sales Summary and Chart Generator

**Project ID:** 022 · **Domain:** Generative AI  
**Entry point:** `main.py`

## Purpose
A Streamlit application that accepts a CSV containing Date and Sales columns, filters one calendar week, plots daily sales and asks a Groq-hosted LLM to summarize the selected data.

## Workflow
1. Upload a CSV and enter a date in day-first format (example: `13-07-2025`).
2. Parse the Date column with pandas and discard rows with invalid Date or missing Sales.
3. Calculate the Monday-to-Sunday range containing the selected date.
4. Plot Sales over Date using Matplotlib.
5. Convert the filtered DataFrame to text and send it through a LangChain prompt to `ChatGroq`.
6. Display and offer the generated summary as a Markdown download.

## Dependencies and configuration
Imports show Streamlit, pandas, Matplotlib, NumPy, LangChain, LangChain Groq and python-dotenv. Configure `GROQ_API_KEY` and the `model_id` environment variable. No requirements file is present in this project folder.

## Findings
- The app assumes the CSV contains exact column names `Date` and `Sales`; schema and numeric validation are limited.
- The selected week is a calendar week (Monday through Sunday), not a rolling seven-day period.
- The LLM receives the raw filtered table text; there is no deterministic KPI calculation, reconciliation or source citation.
- The model name is read from `model_id`; if it is absent, the configured model may be invalid.
- No report template, PDF/XLSX export, tests, sample dataset or measured summary-quality evaluation is included.
- `helper.py` contains only a pandas import and is not used by the app.

## Run and verification
Install the required packages, configure environment variables and run `streamlit run main.py`. Static inspection only; no report or model response was generated.

## Next steps
Validate and normalize input columns, calculate totals/averages/growth in pandas, pass only verified KPIs to the LLM, add source-period metadata, and test week-boundary and missing-data cases.
