#!/usr/bin/python3

""" Module of a class Mylist that inherits from a list """


class MyList(list):
    """
        A sub-class that inherist list from another class

        Args: list
    """

    def print_sorted(self):
        """ A function that prints a list sorted in ascending order """

        print(sorted(self))
