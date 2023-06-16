#!/usr/bin/python3

""" Module of a function that inserts \n  to a file after specific string """


def append_after(filename="", search_string="", new_string=""):
    """ Functiont that new line to a text file afyer certain string """

    with open(filename, mode='r') as f:
        """ Open the file in read mode and read the content """

        line = f.readlines()

    with open(filename, mode='w') as f:
        """ Open file in write mode and write the original line to the file """

        for i in line:
            f.write(i)

            """Write the new line after the line with the search string """
            if search_string in i:
                f.write(new_string)
