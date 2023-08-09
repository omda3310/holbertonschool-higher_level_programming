#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) != int or type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int or type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
