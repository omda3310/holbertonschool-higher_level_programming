#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TabError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def heifht(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value > 0:
            raise ValueError("height must be >= 0")
        self.height = value
