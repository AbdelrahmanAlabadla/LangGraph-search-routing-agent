import requests
import os
from dotenv import load_dotenv

load_dotenv()

def web_search(query:str):
    SERPER_API_KEY=os.getenv("SERPER_API_KEY")

    if not SERPER_API_KEY:
        raise ValueError("SERPER_API_KEY not found in environment variables")
    url="https://google.serper.dev/search"

    payload={
        "q":query
    }

    headers={
        "X-API-KEY":SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    response=requests.post(url,json=payload,headers=headers, timeout=30)
    response.raise_for_status()
    data=response.json()

    results=[]
    for item in data.get("organic",[]):
        results.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet")
        })
    return results


