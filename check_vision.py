import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("Vision sections in database:")
cursor.execute("SELECT * FROM about_sections WHERE section_type = 'vision'")
results = cursor.fetchall()
for row in results:
    print(row)

print("\nAll about_sections:")
cursor.execute("SELECT id, section_type, title, content, is_active FROM about_sections")
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()
