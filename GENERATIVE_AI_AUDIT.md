# Generative AI Domain — Implementation Audit

**Repository:** [Rajkumar-Ai-Engineer/120_ProjectStreak](https://github.com/Rajkumar-Ai-Engineer/120_ProjectStreak)  
**Branch:** `master`  
**Audit date:** 2026-11-05  
**Scope:** `GenerativeAI/` and the separate `genai/` reference-image directory  
**Canonical scope:** Projects 011–029 from `PROJECT_INVENTORY.md`

## 1. Executive summary

The canonical inventory identifies **19 Generative AI project boundaries (IDs 011–029)**. They span agent orchestration, prompt evaluation, code repair, document RAG, financial/medical assistants, quiz generation, report generation, scheduling, web research and flow-graph execution.

All **19 canonical project README files** have been rewritten with source-specific descriptions, architecture/workflow, dependencies/configuration, observed limitations and next steps. A domain index has been added at `GenerativeAI/README.md`.

The separate top-level `genai/` directory contains four PNG reference images and no executable source files in the inspected tree. It is documented separately and is not counted as another project.

| Measure | Result |
|---|---:|
| Canonical Generative AI projects | 19 |
| IDs covered | 011–029 |
| Project-specific README files rewritten | 19 |
| Domain index files created | 1 |
| Separate reference images in `genai/` | 4 |
| Runtime/model/API tests executed | 0 |

## 2. Canonical project register

| ID | Project | Implementation summary | Key review note |
|---:|---|---|---|
| 011 | AgentAuditAI | AutoGen code assistant and evaluator-style proxy with LangSmith tracing | LangSmith evaluation block is commented out; no active scoring benchmark |
| 012 | Autofixer | Streamlit code/error input, LangChain prompt and Groq repair suggestion | SuperAGI client has empty key; Streamlit is missing from requirements; no patch/test loop |
| 013 | ContextArchitect | LlamaIndex document indexing with Groq, BGE embeddings and local persistence | Environment assignment fails if key is absent; two separate helper implementations exist |
| 014 | DecisionSim | CrewAI, LangGraph and AutoGen business-analysis options | AutoGen UI path does not pass the entered scenario explicitly; no external evidence pipeline |
| 015 | FinSightAI | TXT/PDF ingestion, chunking, Chroma retrieval, Gemini and Groq financial explanation | Helper `process_query` has no final return; UI uses fixed `data.txt` |
| 016 | InsightServe | Streamlit Pokémon client with three LangServe ChatOpenAI chains | Backend is `temp/apps.py`; unsafe HTML rendering and missing HTTP error handling |
| 017 | LLMStudioPro | Chat, Tavily ReAct agent and multi-loader RAG with FAISS/Chroma | Fixed agent thread ID; uploaded temporary files are not cleaned up |
| 018 | LangAudit | Prompt-version comparison, Groq outputs and CSV logging | “Hallucination score” is only a Paris keyword check; LangSmith evaluator is unused |
| 019 | MCQ Generator | Groq/LangChain question generation, Flask quiz endpoints and session state | Placeholder Flask secret; heuristic answer scoring; missing templates |
| 020 | MedicalSage | LlamaIndex + Pinecone medical-document retrieval with Groq generation | No explicit embedding configuration; fixed vector dimension; medical safety validation absent |
| 021 | ProjectPilot | Sequential intake → retrieval → plan → write → review multi-agent workflow | No source verification, human approval, retry policy or persistent document export |
| 022 | ReportGenX | Weekly CSV sales chart and Groq-generated narrative summary | No deterministic KPI validation; model ID depends on environment |
| 023 | ScheduleBot | Phidata/Groq scheduling agent with Google Calendar and Sheets client | Flask debug mode; destructive delete tool has no explicit confirmation |
| 024 | StateChatAI | Single LangGraph node that invokes an AutoGen assistant | Hard-coded graph invocation occurs at module import; conversation is not returned into graph state |
| 025 | TaskManager | CrewAI researcher/coder/reviewer tasks followed by AutoGen group chat | Hard-coded topic; missing OpenAI env value can break module import |
| 026 | WebAutoGPT | Search, page extraction, LlamaIndex indexing and GPT-4o query | User-controlled URL fetching creates SSRF exposure; debug mode and brittle search scraping |
| 027 | DocQuery | PDF/URL ingestion, OpenAI embeddings, FAISS retriever and Groq RetrievalQA | Unsafe upload filename and URL ingestion; global chain shared between users |
| 028 | Visual Flow LLM Backend | FastAPI interprets a flow JSON as PromptTemplate + ChatOpenAI chain | Client-supplied API key, wildcard CORS and no auth/schema/graph validation |
| 029 | Langflow JSON Loader API | FastAPI intended to load and invoke a Langflow graph | Missing `@` on route decorator means endpoint is not registered |

## 3. Cross-project findings

### 3.1 Secrets, authentication and API boundaries

- **Autofixer:** `helper.py` constructs a SuperAGI client with an empty API key. The active Groq flow relies on environment configuration.
- **MedicalSage:** assigns environment variables directly from `os.getenv`; absent values cause a TypeError at import.
- **InsightServe:** its FastAPI backend uses the same unsafe environment assignment pattern for `OPENAI_API_KEY`.
- **TaskManager:** `crewaiagents.py` assigns `OPENAI_API_KEY` from the environment without checking for a missing value.
- **Visual Flow Backend:** accepts the OpenAI API key in request flow JSON and prints the complete request payload.
- **MCQ Generator:** contains a placeholder Flask secret key and has no evident authentication or rate limiting.
- **ScheduleBot:** stores Google OAuth credentials in a pickle file and runs Flask with debug mode enabled.

No actual credential value is reproduced in this report. Review the full repository and Git history before deployment; if a real credential has ever been committed, rotate it.

### 3.2 RAG and retrieval quality

- ContextArchitect, FinSightAI, LLMStudioPro, MedicalSage and DocQuery each implement document ingestion or vector retrieval in different forms.
- Source citations, index lifecycle management, user isolation, document deletion and reproducible retrieval evaluation are absent or incomplete across these prototypes.
- MedicalSage fixes Pinecone dimension at 1536 but does not explicitly configure the embedding model in the inspected source.
- DocQuery retrieves only one nearest chunk (`k=1`), which may omit necessary context.
- FinSightAI reuses a persistent Chroma collection without a documented document replacement/deduplication lifecycle.

### 3.3 Agent orchestration and tool safety

- AgentAuditAI, DecisionSim, ProjectPilot, StateChatAI and TaskManager use AutoGen, CrewAI and/or LangGraph.
- The projects demonstrate orchestration patterns but do not establish production-grade isolation, robust checkpointing, structured state validation, source verification or end-to-end agent evaluation.
- ScheduleBot exposes calendar deletion as an agent tool without an explicit confirmation gate.
- Autofixer proposes code but does not validate, test or apply a controlled patch.
- WebAutoGPT and DocQuery retrieve user-specified web content without a robust URL safety boundary.

### 3.4 Evaluation and factuality

- LangAudit's active grading function checks whether the answer contains the word “paris”. This is not a general hallucination metric.
- AgentAuditAI's explicit LangSmith `evaluate(...)` block is commented out.
- No canonical golden dataset or cross-project benchmark was found in the inspected source.
- Saved outputs and generated reports should not be presented as validated model quality without reproducible evaluation.

### 3.5 Dependency and packaging quality

- Several projects lack their own requirements files or have incomplete/conflicting package declarations.
- MCQ Generator's requirements file repeats packages with conflicting versions.
- Autofixer imports Streamlit but does not list it in requirements.
- Visual Flow Backend imports LangChain classes that are not explicitly declared in its requirements file.
- Legacy LangChain/LlamaIndex/AutoGen/CrewAI APIs require version pinning and compatibility testing.

## 4. Project documentation created

The 19 canonical project READMEs have been updated in place. The domain index lists each exact canonical path:

[Open Generative AI project index](GenerativeAI/README.md)

## 5. Separate reference-image directory

The root-level `genai/` folder contains four PNG files:
- `81-details-visual flow.png`
- `81-ref.png`
- `81.png`
- `llmdebulab.png`

No source code or README existed in that directory at the time of inspection. The images are not counted as executable projects, and their project/domain relationship should be confirmed against the original catalogue before assigning IDs.

## 6. Verification boundary

- Recursive Git tree inspection and static review of Python source, existing READMEs, dependency files and selected configuration assets.
- No code was executed; no LLM calls, OAuth, Google Calendar actions, Pinecone/Chroma/FAISS operations, scraping or API server startup was performed.
- No project is certified production-ready.
- Documentation changes do not fix the implementation defects listed above.
- Canonical IDs and inventory paths were preserved; no project was renumbered or moved.

## 7. Recommended remediation order

1. Remove client-supplied API keys from Visual Flow Backend; add authentication, validation and redacted logs.
2. Fix missing environment-variable handling in ContextArchitect, MedicalSage, InsightServe and TaskManager.
3. Fix Langflow JSON Loader route registration (Project 029).
4. Add URL allowlists/SSRF protection and safe upload handling to WebAutoGPT and DocQuery.
5. Replace MCQ keyword scoring and LangAudit's Paris heuristic with deterministic answer keys and a reviewed evaluation dataset.
6. Add confirmation gates for ScheduleBot's destructive Calendar operations.
7. Add source citations, index lifecycle controls and retrieval evaluation to all RAG projects.
8. Pin dependencies, add tests and document verified run instructions for every project.
