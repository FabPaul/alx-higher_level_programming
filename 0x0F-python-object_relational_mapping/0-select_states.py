#!/usr/bin/python3

"Python script that lists all states from the db hbtn_0e_0usa"

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(
      host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states")

    states = db_cursor.fetchall()

    for state in states:
        print(state)

    db_cursor.close()
    db.close()
