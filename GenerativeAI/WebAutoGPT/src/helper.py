import os 
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from dotenv import load_dotenv
load_dotenv()
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.readers.zyte_serp import ZyteSerpReader
from llama_index.readers.web import ZyteWebReader
from llama_index.core import VectorStoreIndex, Settings, Document

zerp_api_key = os.getenv("zyteserp_api_key")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize embedding model (use HuggingFace as default)
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

if openai_api_key and openai_api_key != "YOUR_OPENAI_API_KEY_HERE":
    try:
        Settings.llm = OpenAI(model="gpt-4o", api_key=openai_api_key, default_headers={}, logprobs=False)
    except Exception as e:
        print(f"Warning: Could not initialize OpenAI: {e}")
else:
    print("Warning: OpenAI API key not configured properly") 

if zerp_api_key and zerp_api_key != "YOUR_ZYTE_API_KEY_HERE":
    zerpReader = ZyteSerpReader(api_key=zerp_api_key)
    zerpWebReader = ZyteWebReader(api_key=zerp_api_key)
else:
    print("Warning: Zyte API key not configured properly")
    zerpReader = None
    zerpWebReader = None

def RealTimeSearch(query: str):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        search_url = f"https://www.google.com/search?q={quote(query)}"
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        results = []
        for g in soup.find_all('div', class_='g')[:5]:
            title_elem = g.find('h3')
            link_elem = g.find('a')
            snippet_elem = g.find('span', class_=['aCOpRe', 'st'])
            
            if title_elem and link_elem:
                title = title_elem.get_text()
                link = link_elem.get('href')
                snippet = snippet_elem.get_text() if snippet_elem else ""
                results.append(f"{title}\n{link}\n{snippet}")
        
        print(f"Real-time search found {len(results)} results")
        return results
    except Exception as e:
        print(f"Real-time search error: {e}")
        return []

def Reader(query:str):
    try:
        if not zerpReader:
            print("Zyte SERP Reader not initialized, using real-time search")
            return RealTimeSearch(query)
        
        result = zerpReader.load_data(query=query)
        if not result:
            print("No results from Zyte, falling back to real-time search")
            return RealTimeSearch(query)
            
        print(len(result))
        for res in result[:4]:
            print(res.text)
            print(res.metadata)
        return [r.text for r in result]
    except Exception as e:
        print("Error Caught:",e)
        print("Falling back to real-time search")
        return RealTimeSearch(query)
    finally:
        print("Reader Process is completed Successfully")
        
def DirectScrape(urls):
    try:
        documents = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        for url in urls[:3]:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()[:2000]  # Limit text length
            documents.append(Document(text=text, metadata={"source": url}))
        print(f"Direct scraping got {len(documents)} documents")
        return documents
    except Exception as e:
        print(f"Direct scraping error: {e}")
        return []
        
def WebReader(urls):
    try:
        if not zerpWebReader:
            print("Zyte Web Reader not initialized, using direct scraping")
            return DirectScrape(urls)
        if not urls:
            print("No URLs provided")
            return []
        documents = zerpWebReader.load_data(urls)
        if not documents:
            print("No documents from Zyte, trying direct scraping")
            return DirectScrape(urls)
        print(len(documents))
        return documents
    except Exception as e:
        print("Error Caught:",e)
        print("Falling back to direct scraping")
        return DirectScrape(urls)
    finally:
        print("WebReader completed Successfully")
    
def QueryEngine(query:str,documents):
    try:
        if not documents:
            print("No documents provided for indexing")
            return "No documents available to query"
        if not openai_api_key or openai_api_key == "YOUR_OPENAI_API_KEY_HERE":
            print("OpenAI API key not configured")
            return "OpenAI API key required for querying"
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        response = query_engine.query(query)
        return response
    except Exception as e:
        print("Error Caught:",e)
        return f"Error processing query: {str(e)}"
    finally:
        print("finished Successfully")
        
def run(query1:str,query2:str):
    reader = Reader(query1)
    webreader = WebReader(reader)
    engine = QueryEngine(query=query2,documents=webreader)
    return engine
    
if __name__ == "__main__":
    reader_query = input("Enter your reader query:")
    reader = Reader(reader_query)
    webreader = WebReader(reader)
    query = input("Enter your reader query:")
    engine = QueryEngine(query=query,documents=webreader)
    print(engine)