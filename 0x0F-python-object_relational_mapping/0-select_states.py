#!/usr/bin/python3
'''lists all states from database hbtn_0e_0_usa'''
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
    c.execute("""SELECT * FROM states ORDER BY states.id ASC;""")
    record = c.fetchall()
    for row in record:
        print("({}, \'{}\')".format(row[0], row[1]))
    c.close()
    db.close()
