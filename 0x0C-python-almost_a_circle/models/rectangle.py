#!/usr/bin/python3
"""Module for Rectangle class"""


from models.base import Base

class Rectangle(Base):
    """Rectangle class, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor for Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
