#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    print("Nothing" if not state else "{}: {}".format(state.id, state.name))
# #!/usr/bin/python3
# """
# prints the first State object from the database hbtn_0e_6_us
# """
# from model_state import Base, State
# from sqlalchemy import (create_engine)
# from sys import argv
# from sqlalchemy.orm import sessionmaker

# if __name__ == "__main__":
#     engine = create_engine(
#         'mysql+mysqldb://{}:{}@localhost/{}'
#         .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
#     Base.metadata.create_all(engine)

#     Session = sessionmaker(bind=engine)
#     session = Session()

#     for state in session.query(State). \
#             filter(State.id == 1):
#         print("{}: {}".format(state.id, state.name))
#         if state == None:
#             print ("Nothing")
