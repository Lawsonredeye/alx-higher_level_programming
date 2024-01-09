#!/usr/bin/python3
"""
function that returns True if the object is an
instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    checks if the object is a subclass of our
    selected class

    Args:
        obj: desired object instance
        a_class: comparing class
    """
    return (issubclass(type(obj), a_class) != (type(obj) is a_class))
