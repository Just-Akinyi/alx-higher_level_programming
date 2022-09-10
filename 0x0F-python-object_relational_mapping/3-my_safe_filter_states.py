#!/usr/bin/python3
'''
takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument(safe from MySQL injections!)
'''
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    allstates = cur.fetchall()
    for state in allstates:
        if state[1] == argv[4]:
            print(state)
