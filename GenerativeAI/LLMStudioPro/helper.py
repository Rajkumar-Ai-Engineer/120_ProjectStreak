import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq 
import json 
from langchain_community.utilities import SerpAPIWrapper,GoogleSerperAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_tavily import TavilySearch
load_dotenv()
import re
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders.wikipedia import WikipediaLoader
from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.csv_loader import CSVLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter,CharacterTextSplitter

from langchain_community.embeddings.huggingface import HuggingFaceBgeEmbeddings
from langchain_community.embeddings.openai import OpenAIEmbeddings

from langchain.vectorstores.chroma import Chroma
from langchain.vectorstores.faiss import FAISS
from langchain.vectorstores.pinecone import Pinecone 
import pinecone 

from langchain.prompts import ChatPromptTemplate,PromptTemplate 

from langchain.chains import RetrievalQA


class LLMStudio:
    def __init__(self):
        self.data_from_json = json.load(open("template.json","r",encoding="utf-8"))
        self.api_key = os.getenv("GROQ_API_KEY")
        self.tavily_api_key = os.getenv("Tavily_API_KEY")
        self.memory = MemorySaver()
        self.search = TavilySearch(api_key=self.tavily_api_key)
        self.tools = [self.search]
        self.model = init_chat_model("groq:deepseek-r1-distill-llama-70b")
        self.config = {"configurable":{"thread_id":"abc123"}}
        self.agent_excutor = create_react_agent(model=self.model,checkpointer=self.memory,tools=self.tools)
        
    def agent(self,query:str,tool="No"):
        input_message = {
            "role":"user",
            "content":query + (" Use tool to find" if tool == "Yes" else "")
        }
        
        for step in self.agent_excutor.stream(input={"messages":[input_message]},stream_mode="values",config=self.config):
            result = step["messages"][-1]
        return result
    
    def models_list(self):
        return self.data_from_json["models"][0]["groq_model"]
    
    def llm_cleaned_output(self,result:str):
        
        #remove <think> </think>
        think_pattern = r'<think>.*?</think>'
        cleaned_output = re.sub(think_pattern, '',result,flags=re.DOTALL)
        cleaned_output = re.sub(r'\n\s*\n', '\n\n', cleaned_output.strip())
        return cleaned_output
    
    def run(self,query:str,temperature:int=0.5,model_id:str="deepseek-r1-distill-llama-70b"):
        llm = ChatGroq(model=model_id,temperature=temperature,api_key=self.api_key)
        response = llm.invoke(query)
        return response.content
    
class LLMStudioRAG(LLMStudio):
    def __init__(self, api_key=None):
        super().__init__()
        if api_key:
            self.api_key = api_key
    
    def dataloaders(self,file_format,file):
        if file_format=="pdf":
            reader = PyPDFLoader(file)
            return reader.load()
        elif file_format=="txt":
            reader = TextLoader(file)
            return reader.load()
        elif file_format=="wiki":
            reader = WikipediaLoader(file)
            return reader.load()
        elif file_format=="web":
            reader = WebBaseLoader(file)
            return reader.load()
        elif file_format=="csv":
            reader = CSVLoader(file)
            return reader.load()
    
    def spliters(self,documents,splitter_name):
        if splitter_name == "Character_splitter":
            splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
            doc = splitter.split_documents(documents)
        else:
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
            doc = splitter.split_documents(documents)
        return doc
    
    def embeddings(self,embeddings_name):
        if embeddings_name == "HuggingFace":
            embedding = HuggingFaceBgeEmbeddings()
        elif embeddings_name == "Openai":
            embedding = OpenAIEmbeddings()
        return embedding
    
    def llm_selection(self,model_id="deepseek-r1-distill-llama-70b"):
        llm = ChatGroq(model=model_id,temperature=0.5,api_key=self.api_key)
        return llm 
    
    def template(self,prompt,template_name):
        if template_name == "Prompt":
            template = PromptTemplate.from_template(prompt)
        else:
            template = ChatPromptTemplate.from_messages(prompt)
        return template 
    
    def vector_store(self,store_name,vs,documents,embedding):
        if vs == "faiss":
            db = FAISS.from_documents(documents=documents,embedding=embedding)
        elif vs == "chroma":
            db = Chroma.from_documents(documents=documents,embedding=embedding)
        elif vs == "pinecone":
            pinecone.init(api_key=os.getenv("PINECONE_API_KEY"))
            db = Pinecone.from_documents(documents=documents,embedding=embedding,index_name="data")
        return db
    
    def retriever(self,db,retriever_name,llm,prompt):
        db_retriver = db.as_retriever()
        retrive_chain = RetrievalQA.from_chain_type(chain_type="stuff",llm=llm,retriever=db_retriver,return_source_documents=False,chain_type_kwargs={"prompt":prompt})
        return retrive_chain
    
    def run(self,query:str,retriever):
        response = retriever.run(query)
        return response
          
if __name__ == "__main__":
    studio = LLMStudio()
    # response = studio.run(query="What is Blockchain",model_id="llama-3.1-8b-instant")
    # print(response)
    # studio.models_list()
    studio.agent("What is ai")
