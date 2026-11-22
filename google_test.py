from backend.config import GOOGLE_SEARCH_ENGINE_ID, GOOGLE_API_KEY
import requests

requests.get("https://www.googleapis.com/customsearch/v1?key="GOOGLE_API_KEY":"i insert serch engine id here")

response = response.status_code