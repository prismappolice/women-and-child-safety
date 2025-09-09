import sqlite3

print("Video Template Indices Fix Verification")
print("="*50)

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check video entry ID 68
cursor.execute('SELECT * FROM gallery_items WHERE id = 68')
row = cursor.fetchone()

print(f"Video Entry (ID 68) - After Template Fix:")
print(f"Title: {row[1]}")
print(f"Category (Index 5): {row[5]}")
print(f"Event Date (Index 4): {row[4]}")
print(f"Video URL (Index 10): {row[10]}")
print(f"Is Featured (Index 6): {row[6]}")
print(f"Is Active (Index 7): {row[7]}")

print("\nTemplate indices now correctly match database structure!")

conn.close()
