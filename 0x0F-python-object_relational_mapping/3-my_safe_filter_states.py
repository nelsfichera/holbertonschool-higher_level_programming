#!/usr/bin/python3
'''filters queries by name of state safe injection'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    c = db.cursor()
    c.execute(
        """SELECT * FROM states
        WHERE name=%s
        ORDER BY 'states.id' ASC;""", (sys.argv[4], )
    )
    record = c.fetchall()
    for row in record:
        print("({}, \'{}\')".format(row[0], row[1]))
    c.close()
    db.close()
