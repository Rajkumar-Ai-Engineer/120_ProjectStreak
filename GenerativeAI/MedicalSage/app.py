import streamlit as st
from main import MedicoSage
import os

# Page config
st.set_page_config(page_title="MedicalSage", page_icon="🏥", layout="wide")


if 'medico_sage' not in st.session_state:
    st.session_state.medico_sage = None
if 'index' not in st.session_state:
    st.session_state.index = None

# Title and description
st.title("🏥 MedicalSage")
st.markdown("Ask medical questions and get AI-powered answers from medical documents")

# Sidebar for initialization
with st.sidebar:
    st.header("Setup")
    
    if st.button("Initialize System"):
        with st.spinner("Loading medical data and setting up AI..."):
            try:
                # Initialize MedicoSage
                st.session_state.medico_sage = MedicoSage()
                
                # Load data
                docs = st.session_state.medico_sage.load_data("data")
                
                # Setup vector store
                pinecone_index = st.session_state.medico_sage.vector_store()
                
                # Create index
                st.session_state.index = st.session_state.medico_sage.create_index(docs, pinecone_index)
                
                st.success("System initialized successfully!")
            except Exception as e:
                st.error(f"Error initializing system: {str(e)}")

# Main chat interface
if st.session_state.index is not None:
    st.header("Ask Your Medical Question")
    
    # Query input
    query = st.text_input("Enter your medical question:", placeholder="e.g., What are the symptoms of COVID-19?")
    
    if st.button("Get Answer") and query:
        with st.spinner("Searching medical knowledge..."):
            try:
                response = st.session_state.medico_sage.Query_engine(st.session_state.index, query)
                
                st.subheader("Answer:")
                st.write(response.response)
                print(response.response)
                
                
            except Exception as e:
                st.error(f"Error getting response: {str(e)}")
    
    # Sample questions
    st.subheader("Sample Questions:")
    sample_questions = [
        "What are the symptoms of COVID-19?",
        "How is diabetes diagnosed?",
        "What are the side effects of common medications?",
        "What is the treatment for hypertension?"
    ]
    
    for question in sample_questions:
        if st.button(question, key=question):
            with st.spinner("Searching medical knowledge..."):
                try:
                    response = st.session_state.medico_sage.Query_engine(st.session_state.index, question)
                    st.subheader("Answer:")
                    st.write(response.response)
                except Exception as e:
                    st.error(f"Error getting response: {str(e)}")

else:
    st.info("Please initialize the system using the sidebar to start asking questions.")

# Footer
st.markdown("---")
st.markdown("*Disclaimer: This is an AI assistant for informational purposes only. Always consult healthcare professionals for medical advice.*")