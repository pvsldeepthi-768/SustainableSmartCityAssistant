from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "ibm-granite/granite-3.3-2b-instruct"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_API_TOKEN)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, token=HF_API_TOKEN).to(device)
model.eval()

def generate_answer(prompt):
    chat_prompt = f"Human: {prompt}\nAssistant:"
    input_tokens = tokenizer(chat_prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        output_tokens = model.generate(**input_tokens, max_new_tokens=200, temperature=0.7, top_p=0.9, do_sample=True)
    response_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    return response_text.split("Assistant:")[-1].strip()
