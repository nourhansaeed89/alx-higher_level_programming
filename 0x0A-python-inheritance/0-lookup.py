#!/usr/bin/python3
"""Module for lookup"""

def lookup(obj):
    """Look up object.
    Args:
        obj (object): the object of list.

    Returns:
        list: the list of attributes and methods.
    """
    return dir(obj)
