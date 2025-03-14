import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Anuj@yadav1"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database created successfully")
