# routers/user.py
from fastapi import APIRouter, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..schemas.User import User, UserCreate
from ..schemas.Profile import Profile
from ..utils import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/', response_model=List[User])
def list_users():
    return
    # return {'users': ['a', 'b', 'c']}
@router.post('/create')
def create_user(user: UserCreate, profile: Profile, db: Session = Depends(get_db)):
    crud.create_user(db, user, profile)
    return user

@router.put('/update')
def update_user():
    return

@router.put('/delete')
def delete_user():
    return

