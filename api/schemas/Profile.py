from typing import List
from pydantic import BaseModel
from sqlmodel import Field

class Profile(BaseModel):
    id: int= Field(default=None, primary_key=True)
    name: str
    description: str
    owner_id: int

    class Config:
        from_attributes = True
 
class ProfileCreate(BaseModel):
    name: str
    description: str
    owner_id: int
