from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")


# Below is work from Google API which didnt work
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
