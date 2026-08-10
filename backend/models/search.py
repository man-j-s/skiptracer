from backend.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

class Search(Base):
    __tablename__ = "searches" #Debtor's search arguments.
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    city = Column(String)
    province = Column(String)
    phone = Column(String)
    employer = Column(String)
    email = Column(String) #email is search parameter so nullable=True/False not used here, no point.
    searched_at = Column(DateTime, default=datetime.utcnow)



