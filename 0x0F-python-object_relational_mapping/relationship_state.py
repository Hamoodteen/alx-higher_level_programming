#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """commenttttttttttttttttttttttttttttttt"""
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
