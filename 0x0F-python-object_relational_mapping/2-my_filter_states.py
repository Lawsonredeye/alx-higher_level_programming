#!/usr/bin/python3
'''
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
'''
# import sys and mysqldb
# connect to the database with some arguments from CLA
# connect port at 3306
# connect the cursor to a variable
# execute the cursor using
# select * from states where name = "Nevada" order by states.id asc;
# pass in the 4 arg using .format()
# fetchall from the database and print it
# close cursor and database
# wrap code to check for importation excution

import sys
import MySQLdb


def main():
    '''
    Main function which connects the database and also executes
    the command which would handle the printing of the 4th argument
    passes from the CLA which is the name of the record to locate

    The script takes 4 main argument which would be passed to the func
    '''
    db_connect = MySQLdb.connect(host='localhost',
                                 user=sys.argv[1], port=3306,
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    db_cursor = db_connect.cursor()
    # db_cursor.execute("SELECT * FROM states WHERE name = '{}'"
    #                   "ORDER BY states.id ASC".format(sys.argv[4]))
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY states.id ASC".format(sys.argv[4],))
    db_cursor.execute(query)
    db_print = db_cursor.fetchall()
    for row in db_print:
        print(row)
    db_connect.close()


if __name__ == "__main__":
    main()
