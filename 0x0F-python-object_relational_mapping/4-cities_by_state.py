#!/usr/bin/python3
'''
lists all cities from the database hbtn_0e_4_usa
usinf execute()
'''
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities JOIN states ON cities.state_id=states.id \
                 ORDER BY cities.id ASC")
    for city in cur.fetchall():
        print(city)
