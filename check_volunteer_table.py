import sqlite3

# Connect to database and check volunteer table structure
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Get table schema
cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='volunteers'")
schema = cursor.fetchone()

if schema:
    print("Current volunteers table schema:")
    print(schema[0])
else:
    print("Volunteers table not found")

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("\nAll tables in database:")
for table in tables:
    print(f"- {table[0]}")

conn.close()
