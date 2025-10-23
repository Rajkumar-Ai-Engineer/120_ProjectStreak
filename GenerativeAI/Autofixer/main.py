import streamlit as st 
from google import genai 
import os 
import re
from langchain.prompts import PromptTemplate 
from langchain_groq import ChatGroq

api_key = os.environ.get("GROQ_API_KEY") 

template = """
You are a helpful assistant that fixes the errors in the code.
Code: {code}
Error: {error}
Fixed Code:
"""

prompt = PromptTemplate(
    input_variables=["code", "error"],
    template=template
)

llm = ChatGroq(model="deepseek-r1-distill-llama-70b",)

chain = prompt | llm

def fix_code(code, error):
    response = chain.invoke({"code": code, "error": error})
    print(response)
    
    cleaned_content = re.sub(r'<think>.*?</think>', '', response.content, flags=re.DOTALL)
    cleaned_content = re.sub(r'<[^>]+>', '', cleaned_content)  
    return cleaned_content.strip()


st.title("Code Fixer")
st.write("Enter your code and the error message below:")
code_input = st.text_area("Code", height=300)
error_input = st.text_input("Error Message")
if st.button("Fix Code"):
    if code_input and error_input:
        fixed_code = fix_code(code_input, error_input)
        st.subheader("Fixed Code:")
        st.code(fixed_code, language="python")
    else:
        st.error("Please provide both code and error message.")
        

