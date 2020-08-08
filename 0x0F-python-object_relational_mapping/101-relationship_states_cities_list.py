#!/usr/bin/python3
"""
StateCity module
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys


def fetch_states_cities():
    """Fetches states cities"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    for state in session.query(State).all():
        print("{}: {}".format(state.id, state.name))
        for city in session.query(City).\
                filter(City.state_id == state.id).all():
            print("\t{}: {}".format(city.id, city.name))

    session.commit()
    session.close()

if __name__ == "__main__":
    fetch_states_cities()
