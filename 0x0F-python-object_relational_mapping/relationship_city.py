#!/usr/bin/python3
""" SQLAlchemy class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from relationship_state import Base


class City(Base):
    """ Defination for the database """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
