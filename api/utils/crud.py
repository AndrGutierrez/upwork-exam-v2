from sqlalchemy import Column
from sqlalchemy.orm import Session

from sql_app.db import SessionLocal, engine
from pydantic import BaseModel
import sql_app.models as models
import sql_app.schemas as schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    print("###########")
    user =db.query(models.User).filter(models.User.email == email).first()
    print(user)
    print("$$$$$$$$$$")
    return user 


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profile).offset(skip).limit(limit).all()


def create_user_profile(db: Session, item: schemas.ProfileCreate, user_id: Column[int]):
    db_item = models.Profile(**item.dict(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
