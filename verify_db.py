import sqlite3

print("=== Verifying Database State ===")

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check districts table structure
cursor.execute("PRAGMA table_info(districts)")
columns = cursor.fetchall()
print("Districts table columns:")
for col in columns:
    print(f"  {col[1]} ({col[2]})")

# Check sample districts
print("\n=== Sample Districts ===")
cursor.execute('SELECT id, district_name FROM districts WHERE is_active = 1 ORDER BY district_name LIMIT 5')
districts = cursor.fetchall()
for d in districts:
    print(f'ID: {d[0]}, Name: {d[1]}')

# Find Anakapalli
print("\n=== Anakapalli Verification ===")
cursor.execute('SELECT id, district_name FROM districts WHERE district_name LIKE "%Anakapalli%"')
anakapalli = cursor.fetchone()
if anakapalli:
    print(f'Anakapalli: ID={anakapalli[0]}, Name="{anakapalli[1]}"')
    
    # Check contacts for Anakapalli
    cursor.execute('SELECT id, name, district_id FROM district_sps WHERE district_id = ? AND is_active = 1', (anakapalli[0],))
    sps = cursor.fetchall()
    print(f'SPs count: {len(sps)}')
    for sp in sps:
        print(f'  SP: {sp[1]} (ID: {sp[0]})')
    
    if sps:
        # Test edit query
        sp_id = sps[0][0]
        cursor.execute('''
            SELECT ds.id, ds.name, ds.contact_number, ds.email, ds.district_id, d.district_name 
            FROM district_sps ds 
            JOIN districts d ON ds.district_id = d.id 
            WHERE ds.id = ?
        ''', (sp_id,))
        result = cursor.fetchone()
        print(f'Edit query result for SP {sp_id}:')
        if result:
            print(f'  Array positions: {list(enumerate(result))}')
            print(f'  District name at position 5: "{result[5]}"')
else:
    print('Anakapalli not found!')

conn.close()
print("=== Verification Complete ===")
