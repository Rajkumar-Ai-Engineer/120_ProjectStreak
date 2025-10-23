import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq 
from dotenv import load_dotenv
load_dotenv()
import os

def summary(data):
    prompt = PromptTemplate(
        input_variables=['data'],
        template="""
        Summarize the weekly sales data as a data analyst.
        {data}
        """
    )
    LLM = ChatGroq(api_key=os.environ.get("GROQ_API_KEY"), model=os.getenv("model_id"))
    chain = prompt | LLM
    result = chain.invoke({"data": data.to_string()})
    return result.content

def chart(df, week_day):
    try:
        week_day = pd.to_datetime(week_day, dayfirst=True, errors='coerce')
        if pd.isnull(week_day):
            return None, None
        
        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors='coerce')
        df = df.dropna(subset=["Date", "Sales"])

        start_date = week_day - pd.Timedelta(days=week_day.weekday())
        end_date = start_date + pd.Timedelta(days=6)

        filtered_data = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(filtered_data["Date"], filtered_data["Sales"], marker='o', linestyle='-')
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales")
        ax.set_title("Sales over Time (Weekly)")
        ax.grid(True)

        return fig, filtered_data
    except Exception as e:
        st.error(f"Error in chart generation: {str(e)}")
        return None, None


st.set_page_config(
    page_title="ReportGenX",
    layout="centered"
)

st.title("📊 ReportGenX - Weekly Sales Report Generator")
file = st.file_uploader("📂 Upload your CSV file with 'Date' and 'Sales' columns")

date_of_the_week = st.text_input("📅 Enter the date of the week (e.g., 13-07-2025):")

if st.button("🚀 Generate Report"):
    if file and date_of_the_week:
        try:
            df = pd.read_csv(file)
            st.subheader("📋 Uploaded Data")
            st.dataframe(df)

            fig, filtered_data = chart(df, date_of_the_week)

            if fig is not None and not filtered_data.empty:
                st.pyplot(fig)

                st.subheader("📌 Weekly Summary")
                summary_data = summary(filtered_data)
                st.write(summary_data)

                st.success("✅ Report Generated Successfully")
                st.download_button("⬇️ Download Report", summary_data, file_name="weekly_sales_report.md")
            else:
                st.warning("⚠️ No data found for the selected week. Please check the date and file content.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please upload the file and enter a valid date.")
