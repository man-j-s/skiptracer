####################################################
###DEBTOR SEARCH FIELDS. THIS WILL SHOW THE OUTPUT##
####################################################

from pydantic import BaseModel
from typing import Optional
from fastapi import Depends, APIRouter
from backend.routes.auth import get_current_user
from backend.models.user import User
from backend.models.search import Search
from backend.database import SessionLocal

router = APIRouter()

class SearchDebtor(BaseModel):
    name : str
    city : str
    province : str
    phone : Optional[str] = None
    employer : Optional[str] = None
    email : Optional[str] = None

@router.post("/search")
def search(request : SearchDebtor, user_verify : User = Depends(get_current_user)):
    db = SessionLocal()
    new_search = Search(user_id = user_verify.id, name = request.name, email = request.email, city = request.city, province = request.province, phone = request.phone, employer = request.employer)
    db.add(new_search)
    db.commit()
    return{"search_id" : new_search.id, "name" : request.name,  "city":request.city, "user": user_verify.email }

