import sqlite3

conn = sqlite3.connect('database/phonebook-db.db')
print("Opened database successfully")

conn.execute('CREATE TABLE person (name TEXT, second_name TEXT, phone TEXT)')
print("Table created successfully")
conn.close()