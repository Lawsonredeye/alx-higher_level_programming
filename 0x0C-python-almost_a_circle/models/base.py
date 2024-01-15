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
        """
        This function initializes the class and it can take an argument
        or no argument, with its default argument being NONE and its also
        an integer.

        Args:
            id (int): Takes int as an argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
