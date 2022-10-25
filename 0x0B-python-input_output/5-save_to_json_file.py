#!/usr/bin/python3
""" Save Object to a file """


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using a
    JSON representation
    """
    import json as js
    with open(filename, 'w', encoding="utf-8") as a_files:
        a_files.write(js.dumps(my_obj))
