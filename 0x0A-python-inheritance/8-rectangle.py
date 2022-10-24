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


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Initalization class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
