#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """Define a square"""

    def __init__(self, size):
        """Constructor.

        Args:
            size: the size of the square.
        Raises:
            TypeError: If size not int
            ValueError: If size less zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

