# routers/user.py
# from sql_app import 
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session
from utils import crud
from sql_app.db import SessionLocal
import sql_app.models as models
import sql_app.schemas as schemas
# print(models)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/', response_model=list[schemas.User])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip,limit)
    return users
    # return {'users': ['a', 'b', 'c']}
@router.post('/create')
def create_user(user: schemas.UserCreate, profile: schemas.Profile, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user= crud.create_user(db, user)
    profile = crud.create_user_profile(db, profile, user.id)
    return user

@router.put('/update')
def update_user():
    return

@router.put('/delete')
def delete_user():
    return

