import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Test the corrected queries
print("=== TESTING ALL CORRECTED QUERIES ===")
cursor.execute('SELECT id, name FROM districts WHERE is_active = 1 ORDER BY name')
districts = cursor.fetchall()
print(f"Districts found: {len(districts)}")

for district_id, district_name in districts[:2]:  # Test first 2 districts
    print(f"\n--- Testing district: {district_name} (ID: {district_id}) ---")
    
    # Test SP query
    cursor.execute('SELECT name, contact_number, email FROM district_sps WHERE district_id = ? AND is_active = 1', (district_id,))
    sp_data = cursor.fetchone()
    print(f"SP data: {sp_data}")
    
    # Test Shakthi teams query
    cursor.execute('SELECT team_name, leader_name, contact_number, area_covered FROM shakthi_teams WHERE district_id = ? AND is_active = 1', (district_id,))
    teams_data = cursor.fetchall()
    print(f"Teams data: {len(teams_data)} teams")
    if teams_data:
        print(f"  First team: {teams_data[0]}")
    
    # Test Women PS query
    cursor.execute('SELECT station_name, incharge_name, contact_number, address FROM women_police_stations WHERE district_id = ? AND is_active = 1', (district_id,))
    ps_data = cursor.fetchall()
    print(f"Women PS data: {len(ps_data)} stations")
    if ps_data:
        print(f"  First station: {ps_data[0]}")
    
    # Test OSC query  
    cursor.execute('SELECT center_name, address, incharge_name, contact_number, services_offered FROM one_stop_centers WHERE district_id = ? AND is_active = 1', (district_id,))
    center_data = cursor.fetchall()
    print(f"OSC data: {len(center_data)} centers")
    if center_data:
        print(f"  First center: {center_data[0]}")

conn.close()
