#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttt"""


import sys
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    states = session.query(State, City)\
        .filter(State.id == City.state_id)
    for i in states:
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
    session.close()
