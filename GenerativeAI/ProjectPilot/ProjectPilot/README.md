# ProjectPilot — Five-Stage Research and Writing Agent Workflow

**Project ID:** 021 · **Domain:** Generative AI  
**Entry point:** `main.py`

## Purpose
A multi-agent workflow that turns a user task into a reviewed draft. CrewAI agents perform individual stages while LangGraph connects the stages in a fixed sequence.

## Agent stages
1. **Intake:** interpret the user's goal and identify requirements.
2. **Retriever:** gather supporting information using `SerperDevTool`.
3. **Planner:** organize the requirements and fetched material into a structured plan.
4. **Writer:** create a first draft from the plan and collected context.
5. **Reviewer:** revise and polish the draft.

The LangGraph state stores the original input, extracted requirements, fetched data, planned structure, writer draft and final reviewed version. The graph is compiled and invoked from the terminal. A Mermaid graph image is written to `graph.png` if it does not already exist.

## Technologies and configuration
Python, LangGraph, CrewAI, CrewAI Tools, Serper search and a Groq-compatible OpenAI endpoint. Configure `GROQ_API_KEY` and `SERPER_API_KEY` in the environment. The project has no dedicated requirements file in its canonical folder.

## Findings
- The graph is a fixed sequential pipeline; there is no conditional routing, retry policy, checkpointing or human approval stage.
- Several agents are constructed inside node execution, so repeated invocations recreate agent objects.
- Error handling returns generic fallback strings such as “Planning failed”; downstream stages may continue with these strings.
- Search results and generated drafts are not accompanied by source citations or a claim-verification pass.
- The graph output is printed to the terminal; no persistent final-document export or web UI is included in the inspected package.
- The code uses a third-party search tool; its results and licensing/usage constraints need review.

## Run
Create an environment with compatible CrewAI/LangGraph versions, set the two API keys and run `python main.py` from this directory.

## Next steps
Persist source URLs and evidence, add human approval and structured state validation, implement retry/stop conditions, save final artifacts, and test each agent stage independently.
