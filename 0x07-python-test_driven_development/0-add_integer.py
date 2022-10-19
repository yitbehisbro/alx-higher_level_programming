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
    if type(a) not in [int]:
        a = int(a)
    if type(b) not in [int]:
        b = int(b)
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return a + b
