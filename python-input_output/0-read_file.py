#!/usr/bin/python3
"""Read file method"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding='utf-8') as fl:
        for l in fl:
            print(l, end='')
