#!/usr/bin/python3

""" Module of a function that defines the Base Class. """

import json
import csv
import os


class Base:
    """ The base class function """

    __nb_objects = 0


    def __init__(self, id=None):
        """Function that initializes a new instance of the base class """

        if id is not None:
            self.id = id

        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Function that converts dict to json string """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Func that writes json string representation of list_obj to a file"""

        filename = cls.__name__ + '.json'
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Function that converts JSON string to Dictionary lists """

        if json_string is None or len(json_string) == 0:
            return []

        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Function that returns an instance with all attr set """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)

        elif cls.__name__ == 'Square':
            dummy = cls(1)

        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instances """

        filename = cls.__name__ + '.json'
        try:
            with open(filename) as f:
                json_data = f.read()

                if json_data:
                    data = cls.from_json_string(json_data)
                    return [cls.create(**item) for item in data]

                else:
                    return []

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes list_objs to CSV and saves to a file """

        filename = cls.__name__ + '.csv'
        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)

            if list_objs is not None:
                for objs in list_objs:
                    writer.writerow(objs.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializ instances from CSV and returns lists of instances """

        filename = cls.__name__ + '.csv'
        try:
            with open(filename, newline='') as f:
                reader = csv.reader(file)

                instance = []
                for row in reader:
                    single_instance = cls.create(*row)
                    instance.append(single_instance)
                return instance
        except FileNotFoundError:
            return []
