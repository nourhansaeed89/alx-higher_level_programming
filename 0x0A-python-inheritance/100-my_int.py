#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """Find the value of int!"""
    def __new__(cls, *args, **kwargs):
        """Creat new arg"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
