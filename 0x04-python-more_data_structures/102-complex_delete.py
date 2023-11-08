#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for k, val in a_dictionary.items():
        if val == value:
            del new[k]
    return new
