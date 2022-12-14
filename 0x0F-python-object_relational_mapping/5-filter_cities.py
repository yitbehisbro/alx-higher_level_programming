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
    sql_cmd = "SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = %(state)s"
    conn_cursor.execute(sql_cmd, {"state": sys.argv[4]})
    query_rows = conn_cursor.fetchall()

    print(", ".join([state[1] for state in query_rows]))
