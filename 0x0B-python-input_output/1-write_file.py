#!/usr/bin/python3


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
