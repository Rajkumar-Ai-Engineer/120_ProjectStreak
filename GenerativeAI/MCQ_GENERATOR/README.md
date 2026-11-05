# MCQ Generator — LLM-Based Quiz Creation and Evaluation

**Project ID:** 019 · **Domain:** Generative AI  
**Flask API:** `app.py` · **Generator:** `MCQ.py`

## Purpose
Generate multiple-choice questions from a topic and difficulty level, expose a quiz workflow through Flask endpoints, and ask the LLM to evaluate submitted answers.

## Architecture
- `MCQGenerator` configures a Groq `ChatGroq` model (default model ID `openai/gpt-oss-120b`), a prompt loaded from `template.json` and LangChain `ConversationBufferMemory`.
- `run_quiz` sends topic, question count, difficulty, delivery mode and quiz mode to the chain.
- `app.py` exposes routes for quiz generation, question retrieval and answer submission.
- Each generated question is parsed from model text into question text and four options.
- Per-quiz state is held in a process-local `quiz_sessions` dictionary.

## Setup
Install the listed Flask, LangChain, Groq and python-dotenv dependencies. Configure `GROQ_API_KEY`. The app expects a Flask template named `index.html`, but no templates or static UI files are present in the inspected folder. Run `python app.py` only after supplying the missing template.

## Critical findings
- Flask uses the literal placeholder `your-secret-key-here`; replace it with a strong secret from environment configuration.
- The answer parser extracts options from model-generated text; malformed or differently formatted responses can produce placeholder options.
- Scoring increments when the evaluation text contains “correct” or “right”. This is not reliable answer-key comparison and can award incorrect scores.
- Sessions and generator objects live only in process memory; they are lost on restart and are not suitable for multi-worker deployment.
- No authentication, rate limiting, session expiry, CSRF protection or request schema validation is evident.
- The requirements file repeats packages with conflicting version declarations and does not establish a reproducible environment.

## Verification
Static inspection only; no Flask server or quiz generation was run.

## Next steps
Use structured JSON output with schema validation, store an explicit answer key, score deterministically, add tests for parser edge cases, secure sessions, and provide the missing templates.
