#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
        cursor = conn.cursor()

        # Execute SQL query to select all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

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
