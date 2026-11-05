# MedicalSage — Medical Document Retrieval Assistant

**Project ID:** 020 · **Domain:** Generative AI  
**Streamlit UI:** `app.py` · **RAG implementation:** `main.py`

## Purpose
A Streamlit prototype that loads documents from a local `data/` directory, indexes them in Pinecone and answers questions through a LlamaIndex query engine using a Groq-hosted model.

## Architecture and workflow
1. User selects Initialize System in the Streamlit sidebar.
2. `SimpleDirectoryReader` loads files from `data/`.
3. The Pinecone client creates or reuses an index named `medico-sage` with dimension 1536, cosine metric and AWS us-east-1 serverless configuration.
4. `PineconeVectorStore` is connected to a LlamaIndex `VectorStoreIndex`.
5. The query engine retrieves context and uses the configured Groq LLM (`openai/gpt-oss-120b`) to form an answer.
6. The UI displays the response and includes a disclaimer advising consultation with healthcare professionals.

## Configuration
The code reads `GROQ_API_KEY` and `PINECONE_API_KEY`. Install the listed Streamlit, LlamaIndex, Groq and Pinecone packages. Place supported source documents in `data/`.

## Safety and correctness findings
- The code assigns `os.environ[...] = os.environ.get(...)`; missing keys cause a TypeError during import.
- No embedding model is explicitly configured in the inspected source, while the Pinecone index dimension is fixed at 1536. Confirm the actual embedding provider and dimension before indexing.
- `template.json` contains prescription-oriented wording but is not loaded or used by the active `main.py` query flow.
- No source citations, document provenance, medical guideline versioning, clinical validation or emergency escalation logic is implemented.
- The generated answer must not be treated as a diagnosis, prescription or substitute for professional care.

## Verification
Static inspection only; no document ingestion, Pinecone operation or medical response was executed.

## Next steps
Use an explicitly selected embedding model with matching dimension, display retrieved source passages, add trusted and versioned medical references, evaluate faithfulness and safety with clinical review, and keep sensitive health documents private.
