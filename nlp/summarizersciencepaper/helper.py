from phi.agent import Agent
import os
from dotenv import load_dotenv
from phi.llm.groq import Groq 
from phi.tools.duckduckgo import DuckDuckGo
load_dotenv()

# Configuration
MODEL_ID = "deepseek-r1-distill-llama-70b"
API_KEY = os.getenv("langchain_api_key")

prompt = """
 
You are a Research Paper Summarizer Agent in the Phi Data Agentic Framework. Your task is to extract and summarize key details from research paper abstracts with structured precision.  

**Input:**  
- User provides a research paper *title*, *DOI*, or *arXiv ID*.  

**Output Format:**  
1. **Title**  
2. **Authors**  
3. **Publication Venue/Year** (if in abstract)  
4. **Objective**: Core research goal (1 sentence).  
5. **Method**: Techniques/datasets used (1–2 sentences).  
6. **Key Findings**: Results (1–2 sentences).  
7. **Significance**: Broader impact (if stated, 1 sentence).  

**Rules:**  
- Be concise (3–5 sentences total).  
- Use neutral academic tone.  
- If the paper is inaccessible, request a direct excerpt or clarify the input.  
- Never hallucinate details; omit unclear sections.  
- Abstracts should be self-contained and understandable without external context.
-Abstracts the DuckDuckgo rate limit is 10 requests per minute, so please be patient if you are making multiple requests.
"""  
 


def ResearchPaperSummarizerAgent(researchpaper:str):
    """Create and return the Research Paper Summarizer agent"""
    researchagent = Agent(
        llm=Groq(model_id=MODEL_ID, api_key=API_KEY),
        tools=[DuckDuckGo()],
        prompt=prompt,
        name="ResearchPaperSummarizerAgent",
        description="An agent that summarizes research paper abstracts and extracts key details."
    )
    res = researchagent.run(researchpaper)
    return res.content


if __name__ == "__main__":
    research_paper = input("Enter the research paper:") # Example research paper URL
    summary = ResearchPaperSummarizerAgent(research_paper)
    print(summary) 
    




 
