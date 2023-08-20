#!/usr/bin/python3

"Python script that lists all states from the db hbtn_0e_0usa"

import MySQLdb
import sys

if __name__ = '__main__':

    mysqwl_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQL.connect(host="localhost", port=3306, /
                       user=mysql_username, passwd=mysql_password, db=db_name)

    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states")

    staes = bd_cursor.fetchall()

    for state in states:
        print(states)

    db_cursor.close()
    db.close()
