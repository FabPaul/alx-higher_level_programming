#!/usr/bin/python3

""" This is a module to print names """


def say_my_name(first_name, last_name=""):
    """
    This function returns the name and takes 2 parameters

    Args:
        first_name(str): The first name of the person.
        last_name(str, optional): The last name of the person.

    Raises:
        TypeError: if either 'first_name' or  'last_name' is not a string

        Returns:
            None
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
