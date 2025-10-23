import gradio as gr
import requests

API_URL = "http://localhost:8000"

# Upload PDF
def upload_pdf(file):
    try:
        with open(file.name, "rb") as f:
            files = {'file': (file.name, f, "application/pdf")}
            response = requests.post(f"{API_URL}/upload_pdf/", files=files)
        
        print("Upload response:", response.status_code, response.text)

        if response.status_code == 200:
            return response.json().get("message", "Upload succeeded, but no message received.")
        else:
            return f"❌ Upload failed: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Upload error: {str(e)}"

# Index URL
def index_url(url):
    try:
        data = {'url': url}
        response = requests.post(f"{API_URL}/index_url/", data=data)

        print("Index response:", response.status_code, response.text)

        if response.status_code == 200:
            return response.json().get("message", "URL indexed, but no message received.")
        else:
            
            return f"❌ Indexing failed: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Indexing error: {str(e)}"

# Query Chain
def query_chain(question):
    try:
        # Correct JSON structure for LangServe
        data = {'input': {'query': question}}
        response = requests.post(f"{API_URL}/qA/invoke", json=data)

        print("Query response:", response.status_code, response.text)

        if response.status_code == 200:
            return response.json()['output'].get("result", "No output received.")  # ✅ fixed from "outputs"
        else:
            return f"❌ Query failed: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Query error: {str(e)}"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 📄 DocQuery: Query your documents using LLMs")

    with gr.Tab("📤 Upload PDF"):
        pdf_input = gr.File(label="Upload PDF File", file_types=[".pdf"])
        pdf_output = gr.Textbox(label="Response")
        pdf_button = gr.Button("Upload PDF")
        pdf_button.click(upload_pdf, inputs=pdf_input, outputs=pdf_output)

    with gr.Tab("🔗 Index URL"):
        url_input = gr.Textbox(label="Enter URL")
        url_output = gr.Textbox(label="Response")
        url_button = gr.Button("Index URL")
        url_button.click(index_url, inputs=url_input, outputs=url_output)

    with gr.Tab("💬 Ask Question"):
        question_input = gr.Textbox(label="Enter your question")
        answer_output = gr.Textbox(label="Answer")
        query_button = gr.Button("Get Answer")
        query_button.click(query_chain, inputs=question_input, outputs=answer_output)

demo.launch()
