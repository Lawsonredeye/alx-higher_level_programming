#!/usr/bin/python3
"""
Contains a function that loads a json string into a
python object data-type using the json module
"""


import json


def from_json_string(my_str):
    """
    This function uses the json module to load
    a json string into a python
    object using the json.loads
    (s because we are loading a string and not a file)

    Args:
        my_str (string): it takes a multi-line string as
        an argument and then convert it into a python object
    """
    return json.loads(my_str)
