import sqlite3

# Check the actual structure of the volunteers table
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("Checking volunteers table structure...")

# Get table schema
cursor.execute("PRAGMA table_info(volunteers)")
columns = cursor.fetchall()

if columns:
    print("\nExisting volunteers table columns:")
    for col in columns:
        print(f"- {col[1]} ({col[2]})")
else:
    print("No volunteers table found")

# Check if there are any existing volunteers
cursor.execute("SELECT COUNT(*) FROM volunteers")
count = cursor.fetchone()[0]
print(f"\nNumber of existing volunteers: {count}")

if count > 0:
    # Show first volunteer to see actual data structure
    cursor.execute("SELECT * FROM volunteers LIMIT 1")
    sample = cursor.fetchone()
    print(f"\nSample volunteer data: {sample}")

conn.close()
