import sqlite3
from datetime import datetime

def init_volunteer_tables():
    conn = sqlite3.connect('volunteer_system.db')
    cursor = conn.cursor()
    
    # Create volunteers table in separate database
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            registration_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            age INTEGER,
            address TEXT NOT NULL,
            occupation TEXT,
            education TEXT,
            experience TEXT,
            motivation TEXT,
            availability TEXT,
            skills TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create volunteer_status table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS volunteer_status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            volunteer_id INTEGER UNIQUE,
            status TEXT DEFAULT 'pending',
            admin_notes TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (volunteer_id) REFERENCES volunteers (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def generate_volunteer_id():
    conn = sqlite3.connect('volunteer_system.db')
    cursor = conn.cursor()
    year = datetime.now().year
    cursor.execute('SELECT registration_id FROM volunteers WHERE registration_id LIKE ? ORDER BY id DESC LIMIT 1', (f'VOL-{year}-%',))
    last_reg = cursor.fetchone()
    
    if last_reg:
        last_num = int(last_reg[0].split('-')[2])
        new_num = last_num + 1
    else:
        new_num = 1
    
    registration_id = f'VOL-{year}-{new_num:03d}'
    conn.close()
    return registration_id
