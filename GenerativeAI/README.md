# Generative AI — Project Index

**Canonical inventory:** Projects 011–029 · **Total:** 19 projects  
**Detailed audit:** [GENERATIVE_AI_AUDIT.md](../GENERATIVE_AI_AUDIT.md)  
**Canonical project register:** [PROJECT_INVENTORY.md](../PROJECT_INVENTORY.md)

This index follows the repository's existing project IDs and canonical paths. Documentation is based on the checked-in source and configuration. Static inspection does not establish that an application runs successfully or that a model result is accurate.

| ID | Project | Main technologies / pattern | Project documentation |
|---:|---|---|---|
| 011 | AgentAuditAI | AutoGen, LangSmith tracing, evaluator agent | [README](AgentAuditAI/AgentAudit/README.md) |
| 012 | Autofixer | Streamlit, LangChain, Groq code-repair prompt | [README](Autofixer/README.md) |
| 013 | ContextArchitect | LlamaIndex, Groq, BGE embeddings, local vector index | [README](ContextArchitect/ContextArtitext/README.md) |
| 014 | DecisionSim | CrewAI, LangGraph, AutoGen, business-analysis roles | [README](DecisionSim/README.md) |
| 015 | FinSightAI | Gemini, BGE embeddings, Chroma, financial-document RAG | [README](FinSightAI/README.md) |
| 016 | InsightServe | Streamlit, FastAPI, LangServe, ChatOpenAI | [README](InsightServe/README.md) |
| 017 | LLMStudioPro | LangChain, LangGraph ReAct, Tavily, FAISS/Chroma RAG | [README](LLMStudioPro/README.md) |
| 018 | LangAudit | Prompt variants, Groq, CSV logging, LangSmith imports | [README](LangAudit/README.md) |
| 019 | MCQ Generator | Groq, LangChain memory, Flask quiz API | [README](MCQ_GENERATOR/README.md) |
| 020 | MedicalSage | LlamaIndex, Groq, Pinecone, medical-document QA | [README](MedicalSage/README.md) |
| 021 | ProjectPilot | Five-stage CrewAI + LangGraph research/writing workflow | [README](ProjectPilot/ProjectPilot/README.md) |
| 022 | ReportGenX | Streamlit, pandas, Matplotlib, Groq summaries | [README](ReportGenx/README.md) |
| 023 | ScheduleBot | Phidata agent, Groq, Google Calendar/Sheets APIs | [README](ScheduleBOT/ScheduleBot/README.md) |
| 024 | StateChatAI | LangGraph state wrapper around AutoGen | [README](StateChatAI/README.md) |
| 025 | TaskManager | CrewAI tasks and AutoGen group chat | [README](TaskManager/README.md) |
| 026 | WebAutoGPT | Flask, web search/scraping, LlamaIndex, GPT-4o | [README](WebAutoGPT/src/README.md) |
| 027 | DocQuery | FastAPI, Gradio, FAISS, OpenAI embeddings, Groq RAG | [README](docquery/README.md) |
| 028 | Visual Flow LLM Backend | FastAPI, LangChain, ChatOpenAI flow execution | [README](genai_1/backend/README.md) |
| 029 | Langflow JSON Loader API | FastAPI, Langflow flow loading | [README](genai_1/temp/README.md) |

## Domain-level review priorities

1. **Credential and API security:** remove client-supplied or hard-coded secrets, use server-side secret management, add authentication and rate limits.
2. **RAG reliability:** persist source metadata, expose citations, isolate user indexes, evaluate retrieval relevance and answer faithfulness.
3. **Agent safety:** restrict tools and permissions, isolate generated code, require confirmation for destructive actions, and preserve human review.
4. **Evaluation quality:** replace keyword-only grading with a labelled golden dataset and fit-for-purpose factuality, correctness and groundedness checks.
5. **Reproducibility:** add compatible pinned dependencies, tests, sample inputs and explicit run instructions.

## Verification boundary

The audit inspects source files, README files, dependency manifests and repository assets. No model calls, external APIs, agent workflows, training, server startup or end-to-end tests were executed. A project README is documentation, not a certification of runtime or production readiness.
