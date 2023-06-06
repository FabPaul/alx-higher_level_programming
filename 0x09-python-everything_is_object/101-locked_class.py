#!usr/bin/python3
""" A module that prevents users from dynamically creating new instances """


class LockedClass:
    """ Iitializing the class """

    """ __slots__ is the stopper """
    __slots__ = ['first_name']
