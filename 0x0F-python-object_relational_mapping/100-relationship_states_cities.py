#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'
    .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

newerState = State(name='California')
newerCity = City(name='San Francisco')
newerState.cities.append(newerCity)

session.add(newerState)
session.add(newerCity)
session.commit()
