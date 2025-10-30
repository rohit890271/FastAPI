from pydantic import BaseModel
from typing import Optional, List

#users model
class ProductResponse(BaseModel):  # simple nested version for user
    id: int
    name: str
    price: float
    description: Optional[str]  = None
    model_config = {"from_attributes": True}
class UserCreate(BaseModel):
    name: str
    age: int

class UserResponse(UserCreate):
    id: int
    products: List[ProductResponse] = []

    model_config = {"from_attributes": True}


#product model
class ProductCreate(BaseModel):
    name: str
    price: float
    description:str |None=None
    owner_id:int

class ProductResponse(ProductCreate):
    id: int
    model_config = {"from_attributes": True}
    