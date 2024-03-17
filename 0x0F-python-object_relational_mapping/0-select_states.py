#!/usr/bin/python3

'''
Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password
and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
'''
# import MySQLdb and import sys
# collect the command line arguments which are sys.argv[1] ... argv[3]
# connect to the database with the commands from the command line
# and fill it with the necessary argument
# connect using the port 3306
# create a cursor that would execute the command
# end file with if __name__ == "__main__"

import sys
import MySQLdb


def main():
    '''
    This handles the execution of the script if the main is excuted
    It takes no argument as a parameter and also use the command line argument
    for working with data.
    '''
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    # create a cursor
    db_cursor = db.cursor()
    # execute the cursor
    db_cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = db_cursor.fetchall()
    for row in query_rows:
        print(row)
    # close the connection for the cursor and database
    db_cursor.close()
    db.close()


if __name__ == "__main__":
    '''
    This checks if the script is
    running as main or also if its imported as a module into another module
    '''
    main()
