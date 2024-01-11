#!/usr/bin/python3
"""
This module contains a function that saves a python
object into a json file taking two parameters
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This takes two parameters, a file and an object and then
    save the json object as a json file

    Args:
        my_obj (any): python object to be dumped as a json file
        filename (str): path to desired file to store the json dump
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json_data = json.dumps(my_obj)
        print(json_data)
        f.write(json_data)
