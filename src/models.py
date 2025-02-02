import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planeta(Base):
    __tablename__ = 'planetas'
    
    id_planeta = Column(Integer, primary_key=True, nullable=False)
    tipo_planeta = Column(String(250), nullable=False)
    ubicacion = Column(String(250), nullable=False)

    personajes = relationship("Personaje", back_populates="planeta")

class TipoPersonaje(Base):
    __tablename__ = 'tipos_personajes'
    
    id_tipo = Column(Integer, primary_key=True, nullable=False)
    tipo_personaje = Column(String(250), nullable=False)
    civilizacion = Column(String(250), nullable=False)

    personajes = relationship("Personaje", back_populates="tipo")

class Personaje(Base):
    __tablename__ = 'personajes'
    
    id_personaje = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(250), nullable=False)
    id_planeta = Column(Integer, ForeignKey('planetas.id_planeta'))
    id_tipo = Column(Integer, ForeignKey('tipos_personajes.id_tipo'))
    
    planeta = relationship("Planeta", back_populates="personajes")
    tipo = relationship("TipoPersonaje", back_populates="personajes")
    naves = relationship("NaveEspacial", back_populates="piloto")

class NaveEspacial(Base):
    __tablename__ = 'naves_espaciales'
    
    id_nave = Column(Integer, primary_key=True, nullable=False)
    tipo_nave = Column(String(250), nullable=False)
    id_personaje = Column(Integer, ForeignKey('personajes.id_personaje'))
    
    piloto = relationship("Personaje", back_populates="naves")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
