# FinSightAI — Financial Document RAG and Analysis Assistant

**Project ID:** 015 · **Domain:** Generative AI  
**Primary UI:** `app.py` · **Core RAG logic:** `helper.py`

## Purpose
A Gradio chat prototype that reads a local TXT or PDF financial document, chunks its text, indexes it in Chroma, retrieves relevant context and asks an LLM to explain the result.

## Architecture and observed flow
1. `FinSightAI` initializes Gemini 1.5 Flash through LlamaIndex, BGE-small embeddings and a persistent Chroma collection at `./db`.
2. LangChain loaders read TXT or PDF files.
3. `RecursiveCharacterTextSplitter` uses a chunk size of 1,000.
4. LangChain documents are converted into LlamaIndex documents and inserted into the Chroma-backed vector index.
5. LlamaIndex queries the index.
6. The Gradio app sends the retrieved result to the Groq chat-completions endpoint using model `openai/gpt-oss-120b` for a second financial-analysis response.

A separate `main.py` path uses AutoGen agents to analyse the RAG result. It is not the Gradio UI's active request path.

## Configuration and dependencies
The helper reads `GOOGLE_GENAI_API_KEY`; the Gradio app reads `GROQ_API_KEY`. Install from `requirements.txt` and verify compatible versions of LlamaIndex, ChromaDB, LangChain, Gradio and AutoGen.

## Findings
- The Gradio handler calls `process_query` with the default `data.txt`; the UI does not provide a file-upload control.
- `process_query` in the helper ends without returning the computed result, so the standalone helper path is incomplete.
- The Gradio app performs a direct HTTP request without timeout/status validation and assumes the response contains the expected JSON shape.
- The persistent collection is reused; document replacement, deduplication, source tracking and deletion are not implemented.
- Financial insights are generated from retrieved text and are not independently validated. No benchmark or financial calculation validation is supplied.
- The checked-in sample `data.txt` should be reviewed for licensing and sensitive content before publication.

## Verification
Static inspection only; no document ingestion, vector indexing or LLM request was run.

## Next steps
Add document upload and source citations, return and validate helper outputs, handle API failures, isolate per-user collections, evaluate retrieval/faithfulness, and clearly distinguish extracted facts from generated interpretation.
