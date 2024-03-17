#!/usr/bin/python3
'''
Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
'''
# import sys and Mysqldb
# connect to the mysql database and store the value in a variable
# connect to localhost and a port of 3306
# connect db to a cursor and execute the cursor using
# SELECT * FROM states WHERE name LIKE 'N%' ORDER BY state.id ASC;
# store cursor in variable and loop through the var
# close cursor and database()
# wrap entire function in a main and add import check

import sys
import MySQLdb


def main():
    '''
    This handles the execution of the script if the main is excuted
    It takes no argument as a parameter and also use the command line argument
    for working with data.
    '''
    db_connect = MySQLdb.connect(host='localhost',
                                 port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    print_row = db_cursor.fetchall()
    for row in print_row:
        print(row)
    db_cursor.close()
    db_connect.close()


if __name__ == "__main__":
    '''
    This checks if the script is
    running as main or also if its imported as a module into another module
    '''
    main()
