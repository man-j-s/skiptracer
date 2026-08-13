from fastapi import APIRouter
from backend.database import SessionLocal
from backend.models.user import User
from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__truncate_error=False)

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("/register")
def register(request: RegisterRequest):
    db = SessionLocal()
    hashed_password = pwd_context.hash(request.password)
    new_user = User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    return{"message": "User registered successfully"}



