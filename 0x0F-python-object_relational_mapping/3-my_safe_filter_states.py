#!/usr/bin/python3
'''
Once again, write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name
matches the argument. But this time, write one
that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
'''
# import sys and mysqldb
# connect the database
# create a cursor, and execute the cursor
# make the execute to be safe from SQLI
# print the result
# close cursor and database

import sys
import MySQLdb


def main():
    '''
    Main function which connects the database and also executes
    the command which would handle the printing of the 4th argument
    passes from the CLA which is the name of the record to locate

    The script takes 4 main argument which would be passed to the func
    '''
    data = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    data_cursor = data.cursor()
    data_cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
        (sys.argv[4],)
        )
    print_data = data_cursor.fetchone()
    print(print_data)
    data_cursor.close()
    data.close()


if __name__ == "__main__":
    main()
