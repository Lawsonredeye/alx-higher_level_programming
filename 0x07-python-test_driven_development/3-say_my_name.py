#!/usr/bin/python3
"""
this module has a function that just prints to the standard output
when called

function name: say_my_name()
Returns: nothing
"""


def say_my_name(first_name, last_name=""):
    """
    This function just prints the first name and last name

    Args:
        first_name: string value parameter
        last_name: string value parameter

    Return:
        Nothing

    Raises:
        TypeError: last_name or first_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
