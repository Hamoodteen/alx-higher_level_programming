#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    Base = declarative_base()

    class State(Base):
        """commenttttttttttttttttttttttttttttttt"""
        __tablename__ = 'states'
        id = Column(Integer,
                    primary_key=True,
                    nullable=False,
                    autoincrement=True)
        name = Column(String(128), nullable=False)

    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
