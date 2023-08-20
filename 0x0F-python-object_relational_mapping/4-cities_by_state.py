#!/usr/bin/python3

"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()
    db_cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
          JOIN states ON cities.states_id = states.id ORDER BY cities.id ASC")

    states = db_cursor.fetchall()
    for state in states:
        print(state)

    db_cursor.close()
    db.close()
