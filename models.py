from sqlalchemy import Column, Integer, String,Float
from database import Base

class User(Base):
    __tablename__ = "users"  # table name in DB

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


class Product(Base):
    __tablename__ = "products" 

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String,nullable=False)
    price=Column(Float,nullable=False)
    description=Column(String)