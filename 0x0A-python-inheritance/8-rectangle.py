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
        self.__width = width
        self.__height = height
        self.integer_validator(width, height)

    def integer_validator(self, width, height):
        """ Validates integer
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be positive integer")
        if height < 0:
            raise ValueError("height must be positive integer")
