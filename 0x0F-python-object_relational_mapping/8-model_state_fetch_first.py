#!/usr/bin/python3
"""
Script that connects to a database and prints its values
"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # create the engine
    engine = create_engine(f"mysql://{sys.argv[1]}:"
                           "{sys.argv[2]}/{sys.argv[3]}:3306")
    # create the session and bind it to the engine
    Session = sessionmaker(bind=engine)
    session = Session()
    # fetch the data using session.query.filter
    result = session.query(State).first()
    # print result
    for r in result:
        print(f"{r.id}: {r.name}")
