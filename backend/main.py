from fastapi import FastAPI
from backend.database import Base, engine
from backend.models.user import User
from backend.models.search import Search #use name of class, not table

app = FastAPI()
Base.metadata.create_all(bind = engine)
