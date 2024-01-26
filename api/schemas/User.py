from typing import List
from pydantic import BaseModel
from .Profile import Profile
from sqlmodel import Field, Session, SQLModel, create_engine


# class UserCreate(BaseModel):
#     email: str

class User(BaseModel):
    id: int= Field(default=None, primary_key=True)
    email: str
    profile: Profile=Field(default=None)

    # class Config:
    #     orm_mode = True

class UserCreate(BaseModel):
    email: str

    class Config:
        from_attributes = True

