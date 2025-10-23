import os
from dotenv import load_dotenv

load_dotenv()
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory.buffer import ConversationBufferMemory
import threading
import json


class MCQGenerator:
    def __init__(self, model_id="openai/gpt-oss-120b", temperature=0.5):
        self.llm_api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(model=model_id, temperature=temperature, api_key=self.llm_api_key,verbose=True)
        self.memory = ConversationBufferMemory(input_key="quiz_input", memory_key="chat_history", return_messages=True)

        try:
            self.load_data = json.load(open("template.json", 'r', encoding="utf-8"))
        except FileNotFoundError:
            print("template.json not found. Using default system message.")
            self.load_data = {
                "messages": [{
                    "content": "You are an expert MCQ generator. Create multiple choice questions based on the given topic, number of questions, difficulty level, and delivery mode. Format the questions clearly with options A, B, C, D and provide explanations for correct answers when evaluating responses."
                }]
            }

        self.user_prompt = "{quiz_input}"
        self.system_message = self.load_data["messages"][0]["content"]
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", self.system_message),
            ("user", self.user_prompt),
        ])
        self.chain = LLMChain(memory=self.memory, llm=self.llm, prompt=self.prompt_template)

    def run_quiz(self, topic, num_questions, valuation, delivery_mode, level="easy", real_time_quiz_tool=False):
        initial_input = (
            f"topic: {topic}\n"
            f"num_questions: {num_questions}\n"
            f"valuation: {valuation}\n"
            f"delivery_mode: {delivery_mode}\n"
            f"level: {level}\n"
            f"real_time_quiz_tool: {real_time_quiz_tool}"
        )
        response = self.chain.invoke({"quiz_input": initial_input})
        return response["text"]

    def answer_quiz(self,user_ans, result):
        response = self.chain.invoke({"quiz_input": f"My answer: {user_ans} for the quiz {result}"})
        return response["text"]

    def initial_process(self):
        try:
            topic = input("Enter your topic: ")
            num_questions = int(input("Enter the number of quizzes needed: "))
            valuation = "one_by_one"
            delivery_mode = "quiz"
            result = self.run_quiz(topic, num_questions, valuation, delivery_mode)
            return result
        except ValueError:
            print("Please enter a valid number for the quiz count.")
            return None
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None

    def quiz_mode(self, quizzes):
        if not quizzes:
            print("No quiz data available.")
            return

        print("\n" + "=" * 50)
        print("QUIZ MODE - Enter your answers or type 'exit' to quit")
        print("=" * 50)

        while True:
            try:
                ans = input("\nType your answer option (A/B/C/D) or 'exit' to quit: ").strip()

                # Fixed the comparison bug here
                if ans.lower() == "exit":
                    print("👋 Exiting quiz. Goodbye!")
                    break

                if not ans:
                    print("Please enter a valid answer or 'exit'.")
                    continue

                follow_up = self.answer_quiz(ans, quizzes)
                print("\nAI Response:")
                print("-" * 30)
                print(follow_up)
                print("-" * 30)

            except KeyboardInterrupt:
                print("\n👋 Quiz interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")


def main():
    """Main function to run the MCQ Generator"""
    try:
        print("🎯 MCQ Generator Starting...")
        print("=" * 40)

        generator = MCQGenerator()
        results = generator.initial_process()

        if results:
            print("\n📋 Quiz Generated Successfully!")
            print("=" * 40)
            print(results)
            print("=" * 40)
            generator.quiz_mode(results)
        else:
            print("❌ Failed to generate quiz. Please try again.")

    except Exception as e:
        print(f"❌ Application error: {e}")


if __name__ == "__main__":
    main()