
import mysql.connector
def connect(host , username, password,db_name,sql_function):
        
    database = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=db_name
    )

    mycursor = database.cursor()

    mycursor.execute(sql_function)

    myresult = mycursor.fetchall()
       
    database.close()
    mycursor.close()
    return myresult
