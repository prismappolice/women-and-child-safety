import sqlite3
import os

print("Checking database...")
print(f"Current directory: {os.getcwd()}")
print(f"Database file exists: {os.path.exists('women_safety.db')}")

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check if districts table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='districts'")
table_exists = cursor.fetchone()
print(f"Districts table exists: {table_exists is not None}")

if table_exists:
    # Check districts count
    cursor.execute('SELECT COUNT(*) FROM districts')
    total_count = cursor.fetchone()[0]
    print(f"Total districts in table: {total_count}")
    
    cursor.execute('SELECT COUNT(*) FROM districts WHERE is_active = 1')
    active_count = cursor.fetchone()[0]
    print(f"Active districts: {active_count}")
    
    # Show first 5 districts
    cursor.execute('SELECT id, district_name, is_active FROM districts LIMIT 5')
    districts = cursor.fetchall()
    print("First 5 districts:")
    for d in districts:
        print(f"  {d[0]}: {d[1]} (active: {d[2]})")
else:
    print("Districts table does not exist!")

conn.close()
