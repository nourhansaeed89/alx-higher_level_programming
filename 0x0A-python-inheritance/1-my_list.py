#!/usr/bin/python3
'''Module for List class.'''


class MyList(list):
    '''Custom MyList class.'''
    def print_sorted(self):
        '''Method for printing.'''
        print(sorted(self))
