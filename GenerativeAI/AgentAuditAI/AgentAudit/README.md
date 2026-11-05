# AgentAuditAI — Multi-Agent Code Assistant Audit

**Project ID:** 011 · **Domain:** Generative AI  
**Entry point:** `main.py`

## Purpose
A small AutoGen experiment that sends a user-provided coding task to an assistant agent and coordinates a second evaluator-style user-proxy agent. LangSmith tracing is attached to the evaluation function.

## Implemented flow
1. Load environment variables with python-dotenv.
2. Configure AutoGen to use `gpt-3.5-turbo` with `OPENAI_API_KEY` and temperature 0.5. A Groq configuration remains commented out.
3. Create an `AssistantAgent` with a code-creation system message.
4. Create a `UserProxyAgent` with evaluator instructions, `human_input_mode="NEVER"` and Docker execution disabled.
5. Start a two-turn chat for the task entered in the terminal.
6. Use a LangSmith `traceable` decorator and a LangSmith client configured for the `agentaudit` project.

## Important implementation distinction
The code defines an evaluator agent, but the explicit LangSmith `evaluate(...)` call and evaluator metrics are commented out. The current active workflow is a short agent conversation, not a completed automated correctness benchmark.

## Configuration and dependencies
Required environment variables: `OPENAI_API_KEY` and `LANGSMITH_API_KEY`. Imports indicate AutoGen, LangSmith and python-dotenv. No project-specific requirements file is present.

## Review findings
- `llm_config` is passed to the agent methods as a module-level global rather than consistently using the instance configuration.
- `evaluate_task` does not return a measured evaluation result; the former evaluation block is commented.
- Docker execution is disabled, but this should not be treated as a complete sandbox for arbitrary generated code.
- No task dataset, expected answers, tests, score aggregation or reproducible evaluation report is included.
- The logger removes all handlers from its logger instance before adding the file handler; the stream handler created earlier is therefore removed.

## Run
From this directory, configure the environment and run `python main.py`. Static review only; no model call or LangSmith trace was executed.

## Next steps
Restore a real evaluator pipeline with explicit criteria and test cases, persist run IDs/results, add dependency pins, and isolate any code execution in a properly restricted environment.
