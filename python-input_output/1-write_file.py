#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """Writing to a file"""
    with open(filename, mode='w', encoding='utf-8') as fl:
        return fl.write(text)
