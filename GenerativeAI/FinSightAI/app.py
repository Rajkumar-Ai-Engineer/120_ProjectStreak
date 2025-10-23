import gradio as gr
import os 
from dotenv import load_dotenv
load_dotenv()
from helper import FinSightAI
import requests

obj = FinSightAI()

api_key = os.environ.get("GROQ_API_KEY")

llm_config = {
    "model": "openai/gpt-oss-120b",
    "base_url": "https://api.groq.com/openai/v1",
    "api_key": api_key,
    "temperature": 0.7,        
}

def analyze_with_llm(result):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": llm_config["model"],
        "messages": [
            {"role": "system", "content": "You are a financial analyst. Analyze the provided financial data and give insights."},
            {"role": "user", "content": f"Analyze this financial report: {result}"}
        ],
        "temperature": llm_config["temperature"]
    }
    
    response = requests.post(llm_config["base_url"] + "/chat/completions", headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]

def process_query(query, file_path="data.txt"):
    # Load data
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
    
    # Query engine
    result = obj.query_engine(index, query)
    if not result:
        return "Failed to get result"
    
    # Analyze with LLM
    analysis = analyze_with_llm(str(result))
    
    return f"Query Result: {result}\n\nFinancial Analysis: {analysis}"

def chat_interface(message, history):
    response = process_query(message)
    history.append([message, response])
    return "", history

with gr.Blocks(title="FinSightAI Chat Assistant") as demo:
    gr.Markdown("# FinSightAI - Financial Analysis Chat Assistant")
    
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask about your financial data...")
    clear = gr.Button("Clear")
    
    msg.submit(chat_interface, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()