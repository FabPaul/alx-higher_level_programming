#!/usr/bin/python3

""" Module for function to open file with write permissions """


def write_file(filename="", text=""):
    """ Function to open file and write a string to it """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
