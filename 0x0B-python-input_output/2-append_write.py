#!/usr/bin/python3

""" Module of a function that opens a file with append permissions """


def append_write(filename="", text=""):
    """ function to add text in a file opened with appened permission """

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
