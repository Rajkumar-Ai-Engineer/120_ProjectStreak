# LLMStudioPro — Multi-Model Chat, Agent and RAG Workbench

**Project ID:** 017 · **Domain:** Generative AI  
**Entry point:** `app.py` · **Core services:** `helper.py`

## Purpose
A Streamlit workbench with three modes: direct LLM chat, tool-using agent chat, and document/question-answering RAG. Users can select a Groq model and configure document loaders, embedding model and vector store.

## Implemented capabilities
- **Chat:** creates a LangChain `ChatGroq` model and invokes it with a text prompt.
- **Agent:** builds a LangGraph ReAct agent with Tavily search and an in-memory checkpointer.
- **RAG ingestion:** supports PDF, TXT, Wikipedia page, web URL and CSV loaders.
- **Chunking:** recursive or character text splitting with 1,000-character chunks and 200 overlap.
- **Embeddings:** Hugging Face BGE or OpenAI embeddings.
- **Vector stores:** FAISS and Chroma are exposed in the UI; helper code also contains a Pinecone branch.
- **Retrieval:** LangChain RetrievalQA with a context/question prompt.
- **Output cleanup:** removes `<think>` blocks and normalizes whitespace.

## Configuration
The helper reads `GROQ_API_KEY` and `Tavily_API_KEY`; OpenAI embeddings require `OPENAI_API_KEY`. Install the packages listed in `requirements.txt` with mutually compatible LangChain versions.

## Findings and limitations
- Agent checkpoint configuration uses a fixed thread ID (`abc123`), so conversations may share state rather than being isolated per user/session.
- Uploaded files are written to temporary paths but are not removed after processing.
- The UI's vector-store choices are FAISS and Chroma; the Pinecone code path is not exposed by the UI.
- The selected LLM and retrieval pipeline are assembled at request time; no persisted index lifecycle, source citation UI, document deletion or user-level isolation is present.
- The app relies on legacy LangChain modules/APIs; compatibility must be verified against pinned versions.
- No prompt-injection defenses, retrieval evaluation or model-output validation are implemented.

## Run
Set the relevant API keys, install requirements and run `streamlit run app.py` from this directory.

## Next steps
Use per-session checkpointer IDs, secure uploaded-file handling, persist/manage indexes explicitly, display source references, add prompt-injection boundaries and test retrieval quality across a golden dataset.
