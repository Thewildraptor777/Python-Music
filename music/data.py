import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Tyler",
    password="Blackrobin7",
    database="music"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Slime")

myresult = mycursor.fetchall()
