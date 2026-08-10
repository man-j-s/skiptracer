from backend.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class User(Base):
    __tablename__ = "users" #Debt Collectors
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
