import streamlit as st
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Load .env file for local development
load_dotenv()

# Get the Hugging Face token from environment
HF_TOKEN = os.getenv("HF_TOKEN")

def convert_with_codegen2(code):
    prompt = f"Convert the following C# code to Java:\n\n{code}\n\nJava Code:"

    # === Primary: StarCoder ===
    try:
        client = InferenceClient("bigcode/starcoder", token=HF_TOKEN)
        response = client.text_generation(prompt, max_new_tokens=512, temperature=0.3, top_p=0.95)
        return response.strip()
    except Exception as e1:
        print("❌ StarCoder failed:", e1)

    # === Fallback 1: DeepSeek-Coder ===
    try:
        client = InferenceClient("deepseek-ai/deepseek-coder-1.3b-instruct", token=HF_TOKEN)
        response = client.text_generation(prompt, max_new_tokens=512, temperature=0.3, top_p=0.95)
        return "[⚠️ Using fallback: DeepSeek-Coder]\n" + response.strip()
    except Exception as e2:
        print("❌ DeepSeek-Coder failed:", e2)

    # === Fallback 2: CodeGen2-1B ===
    try:
        client = InferenceClient("Salesforce/codegen2-1B", token=HF_TOKEN)
        response = client.text_generation(prompt, max_new_tokens=512, temperature=0.3, top_p=0.95)
        return "[⚠️ Using fallback: CodeGen2-1B]\n" + response.strip()
    except Exception as e3:
        print("❌ CodeGen2-1B failed:", e3)

    return "💥 All model servers are currently unavailable. Please try again later!"
