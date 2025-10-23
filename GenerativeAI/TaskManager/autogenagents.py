# autogenagents.py
from autogen import AssistantAgent
from agents_config import agents_config

autogen_agents = {}

for cfg in agents_config:
    agent = AssistantAgent(
        name=cfg["name"],
        llm_config=cfg["llm_config"]  # Correct usage
    )
    autogen_agents[cfg["name"]] = agent
