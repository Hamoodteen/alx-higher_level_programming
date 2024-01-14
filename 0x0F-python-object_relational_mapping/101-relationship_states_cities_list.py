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
    data = session.query(State).order_by(State.id)
    current_state_id = None
    for city_id, city_name, state_id, state_name in data:
        if state_id != current_state_id:
            if current_state_id is not None:
                print()
            print(f"{state_id}: {state_name}")
            current_state_id = state_id
        print(f"    {city_id}: {city_name}")
    session.close()
