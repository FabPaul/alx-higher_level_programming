#!/usr/bin/python3

""" Module for a function that reads a text file and prints to stdout """


def read_file(filename=""):
    """ function to read a text file """

    with open(filename, encoding='utf-8') as f:
        """ Open a file with utf-8 unicode & close it without my permission """

        print(f.read(), end='')
