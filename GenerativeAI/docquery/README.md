# DocQuery — PDF and URL Retrieval-Augmented Question Answering

**Project ID:** 027 · **Domain:** Generative AI  
**FastAPI backend:** `backend/app.py` · **RAG pipeline:** `backend/ragchain.py` · **Gradio UI:** `frontend/frontend.py`

## Purpose
Upload a PDF or submit a web URL, index its text with embeddings and answer questions through a LangChain RetrievalQA chain.

## Architecture
- FastAPI exposes `POST /upload_pdf/` and `POST /index_url/`.
- PDF files are written under `./uploads`; LlamaIndex `SimpleDirectoryReader` loads the directory.
- URL ingestion uses LlamaIndex's BeautifulSoup web reader.
- Loaded text is converted to LangChain documents and embedded with OpenAI embeddings.
- FAISS stores vectors and exposes a similarity retriever configured with `k=1`.
- RetrievalQA uses Groq `ChatGroq` (DeepSeek R1 Distill Llama 70B model ID in source) and a context-grounded prompt.
- LangServe registers the QA chain under `/qA`; the Gradio client calls its `/invoke` route.

## Configuration and run
Configure `OPENAI_API_KEY` for embeddings and `GROQ_API_KEY` for generation. Install `requirements.txt`. Start the backend with Uvicorn via `python backend/app.py` from the backend directory, then run the Gradio frontend separately.

## Findings
- The upload endpoint uses the supplied filename directly in a filesystem path; sanitize names and prevent path traversal.
- The URL endpoint fetches user-provided URLs; add SSRF protections, redirect checks, size limits and domain policy.
- Uploaded files have no explicit size/type/content validation, retention policy or cleanup.
- `qa_chain` is a module-global variable; multiple users can overwrite one another's active index/chain.
- Retriever `k=1` may provide too little context for broad questions.
- The code assigns `os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")`; a missing key causes TypeError.
- LangServe route registration occurs dynamically after ingestion; no auth, tenant isolation or persistent index registry is implemented.

## Verification
Static inspection only; no PDF, URL, embedding, API or model execution was performed.

## Next steps
Use safe temporary storage, validate uploads and URLs, isolate indexes by user/session, persist ingestion metadata, return source citations, increase/evaluate retrieval depth and add API authentication.
