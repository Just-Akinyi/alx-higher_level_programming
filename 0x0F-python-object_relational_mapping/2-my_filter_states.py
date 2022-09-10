#!/usr/bin/python3
"""
takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))
    allstates = cur.fetchall()
    for state in allstates:
        if state[1] == argv[4]:
            print(state)
