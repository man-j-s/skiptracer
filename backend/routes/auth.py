from fastapi import APIRouter, HTTPException
from backend.database import SessionLocal
from backend.models.user import User
from passlib.context import CryptContext
from pydantic import BaseModel
from jose import jwt
from backend.config import SECRET_KEY

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

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    db = SessionLocal()
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found")
    if not pwd_context.verify(request.password, user.password):
        raise HTTPException(status_code = 401, detail = "Incorrect password")
    token_data = {"sub": user.email}
    token = jwt.encode(token_data, SECRET_KEY, algorithm = "HS256")
    return{"access_token": token, "token_type": "bearer"}



