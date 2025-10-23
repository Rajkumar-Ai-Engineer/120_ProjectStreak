import os
from typing import Annotated, TypedDict
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import END, StateGraph
from langgraph.graph import add_messages
import streamlit as st

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama3-8b-8192", api_key=api_key)
output_parser = StrOutputParser()


class GraphState(TypedDict):
    input_data: Annotated[str, add_messages]
    market_analysis: str
    financial_analysis: str
    decision_making: str
    
def market_analysis_node(state: GraphState) -> dict:
    input_data = state.get("input_data", "")
    prompt = ChatPromptTemplate.from_template(
        "You are a market analyst. Analyze the following market data:\n\n{input_data}"
    )
    chain = prompt | llm | output_parser
    result = chain.invoke({"input_data": input_data})
    return {"market_analysis": result}


def financial_analysis_node(state: GraphState) -> dict:
    input_data = state.get("input_data", "")
    prompt = ChatPromptTemplate.from_template(
        "You are a financial analyst. Analyze the financial implications of this market data:\n\n{input_data}"
    )
    chain = prompt | llm | output_parser
    result = chain.invoke({"input_data": input_data})
    return {"financial_analysis": result}


def decision_making_node(state: GraphState) -> dict:
    market = state.get("market_analysis", "")
    finance = state.get("financial_analysis", "")
    prompt = ChatPromptTemplate.from_template(
        "You are a strategic decision-maker. Based on the following analyses:\n\nMarket:\n{market_analysis}\n\nFinance:\n{financial_analysis}\n\nWhat is the best business strategy?"
    )
    chain = prompt | llm | output_parser
    result = chain.invoke({
        "market_analysis": market,
        "financial_analysis": finance
    })
    return {"decision_making": result}


graph_builder = StateGraph(GraphState)
graph_builder.add_node("market_analysis", market_analysis_node)
graph_builder.add_node("financial_analysis", financial_analysis_node)
graph_builder.add_node("decision_making", decision_making_node)


graph_builder.set_entry_point("market_analysis")
graph_builder.add_edge("market_analysis", "financial_analysis")
graph_builder.add_edge("financial_analysis", "decision_making")
graph_builder.add_edge("decision_making", END)


@st.cache_resource
def graph():
    return graph_builder.compile()



if __name__ == "__main__":
    try:
        user_input = input("📥 Enter market data or scenario for analysis:\n")
        print("\n🚀 Running LangGraph pipeline...\n")

        result = graph.invoke({"input_data": user_input})

        print("\n📊 Market Analysis:\n", result["market_analysis"])
        print("\n💰 Financial Analysis:\n", result["financial_analysis"])
        print("\n📈 Strategic Decision:\n", result["decision_making"])
        print("\n✅ LangGraph process completed.\n")

    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
