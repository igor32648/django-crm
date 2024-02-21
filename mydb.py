#install mysql
#pip install mysql
#pip install mysql-connector or mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)

#prepare a cursor object

cursorObject = dataBase.cursor()

#create a databade

cursorObject.execute("CREATE DATABASE django_crm")

print("DB done!")