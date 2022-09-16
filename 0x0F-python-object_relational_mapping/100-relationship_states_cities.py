#!/usr/bin/python3
"""adds the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], str(sys.argv[2]), sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = State(name='California')
    state.cities = [City(name="San Francisco")]
    session.add(state)
    session.commit()
    session.close()
