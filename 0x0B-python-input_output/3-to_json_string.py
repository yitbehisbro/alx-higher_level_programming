#!/usr/bin/python3
""" To JSON string module """


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string)
    """
    import json as js
    result = js.dumps(my_obj)
    return str(result)
