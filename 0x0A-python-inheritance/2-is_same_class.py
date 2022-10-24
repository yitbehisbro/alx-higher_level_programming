#!/usr/bin/python3
""" Exact same object """


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly an instance
    of the specified class ; otherwise False """
    return True if isinstance(obj, a_class) else False
