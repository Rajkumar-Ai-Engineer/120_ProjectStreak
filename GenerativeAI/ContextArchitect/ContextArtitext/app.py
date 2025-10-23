from helper import ContextArchitect
import streamlit as st 

st.set_page_config(page_title="Context Architect", page_icon="📚", layout="wide")
st.title("Context Architect")

@st.cache_resource
def load_model():
    return ContextArchitect()

ca = load_model()

query = st.text_input("Enter your query:")
if st.button("Search") and query:
    with st.spinner("Searching..."):
        response = ca.run(query)
        st.write(response.response)

