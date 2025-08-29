import sqlite3
import os

# Change to the correct directory
os.chdir(r'd:\new ap women safety')

print("Starting manual database setup...")

try:
    # Connect to database
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    print("Connected to database successfully")
    
    # Drop existing tables if they exist (to ensure clean setup)
    print("Dropping existing tables...")
    cursor.execute('DROP TABLE IF EXISTS one_stop_centers')
    cursor.execute('DROP TABLE IF EXISTS women_police_stations') 
    cursor.execute('DROP TABLE IF EXISTS shakthi_teams')
    cursor.execute('DROP TABLE IF EXISTS district_sps')
    cursor.execute('DROP TABLE IF EXISTS districts')
    
    # Create Districts table
    print("Creating districts table...")
    cursor.execute('''
        CREATE TABLE districts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            district_code TEXT,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create District SPs table
    print("Creating district_sps table...")
    cursor.execute('''
        CREATE TABLE district_sps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            district_id INTEGER,
            name TEXT NOT NULL,
            contact_number TEXT,
            email TEXT,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (district_id) REFERENCES districts (id)
        )
    ''')
    
    # Create Shakthi Teams table
    print("Creating shakthi_teams table...")
    cursor.execute('''
        CREATE TABLE shakthi_teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            district_id INTEGER,
            team_name TEXT NOT NULL,
            leader_name TEXT,
            contact_number TEXT,
            area_covered TEXT,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (district_id) REFERENCES districts (id)
        )
    ''')
    
    # Create Women Police Stations table
    print("Creating women_police_stations table...")
    cursor.execute('''
        CREATE TABLE women_police_stations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            district_id INTEGER,
            station_name TEXT NOT NULL,
            incharge_name TEXT,
            contact_number TEXT,
            address TEXT,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (district_id) REFERENCES districts (id)
        )
    ''')
    
    # Create One Stop Centers table
    print("Creating one_stop_centers table...")
    cursor.execute('''
        CREATE TABLE one_stop_centers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            district_id INTEGER,
            center_name TEXT NOT NULL,
            address TEXT,
            incharge_name TEXT,
            contact_number TEXT,
            services_offered TEXT,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (district_id) REFERENCES districts (id)
        )
    ''')
    
    print("All tables created successfully!")
    
    # Insert districts
    print("Inserting districts...")
    districts = [
        ('Visakhapatnam', 'VSKP'),
        ('Vijayawada', 'VJA'),
        ('Guntur', 'GTR'),
        ('Nellore', 'NLR'),
        ('Tirupati', 'TPT'),
        ('Kurnool', 'KNL'),
        ('Kakinada', 'KKD'),
        ('Rajahmundry', 'RJY'),
        ('Eluru', 'ELR'),
        ('Machilipatnam', 'MCP'),
        ('Chittoor', 'CTR'),
        ('Anantapur', 'ATP'),
        ('Kadapa', 'KDP')
    ]
    
    for name, code in districts:
        cursor.execute('INSERT INTO districts (name, district_code) VALUES (?, ?)', (name, code))
        print(f"Inserted district: {name}")
    
    # Insert sample data for each district
    print("Inserting sample data...")
    
    # Get all district IDs
    cursor.execute('SELECT id, name FROM districts')
    all_districts = cursor.fetchall()
    
    for district_id, district_name in all_districts:
        # Insert District SP
        cursor.execute('''
            INSERT INTO district_sps (district_id, name, contact_number, email)
            VALUES (?, ?, ?, ?)
        ''', (district_id, f'SP {district_name}', f'+91-{8000000000 + (district_id * 1000000)}', f'{district_name.lower().replace(" ", "")}.sp@appolice.gov.in'))
        
        # Insert Shakthi Teams
        teams = ['Urban Protection Team', 'Rural Safety Team', 'Highway Patrol Team']
        for i, team_name in enumerate(teams):
            cursor.execute('''
                INSERT INTO shakthi_teams (district_id, team_name, leader_name, contact_number, area_covered)
                VALUES (?, ?, ?, ?, ?)
            ''', (district_id, team_name, f'Inspector {district_name[:3]}-{i+1}', f'+91-{9000000000 + (district_id * 100000) + ((i+1)*1000)}', f'Zone {i+1} - {["Urban areas", "Rural villages", "Highways"][i]}'))
        
        # Insert Women Police Station
        cursor.execute('''
            INSERT INTO women_police_stations (district_id, station_name, incharge_name, contact_number, address)
            VALUES (?, ?, ?, ?, ?)
        ''', (district_id, f'{district_name} Women Police Station', f'CI {district_name}', f'+91-{7000000000 + (district_id * 1000000)}', f'Women Police Station, {district_name} District'))
        
        # Insert One Stop Center
        cursor.execute('''
            INSERT INTO one_stop_centers (district_id, center_name, address, incharge_name, contact_number, services_offered)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (district_id, f'{district_name} One Stop Center', f'One Stop Center, Collectorate Complex, {district_name}', f'Coordinator {district_name}', f'+91-{6000000000 + (district_id * 1000000)}', 'Legal Aid, Medical Support, Counseling, Shelter Services'))
        
        print(f"Inserted sample data for {district_name}")
    
    # Commit all changes
    conn.commit()
    print("All data committed successfully!")
    
    # Verify the data
    cursor.execute('SELECT COUNT(*) FROM districts')
    district_count = cursor.fetchone()[0]
    print(f"✅ Total districts: {district_count}")
    
    cursor.execute('SELECT COUNT(*) FROM district_sps')
    sp_count = cursor.fetchone()[0]
    print(f"✅ Total District SPs: {sp_count}")
    
    cursor.execute('SELECT COUNT(*) FROM shakthi_teams')
    team_count = cursor.fetchone()[0]
    print(f"✅ Total Shakthi Teams: {team_count}")
    
    cursor.execute('SELECT COUNT(*) FROM women_police_stations')
    station_count = cursor.fetchone()[0]
    print(f"✅ Total Women Police Stations: {station_count}")
    
    cursor.execute('SELECT COUNT(*) FROM one_stop_centers')
    center_count = cursor.fetchone()[0]
    print(f"✅ Total One Stop Centers: {center_count}")
    
    conn.close()
    print("✅ Database setup completed successfully!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
