from llama_index.core import SimpleDirectoryReader, download_loader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain.chains import LLMChain 
from langchain.prompts import PromptTemplate 
from langchain.chains import RetrievalQA 
from langchain_groq import ChatGroq
import os 


os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")

def build_from_pdf(pdf_directory:str):
    docs = SimpleDirectoryReader(pdf_directory).load_data()
    docs = [Document(page_content=doc.text) for doc in docs]
    embeddings = OpenAIEmbeddings() 
    vector_store = FAISS.from_documents(docs,embeddings)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 1})
    return retriever
    

def build_from_url(url:str):
    BeautifulsoupWebReader = download_loader("BeautifulSoupWebReader")
    loader = BeautifulsoupWebReader()
    docs = loader.load_data(urls=[url])
    docs = [Document(page_content=doc.text) for doc in docs]
    embeddings = OpenAIEmbeddings() 
    vector_store = FAISS.from_documents(docs,embeddings)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 1  })
    return retriever

def build_from_qa_chain(retriever):
    llm = ChatGroq(model="deepseek-r1-distill-llama-70b",temperature=0.1)
    prompt = """
            You are a helpful assistant that answers questions based on the provided context.
            If the context does not contain enough information to answer the question, say "I don't know.
            Context: {context}
            Question: {question}
            """
    template = PromptTemplate.from_template(prompt)
    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        chain_type_kwargs={"prompt": template},
                                        retriever =retriever,
                                        )
    print("📌 Retriever passed in:", retriever)

    return chain 
    