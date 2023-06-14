#!/usr/bin/python3

""" Module of a function that defines a Class Student some some attributes """


class Student:
    """ A class student which will have some specific attributes """

    def __init__(self, first_name, last_name, age):
        """ initializing the student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Function that retireves the dict representation of the student """

        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            """
                If attrs is a list of str, only attribute names
                contained in the list must be retrieved
            """

            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

        """ Otherwise, all attributes must be retrieved """

        return self.__dict__

    def reload_from_json(self, json):
        """ Function that replaces all attributes of student instance """
        for a, b in json.items():
            """
                The items() is used to retrieve a list of key-value
                pairs contained in a list
            """
            setattr(self, a, b)
