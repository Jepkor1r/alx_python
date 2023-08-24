import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to list states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all rows from the result set
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

