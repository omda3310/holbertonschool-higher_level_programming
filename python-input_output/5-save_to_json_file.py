#!/usr/bin/python3
"""a function that writes an Object to a text file,
using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """save object to file"""
    with open(filename, "w", encoding="utf-8") as fl:
        jstring = json.dump(my_obj)
        fl.write(jstring)
