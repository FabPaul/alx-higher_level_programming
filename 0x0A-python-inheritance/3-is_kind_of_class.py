#!/usr/bin/python3

"""
    Module that returns True if an object is an instance of or if the object
    is an instance of a class that inherited from specified class, else, False
"""


def is_kind_of_class(obj, a_class):
    """
        Function to check the instance of a class object

        Args:
            obj: the object
            a_class: the second element

        Returns:
            True if instance or False if not
    """

    return isinstance(obj, a_class)
