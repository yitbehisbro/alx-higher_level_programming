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
    query = "SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}'".format(sys.argv[4])
    conn_cursor.execute(query)
    query_rows = conn_cursor.fetchall()
    for row in query_rows:
        print(row)
