#!/usr/bin/python3

""" Module of a function that returns Python object reprensated by json """

import json


def from_json_string(my_str):
    """ Function to return Python data structure represented by json """

    return json.loads(my_str)
