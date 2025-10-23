import os 
from dotenv import load_dotenv
load_dotenv()
os.makedirs("storage", exist_ok=True)
os.makedirs("data", exist_ok=True)
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.groq import Groq 
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from logs import logger
import traceback

os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")

class ContextArchitect:
    def __init__(self):
        self.llm = Groq(model="llama3-8b-8192")
        self.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model 
        
    def read_data(self,path):
        try:
            documents = SimpleDirectoryReader(path).load_data()
            return documents 
        except Exception as e:
            print("Error Caught")
            logger.error(f"Error reading data: {e}")
            logger.error(traceback.format_exc())
            return None
             
    
    def create_index(self,documents):
        try:
            index = VectorStoreIndex.from_documents(documents)
            index.storage_context.persist(persist_dir="storage")
            return index
        except Exception as e:
            print("error Caught")
            logger.error(f"Error creating index: {e}")
            logger.error(traceback.format_exc())
            return None

    def load_index(self, path):
        try:
            storage_context = StorageContext.from_defaults(persist_dir=path)
            index = load_index_from_storage(storage_context)
            return index 
        except Exception as e:
            print("Error Caught")
            logger.error(f"Error loading index: {e}")
            logger.error(traceback.format_exc())
            return None
    
    def QueryEngine(self,index,question):
        try:
            if index is None:
                return "Index not available"
            engine = index.as_query_engine()
            response = engine.query(question)
            return response
        except Exception as e:
            print("Error Caught")
            logger.error(f"Error in QueryEngine: {e}")
            logger.error(traceback.format_exc())
            return "Error processing query" 

    def run(self,query:str):
        index = self.load_index("storage/")
        if index is None:
            print("Creating new index...")
            documents = self.read_data("data/")
            if documents:
                index = self.create_index(documents)
        return self.QueryEngine(index, query)
