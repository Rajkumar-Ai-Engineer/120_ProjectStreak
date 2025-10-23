from langgraph.graph import StateGraph, add_messages, START, END
from crewai import Task, Agent, Crew, Process
from autogen import UserProxyAgent, GroupChat, GroupChatManager,AssistantAgent
import os
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate 
from typing import Annotated,TypedDict
import streamlit as st


api = os.getenv("GROQ_API_KEY")


class DecisionSim:
    def __init__(self):
        self.llm_config = {
            "model": "llama3-8b-8192",
            "base_url": "https://api.groq.com/openai/v1",
            "api_key": os.getenv("GROQ_API_KEY"),
            "temperature": 0.7,
        }
        self.llm = llm = ChatGroq(api_key=api,model="deepseek-r1-distill-llama-70b")

    def agents_config(self):
        return [
            {
                "Name": "MarketAnalyst",
                "Role": "Market Research Specialist",
                "Goal": "Analyze market trends and provide insights",
                "Backstory": "A market research expert skilled in analyzing trends, consumer behavior, and competitive landscapes to inform strategic decisions.",
                "llm_config": self.llm_config
            },
            {
                "Name": "Finance Analyst",
                "Role": "Financial Research Specialist",
                "Goal": "Evaluate financial data and provide investment recommendations",
                "Backstory": "A financial analyst with expertise in evaluating financial statements, market conditions, and investment opportunities to guide financial decisions.",
                "llm_config": self.llm_config
            },
            {
                "Name": "CEO",
                "Role": "Chief Executive Officer",
                "Goal": "Make strategic decisions based on insights from analysts",
                "Backstory": "The CEO is responsible for the overall strategic direction of the company, making high-level decisions based on insights from market and financial analysts.",
                "llm_config": self.llm_config
            }
        ]

    def create_agents(self):
        agents = {}
        for cfg in self.agents_config():
            agent = Agent(
                name=cfg["Name"],
                role=cfg["Role"],
                goal=cfg["Goal"],
                backstory=cfg["Backstory"],
                llm_config=cfg["llm_config"]
            )
            agents[cfg["Name"]] = agent
        return agents

    def create_task(self, user_input=None):
        agents = self.create_agents()

        Market_task = Task(
            name="Market Research",
            description="Analyze the provided market data to support strategic decisions.",
            agent=agents["MarketAnalyst"],
            expected_output="Strategic insights based on market trends.",
            input=user_input or "Default market data.",  
            llm_config=self.llm_config
        )

        Finance_task = Task(
            name="Financial Analysis",
            description="Analyze the financial data to provide investment recommendations.",
            agent=agents["Finance Analyst"],
            expected_output="Investment recommendations.",
            input=user_input or "Default financial data.",  
            llm_config=self.llm_config
        )

        decision_task = Task(
            name="Decision Making",
            description="Make strategic decisions based on analysts' outputs.",
            agent=agents["CEO"],
            expected_output="Final strategic decisions.",
            context=[Market_task, Finance_task],  
            llm_config=self.llm_config
        )

        return [Market_task, Finance_task, decision_task]

 

    def langgraph_graph(self, user_input=None, path="graph.png"):
        class GraphState(TypedDict):
            input_data: Annotated[list, add_messages]
            market_analysis:str 
            financial_analysis:str
            decision_making:str

        def market_analysis_node(state: GraphState) -> dict:
            input_data = state.get("input_data", "")
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a business market analyst. Analyze the market conditions based on the given input."),
                ("human", "Here is the input data to analyze: {input_data}")
            ])
            final_prompt = prompt.format_messages(input_data=input_data)
            response = self.llm.invoke(final_prompt)
            return {"market_analysis": response.content}

        def financial_analysis_node(state: GraphState) -> dict:
            input_data = state.get("input_data", "")
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a financial analyst. Provide detailed investment recommendations based on the following financial data."),
                ("human", "Here is the financial data to analyze: {input_data}")
            ])
            final_prompt = prompt.format_messages(input_data=input_data)
            response = self.llm.invoke(final_prompt)
            return {"financial_analysis": response.content}

        def decision_node(state: GraphState) -> dict:
            input_data = state.get("input_data", "")
            market_analysis = state.get("market_analysis", "")
            financial_analysis = state.get("financial_analysis", "")
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are the CEO. Make a final strategic decision based on the market and financial analysis."),
                ("human", """Input Data: {input_data}
                    Market Analysis: {market_analysis}
                    Financial Analysis: {financial_analysis}
                    Make the best strategic decision based on the above.""")
            ])
            final_prompt = prompt.format_messages(
                input_data=input_data,
                market_analysis=market_analysis,
                financial_analysis=financial_analysis
            )
            response = self.llm.invoke(final_prompt)
            return {"decision_making": response.content}


            
        graph = StateGraph(GraphState)
        graph.add_node("market_analysis", market_analysis_node)
        graph.add_node("financial_analysis", financial_analysis_node)
        graph.add_node("decision_making", decision_node)

        graph.set_entry_point("market_analysis")
        graph.add_edge("market_analysis", "financial_analysis")
        graph.add_edge("financial_analysis", "decision_making")
        graph.add_edge("decision_making", END)

        graph_builder = graph.compile()

        
        try:
            from IPython.display import Image, display
            image_data = graph_builder.get_graph().draw_mermaid_png()
            with open(path, "wb") as f:
                f.write(image_data)
            print(f"Graph image saved at: {os.path.abspath(path)}")
            display(Image(filename=path))
        except Exception as e:
            print(f"Could not save image: {e}")

        return graph_builder

    def create_autogen_agents(self):
        market_analyst = AssistantAgent(
            name="MarketAnalyst",
            llm_config=self.llm_config,
            system_message="You are a Market Analyst. Your job is to provide insights about market trends."
        )

        finance_analyst = AssistantAgent(
            name="FinanceAnalyst",
            llm_config=self.llm_config,
            system_message="You are a Finance Analyst. You evaluate financial statements and give advice."
        )

        ceo = AssistantAgent(
            name="CEO",
            llm_config=self.llm_config,
            system_message="You are the CEO. You will make final decisions based on the team's input."
        )

        return {
            "MarketAnalyst": market_analyst,
            "FinanceAnalyst": finance_analyst,
            "CEO": ceo
        }

    def autogen_process(self):
        agents = self.create_autogen_agents()

        user_proxy = UserProxyAgent(
            name="UserProxy",
            human_input_mode="NEVER",  # or "ALWAYS" for manual input
            code_execution_config={"use_docker": False}
        )

        groupchat = GroupChat(
            agents=[
                agents["MarketAnalyst"],
                agents["FinanceAnalyst"],
                agents["CEO"],
                user_proxy
            ],
            messages=[],
            max_round=5
        )

        manager = GroupChatManager(
            groupchat=groupchat,
            llm_config=self.llm_config
        )

        # Start the conversation
        user_proxy.initiate_chat(manager)

        # Return conversation log
        return groupchat.messages

    def crew_process(self, user_input=None):
        agent_dict = self.create_agents()
        agent_list = list(agent_dict.values())

        tasks = self.create_task(user_input=user_input) 

        crew = Crew(
            name="Decision Making Crew",
            agents=agent_list,
            tasks=tasks,
            llm_config=self.llm_config,
            process=Process.sequential
        )
        return crew


    def run(self, use_graph=False, user_input=None):
        if use_graph:
            print("Running via LangGraph...")
            graph = self.langgraph_graph(user_input=user_input)
            result = graph.invoke({"input_data": user_input})

            print("\n🧠 Final Result from Graph:", result)
        else:
            print("Running via CrewAI Sequential Process...")
            crew = self.crew_process(user_input=user_input)
            result = crew.kickoff()
            print("\n🧠 Final Result from Crew:", result)
        return result
@st.cache_resource
def get_decision_sim():
    return DecisionSim()

# Example of using the class
if __name__ == "__main__":
    sim = DecisionSim()
    sample_input = """
            Market Data:
            - Industry: Electric Vehicles (EV)
            - Region: North America
            - Current Trends:
            - 40% YoY growth in EV adoption.
            - Government subsidies increasing for EV infrastructure.
            - Tesla and Rivian leading the market share.
            - Rising demand in urban areas for short-range EVs.
            - Battery production costs reduced by 15% over the past year.

            Financial Data:
            - Company: GreenVolt Motors Inc.
            - Revenue: $320 million (Q2 2025), up from $250 million in Q1 2025.
            - Net Profit: $45 million (Q2), increased by 20% compared to last quarter.
            - R&D Investment: $60 million, focused on battery tech and AI-based driving.
            - Debt-to-Equity Ratio: 0.4
            - Cash Reserves: $150 million
            - Stock Price Change: +12% over the last 3 months.

            Goal:
            Based on this data, analyze the market viability for new product launch and provide financial recommendations for investment or strategic scaling.
            """
    use_graph = input("Enter yes or no:").strip().lower() == "yes"
    sim.run(use_graph=use_graph, user_input=sample_input)

