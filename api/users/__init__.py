# routers/user.py
# from sql_app import 
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from sqlalchemy import Column
from sqlalchemy.orm import Session
from utils.crud import user as user_crud, profile as profile_crud
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
    users = user_crud.get_users(db, skip,limit)
    return users
    # return {'users': ['a', 'b', 'c']}
@router.post('/create', response_model=schemas.User)
def create_user(user: schemas.UserCreate, profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user= user_crud.create_user(db, user)
    profile = profile_crud.create_user_profile(db, profile, user.id)
    user.profile=[profile]
    return user

@router.put('/update',response_model=schemas.User)
def update_user(id: int, data: schemas.UserBase, db: Session = Depends(get_db)):
    user=user_crud.update_user(db, id, data)
    return user

@router.delete('/delete')
def delete_user(id: int = 0, email: str = "", db: Session = Depends(get_db)):
    user_crud.delete(db, id, email)
    return None

