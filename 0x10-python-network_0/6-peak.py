#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    Find the peak integer in a given list of integers.

    Parameters:
        list_of_integers (list): A list of integers.

    Returns:
        int or None: The peak integer if found, None if the list is empty.
    """
    peak_integer = 0
    if len(list_of_integers) == 0:
        return None
    else:
        for integer in list_of_integers:
            if integer > peak_integer:
                peak_integer = integer
        return peak_integer
