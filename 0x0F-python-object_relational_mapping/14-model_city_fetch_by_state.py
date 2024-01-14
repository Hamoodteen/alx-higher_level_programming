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
    cities_data = session.query(City.id, City.name, State.name)\
        .join(State, City.state_id == State.id)\
        .order_by(City.id.asc())\
        .all()
    for city_id, city_name, state_name in cities_data:
        print("City ID: {}, Name: {}, State: {}".format(
            city_id, city_name, state_name))
    session.close()
