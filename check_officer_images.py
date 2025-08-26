import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("Officers in database:")
cursor.execute('SELECT id, name, designation, image_url FROM officers')
officers = cursor.fetchall()

for officer in officers:
    print(f"ID: {officer[0]}")
    print(f"Name: {officer[1]}")
    print(f"Designation: {officer[2]}")
    print(f"Image URL: {officer[3]}")
    print("-" * 40)

conn.close()
