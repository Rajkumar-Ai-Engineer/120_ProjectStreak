from crewai import Crew,Agent,Process
from langgraph.graph import END,StateGraph,add_messages
from dotenv import load_dotenv
load_dotenv()
from crewai_tools import SerperDevTool
from crewai.task import Task
from typing import Dict
import os
import traceback
from logging_File import logger 
from typing import TypedDict,Annotated 
from crewai.crews.crew_output import CrewOutput

api_config_llm = {
    "model":"deepseek-r1-distill-llama-70b",
    "base_url":"https://api.groq.com/openai/v1",
    "api_key":os.getenv("GROQ_API_KEY"),
    "temperature":0.6
}

my_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))

#Agents 
class MultiAI_Agent_System:
    
    def IntakeAgent(self):
        try:
            intake_agent = Agent(
                name="IntakeAgent",
                role="Intake Agent",
                goal="Extract the core objective from the user's input",
                backstory="Expert in clarifying the user requirements",
                llm_config = api_config_llm,
                tools=[my_tool]
            )
        except Exception as E:
            error_message = traceback.format_exc()
            print("Caught an Error:")
            print(error_message)
            logger.error(error_message)
        finally:
            logger.info("Intake Agent is Initialized")
        return intake_agent
    
    def RetrieverAgent(self):
        try:
            retriever_agent = Agent(
                name="retriever",
                role="Retriever Agent",
                goal="Retrieve the Accurate data or fetch data from internet using the given tools.Note you is agent to fetch the exact accurate answer and before taking decision you must include multiple sources to take the data as a content for result",
                backstory="Expert in Researching about the information",
                llm_config = api_config_llm,
                tools=[my_tool]
            )
        except Exception as E:
            error_message = traceback.format_exc()
            print("Caught an Error:")
            print(error_message)
            logger.error(error_message)
        finally:
            logger.info(f"Retrieve Agent is Initialized")
        return retriever_agent
    
    def PlannerAgent(self):
        try:
            planner_agent = Agent(
                name="planner",
                role="Planner Agent",
                goal="Create Structured Plan to complete the goal",
                backstory="Experienced planner and Strategist",
                llm_config = api_config_llm,
                tools=[my_tool]
            )
        except Exception as E:
            error_message = traceback.format_exc()
            print("Caught an Error:")
            print(error_message)
            logger.error(error_message)
        finally:
            logger.info(f"Planner Agent is Initialized")
        return planner_agent 
    
    def WriterAgent(self):
        try:
            writer_agent = Agent(
                name="writer",
                role="Writer Agent",
                goal="Write the first draft and based on the plan and context",
                backstory="Professional writer trained in converting plans into Content",
                llm_config = api_config_llm,
                tools=[my_tool]
            )
        except Exception as E:
            error_message = traceback.format_exc()
            print("Caught an Error:")
            print(error_message)
            logger.error(error_message)
        finally:
            logger.info(f"Writer Agent is Initialized")
        return writer_agent
    
    def Reviewer(self):
        try:
            reviewer_agent = Agent(
                name="reviewer",
                role="Reviewer Agent",
                goal="Review and polish the draft to final Form",
                backstory="Expert Editor",
                llm_config = api_config_llm,
                tools=[my_tool]
            )
        except Exception as E:
            error_message = traceback.format_exc()
            print("Caught an Error:")
            print(error_message)
            logger.error(error_message)
        finally:
            logger.info(f"reviewer Agent is Initialized")
        return reviewer_agent
    
AgentManager = MultiAI_Agent_System()


class State(TypedDict):
    Input:str
    input_summary:str
    Fetched_data:str 
    Planned_structure:str 
    writer_draft:str 
    final_reviewed_version:str 
    
graph_builder  = StateGraph(State)




def intake_agent_node(state: State):
    try:
        crew = Crew(
            agents=[AgentManager.IntakeAgent()],
            tasks=[Task(
                name="intake_agent_task",
                description=("Understand the user's Input:{input}"),
                agent=AgentManager.IntakeAgent(),
                expected_output="A brief summary of the user's main objective",
                tools=[my_tool])],
            process=Process.sequential
        )
        result = crew.kickoff(inputs={"input": state["Input"]})
        print(result)
        
    except Exception:
        logger.error(traceback.format_exc())
        result = "Error during intake agent execution"
    return {"input_summary": result}


