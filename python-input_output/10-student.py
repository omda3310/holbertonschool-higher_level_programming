#!/usr/bin/python3
"""a class Student"""


class Student:
    """Initialisation of class Student"""
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list and attrs is not None:
            return {attrs: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__
