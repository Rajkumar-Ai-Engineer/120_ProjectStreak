# from fastapi import FastAPI, HTTPException
# from langchain_openai import ChatOpenAI
# from langserve import add_routes
# from langchain.prompts import ChatPromptTemplate
# from langchain.chains import LLMChain
# import os
# import uvicorn
# from openai import APIError

# # Validate API Key
# if not os.environ.get("OPENAI_API_KEY"):
#     raise ValueError("OPENAI_API_KEY not set!")

# app = FastAPI(title="Pokemon API")

# model = ChatOpenAI(model="gpt-3.5-turbo")

# prompt = ChatPromptTemplate.from_template("Answer briefly: {question}")
# chain = LLMChain(llm=model, prompt=prompt)

# @app.post("/pokemon/ask")
# async def ask_question(question: str):
#     try:
#         response = chain.invoke({"question": question})
#         return response
#     except APIError:
#         raise HTTPException(status_code=503, detail="OpenAI API error")

# add_routes(app, chain, path="/pokemon/ask")

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# from langchain.chains import LLMChain
# import uvicorn

# app = FastAPI()

# # Define Pydantic models for input validation
# class QuestionInput(BaseModel):
#     question: str

# class PokemonInput(BaseModel):
#     pokemon_name: str

# # Initialize model and chains
# model = ChatOpenAI(model="gpt-3.5-turbo")

# prompt1 = ChatPromptTemplate.from_template("Answer: {question}")
# chain1 = LLMChain(llm=model, prompt=prompt1)

# # Create explicit endpoints instead of using add_routes
# @app.post("/pokemon/ask")
# async def ask_question(input: QuestionInput):
#     try:
#         result = chain1.invoke({"question": input.question})
#         return {"response": result["text"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)

from langserve import add_routes 
from fastapi import FastAPI
from langchain_groq import ChatGroq 
import os 
import uvicorn 
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate 
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

app = FastAPI(
    title="Langserve Server",
    version="1.0",
    description= "A simple Api server"
) 

model = ChatOpenAI()

prompt1 = ChatPromptTemplate.from_template("You are a helpful  Pokemon assistant.Answer the question: {question} in a concise manner.")
prompt2 = ChatPromptTemplate.from_template("You are a helpful  Pokemon assistant.Write the pokemon details and the region of the pokemon: {pokemon_name} in a concise manner.")
prompt3 = ChatPromptTemplate.from_template("You are a helpful  Pokemon assistant.Write the pokemon moves,weakness and Pokemon dex data: {pokemon_name} in a concise manner. Also, write the pokemon type and its abilities.")



chain1 = LLMChain(prompt=prompt1,llm=model)
chain2 = LLMChain(prompt=prompt2,llm=model)
chain3 = LLMChain(prompt=prompt3,llm=model)

#Route1 
add_routes(
    app,
    chain1,
    path="/pokemon_assistant",
)

add_routes(
    app,
    chain2,
    path="/pokemon_details",
)

add_routes(
    app,
    chain3,
    path="/pokemon_dex",
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)