import sqlite3

# Let's also check if there are any issues with the officers table structure
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("Officers table structure:")
cursor.execute("PRAGMA table_info(officers)")
columns = cursor.fetchall()
for col in columns:
    print(f"Column: {col[1]}, Type: {col[2]}")

print("\nCurrent officers:")
cursor.execute('SELECT id, name, designation, image_url FROM officers')
officers = cursor.fetchall()

if officers:
    for officer in officers:
        print(f"ID: {officer[0]}, Name: {officer[1]}, Image: {officer[3]}")
else:
    print("No officers found in database")

conn.close()
