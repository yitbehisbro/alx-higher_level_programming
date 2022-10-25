#!/usr/bin/python3
""" Student to JSON module"""


class Student:
    """ Students class """
    def __init__(self, first_name, last_name, age):
        """ Initalization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns the dictionary description """
        return self.__dict__.copy() if hasattr(self, "__dict__") else None
