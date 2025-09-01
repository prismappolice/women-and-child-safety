import sqlite3

# Connect to database
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check current districts
cursor.execute('SELECT COUNT(*) FROM districts WHERE is_active = 1')
count = cursor.fetchone()[0]
print(f"Current districts in database: {count}")

if count == 0:
    print("No districts found. Adding all 26 districts...")
    
    # List of 26 official AP districts
    districts = [
        "Alluri Sitarama Raju", "Anakapalli", "Ananthapuramu", "Annamayya", "Bapatla",
        "Chittoor", "East Godavari", "Eluru", "Guntur", "Kakinada", "Konaseema",
        "Krishna", "Kurnool", "Nandyal", "NTR", "Palnadu", "Parvathipuram Manyam",
        "Prakasam", "Sri Potti Sriramulu Nellore", "Sri Sathya Sai", "Srikakulam",
        "Tirupati", "Visakhapatnam", "Vizianagaram", "West Godavari", "YSR (Kadapa)"
    ]
    
    # Insert all districts
    for i, district in enumerate(districts, 1):
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO districts 
                (id, district_name, district_code, is_active, created_at) 
                VALUES (?, ?, ?, 1, datetime('now'))
            ''', (i, district, district.upper().replace(' ', '_')))
            print(f"Added: {district}")
        except Exception as e:
            print(f"Error adding {district}: {e}")
    
    conn.commit()
    
    # Check final count
    cursor.execute('SELECT COUNT(*) FROM districts WHERE is_active = 1')
    final_count = cursor.fetchone()[0]
    print(f"Final districts count: {final_count}")
else:
    print("Districts already exist in database")

conn.close()
print("Done!")
