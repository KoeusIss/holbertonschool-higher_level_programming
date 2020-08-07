#!/usr/bin/python3
"""
SelectStates module
"""
import MySQLdb
import sys


def main():
    """Grab data from database

    Args:
        argv (tuple): a tuple of given arguments should be:
                    username, password and database
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
