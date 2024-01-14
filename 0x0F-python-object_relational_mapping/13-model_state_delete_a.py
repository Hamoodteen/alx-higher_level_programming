#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttt"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    new_name = session.query(State).filter(State.name.like('%a%')).all()
    for state in new_name:
        session.delete(state)
    session.commit()
    session.close()
