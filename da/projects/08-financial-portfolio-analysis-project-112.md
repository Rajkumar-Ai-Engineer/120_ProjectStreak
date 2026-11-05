# Project 112/120 — Financial Portfolio Analysis using Python

**Evidence:** Screenshot: `Screenshot 2026-11-03 183222.png`

## What the evidence shows

The accompanying social post identifies this as “Project 112/120 | Data Analysis 12/20 – Financial Portfolio Analysis using Python.” It states a January 2024 to January 2025 period, stocks AMZN, GOOGL, MSFT and AAPL, portfolio weights [0.4, 0.3, 0.2, 0.1], analysis of daily closing prices, and claimed annual returns of 35.4% for an “optimal weighting” and 20.24% for a “conservative investment mix.” It describes Amazon as the highest-growth contributor and portfolio volatility as moderate.

## Unknowns and evidence limits

These are claims visible in the posted project summary, not independently reproduced results. The post does not explain the optimization objective, constraints, price adjustment, benchmark, risk calculation, or how the conservative mix was selected. The screenshot does not establish that 35.4% is a realized portfolio return unless weights and calculation methodology are verified.

## Tools and implementation evidence

Python and Matplotlib are explicitly named in the post/chart context.

## Recommended technical validation and improvements

Reproduce the return calculations from raw price data; define optimality objective and constraints; show both weight vectors; account for dividends, fees and rebalancing; report volatility, drawdown and benchmark comparison.

## Verification status

This page documents only what is visible in the repository screenshot. It is not a source-code review, reproducibility check, or validation of the underlying dataset or numerical results. No code or dashboard was executed during this audit.
