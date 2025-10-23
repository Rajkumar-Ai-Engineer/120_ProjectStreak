import os 
from dotenv import load_dotenv
load_dotenv()

agents_config =  [
    {
        "name": "Researcher",
        "role": "AI Research Specialist",
        "goal": "Gather useful facts and data",
        "backstory": "A detail-oriented research expert trained to gather and analyze complex information from various sources to support decision-making.",
        "llm_config": {
            "model": "llama3-8b-8192",
            "base_url": "https://api.groq.com/openai/v1",
            "api_key": os.getenv("GROQ_API_KEY"),
            "temperature": 0.7,
        }
    },
    {
        "name": "Coder",
        "role": "Python Developer",
        "goal": "Write Python code",
        "backstory": "A skilled Python programmer who specializes in building efficient, clean, and scalable code for automation and AI applications.",
        "llm_config": {
            "model": "llama3-8b-8192",
            "base_url": "https://api.groq.com/openai/v1",
            "api_key": os.getenv("GROQ_API_KEY"),
            "temperature": 0.7,
        }
    },
    {
        "name": "Reviewer",
        "role": "Code Quality Analyst",
        "goal": "Check and improve code quality",
        "backstory": "An experienced code reviewer with an eye for detail, ensuring code quality, best practices, and performance optimization.",
        "llm_config": {
            "model": "llama3-8b-8192",
            "base_url": "https://api.groq.com/openai/v1",
            "api_key": os.getenv("GROQ_API_KEY"),
            "temperature": 0.7,
        }
    }
]
