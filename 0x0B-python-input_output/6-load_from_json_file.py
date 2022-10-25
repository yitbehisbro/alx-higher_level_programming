#!/usr/bin/python3
""" Create object from a JSON file """


def load_from_json_file(filename):
    """ Creates an Object from a JSON file """
    import json as js
    with open(filename, 'r', encoding="utf-8") as c_file:
        return js.load(c_file)
