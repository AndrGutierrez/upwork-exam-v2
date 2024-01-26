from typing import List
from pydantic import BaseModel

class ProfileBase(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True
 
class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    profile: list[Profile]=[]
    class Config:
        orm_mode = True

