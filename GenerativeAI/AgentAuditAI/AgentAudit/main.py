from autogen import AssistantAgent,UserProxyAgent 
from dotenv import load_dotenv
load_dotenv()
from langsmith.evaluation import evaluate 
from langsmith import traceable,Client
from langsmith.run_helpers import get_tracing_context
import threading 
import os
from logs import logger
import traceback

# llm_config = {
#     "model":"deepseek-r1-distill-llama-70b",
#     "base_url":"https://api.groq.com/openai/v1",
#     "api_key": os.getenv("GROQ_API_KEY"),
#     "temperature":0.5
# }

llm_config = {
    "model": "gpt-3.5-turbo",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "temperature": 0.5
}




class AgentAudit:
    def __init__(self,llm_config):
        self.llm_config = llm_config
        self.langsmith_client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))
        
        
    def worker_agent(self,agent_name="Code_assistant"):
        try:
            working_agent = AssistantAgent(name=agent_name,system_message="you are a helpful assistant for code Creation",llm_config=llm_config)
        except Exception as e:
            logger.error(traceback.format_exc())
            return None
        return working_agent
    
    def meta_agent_auditor(self,auditor_name="Evaluator"):
        try:
            meta_agent = UserProxyAgent(name=auditor_name,system_message="You are an Evaluator agent.you will assess the outputs of assistant agents based on reasoning,correctness and efficiency.",
                                human_input_mode="NEVER",llm_config=llm_config,code_execution_config={"use_docker":False})
        except Exception as e:
            logger.error(traceback.format_exc())
            return None
        return meta_agent

evaluator = AgentAudit(llm_config=llm_config)
   
    
@traceable(name="Meta-Evaluation", client=evaluator.langsmith_client, project_name="agentaudit")   
def evaluate_task(task: str):
    print("[Evaluation] Starting Agent Sandbox...")

    meta_agent = evaluator.meta_agent_auditor()
    worker_agent = evaluator.worker_agent()
    if meta_agent is None or worker_agent is None:
        logger.error("Failed to initialize agents. Aborting evaluation.")
        return None

    meta_agent.initiate_chat(
        worker_agent,
        message=task,
        max_turns=2
    )
    print("[Evaluation] Completed Successfully..")

    

    result = None
    # try:
    #     trace_info = get_tracing_context()
        
    #     run_id = trace_info["parent"].id if trace_info else None
    #     print(f"[LangSmith] Run ID: {run_id}")

    #     if run_id:
    #         print("run_id processed")
    #         result = evaluate(
    #             target="Use a recursive function to calculate factorial.",
    #             run_ids=[run_id],
    #             evaluation_name="AgentAuditPro-Eval",
    #             evaluators=["correctness", "helpfulness", "conciseness"],
                
    #         )
    #         print("\n--- Evaluation Result ---")
    #         print(result)
    #     else:
    #         print("[Evaluation] No run_id found. Skipping evaluation step.")
    # except Exception as e:
    #     logger.error(f"Evaluate error: {e}")
    #     result = None

    # return result




if __name__ == "__main__":
    task = input("Enter your task:🤖")
    result =evaluate_task(task)
    