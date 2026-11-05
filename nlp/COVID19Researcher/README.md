# COVID19Researcher — COVID-19 Research and News Agent

**Domain:** NLP / LLM-assisted research. **Entry point:** main.py.

## Purpose and flow
A Streamlit interface accepts a natural-language COVID-19 research/news question. The helper creates a Phidata Agent using Groq gemma2-9b-it (temperature 0.2) and the GoogleSearch tool. The agent response is rendered in Streamlit with elapsed time.

## Configuration
The code reads the environment variable langchain_api_key as its Groq API key. Install requirements.txt, configure that value in .env, and run streamlit run main.py from this directory.

## Findings
- The key variable name is misleading for a Groq credential; use a provider-specific name.
- prompt_template() is an empty stub.
- DuckDuckGo is imported but not registered as an agent tool.
- No scholarly database, primary-source verification or source citations are displayed.
- COVID-19 information is time-sensitive; model summaries must not replace current official public-health guidance.

## Verification and next steps
Static source inspection only; no search, model call or app run. Add dated citations, authoritative sources, provider error handling and tests for empty input.
