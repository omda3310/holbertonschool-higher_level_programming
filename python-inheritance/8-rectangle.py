#!/usr/bin/python3
"""Geometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from
    Methods:
          __init__(self, width, height)
    """

    def __init__(self, width, height):
        """Initialisation Rectangle
        Args:
            width (int): private
            height (int): private
        """

        super().intger_validator(self, "width", width)
        self.__width = width
        super().integer_validator(self, "height", height)
        self.__height = height
