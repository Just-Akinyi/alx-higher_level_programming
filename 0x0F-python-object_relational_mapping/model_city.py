#!/usr/bin/python3
"""
Contains City class
"""
from sqlalchemy import Column, Integer, String, MetaData
from model_state import Base

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=True, Foreignkey("states.id"))
