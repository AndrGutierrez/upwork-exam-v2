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

@router.get('/', response_model=list[schemas.Profile])
def list_profiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    profiles = profile_crud.get_profiles(db, skip,limit)
    return profiles

@router.post('/create', response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    db_profile = profile_crud.get_user_profile(db, user_id=profile.user_id)
    if db_profile:
        raise HTTPException(status_code=400, detail="User already has a profile")
    db_user = user_crud.get_user(db, profile.user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="user desn't exist")

    profile= profile_crud.create_user_profile(db, profile, db_user.id)
    return profile

@router.put('/update',response_model=schemas.ProfileBase)
def update_user(id: int, data: schemas.ProfileBase, db: Session = Depends(get_db)):
    profile=profile_crud.update_profile(db, id, data)
    return profile

@router.delete('/delete')
def delete_user(id: int = 0, db: Session = Depends(get_db)):
    profile_crud.delete(db, id)
    return None