def retriever_agent_node(state: State):
    try:
        agent = AgentManager.RetrieverAgent()
        print(state["input_summary"])
        print(type(state["input_summary"]))
        crew = Crew(
            agents=[agent],
            tasks=[Task(
                name="retriever_agent",
                tools=[my_tool],
                agent=agent,
                description=("Search and retrieve relevant data for the topic: {topic}"),
                expected_output="Relevant, structured and concise data."
        )],
            process=Process.sequential
        )
        result = crew.kickoff(inputs={"topic": str(state["input_summary"])})
        try:
            print(result)
            
        except Exception as e:
            print(f"Error Caught:{e}")

    except Exception:
        logger.error(traceback.format_exc())
        result = "Retrieval failed"

    return {
        "Fetched_data": result}

def planner_agent_node(state: State):
    try:
        agent = AgentManager.PlannerAgent()
        crew = Crew(
            agents=[agent],
            tasks=[Task(
                name="planner_agent",
                agent=agent,
                tools=[my_tool],
                description=("Create a structured plan from summary: {summary} and data: {fetched_data}"),
                expected_output="A detailed, structured plan to accomplish the objective.")],
            process=Process.sequential
        )
        
        
        result = crew.kickoff(inputs={"summary": str(state["input_summary"]), "fetched_data": str(state["Fetched_data"])})
        print(result)

    except Exception:
        logger.error(traceback.format_exc())
        result = "Planning failed"

    return {
        "Planned_structure": result
    }


def writer_agent_node(state: State):
    try:
        crew = Crew(
            agents=[AgentManager.WriterAgent()],
            tasks=[Task(
                name="writer_agent",
                agent=AgentManager.WriterAgent(),
                description=("Write a first draft based on the plan: {planned_structure} and content: {fetched_data}"),
                expected_output="A complete first draft based on the plan and fetched content")],
            process=Process.sequential
        )
        
        result = crew.kickoff(inputs={
            "planned_structure": str(state["Planned_structure"]),
            "fetched_data": str(state["Fetched_data"])
        })
        
        
        print(result)
    except Exception:
        logger.error(traceback.format_exc())
        result = "Drafting failed"
    return {
        "writer_draft": result
    }



def reviewer_agent_node(state: State):
    try:
        print("\n🧪 DEBUG: writer_draft content before review:")
        print(state["writer_draft"])

        crew = Crew(
            agents=[AgentManager.Reviewer()],
            tasks=[Task(
                name="reviewer_agent",
                agent=AgentManager.Reviewer(),
                description=("Polish and finalize the draft: {writer_draft}"),
                expected_output="Final polished version of the draft")],
            process=Process.sequential
        )

        result = crew.kickoff(inputs={"writer_draft": str(state["writer_draft"])})
        print("\n✅ Review result:")
        print(result)

    except Exception as e:
        logger.error("Review error:\n" + traceback.format_exc())
        result = f"Review failed due to: {str(e)}"

    return {
        "final_reviewed_version": result
    }




# Build graph pipeline
graph_builder.add_node("intake", intake_agent_node)
graph_builder.add_node("retrieve", retriever_agent_node)
graph_builder.add_node("plan", planner_agent_node)
graph_builder.add_node("write", writer_agent_node)
graph_builder.add_node("review", reviewer_agent_node)

# Define flow
graph_builder.set_entry_point("intake")
graph_builder.add_edge("intake", "retrieve")
graph_builder.add_edge("retrieve", "plan")
graph_builder.add_edge("plan", "write")
graph_builder.add_edge("write", "review")
graph_builder.add_edge("review", END)


ai_writer_app = graph_builder.compile()

img_path = "graph.png"
if not os.path.exists(img_path):
    with open(img_path,mode='wb') as img_file:
        img_file.write(ai_writer_app.get_graph().draw_mermaid_png())
        print("Img File is Saved!")

if __name__ == "__main__":
    user_input = input("Enter your task or idea: ")
    output = ai_writer_app.invoke({"Input": user_input})
    print("\n✅ Final Output:\n", output["final_reviewed_version"])