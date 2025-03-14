# For Creating Database in MySQL
# This is optional, you can create database from MySQL Workbench or any other MySQL GUI tool.

import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Anuj@yadav1"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database created successfully")
