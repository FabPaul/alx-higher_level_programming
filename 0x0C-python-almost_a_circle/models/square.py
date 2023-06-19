#!/usr/bin/python3

""" Module that defines the square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Function that initializes the square instance """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Function that returns the str representation of the Square """

        return ('[Square] ({}) {}/{} - {}'
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ To retrieve the size of the sqaure """

        return self.width

    @size.setter
    def size(self, value):
        """ To set the size the size of the square """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Function that assigns attributes """

        if args:
            names_of_att = ['id', 'size', 'x', 'y']

            for i, j in enumerate(args):
                setattr(self, names_of_att[i], j)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Function that returns the dictionary representation of Rectangle"""

        dictionary = {'id': self.id, 'width': self.width,
                      'x': self.x, 'y': self.y}
        return dictionary
