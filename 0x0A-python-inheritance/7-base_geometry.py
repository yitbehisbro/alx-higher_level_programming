#!/usr/bin/python3
""" Geometry module """


class BaseGeometry:
    """ A Base Geometry class """

    def area(self):
        """ Method for area calculation """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates integer
            Args:
                name (str): name
                value (int): integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
