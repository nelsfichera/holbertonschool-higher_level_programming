#!/usr/bin/python3
'''lists all states from database hbtn_0e_0_usa'''

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

   cur = db.cursor()
   cur.execute("SELECT * FROM states ORDER by id")
   [print(state) for state in cur.fetchall()]
