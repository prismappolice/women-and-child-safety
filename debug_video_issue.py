import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Get column names
cursor.execute("PRAGMA table_info(gallery_items)")
columns = cursor.fetchall()
print("Database column structure:")
for i, col in enumerate(columns):
    print(f"Index {i}: {col[1]} ({col[2]})")

print("\n" + "="*50)

# Check specific video entry
cursor.execute('SELECT * FROM gallery_items WHERE id = 68')
row = cursor.fetchone()
print(f"\nVideo entry (ID 68) data:")
for i, value in enumerate(row):
    print(f"Index {i}: {value}")

conn.close()
