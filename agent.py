import os

import requests
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("MODEL_NAME")
URL = os.getenv("LLM_BASE_URL")

if not MODEL or not URL:
    raise ValueError("Missing MODEL_NAME or LLM_BASE_URL in .env")

def call_llm(prompt: str) -> str:


    payload = {
        "model": MODEL,
        "input": prompt,
        "temperature": 0.3,
        "max_output_tokens": 20000,
        "stream": False,
    }

    response = requests.post(URL, json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()

    full_response = ""
    for item in data.get("output", []):
        if item.get("type") == "message":
            content = item.get("content", "")
            full_response += content

    if not full_response:
        print("\n[DEBUG] full_response is empty!")

    return full_response
