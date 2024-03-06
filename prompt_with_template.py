import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_community.llms import HuggingFaceEndpoint

huggingface_api_key = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_key

# Mendefinisikan model AI
llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",
    huggingface_api_key= huggingface_api_key
)

# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
prompt = PromptTemplate(
    input_variables=["posisi", "perusahaan", "keterampilan"],
    template="Dear HRD Manager {perusahaan},\n\nWith this letter, I [YOUR NAME], would like to apply for the position {posisi} at {perusahaan}. I have experience in {keterampilan} area. Thank you for considering my application.\n\nSincerely,\n[YOUR NAME]"
)

# Define a function to generate a cover letter using the llm and user input
def generate_cover_letter(posisi: str, perusahaan: str, keterampilan: str) -> str:
    formatted_prompt = prompt.format(posisi=posisi, perusahaan=perusahaan, keterampilan=keterampilan)
    response = llm(formatted_prompt)
    return response

# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Posisi"),
    gr.Textbox(label="Perusahaan"),
    gr.Textbox(label="Keterampilan")
]

# Define the Gradio interface output
output = gr.Textbox(label="Template Surat")

# Launch the Gradio interface
gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(server_name="0.0.0.0", server_port= 7860, share=True)
