from llama_index.core import SimpleDirectoryReader,VectorStoreIndex,StorageContext,Settings
import os 
from dotenv import load_dotenv
load_dotenv()
from pinecone import Pinecone,ServerlessSpec
from llama_index.llms.groq import Groq
from llama_index.vector_stores.pinecone import PineconeVectorStore

os.environ["GROQ_API_KEY"]  = os.environ.get("GROQ_API_KEY")
os.environ["PINECONE_API_KEY"] = os.environ.get("PINECONE_API_KEY")


class MedicoSage:
    def __init__(self):
        self.llm = Groq(model="openai/gpt-oss-120b")
        Settings.llm = self.llm
        
    def load_data(self,data_dir):
        reader = SimpleDirectoryReader(input_dir=data_dir)
        docs = reader.load_data()
        return docs
    
    def vector_store(self):
        pc = Pinecone()
        if "medico-sage" not in pc.list_indexes().names():
            pc.create_index(
                name="medico-sage",
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )
        pinecone_index = pc.Index("medico-sage")
        return pinecone_index 
    
    def create_index(self, docs, pinecone_index):
        vector_store = PineconeVectorStore(pinecone_index=pinecone_index) 
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        index = VectorStoreIndex.from_documents(
            documents=docs,
            storage_context=storage_context)
        return index 
    
    def Query_engine(self,index,query):
        query_engine = index.as_query_engine()
        response = query_engine.query(query)
        return response
    
    

if __name__ == "__main__":
    medico_sage = MedicoSage()
    docs = medico_sage.load_data("data")
    pinecone_index = medico_sage.vector_store()
    index = medico_sage.create_index(docs, pinecone_index)
    query = "what is the symptoms of covid-19"
    response = medico_sage.Query_engine(index,query)
    print(response)

    

        
        
