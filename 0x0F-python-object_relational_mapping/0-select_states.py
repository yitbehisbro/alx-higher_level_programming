#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    conn_cursor = conn.cursor()
    conn_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = conn_cursor.fetchall()
    for row in query_rows:
        print(row)
