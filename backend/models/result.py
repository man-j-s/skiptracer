from backend.database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Boolean
from datetime import datetime

class Result(Base):
    __tablename__ = "results" #Debtor's search results.
    id = Column(Integer, primary_key = True)
    search_id = Column(Integer, ForeignKey("searches.id"), nullable=False)
    type = Column(String, nullable=False)
    url = Column(String)
    is_inferred = Column(Boolean)
    confidence = Column(Float)
    found_at = Column(DateTime, default=datetime.utcnow)
