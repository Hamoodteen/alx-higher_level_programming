#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttt"""


import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(City.id, City.name, State.name)\
        .join(State, City.state_id == State.id)\
        .order_by(City.id.asc()).all()
    for state in states:
        print(state.id)
    session.close()
