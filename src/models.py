import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    
    addresses = relationship("Address", back_populates="person")

class Address(Base):
    __tablename__ = 'address'
    
    id = Column(Integer, primary_key=True, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    post_code = Column(String(250), nullable=False)
    street_name = Column(String(250))
    street_number = Column(String(250))
    
    person = relationship("Person", back_populates="addresses")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
