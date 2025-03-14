# For Creating Database in MySQL
# This is optional, you can create database from MySQL Workbench or any other MySQL GUI tool.

import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost", #Your my Sql Hostname " This is my hostname, you have to put your hostname here"
    user="root",    #Your my Sql Username " This is my username, you have to put your username here"
    passwd="Anuj@yadav1"  #Your my Sql Password " This is my password, you have to put your password here"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database created successfully")
