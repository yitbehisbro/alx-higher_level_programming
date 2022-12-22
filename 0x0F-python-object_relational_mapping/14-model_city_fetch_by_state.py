#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """
import sys
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for s, c in session.query(State, City).filter(State.id ==
                                                  City.state_id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
