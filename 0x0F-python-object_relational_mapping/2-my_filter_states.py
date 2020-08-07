#!/usr/bin/python3
"""
SelectStates module
"""
import MySQLdb
import sys


def find_state():
    """Finds states with the given name in database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )
    cur = db.cursor()
    cur.execute("SELECT *\
                FROM states\
                WHERE name = %(searched_name)s\
                ORDER BY id ASC",
                {'searched_name': searched}
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    find_state()
