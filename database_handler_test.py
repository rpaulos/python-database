import mysql.connector

# Make a connection with the DB
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="pytest_db"
)

print(mydb)

# Used to execute statements
mycursor = mydb.cursor()

# Creates a DB called pytest_db
mycursor.execute("CREATE DATABASE pytest_db")

# Shows all the DB in MySQL
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# Create a table 
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")