from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# Create an interface for the model
iface = gr.Interface(fn=predict, inputs="textbox", outputs="text")
iface.launch()
