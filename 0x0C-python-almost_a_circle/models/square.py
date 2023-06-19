#!/usr/bin/python3

""" Module that defines the square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Function that initializes the square instance """

        super().__init__(size, size, x, y, id)

    def __Str__(self):
        """ Function that returns the str representation of the Square """

        return ('[Square] ({}) {}/{} - {}'
                .format(self.id, self.x, self.y, self.idwidth))
