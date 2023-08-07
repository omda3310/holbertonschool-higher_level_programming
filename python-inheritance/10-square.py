#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initialisation"""

    def __init__(self, size):
        """Square constructor"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of Square"""
        return self.__size * self.__size
