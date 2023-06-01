import mysql.connector


def create():
    mydb = mysql.connector.connect(
        host="localhost",
        user="Tyler",
        password="Blackrobin7",
        database="music"
    )

    mycursor = mydb.cursor()

    # Execute the SHOW TABLES query
    mycursor.execute("SHOW TABLES")

    # Fetch all the table names
    tables = mycursor.fetchall()
    file = open("html/player/final.html", "a")
    # Print the table names
    for table in tables:
        file.write(table[0])

    # Close the cursor and connection
    mycursor.close()
    mydb.close()
    file.close()
