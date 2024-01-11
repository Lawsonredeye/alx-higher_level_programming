#!/usr/bin/python3
"""
This contains a function that turns a json file into an
object data using the json libray as an aid
"""


import json


def load_from_json_file(filename):
    """
    This creates an object from a json file using the json module
    it takes the file name and reads it, retrieves it data and store
    the value in a container and return the converted object data

    Args:
        my_obj (any): python object to be dumped as a json file
        filename (str): path to desired file to store the json dump
    """
    with open(filename, "r", encoding="UTF-8") as f:
        read_data = f.read()
    return json.loads(read_data)
