from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import datetime

def init_volunteer_db():
    conn = sqlite3.connect('volunteer_system.db')
    cursor = conn.cursor()
    
    # Create volunteers table
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
    
    # Create admin_users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def generate_registration_id():
    conn = sqlite3.connect('volunteer_system.db')
    cursor = conn.cursor()
    
    # Get the current year
    year = datetime.now().year
    
    # Get the last registration number for this year
    cursor.execute('SELECT registration_id FROM volunteers WHERE registration_id LIKE ? ORDER BY id DESC LIMIT 1', (f'VOL-{year}-%',))
    last_reg = cursor.fetchone()
    
    if last_reg:
        # Extract the number from the last registration ID and increment
        last_num = int(last_reg[0].split('-')[2])
        new_num = last_num + 1
    else:
        new_num = 1
    
    # Generate new registration ID (format: VOL-2025-001)
    registration_id = f'VOL-{year}-{new_num:03d}'
    
    conn.close()
    return registration_id

# Initialize the database when this module is imported
init_volunteer_db()
