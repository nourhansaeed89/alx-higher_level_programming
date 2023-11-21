#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
