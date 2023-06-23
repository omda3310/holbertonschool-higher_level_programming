#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:

    """Improve Geometry"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method validation"""

        if type(value) is not int:
            raise Exception("{} must be an integer".format(name))
        if value <= 0:
            raise Exception("{} must be greater than 0".format(name))
