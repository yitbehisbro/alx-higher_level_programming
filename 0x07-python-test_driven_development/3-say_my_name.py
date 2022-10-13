#!/usr/bin/python3
""" Say my name
"""


def say_my_name(first_name, last_name=""):
    """ Prints My name is <first name> <last name>
    """

    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    elif type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
