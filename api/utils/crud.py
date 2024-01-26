from sqlalchemy.orm import Session

from ..schemas.User import User, UserCreate
from ..schemas.Profile import Profile, ProfileCreate
from ..db import SessionLocal, engine
from pydantic import BaseModel


def get_by_id(db: Session, user_id: int, model):
    return db.query(model).filter(model.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


def list(db: Session, model, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate, profile: Profile):
    db_user = User(email=user.email, profile=profile)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_profile(db: Session, item: ProfileCreate, user_id: int):
    db_item = Profile(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
