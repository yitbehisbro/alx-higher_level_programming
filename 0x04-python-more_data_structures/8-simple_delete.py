#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        if key in a_dictionary:
            rm = a_dictionary.get(key)
            del rm
            return a_dictionary
        else:
            return a_dictionary
