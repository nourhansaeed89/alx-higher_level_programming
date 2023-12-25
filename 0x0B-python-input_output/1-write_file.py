#!/usr/bin/python3
"""Module for reading a text file."""


def write_file(filename="", text=""):
    with open(filename, encoding="utf-8") as file:
        return file.write(text)
