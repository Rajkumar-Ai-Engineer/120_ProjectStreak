import streamlit as st 
import os
from helper import LLMStudio,LLMStudioRAG

st.set_page_config(
    page_title="LLMStudio",
    layout="wide",
    page_icon="👨‍💻"
)

st.title("LLMStudio🏢")

def slideBar(options_for_LLm):
    with st.sidebar:
        page = st.selectbox(label="Select the option",options=["Chat","RAG","Agent"])
    if page == "Chat":
        query = st.text_input(label="Enter your Query:")
        llm = st.sidebar.selectbox("Select the llm",options=options_for_LLm)
        if st.button("Generate"):
            with st.spinner(text="Processing..."):
                if query!=None and query!="":
                    response = studio.run(query,model_id=llm)
                    cleaned_response = studio.llm_cleaned_output(response)
                    st.write(cleaned_response)
                else:
                    st.error("Please enter the query")

    if page == "Agent":
        query = st.text_input(label="Enter your Query:")
        tool = st.sidebar.radio("Select yes if need real time tool to search",options=["Yes","No"])
        if st.button("Generate"):
            with st.spinner(text="Processing..."):
                if query!=None and query!="":
                    response = studio.agent(query,tool)
                    
                    st.write(response)
                else:
                    st.error("Please enter the query")
                    
    if page == "RAG":
        with st.sidebar:
            file_format = st.selectbox(options=["pdf","txt","wiki","web","csv"],label="Select the file format")
            if file_format in ["wiki", "web"]:
                file_input = st.text_input(f"Enter {file_format} {'page title' if file_format == 'wiki' else 'URL'}:")
            else:
                file_input = st.file_uploader(label="Upload the file",type=file_format)
            
            embedding_type = st.selectbox("Select Embedding", ["HuggingFace", "Openai"])
            vector_store = st.selectbox("Select Vector Store", ["faiss", "chroma"])
            llm_model = st.selectbox("Select LLM", options_for_LLm)
            
        query = st.text_input("Enter your question:")
        
        if file_input and st.button("Process & Query"):
            with st.spinner("Processing document..."):
                try:
                    # Save uploaded file temporarily for processing
                    if file_format not in ["wiki", "web"]:
                        temp_path = f"temp_{file_input.name}"
                        with open(temp_path, "wb") as f:
                            f.write(file_input.getbuffer())
                        file_path = temp_path
                    else:
                        file_path = file_input
                    
                    # Load and process document
                    documents = studioRag.dataloaders(file_format, file_path)
                    split_docs = studioRag.spliters(documents, "Recursive")
                    embeddings = studioRag.embeddings(embedding_type)
                    db = studioRag.vector_store("store", vector_store, split_docs, embeddings)
                    
                    # Create retriever
                    llm = studioRag.llm_selection(llm_model)
                    prompt_template = """Use the following context to answer the question:
                    Context: {context}
                    Question: {question}
                    Answer:"""
                    prompt = studioRag.template(prompt_template, "Prompt")
                    retriever = studioRag.retriever(db, "qa", llm, prompt)
                    
                    if query:
                        response = studioRag.run(query, retriever)
                        cleaned_response = studio.llm_cleaned_output(response)
                        st.write(cleaned_response)
                    else:
                        st.success("Document processed! Enter a question above.")
                        
                except Exception as e:
                    st.error(f"Error processing document: {str(e)}")
                    
        
if __name__ == "__main__":
    studio = LLMStudio()
    studioRag = LLMStudioRAG(os.getenv("GROQ_API_KEY"))
    llm = studio.models_list()
    slideBar(options_for_LLm=llm)