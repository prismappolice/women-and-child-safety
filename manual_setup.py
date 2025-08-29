import sqlite3
import os

def setup_district_tables():
    # Change to the correct directory
    os.chdir(r'd:\new ap women safety')
    
    print("Setting up district contacts database...")
    
    # Connect to database
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    try:
        # Create Districts table
        print("Creating districts table...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS districts (
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
            CREATE TABLE IF NOT EXISTS district_sps (
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
            CREATE TABLE IF NOT EXISTS shakthi_teams (
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
        print("Creating one_stop_centers table...")
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
        
        # Insert AP districts
        print("Inserting district data...")
        districts_data = [
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
        
        for district_name, district_code in districts_data:
            cursor.execute('''
                INSERT OR IGNORE INTO districts (name, district_code) 
                VALUES (?, ?)
            ''', (district_name, district_code))
        
        # Insert sample District SPs
        print("Inserting sample District SPs...")
        cursor.execute('''
            INSERT OR IGNORE INTO district_sps (district_id, name, contact_number, email)
            SELECT id, 'SP ' || name, '+91-' || CAST((8000000000 + (id * 1000000)) AS TEXT), 
                   LOWER(REPLACE(name, ' ', '')) || '.sp@appolice.gov.in'
            FROM districts WHERE is_active = 1
        ''')
        
        # Insert sample Shakthi Teams
        print("Inserting sample Shakthi Teams...")
        team_names = ['Urban Protection Team', 'Rural Safety Team', 'Highway Patrol Team']
        for i, team_name in enumerate(team_names):
            cursor.execute('''
                INSERT OR IGNORE INTO shakthi_teams (district_id, team_name, leader_name, contact_number, area_covered)
                SELECT id, ?, 'Inspector ' || SUBSTR(name, 1, 3) || '-' || ?, 
                       '+91-' || CAST((9000000000 + (id * 100000) + ?) AS TEXT), 
                       CASE ? 
                           WHEN 0 THEN 'Urban areas and city centers'
                           WHEN 1 THEN 'Rural villages and remote areas'
                           ELSE 'National and state highways'
                       END
                FROM districts WHERE is_active = 1
            ''', (team_name, str(i+1), (i+1)*1000, i))
        
        # Insert sample Women Police Stations
        print("Inserting sample Women Police Stations...")
        cursor.execute('''
            INSERT OR IGNORE INTO women_police_stations (district_id, station_name, incharge_name, contact_number, address)
            SELECT id, name || ' Women Police Station', 'CI ' || name, 
                   '+91-' || CAST((7000000000 + (id * 1000000)) AS TEXT),
                   'Women Police Station, ' || name || ' District'
            FROM districts WHERE is_active = 1
        ''')
        
        # Insert sample One Stop Centers
        print("Inserting sample One Stop Centers...")
        cursor.execute('''
            INSERT OR IGNORE INTO one_stop_centers (district_id, center_name, address, incharge_name, contact_number, services_offered)
            SELECT id, name || ' One Stop Center', 
                   'One Stop Center, Collectorate Complex, ' || name,
                   'Coordinator ' || name,
                   '+91-' || CAST((6000000000 + (id * 1000000)) AS TEXT),
                   'Legal Aid, Medical Support, Psychological Counseling, Shelter Services, Police Assistance'
            FROM districts WHERE is_active = 1
        ''')
        
        conn.commit()
        print("✅ Database setup completed successfully!")
        print("✅ All tables created")
        print("✅ Sample data inserted for all 13 AP districts")
        
        # Verify data
        cursor.execute('SELECT COUNT(*) FROM districts')
        district_count = cursor.fetchone()[0]
        print(f"✅ {district_count} districts created")
        
        cursor.execute('SELECT COUNT(*) FROM district_sps')
        sp_count = cursor.fetchone()[0]
        print(f"✅ {sp_count} District SPs added")
        
        cursor.execute('SELECT COUNT(*) FROM shakthi_teams')
        team_count = cursor.fetchone()[0]
        print(f"✅ {team_count} Shakthi Teams added")
        
        cursor.execute('SELECT COUNT(*) FROM women_police_stations')
        station_count = cursor.fetchone()[0]
        print(f"✅ {station_count} Women Police Stations added")
        
        cursor.execute('SELECT COUNT(*) FROM one_stop_centers')
        center_count = cursor.fetchone()[0]
        print(f"✅ {center_count} One Stop Centers added")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    setup_district_tables()
