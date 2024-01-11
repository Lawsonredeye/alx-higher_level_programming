#!/usr/bin/python3
"""
module that contains a class and several modules
"""


class Student:
    """
    class Student that defines a student by
    name and age
    """

    def __init__(self, first_name, last_name, age):
        """
        initialize the class and the object

        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function that returns the dictionary
        description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object.

        Args:
            obj: any object value

        Return:
            new dict: new dictionary value like json
        """

        new_dict = {}
        for name, value in vars(self).items():
            if type(value) in [str, bool, int, list, dict]:
                new_dict[name] = value
        return new_dict
