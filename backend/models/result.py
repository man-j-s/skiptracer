from backend.database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Boolean
from datetime import datetime

class Result(Base):
    __tablename__ = "results" #Debtor's search results.
    id = Column(Integer, primary_key = True)
    search_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    city = Column(String)
    province = Column(String)
    phone = Column(String)
    employer = Column(String)
    email = Column(String) #email is search parameter so nullable=True/False not used here, no point.
    searched_at = Column(DateTime, default=datetime.utcnow)
