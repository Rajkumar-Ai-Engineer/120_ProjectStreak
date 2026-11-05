# TaskManager — Research, Coding and Review Agent Demonstration

**Project ID:** 025 · **Domain:** Generative AI  
**Entry point:** `main.py`

## Purpose
A fixed demonstration that combines CrewAI role-based tasks with an AutoGen group-chat discussion. The example topic is researching AI adoption and creating/reviewing a Python visualization script.

## Architecture
- `agents_config.py` defines Researcher, Coder and Reviewer roles, goals, backstories and Groq-compatible LLM configuration.
- `crewaiagents.py` creates CrewAI agents from that configuration.
- `main.py` defines three sequential CrewAI tasks: gather AI adoption facts, write a visualization script, and review/improve it.
- After the CrewAI run, `autogenagents.py` creates matching AutoGen assistants.
- An AutoGen `GroupChat` and `GroupChatManager` start a five-round brainstorming discussion.

## Configuration
Configure `GROQ_API_KEY` and install the dependencies listed in `requirements.txt`, including CrewAI, CrewAI Tools, PyAutoGen and python-dotenv.

## Findings
- The task descriptions are hard-coded; the workflow does not accept a user-defined task or persist structured results.
- `crewaiagents.py` assigns `os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")`; this raises TypeError when the variable is absent, and the agents are configured with Groq endpoint settings.
- `config_list_from_json` is imported but unused.
- CrewAI and AutoGen agents are configured separately; the AutoGen conversation does not receive a structured CrewAI result as context.
- No source verification, code execution test, artifact saving, evaluation or UI is included.

## Run
Set required environment variables, install compatible dependencies and execute `python main.py`.

## Next steps
Accept task input, pass typed artifacts between frameworks, validate research sources, run generated code in a sandbox, save outputs, and add tests for each stage.
