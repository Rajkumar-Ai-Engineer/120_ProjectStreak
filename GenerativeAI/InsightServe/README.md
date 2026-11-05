# InsightServe — Pokémon LLM Chain-to-API Assistant

**Project ID:** 016 · **Domain:** Generative AI  
**Streamlit client:** `main.py` · **FastAPI/LangServe backend:** `temp/apps.py`

## Purpose
A three-route Pokémon information assistant. The Streamlit client sends questions to a local LangServe API; the backend uses three prompt chains backed by ChatOpenAI.

## Routes and flow
- `/pokemon_assistant`: general questions about Pokémon.
- `/pokemon_details`: Pokémon details and region.
- `/pokemon_dex`: moves, weaknesses, Pokédex data, type and abilities.

The backend builds three `ChatPromptTemplate` + `LLMChain` combinations and registers them with LangServe. The Streamlit client posts to each route's `/invoke` endpoint and renders the returned text.

## Setup
The backend requires `OPENAI_API_KEY` and runs on localhost port 8000 using Uvicorn. The client uses Streamlit and Requests. Install the backend requirements from `requirements.txt` and run the FastAPI server before starting the Streamlit client.

## Review findings
- The backend implementation is in `temp/apps.py`; `main.py` is the Streamlit client, not the API server.
- `os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")` fails if the key is absent.
- Client requests have no timeout, status-code validation or structured error handling.
- The backend uses an LLM prompt for Pokémon facts; no authoritative Pokédex API, retrieval source, citations or factual validation is wired in.
- The Streamlit client renders model text with `unsafe_allow_html=True`; untrusted generated HTML should not be rendered this way.
- The old commented FastAPI alternatives in `temp/apps.py` are not active implementation.

## Verification
Static inspection only; neither server nor client was started and no OpenAI request was made.

## Next steps
Use an authoritative Pokémon data source, add response schemas and citations, validate HTTP responses, add timeouts, remove unsafe HTML rendering, and configure CORS/API access explicitly.
