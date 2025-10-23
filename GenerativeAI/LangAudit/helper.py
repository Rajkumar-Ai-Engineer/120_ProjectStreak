import os
import hashlib
import csv
import json
from datetime import datetime
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langsmith import Client
from langsmith.evaluation import StringEvaluator
from dotenv import load_dotenv

def load_prompts(file_path="prompts.json"):
     
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            prompts = json.load(f)
            print(f"✅ Loaded prompts from {file_path}")
    else:
        print(f"⚠️ File {file_path} not found. Using default prompts.")
        prompts = {
            "v1": "you are a helpful assistant. Please answer the question: {question}",
            "v2": "you are a highly factual assistant. Please answer the question: {question}",
        }
    return prompts

def compute_prompt_hash(prompt_text: str) -> str:
    """Compute MD5 hash of prompt text."""
    return hashlib.md5(prompt_text.encode()).hexdigest()

def get_user_question():
    """
    Prompt user for a question to ask.
    """
    question = input("📝 Enter your question to audit: ").strip()
    if not question:
        raise ValueError("Question cannot be empty!")
    return question

def grading_function(prediction, reference):
    """
    Very simple grading: score 1 if 'paris' in answer (case-insensitive).
    """
    return {"score": 1 if "paris" in prediction.lower() else 0}

def main():
    # Load env vars
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY_1")
    PROJECT_NAME = os.getenv("project")

    if not GROQ_API_KEY or not LANGSMITH_API_KEY or not PROJECT_NAME:
        raise EnvironmentError("Missing required env vars in .env file.")

    # Initialize LangSmith client
    client = Client(api_key=LANGSMITH_API_KEY)

    # Load prompts
    prompts = load_prompts()

    # Initialize LLM
    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0.1,
        api_key=GROQ_API_KEY
    )

    # Ask user for question
    question = get_user_question()
    inputs = {"question": question}

    evaluator = StringEvaluator(grading_function=grading_function)
    audit_results = []

    for version, prompt_text in prompts.items():
        prompt_hash = compute_prompt_hash(prompt_text)
        prompt = ChatPromptTemplate.from_template(prompt_text)

        # Modern chain: prompt | llm
        chain = prompt | llm

        # Run
        output = chain.invoke(inputs)

        # Extract answer text
        if isinstance(output, dict) and "content" in output:
            answer = output["content"]
        elif hasattr(output, "content"):
            answer = output.content
        else:
            answer = str(output)

        # Evaluate
        eval_result = grading_function(answer, "Paris")
        hallucination_score = eval_result.get("score", 0)

        # Append to audit log
        audit_results.append({
            "timestamp": datetime.utcnow().isoformat(),
            "version": version,
            "prompt_hash": prompt_hash,
            "output": answer,
            "hallucination_score": hallucination_score
        })

        print(f"\n[Version: {version}]")
        print(f"Prompt Hash: {prompt_hash}")
        print(f"Output: {answer}")
        print(f"Hallucination Score: {hallucination_score}")

    # Save audit log
    log_file = "prompt_audit_log.csv"
    file_exists = os.path.isfile(log_file)
    with open(log_file, mode='a', newline='', encoding="utf-8") as csvfile:
        fieldnames = ["timestamp", "version", "prompt_hash", "output", "hallucination_score"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerows(audit_results)

    print(f"\n✅ Audit finished. Results saved to: {log_file}")

if __name__ == "__main__":
    main()
