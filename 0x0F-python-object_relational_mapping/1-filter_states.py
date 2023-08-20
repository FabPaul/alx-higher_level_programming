#!/usr/bin/python3

""" Script that lists all states with a name starting with N from db """

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQL.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id")

    states = db_cursor.fetchall()
    for state in states:
        print(state)

    db_cursor.close()
    db.close()
