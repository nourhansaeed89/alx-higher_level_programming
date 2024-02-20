#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
        cursor = conn.cursor()

        # Execute SQL query to select states with matching name
        cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

        # Fetch all rows
        states = cursor.fetchall()

        # Close connection
        cursor.close()
        conn.close()

        # Display results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)
