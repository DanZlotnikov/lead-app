import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE leads (id integer PRIMARY KEY, full_name text, phone_number integer, email text)')
print ("Table created successfully")
conn.close()