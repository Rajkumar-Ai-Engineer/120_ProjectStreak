# DecisionSim — Multi-Agent Business Decision Support

**Project ID:** 014 · **Domain:** Generative AI  
**UI entry point:** `app.py` · **LangGraph workflow:** `test.py` · **Agent orchestration:** `helper.py`

## Purpose
A Streamlit prototype for analysing a user-entered business/market scenario through three roles: Market Analyst, Financial Analyst and CEO/strategic decision-maker. The UI offers CrewAI, LangGraph and AutoGen engine choices.

## Implemented paths
- **LangGraph:** `test.py` defines a typed state with input, market analysis, financial analysis and decision fields. Three sequential nodes call a Groq `ChatGroq` model: market analysis → financial analysis → decision recommendation.
- **CrewAI:** `helper.py` defines role-specific agents and tasks for market research, finance analysis and decision-making.
- **AutoGen:** helper code configures AutoGen agents/group chat for an agent discussion.
- **Streamlit:** user enters a scenario, selects an engine and views the result. LangGraph output can be downloaded as Markdown.

## Configuration
The source reads `GROQ_API_KEY` from a .env file. Imports show LangGraph, LangChain Groq, CrewAI, AutoGen, Pydantic and Streamlit. No project requirements file is checked in.

## Findings
- The LangGraph path has a clear sequential three-node structure; it is not evidence of external market-data retrieval. The prompts analyse only the user-provided scenario.
- The Streamlit AutoGen branch calls `decision_sim.autogen_process()` without passing the scenario entered in the UI; verify how the helper obtains its input.
- The app creates both the graph and DecisionSim objects at module import time.
- No data sources, financial calculation engine, fact-checking, uncertainty calibration, or decision outcome evaluation is included.
- The generated recommendations are LLM outputs, not financial advice or verified business forecasts.

## Run and verification
Configure `GROQ_API_KEY`, install compatible versions of the imported frameworks, then run `streamlit run app.py`. Static source inspection only; no agent execution was performed.

## Next steps
Pass the scenario consistently to all engines, attach cited and dated evidence, separate calculations from narrative generation, add structured outputs and tests, and label recommendations with evidence quality and uncertainty.
