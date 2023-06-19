#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """private instance width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """private instance height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    """print rectangle"""

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
                if i != self.__height - 1:
                    rectangle += "\n"
        return rectangle
