#!/usr/bin/python3

def raise_exception():
    raise TypeError("Exception raised")

# Test case
try:
    raise_exception()
except TypeError:
    print("Exception raised")