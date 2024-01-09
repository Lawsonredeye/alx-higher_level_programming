#!/usr/bin/python3
"""
Module that just prints to the stdout returning the list of a specific
object being passed
"""


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object

    Args:
        obj: any object at all

    Return:
        List: a list of all available attribute
    """
    return dir(obj)
