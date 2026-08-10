from sqlalchemy import create_engine, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
