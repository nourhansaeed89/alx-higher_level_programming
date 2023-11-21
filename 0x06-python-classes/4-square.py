#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: the size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute.

        Args:
            value: the new size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
