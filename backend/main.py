from fastapi import FastAPI
from backend.database import Base, engine
from backend.models.user import User

app = FastAPI()
Base.metadata.create_all(bind = engine)
