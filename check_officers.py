import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("Officers table structure:")
cursor.execute("PRAGMA table_info(officers)")
structure = cursor.fetchall()
for col in structure:
    print(col)

print("\nCurrent Officers data:")
cursor.execute("SELECT * FROM officers")
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()
