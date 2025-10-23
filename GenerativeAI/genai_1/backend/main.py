# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
# import tempfile
# import json

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # allow all origins (use specific in prod)
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/run-flow")
# async def run_flow(request: Request):
#     try:
#         data = await request.json()
#         flow = data["flow"]
#         input_text = data["input"]

#         print("=== Full received data ===")
#         print(data)
#         print("\n=== input_text ===")
#         print(input_text)

#         # save flow json for debug
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".json",mode='w') as tmpfile:
#             json.dump(flow, tmpfile)
#             print(f"\n=== Saved flow JSON to {tmpfile.name} ===")

#         # Extract template text and api key
#         prompt_node = next(n for n in flow["nodes"] if n["data"]["type"] == "PromptTemplate")
#         llm_node = next(n for n in flow["nodes"] if n["data"]["type"] == "OpenAI")

#         template_text = prompt_node["data"]["node"]["template"]["template"]["value"]
#         openai_api_key = llm_node["data"]["node"]["template"]["openai_api_key"]["value"]

#         # Build prompt & LLM
#         prompt = PromptTemplate(template=template_text, input_variables=["input"])
#         llm = OpenAI(openai_api_key=openai_api_key, temperature=0.7)

#         # Build chain & run
#         chain = LLMChain(prompt=prompt, llm=llm)
#         result = chain.run({"input": input_text})

#         return {"result": result}

#     except Exception as e:
#         print("\n=== Exception occurred ===")
#         print(e)
#         return {"error": str(e)}
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run-flow")
async def run_flow(request: Request):
    try:
        data = await request.json()
        print("=== Full received data ===")
        print(data)

        flow_json = data["flow"]
        input_text = data["input"]
        print("\n=== input_text ===")
        print(input_text)

        # Extract nodes by type
        prompt_node = next(n for n in flow_json["nodes"] if n["data"]["type"] == "PromptTemplate")
        llm_node = next(n for n in flow_json["nodes"] if n["data"]["type"] in ["ChatOpenAI", "OpenAI"])
        chain_node = next(n for n in flow_json["nodes"] if n["data"]["type"] == "LLMChain")

        # Build prompt
        template_value = prompt_node["data"]["node"]["template"]["template"]["value"]
        prompt = PromptTemplate(input_variables=["input"], template=template_value)

        # Build LLM
        llm_config = llm_node["data"]["node"]["template"]
        model_name = llm_config["model_name"]["value"]
        temperature = float(llm_config["temperature"]["value"])
        api_key = llm_config["openai_api_key"]["value"]

        llm = ChatOpenAI(
            openai_api_key=api_key,
            model_name=model_name,
            temperature=temperature
        )

        # Build chain
        chain = LLMChain(llm=llm, prompt=prompt, verbose=False)

        # Run chain
        result = chain.run({"input": input_text})
        print("\n=== chain result ===")
        print(result)
        # print(type(result))

        return JSONResponse(content={ "output": result })

    except Exception as e:
        print("\n=== Exception occurred ===")
        print(str(e))
        return JSONResponse(content={ "output": f"Error: {str(e)}" })
