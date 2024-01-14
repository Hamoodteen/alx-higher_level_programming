#!/usr/bin/python3
# commentttttttttttttttttttttttttttttt


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()
states = session.query(State).order_by(State.id).all()
for state in states:
    print("{}: {}".format(state.id, state.name))
session.close()
