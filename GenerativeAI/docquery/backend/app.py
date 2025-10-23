from fastapi import FastAPI, UploadFile, Form
from langserve import add_routes
from ragchain import build_from_pdf, build_from_url, build_from_qa_chain
import uvicorn
import shutil
import os

app = FastAPI(
    title="DocQuery API",
    description="API for Document Querying using LangChain and LlamaIndex"
)

qa_chain = None
routes_registered = False  

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile):
    try:
        save_path = f"./uploads/{file.filename}"
        os.makedirs("./uploads", exist_ok=True)

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        retriever = build_from_pdf(pdf_directory="./uploads")

        global qa_chain, routes_registered
        qa_chain = build_from_qa_chain(retriever)

        if not routes_registered:
            add_routes(app, qa_chain, path="/qA")
            routes_registered = True

        return {"message": "PDF uploaded and indexed successfully", "filename": file.filename}
    
    except Exception as e:
        print(f"❌ Error during upload: {e}")
        return {"message": f"Upload failed with error: {str(e)}"}

@app.post("/index_url/")
async def index_url(url: str = Form(...)):
    retriever = build_from_url(url=url)  # ✅ this is a retriever, not an index

    global qa_chain, routes_registered
    qa_chain = build_from_qa_chain(retriever)  # ✅ pass retriever, not index
    print("✅ QA Chain built:", qa_chain)

    if not routes_registered:
        add_routes(app, qa_chain, path="/qA")
        routes_registered = True

    return {"message": "URL indexed successfully", "url": url}

@app.get("/")
async def root():
    return {
        "message": "Welcome to the DocQuery API. Use /upload_pdf/ to upload a PDF or /index_url/ to index a URL."
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, log_level="info", reload=True)
