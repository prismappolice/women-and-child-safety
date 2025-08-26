import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("About content in database:")
cursor.execute("SELECT * FROM about_content")
results = cursor.fetchall()
for row in results:
    print(row)

print("\nTable structure:")
cursor.execute("PRAGMA table_info(about_content)")
structure = cursor.fetchall()
for col in structure:
    print(col)

conn.close()
