#!/usr/bin/python3
"""
This module contains a function that checks if an object is of the
desired class type
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an
    instance of the specified class ; otherwise False

    Args:
        obj: any type of object
        a_class: any desired class

    Return:
        True: if its same class
        False: if its not the same class
    """

    if type(obj) is a_class:
        return True
    else:
        return False
