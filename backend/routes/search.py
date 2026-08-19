####################################################
###DEBTOR SEARCH FIELDS. THIS WILL SHOW THE OUTPUT##
####################################################

from pydantic import Basemodel
from typing import Optional

class SearchDebtor(BaseModel):
    name = str
    city = str
    province = str
    phone = Optional[str] = None
    employer = Optional[str] = None
    email = Optional[str] = None
    