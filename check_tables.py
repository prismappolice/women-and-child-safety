import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("All tables in the database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
for table in tables:
    print(table[0])

conn.close()
