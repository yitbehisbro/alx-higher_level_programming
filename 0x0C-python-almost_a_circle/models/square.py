#!/usr/bin/python3
""" And now, the Square! module file """
from . import rectangle


class Square(rectangle.Rectangle):
    """ Subclass for Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constractor """
        self.x = x
        self.y = y
        super().__init__(size, size, self.x, self.y, id)

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ String repersentation """
        text = "".join("[Square] ({}) {}/{} - {}".format(
            self.id, super().x, super().y, super().width))
        return text

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        attributes = ['id', 'size', 'x', 'y']
        dict_result = {}

        for key in attributes:
            if key == 'size':
                dict_result[key] = getattr(self, 'width')
            else:
                dict_result[key] = getattr(self, key)

        return dict_result
