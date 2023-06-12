#!/usr/bin/python3

"""
    Module that returns True is an object is an instance of a class inherited
    directly or indirectly from the specified class, otherwise, False
"""


def inherits_from(obj, a_class):
    """
        Check if an object is indirectly or directly inherited from a class

        Args:
            obj: Object
            a_class: class object

        Returns:
            True: if the object is directly or indirectly inherited
                from specified class
            False: if the object is not directly or indirectly inherited
                from a specified class
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
