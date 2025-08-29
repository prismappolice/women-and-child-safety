import sqlite3

def setup_district_contacts_database():
    """
    Set up comprehensive district contacts database with all required tables
    """
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Create Districts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS districts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            district_name TEXT NOT NULL UNIQUE,
            district_code TEXT,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create District SPs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS district_sps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            district_id INTEGER,
            sp_name TEXT NOT NULL,
            contact_number TEXT,
            email TEXT,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (district_id) REFERENCES districts (id)
        )
    ''')
    
    # Create Shakthi Teams table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS shakthi_teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            district_id INTEGER,
            team_name TEXT NOT NULL,
            incharge_name TEXT,
            contact_number TEXT,
            area_coverage TEXT,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (district_id) REFERENCES districts (id)
        )
    ''')
    
    # Create Women Police Stations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS women_police_stations (
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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS one_stop_centers (
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
    
    # Insert default districts
    districts_data = [
        ('Visakhapatnam', 'VSKP'),
        ('Vijayawada', 'VJA'),
        ('Guntur', 'GTR'),
        ('Nellore', 'NLR'),
        ('Tirupati', 'TPT'),
        ('Kurnool', 'KNL'),
        ('Kakinada', 'KKD'),
        ('Rajamahendravaram', 'RJY'),
        ('Eluru', 'ELR'),
        ('Machilipatnam', 'MCP'),
        ('Chittoor', 'CTR'),
        ('Anantapur', 'ATP'),
        ('Kadapa', 'KDP')
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO districts (district_name, district_code) 
        VALUES (?, ?)
    ''', districts_data)
    
    # Insert sample data for demonstration
    print("Creating sample district contacts data...")
    
    # Sample District SPs
    cursor.execute('''
        INSERT OR IGNORE INTO district_sps (district_id, sp_name, contact_number, email)
        SELECT id, 'SP ' || district_name, '+91-' || CAST((8000000000 + (id * 1000000)) AS TEXT), 
               LOWER(district_name) || '.sp@appolice.gov.in'
        FROM districts WHERE is_active = 1
    ''')
    
    # Sample Shakthi Teams (4-5 per district)
    sample_teams = ['Team Alpha', 'Team Beta', 'Team Gamma', 'Team Delta', 'Team Omega']
    for i, team in enumerate(sample_teams):
        cursor.execute('''
            INSERT OR IGNORE INTO shakthi_teams (district_id, team_name, incharge_name, contact_number, area_coverage)
            SELECT id, ?, 'Inspector ' || ?, '+91-' || CAST((9000000000 + (id * 100000) + ?) AS TEXT), 
                   'Zone ' || CAST(? AS TEXT)
            FROM districts WHERE is_active = 1
        ''', (team, team.split()[1], (i+1)*1000, i+1))
    
    # Sample Women Police Stations
    cursor.execute('''
        INSERT OR IGNORE INTO women_police_stations (district_id, station_name, incharge_name, contact_number, address)
        SELECT id, district_name || ' Women PS', 'CI ' || district_name, 
               '+91-' || CAST((7000000000 + (id * 1000000)) AS TEXT),
               'Women Police Station, ' || district_name
        FROM districts WHERE is_active = 1
    ''')
    
    # Sample One Stop Centers
    cursor.execute('''
        INSERT OR IGNORE INTO one_stop_centers (district_id, center_name, address, incharge_name, contact_number, services_offered)
        SELECT id, district_name || ' One Stop Center', 
               'One Stop Center, Collectorate Complex, ' || district_name,
               'Coordinator ' || district_name,
               '+91-' || CAST((6000000000 + (id * 1000000)) AS TEXT),
               'Legal Aid, Medical Support, Counseling, Shelter'
        FROM districts WHERE is_active = 1
    ''')
    
    conn.commit()
    conn.close()
    
    print("✅ District contacts database setup completed!")
    print("✅ All tables created successfully")
    print("✅ Sample data inserted")
    print("\nTables created:")
    print("- districts")
    print("- district_sps")
    print("- shakthi_teams")
    print("- women_police_stations")
    print("- one_stop_centers")

if __name__ == "__main__":
    setup_district_contacts_database()
