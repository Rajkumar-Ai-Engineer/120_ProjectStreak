from crewai import Crew, Task 
from autogen import GroupChat, GroupChatManager
from crewaiagents import crewai_agents 
from autogenagents import autogen_agents 
from autogen import config_list_from_json
import os
# Define structured tasks with expected_output
tasks = [
    Task(
        description="Find the interesting data about AI adoption",
        agent=crewai_agents["Researcher"],
        expected_output="A list of data points and trends related to AI adoption across industries."
    ),
    Task(
        description="Write a Python script to visualize the data",
        agent=crewai_agents["Coder"],
        expected_output="A Python script using matplotlib or seaborn that visualizes the AI adoption data."
    ),
    Task(
        description="Review and improve the script",
        agent=crewai_agents["Reviewer"],
        expected_output="Feedback and an improved version of the visualization script with comments."
    )
]

llm_config = {
    "model": "llama3-8b-8192",
    "base_url": "https://api.groq.com/openai/v1",
    "api_key": os.getenv("GROQ_API_KEY"),
    "temperature": 0.7,
    "cache_seed": 42
}

# Run CrewAI workflow
crew = Crew(agents=list(crewai_agents.values()), tasks=tasks)
print("🚀 Running CrewAI Structured Workflow...")
crew.kickoff()

# Dynamic brainstorming with autogen agents
groupchat = GroupChat(
    agents=list(autogen_agents.values()),
    messages=[],
    max_round=5
)

manager = GroupChatManager(groupchat=groupchat,llm_config=llm_config)
print("\n💬 Starting Autogen Dynamic Brainstorming...")
manager.initiate_chat(user_message="Team, discuss how to improve the code further and add features.",recipient=autogen_agents["Researcher"])
