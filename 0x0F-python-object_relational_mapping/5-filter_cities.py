#!/usr/bin/python3
'''lists all states from database hbtn_0e_0_usa'''

if __name__ == "__main__":
    import MySQLdb
    import re
    from sys import argv

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=arg[2],
                           db=argv[3],
                           charset="utf=8")
    cur = conn.cursor()
    argv[4] = re.sub("[^a-zA-Z0-9]", "", argv[4])
    cur.execute("SELECT cities.name
                FROM cities
                LEFT JOIN states
                ON cities.state_id=states.id
                WHERE states.name=\'{}\'
                ORDER BY cities.id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for x in range(len(query_rows)):
        if x != 0:
            print(", ", end='')
        print("{}".format(query_rows[x][0]), end='')
    print()
    cur.close()
    conn.close()
