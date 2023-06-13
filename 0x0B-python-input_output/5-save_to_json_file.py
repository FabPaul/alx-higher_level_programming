#!/usr/bin/python3

""" Module of a function that writes and saves an Object file """

import json


def save_to_json_file(my_obj, filename):
    """ Function to write an object file to a file """

    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
