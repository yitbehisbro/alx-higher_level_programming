#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ Display a peak """
    if len(list_of_integers) <= 0:
        return None
    else:
        a_peak = list_of_integers[0]
        for i in list_of_integers:
            if i >= a_peak:
                a_peak = i
    return a_peak
