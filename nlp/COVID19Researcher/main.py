import streamlit as st
from helper import Covid_Researcher
import time

cr = Covid_Researcher()

st.set_page_config(
    page_title="Covid19",
    page_icon="🧫",
    layout= "wide",
    initial_sidebar_state="expanded"
)
st.title("Covid Research Agent🦠")

st.info("Covid Info...🤖")

text = st.text_input(label="Enter the covid details whatever you need")

if st.button("Research🔍"):
    if not text:
        st.info("Please type the prompt ❌")
    else:
        st.info("Please wait while we are researching...🧠")
        with st.spinner("Analysing..🤖"):
            start_time = time.time()
            response = cr.covid_agent(text)
            st.markdown(f"**{response.content}**")
            end_time = time.time()
            time_taken = end_time - start_time
            st.success(f"✅Program Excution Finished and taken {time_taken} seconds")
