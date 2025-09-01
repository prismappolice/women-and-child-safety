import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check Anakapalli district data
cursor.execute('SELECT id, district_name FROM districts WHERE district_name LIKE "%Anakapalli%"')
anakapalli = cursor.fetchone()
print('Anakapalli district:', anakapalli)

if anakapalli:
    district_id = anakapalli[0]
    print(f'District ID: {district_id}')
    
    # Check all contacts for Anakapalli
    cursor.execute('SELECT id, name, contact_number FROM district_sps WHERE district_id = ? AND is_active = 1', (district_id,))
    sps = cursor.fetchall()
    print('SPs:', sps)
    
    cursor.execute('SELECT id, team_name, leader_name FROM shakthi_teams WHERE district_id = ? AND is_active = 1', (district_id,))
    teams = cursor.fetchall()
    print('Teams:', teams)
    
    cursor.execute('SELECT id, station_name, incharge_name FROM women_police_stations WHERE district_id = ? AND is_active = 1', (district_id,))
    stations = cursor.fetchall()
    print('Stations:', stations)
    
    # Test the exact query from edit route
    if sps:
        sp_id = sps[0][0]
        cursor.execute('''
            SELECT ds.id, ds.name, ds.contact_number, ds.email, ds.district_id, d.district_name 
            FROM district_sps ds 
            JOIN districts d ON ds.district_id = d.id 
            WHERE ds.id = ?
        ''', (sp_id,))
        sp_edit_data = cursor.fetchone()
        print('SP Edit Data:', sp_edit_data)

conn.close()
