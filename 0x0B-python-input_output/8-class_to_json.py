#!/usr/bin/python3
"""
module that seems just like json
"""


def class_to_json(obj):
    """
    Write a function that returns the dictionary
    description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj: any object value

    Return:
        new dict: new dictionary value like json
    """
    new_dict = {}
    for name, value in vars(obj).items():
        if type(value) in [str, bool, int, list, dict]:
            new_dict[name] = value
    return new_dict
