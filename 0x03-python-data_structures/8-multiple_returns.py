#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size == 0:
        result = None
    else:
        result = sentence[0]
    return size, result
