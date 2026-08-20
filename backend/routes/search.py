####################################################
###DEBTOR SEARCH FIELDS. THIS WILL SHOW THE OUTPUT##
####################################################

from pydantic import BaseModel
from typing import Optional
from fastapi import Depends, APIRouter
from backend.routes.auth import get_current_user
from backend.models.user import User

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
    return{"name" : request.name,  "city":request.city, "user": user_verify.email }
