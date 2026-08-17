from fastapi import FastAPI
from backend.database import Base, engine
from backend.models.user import User
from backend.models.search import Search #use name of class, not table
from backend.models.result import Result #shows the search results
from backend.models.email import Email
from backend.routes.auth import router as auth_router


app = FastAPI()
Base.metadata.create_all(bind = engine)
app.include_router(auth_router)

# ***************************************************
# ** IMPORTANT COMMANDS **
# Activate virtual environment:
# venv\Scripts\activate

# Start the server:
# python -m uvicorn backend.main:app --reload

# Connect to PostgreSQL:
# psql -U postgres -d skiptracer

# Check tables in PostgreSQL:
# \dt

# Exit PostgreSQL:
# \q

# TEST USER 
# {
#   "name": "Test User 2",
#   "email": "test2@test.com",
#   "password": "test123"
# }
# TEST USER After TOKEN 
# {
#   "name": "Test User 3",
#   "email": "test3@testmail.com",
#   "password": "password123"
# }
# ****************************************************