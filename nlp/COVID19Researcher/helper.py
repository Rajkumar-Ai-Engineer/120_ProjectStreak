from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from dotenv import load_dotenv
load_dotenv()
import os

class Covid_Researcher:
    
    def __init__(self):
        self.llm_api_key = os.getenv("langchain_api_key")
    def prompt_template(self):
        pass 
    
    def covid_agent(self,text):
        
        covid_research_agent = Agent(
            model = Groq(id="gemma2-9b-it",temperature=0.2,api_key = self.llm_api_key),
            instructions= ["You is a very good Covid virus research and news scrapper about the covid virus.",
                           "You search based on the user needs about covid news and Research",
                           "You only return original research details and the news,you research on many article and websites to take decision.",
                           "you neglect the output of unneccessary details."],
            name="Covid_Agent",
            tools=[GoogleSearch()]
            
        )
        
        response = covid_research_agent.run(text)
        return response
    
    