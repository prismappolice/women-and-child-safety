import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("=== CHECKING DISTRICT-SP MAPPING ===")

# Get Anakapalli district
cursor.execute('SELECT id, district_name FROM districts WHERE district_name LIKE "%Anakapalli%"')
anakapalli = cursor.fetchone()

if anakapalli:
    anakapalli_id, anakapalli_name = anakapalli
    print(f"Anakapalli District: ID={anakapalli_id}, Name='{anakapalli_name}'")
    
    # Check what SPs are assigned to Anakapalli
    cursor.execute('SELECT id, name, district_id FROM district_sps WHERE district_id = ? AND is_active = 1', (anakapalli_id,))
    anakapalli_sps = cursor.fetchall()
    
    print(f"\nSPs assigned to Anakapalli (ID {anakapalli_id}):")
    for sp in anakapalli_sps:
        print(f"  SP ID: {sp[0]}, Name: '{sp[1]}'")

# Check if there's a "SP Vijayawada" and where it should belong
cursor.execute('SELECT id, name, district_id FROM district_sps WHERE name LIKE "%Vijayawada%" AND is_active = 1')
vijayawada_sp = cursor.fetchone()

if vijayawada_sp:
    sp_id, sp_name, current_district_id = vijayawada_sp
    print(f"\nFound SP Vijayawada: ID={sp_id}, Name='{sp_name}', Currently in District ID={current_district_id}")
    
    # Check what district this SP is currently assigned to
    cursor.execute('SELECT district_name FROM districts WHERE id = ?', (current_district_id,))
    current_district = cursor.fetchone()
    if current_district:
        print(f"SP Vijayawada is currently assigned to: '{current_district[0]}'")

# Check if there's a proper Vijayawada/Krishna district
cursor.execute('SELECT id, district_name FROM districts WHERE district_name LIKE "%Krishna%" OR district_name LIKE "%Vijayawada%"')
krishna_districts = cursor.fetchall()

print(f"\nKrishna/Vijayawada related districts:")
for district in krishna_districts:
    print(f"  District ID: {district[0]}, Name: '{district[1]}'")

# Show all district-SP mappings to see the full picture
print(f"\n=== ALL DISTRICT-SP MAPPINGS ===")
cursor.execute('''
    SELECT d.district_name, ds.name, ds.id, ds.district_id 
    FROM districts d 
    JOIN district_sps ds ON d.id = ds.district_id 
    WHERE ds.is_active = 1 
    ORDER BY d.district_name
''')
all_mappings = cursor.fetchall()

for mapping in all_mappings:
    print(f"District: {mapping[0]} -> SP: {mapping[1]} (SP_ID: {mapping[2]})")

conn.close()
