import json
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

# Load environment
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(model="openai/gpt-oss-120b")

# Load JSON template (system prompt comes from here)
with open("template.json", "r", encoding="utf-8") as f:
    prompt_data = json.load(f)

system_prompt = prompt_data["messages"][0]["content"]

# Use a single input field for simplicity
user_prompt = "{quiz_input}"

# Build template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", user_prompt)
])

# Memory (tracks conversation)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    input_key="quiz_input",
    return_messages=True
)

# Chain with memory
chain = LLMChain(
    prompt=prompt_template,
    memory=memory,
    llm=llm,
    verbose=True
)

# Function to start the quiz
def run_quiz(topic, num_questions, valuation, delivery_mode, level="easy", real_time_quiz_tool=False):
    initial_input = (
        f"topic: {topic}\n"
        f"num_questions: {num_questions}\n"
        f"valuation: {valuation}\n"
        f"delivery_mode: {delivery_mode}\n"
        f"level: {level}\n"
        f"real_time_quiz_tool: {real_time_quiz_tool}"
    )
    response = chain.invoke({"quiz_input": initial_input})
    return response["text"]

# Function to send user answers back to the AI
def answer_quiz(user_ans,result):
    response = chain.invoke({"quiz_input": f"My answer: {user_ans} for the quiz {result}"})
    return response["text"]

# Main interactive loop
if __name__ == "__main__":
    print("✅ MCQ Generator Interface Started\n")

    # Collect quiz setup
    topic = input("Enter quiz topic: ")
    num_qs = int(input("How many questions? "))
    valuation = "one_by_one"  # could also be "all_at_once"
    delivery_mode = "quiz"

    # Start quiz
    result = run_quiz(topic, num_qs, valuation, delivery_mode)
    print("\nGenerated Quiz:\n", result)

    # Answer loop
    while True:
        user_ans = input("\nYour Answer (or type 'exit' to quit): ")
        if user_ans.lower() == "exit":
            print("👋 Exiting quiz. Goodbye!")
            break

        follow_up = answer_quiz(user_ans,result)
        print("\nAI Response:\n", follow_up)


