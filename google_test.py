from backend.config import GOOGLE_SEARCH_ENGINE_ID, GOOGLE_API_KEY
import requests

params = {
    "key": GOOGLE_API_KEY,
    "cx": GOOGLE_SEARCH_ENGINE_ID,
    "q": "John Smith Toronto",
}

response  = requests.get("https://www.googleapis.com/customsearch/v1, params=params")

print(response.status_code)