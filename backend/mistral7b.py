import streamlit as st
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Load environment variables from .env (safe to keep for local use)
load_dotenv()

# Use environment variable instead of Streamlit secrets
HF_TOKEN = os.getenv("HF_TOKEN")

def convert_with_mistral_7b(code):
    client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.2", token=HF_TOKEN)
    prompt = f"Convert the following C# code to Java:\n\n{code}\n\nJava Code:"
    response = client.text_generation(
        prompt, 
        max_new_tokens=512, 
        temperature=0.3, 
        top_p=0.95
    )
    return response.strip()
