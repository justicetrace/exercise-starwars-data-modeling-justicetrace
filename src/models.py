import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    def serialize(self):
        return {
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=True)
    orbitable_period = Column(String(250), nullable=True)
    diameter = Column(String(250), nullable=True)

    def serialize(self):
        return {
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbitable_period": self.orbitable_period,
            "diameter": self.diameter
        }
    
class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=True)
    passengers = Column(String(250), nullable=True)
    crew = Column(String(250), nullable=True)

    def serialize(self):
        return {
            'name': self.name,
            'model': self.model,
            'passengers': self.passengers,
            'crew': self.crew
        }
    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    def serialize(self):
        return {
            'name': self.name,
            'eye_color': self.eye_color,
            'gender': self.gender,
        }

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=False)
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'),primary_key=True)
    starships_id = Column(Integer, ForeignKey('starships.id'), primary_key=True)

    user = relationship(User)
    people = relationship(People)
    planets = relationship(Planets)
    starships = relationship(Starships)


    def serialize(self):
        return {
            'user_id': self.user_id,
            'people_id': self.people_id,
            'planets_id': self.planets_id,
            'starships_id': self.starships_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
