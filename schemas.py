from pydantic import BaseModel

#users model
class UserCreate(BaseModel):
    name: str
    age: int

class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True  # allows ORM model to convert into JSON


#product model
class ProductCreate(BaseModel):
    name: str
    price: float
    description:str |None=None

class ProductResponse(ProductCreate):
    id: int
    class Config:
        orm_mode = True  # allows ORM model to convert into JSON