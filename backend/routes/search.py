####################################################
###DEBTOR SEARCH FIELDS. THIS WILL SHOW THE OUTPUT##
####################################################

from pydantic import BaseModel
from typing import Optional
from fastapi import Depends

class SearchDebtor(BaseModel):
    name : str
    city : str
    province : str
    phone : Optional[str] = None
    employer : Optional[str] = None
    email : Optional[str] = None

@router.post("/search")
def search(request : SearchDebtor):
