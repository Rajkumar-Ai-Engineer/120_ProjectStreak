import asyncio
from playwright.async_api import async_playwright
from llama_index.core import VectorStoreIndex, SimpleWebPageReader
from llama_index.tools.agentql import AgentQLBrowserToolSpec
from llama_index.core.llms import OpenAI
from superagi import SuperAGIAgent, BaseTool

# Define a custom Playwright tool for SuperAGI
class PlaywrightScrapeTool(BaseTool):
    def __init__(self):
        self.name = "PlaywrightScrapeTool"
        self.description = "Scrapes web pages using Playwright"

    async def _execute(self, url: str) -> dict:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url)
            content = await page.content()
            title = await page.title()
            await browser.close()
            return {"url": url, "title": title, "content": content}

# Initialize LLM and tools
llm = OpenAI(model="gpt-4o", api_key="YOUR_OPENAI_API_KEY")
playwright_tool = PlaywrightScrapeTool()
agentql_tool = AgentQLBrowserToolSpec()  # LlamaIndex's AgentQL for structured extraction

# Define SuperAGI agent
agent = SuperAGIAgent(
    llm=llm,
    tools=[playwright_tool, agentql_tool],
    name="ResearchAgent",
    goal="Research the history of the internet and summarize findings"
)

# Async function to run the research task
async def run_research_task(urls):
    # Scrape data using Playwright
    scraped_data = []
    for url in urls:
        result = await playwright_tool._execute(url)
        scraped_data.append(result)

    # Load data into LlamaIndex
    documents = SimpleWebPageReader().load_data([data["url"] for data in scraped_data])
    index = VectorStoreIndex.from_documents(documents)

    # Query and summarize
    query_engine = index.as_query_engine(llm=llm)
    summary = query_engine.query("Summarize the history of the internet based on the scraped data.")
    
    # Store or output results (e.g., to a file or Google Docs)
    with open("research_summary.md", "w") as f:
        f.write(str(summary))
    
    return summary

# Run the task
urls = ["https://en.wikipedia.org/wiki/History_of_the_Internet"]
summary = asyncio.run(run_research_task(urls))
print(summary)





import os 
from dotenv import load_dotenv
load_dotenv()
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.readers.zyte_serp import ZyteSerpReader
from llama_index.readers.web import ZyteWebReader
from llama_index.core import VectorStoreIndex, Settings

zerp_api_key = os.getenv("zyteserp_api_key")
openai_api_key = os.getenv("OPENAI_API_KEY")


if openai_api_key and openai_api_key != "YOUR_OPENAI_API_KEY_HERE":
    try:
        Settings.llm = OpenAI(model="gpt-4o", api_key=openai_api_key, default_headers={}, logprobs=False)
        Settings.embed_model = OpenAIEmbedding(api_key=openai_api_key)
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

def Reader(query:str):
    try:
        if not zerpReader:
            print("Zyte SERP Reader not initialized")
            return []
        result = zerpReader.load_data(query=query)
        print(len(result))
        for res in result[:4]:
            print(res.text)
            print(res.metadata)
        return [r.text for r in result]
    except Exception as e:
        print("Error Caught:",e)
        return []
    finally:
        print("Reader Process is completed Successfully")
        
def WebReader(urls):
    try:
        if not zerpWebReader:
            print("Zyte Web Reader not initialized")
            return []
        if not urls:
            print("No URLs provided")
            return []
        documents = zerpWebReader.load_data(urls)
        print(len(documents))
        return documents
    except Exception as e:
        print("Error Caught:",e)
        return []
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

    
    



