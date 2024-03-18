#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an
argument and lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username,
mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""
# import sys and mysqldb
# connect to db and cursor with the sys.argv where necessary
# execute the cursor and pass the sys.argv[4]
# and store the value in a variable
# print the value from the variable
# close connect()

import sys
import MySQLdb


def main():
    '''
    This handles the execution of the script if the main is excuted
    It takes no argument as a parameter and also use the command line argument
    for working with data.
    '''
    data = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    data_cursor = data.cursor()
    data_cursor.execute("SELECT cities.name FROM states "
                        "LEFT JOIN cities ON cities.state_id = states.id "
                        "WHERE states.name = %s "
                        "order by cities.id ASC", (sys.argv[4],))
    query_rows = data_cursor.fetchall()
    for row in query_rows:
        print(row)
    data.close()


if __name__ == "__main__":
    main()
