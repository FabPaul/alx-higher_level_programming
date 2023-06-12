#!/usr/bin/python3

"""
    Module of a function that returns a list of available methods
    and objects in a function
    """


def lookup(obj):
    """
        Function to return available attributes and methods in an object.

        Args:
            obj: The objec

        Returns:
            A list of object
    """

    return dir(obj)
