#!/usr/bin/python3
'''lists all states from database hbtn_0e_0_usa'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf=8")
    db.query("""SELECT * FROM states ORDER BY id ASC;""")
    query_rows = db.store_result()
    for row in query_rows.fetch_row(0):
        print(row)
