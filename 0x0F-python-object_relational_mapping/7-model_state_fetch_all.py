#!/usr/bin/python3

# import the sqlalchemy module
# import the state and base
# import select from sqlalchemy
from sqlalchemy import MetaData, create_engine, Table, Column, Integer, String
import sys
from model_state import Base, State


engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))