# Science Paper Summarizer — Search-Assisted Research Agent

**Domain:** NLP / LLM research assistant. **Entry point:** main.py.

## Purpose and architecture
A Streamlit and CLI interface accepts a paper title, DOI or arXiv ID. A Phidata Agent uses Groq deepseek-r1-distill-llama-70b and DuckDuckGo search. Its prompt requests title, authors, venue/year, objective, method, findings and significance; the helper returns agent response content.

## Configuration
The code reads langchain_api_key as a Groq API key. Configure it in .env and install Phidata, python-dotenv, compatible Groq integration and DuckDuckGo search package. No project requirements file is present.

## Findings
- Prompt instructions say not to hallucinate, but no citation, DOI resolution, publisher/arXiv retrieval or source verification is enforced.
- General web search may return secondary pages instead of the original paper.
- The credential variable name is misleading.
- No structured output validation or metadata verification exists.

## Next steps
Resolve DOI/arXiv identifiers against authoritative metadata, retrieve original abstracts, preserve source URLs/dates, validate bibliographic fields and add structured output/factuality checks. Static inspection only; no search/model run.
