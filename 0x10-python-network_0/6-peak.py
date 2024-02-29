#!/usr/bin/python3


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    low, high = 0, len(list_of_integers) - 1
    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1
