#!/usr/bin/python3
"""
module imports json to be used for parsing a data
into a string format
"""


import json
from io import StringIO


def to_json_string(my_obj):
    """
    this function returns the JSON representation of an object (string)

    Args:
        my_obj: any object value

    Return:
        io.getvalue()
    """
    io = StringIO()
    json.dump(my_obj, io)
    return io.getvalue()
