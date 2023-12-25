#!/usr/bin/python3
"""Module for reading a text file."""


def read_file(filename=""):
    """Read and print the contents of a text file."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
