import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password??2005'
    )

cursor = mydb.cursor()
cursor.execute('CREATE DATABASE Students')
mydb.cursor= "Students"

cursor.execute('CREATE TABLE Students (name VARCHAR(255), age INT,)')
cursor.execute('INSERT INTO Students (name, age) VALUES ("Manantsoa", 25)')

