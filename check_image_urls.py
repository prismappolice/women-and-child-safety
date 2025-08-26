import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("=== OFFICERS TABLE DEBUG ===")
cursor.execute('SELECT id, name, designation, image_url FROM officers ORDER BY position_order')
officers = cursor.fetchall()

if officers:
    for i, officer in enumerate(officers):
        print(f"\nOfficer {i+1}:")
        print(f"  ID: {officer[0]}")
        print(f"  Name: {officer[1]}")
        print(f"  Designation: {officer[2]}")
        print(f"  Image URL: '{officer[3]}'")
        
        # Check if image_url is None or empty
        if officer[3] is None:
            print("  ❌ Image URL is NULL")
        elif officer[3] == '':
            print("  ❌ Image URL is empty string")
        elif officer[3]:
            print(f"  ✅ Image URL exists: {officer[3]}")
else:
    print("❌ No officers found in database")

conn.close()
