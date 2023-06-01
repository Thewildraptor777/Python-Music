import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='Tyler',
    password='Blackrobin7',
    database='music'
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute the SHOW TABLES query
cursor.execute("SHOW TABLES")

# Fetch all the table names
tables = cursor.fetchall()

# Print the table names
for table in tables:
    print(table[0])

# Close the cursor and connection
cursor.close()
conn.close()