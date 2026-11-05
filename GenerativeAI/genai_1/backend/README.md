# Visual Flow LLM Backend — JSON Flow to Chat Completion

**Project ID:** 028 · **Domain:** Generative AI  
**Entry point:** `main.py`

## Purpose
A FastAPI endpoint that accepts a flow-graph JSON payload, extracts PromptTemplate and ChatOpenAI/OpenAI node configuration, constructs a LangChain prompt/model chain and returns the generated text.

## Request and execution flow
1. Client posts JSON to `POST /run-flow`.
2. The handler reads `flow` and `input`.
3. It locates nodes with types PromptTemplate, ChatOpenAI/OpenAI and LLMChain.
4. It extracts prompt template text, model name, temperature and OpenAI API key from the flow payload.
5. It constructs a LangChain `PromptTemplate`, `ChatOpenAI` and `LLMChain`, then runs the chain with the supplied input.
6. The endpoint returns the output in a JSON response.

## Dependencies
The checked-in requirements list FastAPI, Uvicorn, Langflow and Pyngrok. The active source also imports LangChain classes; the manifest does not explicitly list the required LangChain/OpenAI integration packages.

## Security and correctness findings
- The API key is accepted inside the client-supplied flow JSON. Treat request bodies as secrets; never print the full payload or expose credentials in logs.
- CORS allows all origins and there is no authentication, rate limiting, request-size limit or model allowlist.
- Prompt templates, model names, temperature and API keys are trusted directly from user input; validate the graph schema and restrict allowed models/parameters.
- The extracted `chain_node` is not used to validate graph connections or execution order; the backend always builds a single prompt-to-LLM chain.
- Exceptions are returned as ordinary JSON output strings rather than appropriate HTTP error statuses.
- The source imports `json` but does not use it in the active implementation.

## Verification
Static inspection only; no FastAPI server or model request was executed.

## Next steps
Use server-side credential management, validate a strict flow schema, verify graph edges, allowlist providers/models, add authentication and quotas, redact logs, and return typed errors.
