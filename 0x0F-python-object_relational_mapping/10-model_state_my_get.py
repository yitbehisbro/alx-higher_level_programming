#!/usr/bin/python3
""" prints the State object with the name passed as argument
from the database hbtn_0e_6_usa """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    search = "{:s}".format(sys.argv[4])

    states = session.query(State).filter(State.name == search).all()

    if not states:
        print("Nothing")

    for i, state in enumerate(states, start=1):
        if i > 1:
            sys.exit()
        else:
            print("{}".format(state.id))
