from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from ..db import Base

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    user = relationship('User', back_populates='profile')
    favorite_profiles = relationship('FavoriteProfiles', back_populates='profile', cascade='all, delete-orphan')

class FavoriteProfiles(Base):
    __tablename__ = 'favorite_profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    user = relationship('User', back_populates='favorite_profiles')
    profile = relationship('Profile', back_populates='favorite_profiles')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    profile= relationship('Profile', back_populates='user', cascade='all, delete-orphan')
    favorite_profiles = relationship('FavoriteProfiles', back_populates='user', cascade='all, delete-orphan')
