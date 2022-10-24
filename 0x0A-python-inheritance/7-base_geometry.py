#!/usr/bin/python3
""" Geometry module """


class BaseGeometry:
    """ A Base Geometry class """
    def area(self):
        """ Method for area calculation """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates integer """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
