import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User_Fav(Base):
    __tablename__ = 'user_Fav'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_id = Column(Integer)
    name = Column(String(50))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    email = Column(String(50))
    password = Column(String(50))
    user_Fav = relationship(User_Fav)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(50))
    rotation_period = Column(Integer)
    orbital_period= Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(50))
    gravity= Column(String(50))
    terrain = Column(String(50))
    population = Column(Integer)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    heigth = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(Integer)
    gender = Column(String(50))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(50))
    model = Column(String(50))
    passengers = Column(Integer)
    consumable = Column(String(50))
    starship_class = Column(String(50))
    length = Column(Integer)
    cargo_capacity = Column(Integer)
    hyperdrive_rating = Column(Integer)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')