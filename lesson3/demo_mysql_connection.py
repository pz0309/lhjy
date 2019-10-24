import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="M1@crowill"
)

print(mydb)

