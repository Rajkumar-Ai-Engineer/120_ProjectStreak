import os 
from dotenv import load_dotenv
load_dotenv()
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,StorageContext,load_index_from_storage,ServiceContext
from llama_index.llms.groq import Groq 
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.faiss import FaissVectorStore
import faiss 
import traceback 



os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")


class ContextArchitect:
    def __init__(self):
        self.llm = Groq(model="llama3-8b-8192")
        self.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        self.faiss_dimension = 384
        self.faiss_index = faiss.IndexFlatL2(self.faiss_dimension)
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model
       
        
    def read_data(self,path):
        try:
            documents = SimpleDirectoryReader(path).load_data()
            return documents 
        except Exception as e:
            print("Error Caught")
            
    
    def create_index(self,documents):
        vector_store = FaissVectorStore(faiss_index=self.faiss_index)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        index = VectorStoreIndex.from_documents(documents,storage_context=storage_context)
        index.storage_context.persist()
        return index

    def load_index(self, path):
        vector_store = FaissVectorStore(faiss_index=self.faiss_index)
        storage_context = StorageContext.from_defaults(vector_store=vector_store, persist_dir=path)
        index = load_index_from_storage(storage_context)
        return index 
    
    def QueryEngine(self,index,question):
        engine = index.as_query_engine()
        response = engine.query(question)
        return response 
    
    
    
if __name__ == "__main__":
    ca = ContextArchitect()
    try:
        index = ca.load_index("storage/")
    except:
        print("Creating new index...")
        documents = ca.read_data("data/")
        index = ca.create_index(documents)
    
    query = input("Enter your query:")
    res = ca.QueryEngine(index, query)
    print(res)
    
    

    
    
    

        



