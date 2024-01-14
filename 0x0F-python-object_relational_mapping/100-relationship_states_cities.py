#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttt"""


import sys
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    states = session.query(State, City).all()
    for state in states:
        print(state.id)
    session.close()
