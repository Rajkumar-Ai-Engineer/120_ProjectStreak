import spacy 
import gradio as gr

nlp = spacy.load("en_core_web_trf")

text = input("Enter content whatever you think about Something🥰:")

process = nlp(text=text)

print(process)