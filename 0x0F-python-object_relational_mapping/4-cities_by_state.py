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
    cur.execute("SELECT cities.name, cities.id, states.name\
                FROM states, cities\
                WHERE cities.state_id = state.id\
                ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
