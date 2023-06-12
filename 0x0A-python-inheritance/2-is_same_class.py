#!/usr/bin/python3

"""
    Module that returns True if an object is exactly an instance of a class
    otherwise False
"""


def is_same_class(obj, a_class):
    """
        Function that checks if an object is an instance of a class

        Args:
            obj: class object
            a_class: class object

        Returns:
            True: if the object is an instance of a class
            False: if the object is not an instance of a class
    """

    return type(obj) == a_class
