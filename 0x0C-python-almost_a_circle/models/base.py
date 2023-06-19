#!/usr/bin/python3

""" Module of a function that defines the Base Class. """


class Base:
    """ The base class function """

    __nb_objects = 0


    def __init__(self, id=None):
        """Function that initializes a new instance of the base class """

        if id is not None:
            self.id = id

        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
