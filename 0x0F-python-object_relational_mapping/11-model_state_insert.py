#!/usr/bin/python3
"""
State module
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


def fetch_all():
    """Fetches all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    state = session.add(new_state)
    state = session.query(State).filter_by(name='Louisiana').first()
    print("{}".format(state.id))
    session.commit()
    session.close()

if __name__ == "__main__":
    fetch_all()
