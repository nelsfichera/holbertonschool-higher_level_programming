#!/usr/bin/python3
'''link to table in db'''

if __name__ == "__main__":
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City
    from sys import argv as av
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://' + '{}'.format(av[1]) +
                           ':{}'.format(av[2]) + '@localhost/' +
                           '{}'.format(av[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    queryTable = session.query(State).order_by(State.id).all()
    for state in queryTable:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
