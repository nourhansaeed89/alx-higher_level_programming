#!/usr/bin/python3
"""Module for lookup"""

def lookup(obj):
    """Return a list of available attributes and methods of an object.
    Args:
        obj (object): the object of list

    Returns:
        list: the list of att
    """
    return dir(obj)
