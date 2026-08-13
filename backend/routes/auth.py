from fastapi import APIRouter
from backend.database import SessionLocal
from backend.models.user import User
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"]), deprecated="auto"