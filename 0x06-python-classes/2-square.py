#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.
    Args:
        size (int): The first parameter.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
