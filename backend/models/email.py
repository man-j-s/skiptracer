from backend.database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Boolean
from datetime import datetime

class Email(Base):
    __tablename__ = "emails" #searching possible email for debtor & saving its search results
    id = Column(Integer, primary_key = True)
    search_id = Column(Integer, ForeignKey("searches.id"), nullable = False)
    email = Column(String, nullable = False)
    is_inferred = Column(Boolean)
    mx_check = Column(Boolean)
    smtp_check = Column(Boolean)
    found_publicly = Column(Boolean)
    confidence = Column(Float)
    found_at = Column(DateTime, default = datetime.utcnow)
