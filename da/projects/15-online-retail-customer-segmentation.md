# Online Retail — Customer Segmentation Notebook

**Evidence:** Screenshot: `Screenshot 2026-11-03 183459.png`

## What the evidence shows

The notebook title/comment indicates a Customer Segmentation problem statement. The visible file explorer contains `Online Retail.xlsx` and `test.ipynb`. Visible code removes duplicates in place and selects `float64` and `int64` columns. A preview shows columns Quantity, UnitPrice and CustomerID.

## Unknowns and evidence limits

The screenshot does not show the segmentation algorithm, feature engineering, customer aggregation, number of clusters, cluster validation, or business interpretation. Selecting numeric columns alone is not sufficient customer-level feature engineering.

## Tools and implementation evidence

Python notebook is visible; pandas operations are visible.

## Recommended technical validation and improvements

Aggregate invoice-line records to customer-level features; inspect cancellations/returns and negative quantities; handle missing CustomerID; scale skewed features; compare clustering methods and validate segments.

## Verification status

This page documents only what is visible in the repository screenshot. It is not a source-code review, reproducibility check, or validation of the underlying dataset or numerical results. No code or dashboard was executed during this audit.
