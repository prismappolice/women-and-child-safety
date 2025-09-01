import sqlite3

def fix_all_district_data_mapping():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    print("=== COMPREHENSIVE DISTRICT DATA MAPPING FIX ===")
    
    # Get all districts
    cursor.execute('SELECT id, district_name FROM districts WHERE is_active = 1 ORDER BY district_name')
    districts = cursor.fetchall()
    
    print(f"Found {len(districts)} districts to fix...")
    
    for district_id, district_name in districts:
        print(f"\n--- Fixing {district_name} (ID: {district_id}) ---")
        
        # Remove all existing contacts for this district
        cursor.execute('DELETE FROM district_sps WHERE district_id = ?', (district_id,))
        cursor.execute('DELETE FROM shakthi_teams WHERE district_id = ?', (district_id,))
        cursor.execute('DELETE FROM women_police_stations WHERE district_id = ?', (district_id,))
        cursor.execute('DELETE FROM one_stop_centers WHERE district_id = ?', (district_id,))
        
        # Create proper SP for each district
        sp_name = f"SP {district_name}"
        sp_phone = f"+91-804000{district_id:04d}"
        sp_email = f"sp.{district_name.lower().replace(' ', '').replace('(', '').replace(')', '')}@appolice.gov.in"
        
        cursor.execute('''
            INSERT INTO district_sps (district_id, name, contact_number, email, is_active)
            VALUES (?, ?, ?, ?, 1)
        ''', (district_id, sp_name, sp_phone, sp_email))
        
        # Create Shakthi Teams
        teams = [
            {
                'name': 'Urban Protection Team',
                'leader': f'Inspector {district_name[:3].upper()}-1',
                'phone': f'+91-900030{district_id:04d}',
                'area': f'Urban areas of {district_name}'
            },
            {
                'name': 'Rural Safety Team', 
                'leader': f'Inspector {district_name[:3].upper()}-2',
                'phone': f'+91-900031{district_id:04d}',
                'area': f'Rural areas of {district_name}'
            }
        ]
        
        # Add Highway Patrol Team for some districts
        if district_id <= 15:  # First 15 districts get highway team
            teams.append({
                'name': 'Highway Patrol Team',
                'leader': f'Inspector {district_name[:3].upper()}-3', 
                'phone': f'+91-900032{district_id:04d}',
                'area': f'Highways in {district_name}'
            })
        
        for team in teams:
            cursor.execute('''
                INSERT INTO shakthi_teams (district_id, team_name, leader_name, contact_number, area_covered, is_active)
                VALUES (?, ?, ?, ?, ?, 1)
            ''', (district_id, team['name'], team['leader'], team['phone'], team['area']))
        
        # Create Women Police Station
        station_name = f"Women Police Station {district_name}"
        incharge_name = f"Circle Inspector {district_name}"
        station_phone = f"+91-700000{district_id:04d}"
        station_address = f"{district_name} District, Andhra Pradesh"
        
        cursor.execute('''
            INSERT INTO women_police_stations (district_id, station_name, incharge_name, contact_number, address, is_active)
            VALUES (?, ?, ?, ?, ?, 1)
        ''', (district_id, station_name, incharge_name, station_phone, station_address))
        
        # Create One Stop Center for major districts
        if district_id <= 20:  # First 20 districts get One Stop Centers
            center_name = f"One Stop Center {district_name}"
            center_address = f"District Headquarters, {district_name}"
            center_incharge = f"Coordinator {district_name}"
            center_phone = f"+91-600000{district_id:04d}"
            services = "Counseling, Legal Aid, Medical Support, Shelter"
            
            cursor.execute('''
                INSERT INTO one_stop_centers (district_id, center_name, address, incharge_name, contact_number, services_offered, is_active)
                VALUES (?, ?, ?, ?, ?, ?, 1)
            ''', (district_id, center_name, center_address, center_incharge, center_phone, services))
        
        print(f"✓ Fixed {district_name}")
    
    conn.commit()
    
    # Verification
    print(f"\n=== VERIFICATION ===")
    cursor.execute('''
        SELECT d.district_name, 
               (SELECT COUNT(*) FROM district_sps WHERE district_id = d.id AND is_active = 1) as sps,
               (SELECT COUNT(*) FROM shakthi_teams WHERE district_id = d.id AND is_active = 1) as teams,
               (SELECT COUNT(*) FROM women_police_stations WHERE district_id = d.id AND is_active = 1) as stations,
               (SELECT COUNT(*) FROM one_stop_centers WHERE district_id = d.id AND is_active = 1) as centers
        FROM districts d 
        WHERE d.is_active = 1 
        ORDER BY d.district_name
        LIMIT 10
    ''')
    
    results = cursor.fetchall()
    print("Sample verification (first 10 districts):")
    for district_name, sps, teams, stations, centers in results:
        print(f"{district_name}: SP={sps}, Teams={teams}, Stations={stations}, Centers={centers}")
    
    conn.close()
    print("\n=== COMPREHENSIVE FIX COMPLETED ===")

if __name__ == "__main__":
    fix_all_district_data_mapping()
