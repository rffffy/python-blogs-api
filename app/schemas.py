import email
from pydantic import BaseModel, EmailStr
from datetime import datetime

# Post Schema
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


# Post Response Schema
class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# User Schema
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# User Response Schema
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str