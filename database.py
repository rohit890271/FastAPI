from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL connection URL
# Format: postgresql://username:password@host:port/database_name
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal class to create session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# ✅ Add this here
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
