#!/usr/bin/python3
"""
This mode is the parent module to all subclasses that would be used
to initialize or keep track of all object instances
"""


class Base:
    """
    Base parent class that would be used to initialize the other
    subclasses.
    It can take in parameters and also decide not to take any parameter

    Args:
        obj: Takes object(as a DEFAULT)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
