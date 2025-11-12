from app import get_db_connection

conn = get_db_connection('main')
cursor = conn.cursor()

print("Checking newly added records:")
print("\n1. Women Police Station ID 55 (chirala ps):")
cursor.execute('SELECT id, district_id, station_name, incharge_name, contact_number, is_active FROM women_police_stations WHERE id = 55')
row = cursor.fetchone()
if row:
    print(f"   District ID: {row[1]}, Name: {row[2]}, Incharge: {row[3]}, Contact: {row[4]}, is_active: {repr(row[5])}")
    
    # Get district name
    cursor.execute('SELECT district_name FROM districts WHERE id = %s', (row[1],))
    district = cursor.fetchone()
    print(f"   District Name: {district[0] if district else 'NOT FOUND'}")
    
    # Check if it shows in user query
    cursor.execute('SELECT station_name FROM women_police_stations WHERE district_id = %s AND is_active::integer = 1', (row[1],))
    user_results = cursor.fetchall()
    print(f"   User view sees {len(user_results)} women PS in this district: {[r[0] for r in user_results]}")

print("\n2. One Stop Center ID 53 (one stop center):")
cursor.execute('SELECT id, district_id, center_name, incharge_name, contact_number, is_active FROM one_stop_centers WHERE id = 53')
row = cursor.fetchone()
if row:
    print(f"   District ID: {row[1]}, Name: {row[2]}, Incharge: {row[3]}, Contact: {row[4]}, is_active: {repr(row[5])}")
    
    # Get district name
    cursor.execute('SELECT district_name FROM districts WHERE id = %s', (row[1],))
    district = cursor.fetchone()
    print(f"   District Name: {district[0] if district else 'NOT FOUND'}")
    
    # Check if it shows in user query
    cursor.execute('SELECT center_name FROM one_stop_centers WHERE district_id = %s AND is_active::integer = 1', (row[1],))
    user_results = cursor.fetchall()
    print(f"   User view sees {len(user_results)} centers in this district: {[r[0] for r in user_results]}")

conn.close()
