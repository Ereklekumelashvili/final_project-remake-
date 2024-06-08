import sqlite3

conn = sqlite3.connect('tablee.db')

conn.execute('CREATE table people(name TEXT,email TEXT,password TEXT) ')

conn.close()