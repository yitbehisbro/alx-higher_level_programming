#!/usr/bin/python3
""" The module that adds two integers.
"""


def add_integer(a, b=98):
    """ Method that accepts integer or float.
    But,
        Returns: the casted integer only.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
