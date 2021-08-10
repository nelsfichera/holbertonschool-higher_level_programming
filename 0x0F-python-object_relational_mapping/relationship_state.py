#!/usr/bin/python3
'''store base sub class for obj def'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''state class'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    __relKwargs = {"cascade": "all, delete-orphan", "backref": "state"}

    cities = relationship("City", **__relKwargs)
