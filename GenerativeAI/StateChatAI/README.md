# StateChatAI — LangGraph Wrapper Around an AutoGen Chat

**Project ID:** 024 · **Domain:** Generative AI  
**Entry point:** `main.py`

## Purpose
A minimal experiment that wraps one AutoGen assistant conversation inside a single LangGraph node.

## Implementation
- Defines a LangGraph state containing a message list annotated with `add_messages`.
- Creates an AutoGen `AssistantAgent` configured for Groq's OpenAI-compatible endpoint and model `llama3-8b-8192`.
- Creates an AutoGen `UserProxyAgent` with Docker-based code execution disabled.
- The `chatbot` node takes the latest state message and starts an AutoGen chat.
- Compiles a one-node graph with START → Chatbot → END.
- Saves a Mermaid-rendered graph image to `graph.png` if it does not already exist.
- Invokes the graph with a hard-coded greeting when the module is run.

## Dependencies and setup
The requirements file lists LangGraph, LangChain, python-dotenv, PyAutoGen, AutoGen, Groq and OpenAI packages. Configure `GROQ_API_KEY` before running `python main.py`.

## Findings
- A hard-coded graph invocation is executed at module import time, not only under a main guard. Importing this module therefore triggers a model call and network dependency.
- The example invocation uses a fixed greeting; no interactive CLI, web UI or external input interface is implemented.
- The LangGraph graph has one node only; it demonstrates state orchestration rather than a multi-step agent workflow.
- The node calls AutoGen's `initiate_chat` and returns the incoming state; the AutoGen conversation transcript is not written back as structured graph state.
- Graph image generation requires the Mermaid rendering dependencies and may fail in a minimal environment.
- No tests, checkpointing, conversation persistence, retry policy or evaluation dataset is included.

## Verification
Static inspection only; no AutoGen conversation or graph rendering was executed.

## Next steps
Return assistant messages into graph state, accept user input, add checkpointing and thread IDs, pin dependencies, and test state transitions and tool permissions.
