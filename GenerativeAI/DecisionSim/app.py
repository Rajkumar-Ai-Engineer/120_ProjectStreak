import streamlit as st 
from test import graph
from helper import get_decision_sim
import time
import sys
import io

graph_func = graph()
decision_sim = get_decision_sim()

# Page Config
st.set_page_config(
    page_title="DecisionSim",
    page_icon="🤖",
    layout="centered",
)

# Page Title
st.title("DecisionSim using LangGraph📉 + CrewAI👨‍💻 + AutoGen🤝")

# Info
st.info("This app simulates business decision making using three AI agents: Market Analyst, Financial Analyst, and CEO.")

# User Input
text = st.text_area("Enter market scenario:", height=200)

# Engine Selector
with st.sidebar:
    options = st.selectbox("Choose Engine", options=["CrewAI", "LangGraph", "AutoGen"])

# Button Click
if st.button("Analyse."):
    if text.strip() == "":
        st.error("❗ Please enter the market scenario.")
    else:
        with st.spinner("⏳ Processing your input..."):
            st_time = time.time()

            try:
                if options == "CrewAI":
                    result = decision_sim.run(use_graph=False, user_input=text)
                    st.markdown("### 🤖 CrewAI Result")
                    st.markdown(result)

                elif options == "LangGraph":
                    result = graph_func.invoke({"input_data": text})
                    
                    st.markdown("### 📊 Market Analysis")
                    st.write(result.get("market_analysis", "❌ Not available."))

                    st.markdown("### 💰 Financial Analysis")
                    st.write(result.get("financial_analysis", "❌ Not available."))

                    st.markdown("### 📈 Strategic Decision")
                    st.write(result.get("decision_making", "❌ Not available."))

                    # Download result
                    result_md = (
                        "### 📊 Market Analysis\n"
                        + str(result.get("market_analysis", "❌ Not available."))
                        + "\n\n### 💰 Financial Analysis\n"
                        + str(result.get("financial_analysis", "❌ Not available."))
                        + "\n\n### 📈 Strategic Decision\n"
                        + str(result.get("decision_making", "❌ Not available."))
                    )
                    st.download_button("📥 Download Result", file_name="langgraph_result.md", data=result_md)

                elif options == "AutoGen":
                    # Capture stdout from AutoGen output
                    old_stdout = sys.stdout
                    sys.stdout = mystdout = io.StringIO()

                    # Trigger AutoGen flow
                    decision_sim.autogen_process()

                    # Reset stdout
                    sys.stdout = old_stdout
                    output = mystdout.getvalue()

                    st.markdown("### 🤝 AutoGen Result")
                    st.text_area("AutoGen Dialogue Output", value=output, height=400)

            except Exception as e:
                st.error(f"❌ Error occurred: {e}")

            end_time = time.time()
            st.success(f"✅ Completed in {round(end_time - st_time, 2)} seconds.")
