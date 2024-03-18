#!/usr/bin/python3
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
    db_cursor.execute("select cities.id,cities.name,states.name "
                      "from cities left join states "
                      "on state_id = states.id order by cities.id asc")
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
