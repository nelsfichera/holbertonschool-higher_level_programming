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
    args = [State.id, State.name, City.id, City.name]
    queryTable = session.query(*args).join(City)
    for row in queryTable:
        print("{}: {} -> {}".format(row[2], row[3], row[1]))
    session.close()
