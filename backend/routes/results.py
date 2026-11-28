from fastapi import Depends, APIRouter, HTTPException
from backend.routes.auth import get_current_user
from backend.models.user import User
from backend.models.search import Search
from backend.models.result import Result
from backend.database import SessionLocal

router = APIRouter()
