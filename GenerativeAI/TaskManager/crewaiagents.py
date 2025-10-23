# crewaiagents.py
import os 
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from agents_config import agents_config

crewai_agents = {}

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

for cfg in agents_config:
    agent = Agent(
        name=cfg["name"],
        role=cfg["role"],             
        goal=cfg["goal"],
        backstory=cfg["backstory"],    
        llm_config=cfg["llm_config"]   
    )
    crewai_agents[cfg["name"]] = agent
