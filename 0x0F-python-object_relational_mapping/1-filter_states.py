#!/usr/bin/python3
'''lists all states from database hbtn_0e_0_usa'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv 

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
			   user=argv[1],
			   passwd=arg[2],
			   db=argv[3],
			   charset="utf=8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                 ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
