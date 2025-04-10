
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def convert_with_mistral_large2(code):
    client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1", token=HF_TOKEN)
    prompt = f"Convert the following C# code to Java:\n\n{code}\n\nJava Code:"
    response = client.text_generation(prompt, max_new_tokens=512, temperature=0.3, top_p=0.95)
    return response.strip()
