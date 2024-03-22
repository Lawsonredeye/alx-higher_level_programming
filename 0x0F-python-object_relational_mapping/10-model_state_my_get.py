#!/usr/bin/python3
"""
Script that connects to a database and prints its values
"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter_by(name=sys.argv[4]).first()
    if query is not None:
        print(query.id)
    else:
        print('Not found')
