#!/usr/bin/python3
"""
commentttttttttttttttttttttttttt
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC",
                (argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    conn.close()
