import gradio as gr 
from helper import resume_parser 

parser = resume_parser()

def resume_parser_func(image):
    
    if image is None:
        return "Please upload an image."
    
    result = parser.parse_resume(image)
    return result


title = "Resume Parser"
description = "Upload a resume image to extract key information such as name, email, phone, skills, education, and experience."

interface = gr.Interface(
    fn=resume_parser_func, 
    inputs=gr.Image(type="pil", label="Upload Resume Image"), 
    outputs=gr.Textbox(label="Parsed Resume Information"), 
    title=title, 
    description=description, 
    theme="default"
)

interface.launch(share=True, debug=True)
