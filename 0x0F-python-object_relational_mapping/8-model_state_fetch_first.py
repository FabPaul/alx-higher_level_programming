#!/usr/bin/python3

""" Script that prints the first State objects from the DB hbnb_0e_6_usa"""

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

    states = session.query(State).order_by(State.id).first()

    for state in states:
        if state is not None:
            print("{}: {}".format(state.id, state.name))
        else:
            print('Nothing')

    session.close()
