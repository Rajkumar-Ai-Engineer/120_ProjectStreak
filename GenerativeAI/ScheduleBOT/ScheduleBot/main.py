from phi.agent import Agent 
from phi.model.groq import Groq 
import os 
from dotenv import load_dotenv
from tools import GoogleCallendarClient
from rich.prompt  import Prompt

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
calendar_tools = GoogleCallendarClient()

def ScheduleBotAgent():
    """Create and configure the ScheduleBot agent."""
    sb = Agent(
        name="ScheduleBot",
        description="A bot that helps you schedule events using Google Calendar and Sheets.Note time in IST",
        model=Groq(id="openai/gpt-oss-120b",api_key=api_key),
        tools=[
            calendar_tools.create_callendar_service,
            calendar_tools.list_upcoming_events,
            calendar_tools.delete_calendar_event
        ],
        show_tool_calls=True,
        markdown=True,
    )
    return sb

def run(question):
    """Run the agent with the given question."""
    try:
        agent = ScheduleBotAgent()
        response = agent.run(question)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    while True:
        print("Welcome to ScheduleBot! Type 'exit' to quit.")
        # question = Prompt.ask(f"[bold] :robot: Ask ScheduleBot [/bold]")
        question  = input("Ask ScheduleBot: ")
        if question.lower() == 'exit':
            break
        response = run(question)
        print(response.content)
    
