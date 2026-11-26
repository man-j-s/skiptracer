from backend.config import SERPER_API_KEY
import requests

def serper_search(query):
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json",
    }
    body = {"q": query}
    response = requests.post("https://google.serper.dev/search", headers=headers, json=body)
    data = response.json()
    return data.get("organic", [])