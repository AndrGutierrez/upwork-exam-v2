from fastapi import HTTPException
from sqlalchemy import Column
from sqlalchemy.orm import Session

import sql_app.models as models
import sql_app.schemas as schemas
from . import profile as profile_crud


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_fav_profiles(db: Session, user_id: int):
    return db.query(models.FavoriteProfiles).filter(models.FavoriteProfiles.user_id == user_id)

def get_user_by_email(db: Session, email: str):
    user: schemas.UserBase =db.query(models.User).filter(models.User.email == email).first()
    return user 


def get_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete(db: Session, id: int,  email: str):
    user = get_user(db, id) 
    if not user:
        user= get_user_by_email(db, email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
    db.query(models.FavoriteProfiles).filter(models.FavoriteProfiles.user_id == user.id).delete()
    db.query(models.Profile).filter(models.Profile.user_id == user.id).delete()
    db.query(models.User).filter(models.User.id == user.id).delete()
    db.commit()
    return {"message": "Deleted Successfully"}
    
def update_user(db: Session, user_id: int, data: schemas.UserBase):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = data.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def add_fav_profile(db: Session, user_id: int, profile_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    profile = profile_crud.get_profile(db, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    fav_profile = models.FavoriteProfiles(user_id=user_id, profile_id=profile_id)

    fp = [profile.profile_id for profile in user.favorite_profiles]
    if profile_id in fp:
        raise HTTPException(status_code=400, detail="Profile already in favorites")
    db.add(fav_profile)
    db.commit()
    db.refresh(fav_profile)
    user.favorite_profiles.append(fav_profile)  
    return user
