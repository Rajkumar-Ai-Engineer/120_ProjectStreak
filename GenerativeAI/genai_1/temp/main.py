from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from langflow.interface.loading import load_flow_from_json 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

app.post("/run-flow")
async def run_flow(request:Request):
    data = await request.json()
    flow_json = data["flow"]
    input_text = data["input"]
    

    try:
        chain = load_flow_from_json(flow_json)
        result = chain.invoke({"input": input_text})
        return {"output": result}
    except Exception as e:
        return {"output": f"Error: {str(e)}"}