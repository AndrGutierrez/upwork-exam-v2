from fastapi import HTTPException
from sqlalchemy import Column
from sqlalchemy.orm import Session

import sql_app.models as models
import sql_app.schemas as schemas

def get_user_profile(db: Session, user_id: int):
    return db.query(models.Profile).filter(models.Profile.user_id == user_id).first()


def get_profile(db: Session, id: int):
    return db.query(models.Profile).filter(models.Profile.id == id).first()


def get_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profile).offset(skip).limit(limit).all()


def create_user_profile(db: Session, profile: schemas.ProfileBase, user_id: Column[int]):
    
    pf= profile.dict()
    if "user_id" in pf.keys():
        del pf["user_id"]
    db_item = models.Profile(**pf, user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete(db: Session, id: int ):
    profile = get_profile(db, id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    db.query(models.FavoriteProfiles).filter(models.FavoriteProfiles.id == id).delete()
    db.query(models.Profile).filter(models.Profile.id == id).delete()
    db.commit()
    return {"message": "Deleted Successfully"}
    

def update_profile(db: Session, id: int, data: schemas.ProfileBase):
    profile = get_profile(db, id)
    if not profile:
        raise HTTPException(status_code=404, detail="User not found")
    profile_data = data.model_dump(exclude_unset=True)
    for key, value in profile_data.items():
        setattr(profile, key, value)
    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile

