from autogen import AssistantAgent,UserProxyAgent
from helper import FinSightAI
import os 
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")

llm_config = {
            "model": "llama3-8b-8192",
            "base_url": "https://api.groq.com/openai/v1",
            "api_key": api_key,
            "temperature": 0.7,
}

obj = FinSightAI()

Agent = AssistantAgent(
    name="FinSightAI",
    system_message="You are a financial analyst. Analyze the finance report results and provide insights.",
    llm_config=llm_config
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    code_execution_config=False
)

def process_query(query: str, file_path: str):
    # Load and process data
    data = obj.load_data(file_path)
    if isinstance(data, str) and "Error" in data:
        return data
    
    # Split documents
    split_data = obj.split_documents(data)
    if not split_data:
        return "Failed to split documents"
    
    # Create index
    index = obj.create_index(split_data)
    if not index:
        return "Failed to create index"
    
    # Query the engine
    result = obj.query_engine(index, query)
    if not result:
        return "Failed to get query result"
    
    
    user_proxy.initiate_chat(
        Agent,
        message=f"Analyze this financial report result: {result}"
    )
    
    return result

if __name__ == "__main__":
    query = "What are the key financial insights?"
    file_path = "data.txt"
    result = process_query(query, file_path)


