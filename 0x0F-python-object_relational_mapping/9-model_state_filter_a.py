#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttt"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    mysql = {'drivername': 'mysql+mysqldb',
             'host': 'localhost',
             'port': '3306',
             'username': argv[1],
             'password': argv[2],
             'database': argv[3],
             }
    url = URL(**mysql)
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    states = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
