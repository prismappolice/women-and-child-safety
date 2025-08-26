import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("Current About Content (including leadership):")
cursor.execute("SELECT id, section_name, title, content, is_active FROM about_content ORDER BY section_name")
results = cursor.fetchall()
for row in results:
    print(f"ID: {row[0]}, Section: {row[1]}, Title: {row[2]}, Active: {row[4]}")
    print(f"Content: {row[3][:100]}...")
    print("-" * 50)

conn.close()
