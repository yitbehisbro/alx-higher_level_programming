#!/usr/bin/python3
""" Student to JSON module"""


class Student:
    """ Students class """
    def __init__(self, first_name, last_name, age):
        """ Initalization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary description """
        dict_l = {}
        if type(attrs) is list:
            for obj in attrs:
                if type(obj) is not str:
                    return self.__dict__.copy()
            for i in range(len(attrs)):
                for j in self.__dict__.copy():
                    if attrs[i] == j:
                        dict_l[j] = self.__dict__.copy()[j]
            return dict_l
        return self.__dict__.copy()
