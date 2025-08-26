import sqlite3

# Connect to database and check initiatives table structure
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check if initiatives table exists and its structure
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='initiatives'")
table_exists = cursor.fetchone()

if table_exists:
    print("Initiatives table exists. Current structure:")
    cursor.execute('PRAGMA table_info(initiatives)')
    columns = cursor.fetchall()
    for col in columns:
        print(f"Column: {col[1]}, Type: {col[2]}, NotNull: {col[3]}, Default: {col[4]}, PK: {col[5]}")
    
    print("\nSample data from initiatives table:")
    cursor.execute('SELECT * FROM initiatives LIMIT 5')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    print(f"\nTotal initiatives: {len(rows)}")
else:
    print("Initiatives table does not exist.")

conn.close()
