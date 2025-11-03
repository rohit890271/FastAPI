from sqlalchemy import Column, Integer, String,Float,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"  # table name in DB

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    password=Column(String , nullable=False)

    products = relationship("Product",back_populates="owner")


class Product(Base):
    __tablename__ = "products" 

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String,nullable=False)
    price=Column(Float,nullable=False)
    description=Column(String)
    owner_id =Column(Integer,ForeignKey("users.id"))

    owner=relationship("User",back_populates="products")