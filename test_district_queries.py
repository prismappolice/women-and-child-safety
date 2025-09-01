import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check districts table
print("=== DISTRICTS TABLE ===")
cursor.execute('SELECT * FROM districts WHERE is_active = 1 ORDER BY district_name')
districts = cursor.fetchall()
print(f"Active districts: {len(districts)}")
for district in districts[:5]:  # Show first 5
    print(district)

print("\n=== DISTRICT SPS TABLE ===")
cursor.execute('SELECT * FROM district_sps WHERE is_active = 1 LIMIT 5')
sps = cursor.fetchall()
print(f"Active SPs: {len(sps)}")
for sp in sps:
    print(sp)

print("\n=== SHAKTHI TEAMS TABLE ===")
cursor.execute('SELECT * FROM shakthi_teams WHERE is_active = 1 LIMIT 5')
teams = cursor.fetchall()
print(f"Active teams: {len(teams)}")
for team in teams:
    print(team)

print("\n=== WOMEN POLICE STATIONS TABLE ===")
cursor.execute('SELECT * FROM women_police_stations WHERE is_active = 1 LIMIT 5')
stations = cursor.fetchall()
print(f"Active women PS: {len(stations)}")
for station in stations:
    print(station)

print("\n=== ONE STOP CENTERS TABLE ===")
cursor.execute('SELECT * FROM one_stop_centers WHERE is_active = 1 LIMIT 5')
centers = cursor.fetchall()
print(f"Active OSCs: {len(centers)}")
for center in centers:
    print(center)

# Test the exact query from contact route
print("\n=== TESTING CONTACT ROUTE QUERY ===")
cursor.execute('SELECT id, district_name FROM districts WHERE is_active = 1 ORDER BY district_name')
districts = cursor.fetchall()
print(f"Districts query result: {len(districts)} districts")

if districts:
    district_id, district_name = districts[0]
    print(f"Testing with district: {district_name} (ID: {district_id})")
    
    # Test SP query
    cursor.execute('SELECT sp_name, contact_number, email FROM district_sps WHERE district_id = ? AND is_active = 1', (district_id,))
    sp_data = cursor.fetchone()
    print(f"SP data: {sp_data}")
    
    # Test Shakthi teams query
    cursor.execute('SELECT team_name, incharge_name, contact_number, area_coverage FROM shakthi_teams WHERE district_id = ? AND is_active = 1', (district_id,))
    teams_data = cursor.fetchall()
    print(f"Teams data: {len(teams_data)} teams")
    
    # Test Women PS query
    cursor.execute('SELECT station_name, incharge_name, contact_number, address FROM women_police_stations WHERE district_id = ? AND is_active = 1', (district_id,))
    ps_data = cursor.fetchall()
    print(f"Women PS data: {len(ps_data)} stations")
    
    # Test OSC query
    cursor.execute('SELECT center_name, address, incharge_name, contact_number, services_offered FROM one_stop_centers WHERE district_id = ? AND is_active = 1', (district_id,))
    center_data = cursor.fetchall()
    print(f"OSC data: {len(center_data)} centers")

conn.close()
