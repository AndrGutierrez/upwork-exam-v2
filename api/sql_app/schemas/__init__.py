"""This module contains the pydantic models for the application."""
from typing import List
from pydantic import BaseModel

# FavoriteProfile
class FavoriteProfileBase(BaseModel):
    user_id: int
    profile_id: int

class FavoriteProfileCreate(FavoriteProfileBase):
    user_id: int
    profile_id: int

class FavoriteProfile(FavoriteProfileBase):
    user_id: int
    profile_id: int
    class Config:
        orm_mode = True

# Profile
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

# User
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    profiles: list[Profile]=[]
    favorite_profiles: list[FavoriteProfile]=[]
    class Config:
        orm_mode = True
