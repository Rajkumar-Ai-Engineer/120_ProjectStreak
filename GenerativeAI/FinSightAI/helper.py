from llama_index.core import VectorStoreIndex, StorageContext, Document as LlamaIndexDocument,load_index_from_storage
from llama_index.vector_stores.chroma import ChromaVectorStore
import os 
from dotenv import load_dotenv
load_dotenv()
import threading 
import traceback 
from logger_mode import logger
from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_index.core import Settings 
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from langchain_community.document_loaders import PyPDFLoader, TextLoader
import chromadb


class FinSightAI:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_GENAI_API_KEY")
        self.llm = GoogleGenAI(api_key=self.api_key,model="gemini-1.5-flash")
        self.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
        self.db = chromadb.PersistentClient(path="./db")
        self.collection = self.db.get_or_create_collection("my_collection")
        self.vector_store = ChromaVectorStore(chroma_collection=self.collection)
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
        
    def load_data(self,file_path):
        data = ""
        try:
            if os.path.exists(file_path):
                if os.path.isfile(file_path):
                    if file_path.endswith(".txt"):
                       data = TextLoader(file_path).load()
                    elif file_path.endswith(".pdf"):
                        data = PyPDFLoader(file_path).load()
                    else:
                        return "Unsupported file format"
                else:
                    return "It is not a file"
            else:
                return "File does not exist"
        except Exception as e:
            print(f"Error Caught:{e}")
            logger.error(traceback.format_exc())
            return ""
        return data
    
    def split_documents(self,documents):
        try:
            splited_documents = self.splitter.split_documents(documents)
        except Exception as e:
            print(f"Error Caught:{e}")
            logger.error(traceback.format_exc())
            return ""
        return splited_documents
    
    def _convert_to_llama_index_documents(self, langchain_documents):
        """Convert LangChain documents to LlamaIndex documents"""
        llama_documents = []
        for i, doc in enumerate(langchain_documents):
            doc_id = getattr(doc, 'id', None)
            if not doc_id:
                doc_id = f"doc_{i}"
            llama_doc = LlamaIndexDocument(
                text=doc.page_content,
                metadata=doc.metadata,
                id_=doc_id
            )
            llama_documents.append(llama_doc)
        return llama_documents
            
    def create_index(self,documents):
        try:
            # Convert LangChain documents to LlamaIndex documents
            llama_documents = self._convert_to_llama_index_documents(documents)
            index = VectorStoreIndex.from_documents(llama_documents,storage_context=self.storage_context)
            return index
        except Exception as e:
            print(f"Error Caught:{e}")
            logger.error(traceback.format_exc())
            return ""
    
    def load_index(self):
        vector_Index = VectorStoreIndex.from_vector_store(vector_store=self.vector_store,
                                                          embed_model=self.embed_model)
        return vector_Index
      
    def query_engine(self,index,query):
        try:
            query_engine = index.as_query_engine()
            response = query_engine.query(query)
            return response
        except Exception as e:
            print(f"Error Caught:{e}")
            logger.error(traceback.format_exc())
            return ""
        
    def process_query(self,query: str, file_path: str):
            # Load and process data
        data = self.load_data(file_path)
        if isinstance(data, str) and "Error" in data:
            return data
        
        # Split documents
        split_data = self.split_documents(data)
        if not split_data:
            return "Failed to split documents"
        
        # Create index
        index = self.create_index(split_data)
        if not index:
            return "Failed to create index"
        
        
        result = self.query_engine(index, query)
        if not result:
            return "Failed to get query result"
        
    
        
if __name__ == "__main__":
    obj = FinSightAI()
    # path = "attention.pdf"
    # data = obj.load_data(path)
    # splited_data = obj.split_documents(data)
    # index = obj.create_index(splited_data)
    index = obj.load_index()
    query = input("Enter your query:")
    response = obj.query_engine(index,query)
    print(response)

    


        

    


        