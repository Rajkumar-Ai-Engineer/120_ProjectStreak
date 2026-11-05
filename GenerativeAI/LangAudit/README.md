# LangAudit — Prompt Version Comparison and Lightweight Output Audit

**Project ID:** 018 · **Domain:** Generative AI  
**Entry point:** `helper.py`

## Purpose
A command-line experiment that compares answers generated from multiple prompt versions and appends the outputs and a simple score to a CSV audit log.

## Workflow
1. Load prompt variants from `prompts.json`; if the file is absent, use two built-in prompt templates.
2. Read `GROQ_API_KEY`, `LANGSMITH_API_KEY_1` and `project` from the environment.
3. Initialize a Groq `ChatGroq` model using `llama3-8b-8192` at temperature 0.1.
4. Ask the user for a question.
5. Invoke each prompt/model chain, hash each prompt with MD5 and print its output.
6. Append timestamp, prompt version, prompt hash, generated output and score to `prompt_audit_log.csv`.

## Important evaluation caveat
The current `grading_function` returns 1 if the generated answer contains the word “paris”, otherwise 0. This is a hard-coded keyword check, not a general hallucination detector or factuality evaluator. The `StringEvaluator` object and LangSmith client are initialized but are not used to run a LangSmith evaluation in the active loop.

## Dependencies and setup
Install `requirements.txt`, configure the three environment variables, optionally provide `prompts.json`, then run `python helper.py`.

## Findings
- The metric name `hallucination_score` overstates what the Paris keyword rule measures.
- Prompt hashes use MD5 for identification; do not use this hash for security or integrity guarantees.
- No reference-answer dataset, semantic judge, source grounding check, repeatability analysis or aggregate comparison report exists.
- CSV output is appended without data-retention controls or escaping policy for downstream consumers.
- The project name suggests a general language audit, but the current implementation is a narrow prompt-variant experiment.

## Verification
Static inspection only; no LLM calls or score validation were performed.

## Next steps
Use a labelled golden dataset, multiple fit-for-purpose metrics, calibrated human-reviewed evaluators, LangSmith experiment tracking and clear separation of prompt identity from evaluation score.
