#!/usr/bin/python3
"""Same object"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly 
    an instance of the specified class 
    """
    return type(obj) is a_class
