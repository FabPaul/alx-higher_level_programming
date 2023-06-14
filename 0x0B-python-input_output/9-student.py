#!/usr/bin/python3

""" Module of a function that defines a Class Student some some attributes """


class Student:
    """ A class student which will have some specific attributes """

    def __init__(self, first_name, last_name, age):
        """ initializing the student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Function that retireves the dict representation of the student """

        return self.__dict__
