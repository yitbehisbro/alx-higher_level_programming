#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None and key is not None:
        element = a_dictionary.get(key)
        del element
        return a_dictionary
