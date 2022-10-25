#!/usr/bin/python3
""" From JSON string to Object """


def from_json_string(my_str):
    """ Returns an object (Python data structure)
    represented by a JSON string
    """
    import json as js
    result = js.loads(my_str)
    return result
