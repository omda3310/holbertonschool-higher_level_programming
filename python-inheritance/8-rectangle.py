#!/usr/bin/python3
"""Geometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from"""

    def __init__(self, width, height):
        """Initialisation Rectangle"""

        self.intger_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
