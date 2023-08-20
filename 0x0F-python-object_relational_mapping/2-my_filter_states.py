#!/usr/bin/python3

"""Script that takes an arg and displays in the states table
where name matches arg"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER \
            BY id ASC".format(argv[4]))

    states = db_cursor.fetchall()
    for state in states:
        print(state)

    db_cursor.close()
    db.close()
