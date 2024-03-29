#!/usr/bin/python3
"""a function that creates
an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """Open file to read"""
    with open(filename, "r", encoding="utf-8") as fl:
        return json.load(fl)
