from datetime import datetime
from pydantic import BaseModel, Field

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)
    surname: str = Field(max_length=128)
    password: str = Field(min_length=6)

class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    surname: str = Field(max_length=128)
    email: str = Field(max_length=128)

class ProductIn(BaseModel):
    title: str = Field(max_length=32)
    description: str = Field(max_length=512)
    price: float 

class Product(BaseModel):
    id: int
    title: str = Field(max_length=32)
    description: str = Field(max_length=512)
    price: float 

class OrderIn(BaseModel):
    user_id: int
    product_id: int
    date: datetime = Field(default=datetime.now())
    status: bool = Field(default="True")

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    date: str
    status: bool = Field(default="True")
