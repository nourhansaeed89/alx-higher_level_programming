#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: the size of the square.
            position: the position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute.

        Args:
            value: the new position value.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
