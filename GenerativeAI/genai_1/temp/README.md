# Langflow JSON Loader API — Experimental Backend

**Project ID:** 029 · **Domain:** Generative AI  
**Entry point:** `main.py`

## Purpose
A minimal FastAPI experiment intended to load a serialized Langflow graph and invoke it with user input using Langflow's `load_flow_from_json`.

## Intended workflow
- Receive a JSON request containing `flow` and `input`.
- Load the flow using `load_flow_from_json(flow_json)`.
- Invoke the resulting chain with the input.
- Return the output or an error message.

## Critical implementation defect
The route decorator is written as `app.post("/run-flow")` without the leading `@`. As written, this expression does not decorate `run_flow`; the function is not registered as the intended POST route. The endpoint therefore cannot be assumed to work.

## Security and configuration
CORS is configured with wildcard origins, methods and headers, and credentials are allowed. There is no authentication, request validation, model/provider allowlist, resource limit or execution timeout. Langflow flow files may describe external integrations and must be treated as untrusted input.

## Dependencies
The requirements file pins Langflow 0.0.53 and LangChain 0.0.131 and lists FastAPI, Uvicorn and Pyngrok. This is an older dependency stack; verify compatibility and security before installation.

## Verification
Static inspection only. No route registration, flow loading or invocation was executed.

## Next steps
Correct the decorator, validate the flow schema, restrict allowed components and tools, isolate execution, add authentication and request limits, and pin a supported dependency set.
