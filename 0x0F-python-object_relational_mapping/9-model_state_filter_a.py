#!/usr/bin/python3

""" Script that prints State with letter a objects from the DB hbnb_0e_6_usa"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    """
    Checks if the script is being run as the main program. If it is,
    access the DB and extract the States
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_string.format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name.contains('a'))

    if states is not None:
        for state in states:
            print("{}: {}".format(state.id, state.name))

    session.close()
