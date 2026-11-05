# ContextArchitect — Local Document Index and Query App

**Project ID:** 013 · **Domain:** Generative AI  
**Streamlit entry point:** `app.py` · **Core implementation:** `helper.py`

## Purpose
Index documents placed in a local data directory and answer user questions through a LlamaIndex query engine. The app uses a Groq LLM and Hugging Face embeddings.

## Architecture
- UI: Streamlit text input and Search button.
- Document loading: `SimpleDirectoryReader` reads files from `data/`.
- Embeddings: `BAAI/bge-small-en-v1.5` through `HuggingFaceEmbedding`.
- LLM: LlamaIndex Groq integration configured for `llama3-8b-8192`.
- Index: `VectorStoreIndex`, persisted to local `storage/`.
- Query: load the persisted index; if unavailable, read data, build an index and query it.

The repository also contains a separate root-level `ContextArchitect/helper.py` implementation using FAISS. The Streamlit app imports the nested `ContextArtitext/helper.py`, not that alternate helper.

## Setup
Install dependencies from the parent `ContextArchitect/requirements.txt`, configure `GROQ_API_KEY`, place supported source documents in `data/`, then run `streamlit run app.py` from the nested app directory. Paths are relative to the current working directory.

## Review findings
- `os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")` raises a TypeError when the variable is absent because environment values must be strings.
- The nested helper persists to a relative `storage` directory and reads a relative `data` directory; launching from another working directory changes their meaning.
- The nested package's `main.py` is empty. The parent helper is a separate FAISS implementation and is not wired into the Streamlit app.
- No source-document upload, delete/update workflow, citation display, access control, retrieval evaluation or automated tests are included.
- Persisted vector-store JSON files are checked into the repository; confirm whether they contain user documents or derived data before sharing.

## Verification
Static inspection only. No index creation, embedding generation, model call or retrieval evaluation was run.

## Next steps
Make paths configurable, validate the API key, add upload and index-refresh controls, show source citations, keep private indexes out of Git, and evaluate retrieval relevance and answer faithfulness.
