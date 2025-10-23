from langgraph.graph import StateGraph, START, END, add_messages
import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from autogen import UserProxyAgent, AssistantAgent
from IPython.display import display, Image
load_dotenv()

class State(TypedDict):
    message: Annotated[list, add_messages]

graph_builder = StateGraph(State)
assistant_agent = AssistantAgent(
    name="assistant",
    llm_config={
        "model": "llama3-8b-8192",
        "base_url": "https://api.groq.com/openai/v1",
        "api_key": os.getenv("GROQ_API_KEY"),
        "temperature": 0.7,
        }
    )
user = UserProxyAgent("user", code_execution_config={"use_docker": False})

def chatbot(state: State):
    last_message = state["message"][-1]
    user.initiate_chat(assistant_agent, message=last_message)
    return state

graph_builder.add_node("Chatbot", chatbot)
graph_builder.add_edge(START, "Chatbot")
graph_builder.add_edge("Chatbot", END)

graph = graph_builder.compile()

path_img = "graph.png"

if not os.path.exists(path_img):
    with open(path_img,'wb') as img_file:
        img_file.write(graph.get_graph().draw_mermaid_png())
    print(f"Image is Saved in the path of {os.path.join(os.getcwd(),path_img)}")
else:
    print("Image is  Already Saved!...")

output = graph.invoke({"message": {"role": "user", "content": "Hello, how are you?"}})

