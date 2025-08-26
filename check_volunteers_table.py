import sqlite3

# Connect to database and check volunteers table structure
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check if volunteers table exists and its structure
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='volunteers'")
table_exists = cursor.fetchone()

if table_exists:
    print("Volunteers table exists. Current structure:")
    cursor.execute('PRAGMA table_info(volunteers)')
    columns = cursor.fetchall()
    for col in columns:
        print(f"Column: {col[1]}, Type: {col[2]}, NotNull: {col[3]}, Default: {col[4]}, PK: {col[5]}")
else:
    print("Volunteers table does not exist.")

# Check what data is in volunteers table if it exists
if table_exists:
    print("\nSample data from volunteers table:")
    cursor.execute('SELECT * FROM volunteers LIMIT 3')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn.close()
