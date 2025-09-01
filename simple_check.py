#!/usr/bin/env python3
import sqlite3
import sys
import os

# Change to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

try:
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Test if we can access the database
    cursor.execute('SELECT COUNT(*) FROM districts')
    count = cursor.fetchone()[0]
    print(f"Total districts: {count}")
    
    # Check Anakapalli specifically
    cursor.execute('SELECT id, district_name FROM districts WHERE district_name LIKE "%Anakapalli%"')
    anakapalli = cursor.fetchone()
    
    if anakapalli:
        print(f"Found Anakapalli: ID={anakapalli[0]}, Name='{anakapalli[1]}'")
        
        # Check SP data
        cursor.execute('SELECT id, name FROM district_sps WHERE district_id = ? AND is_active = 1', (anakapalli[0],))
        sps = cursor.fetchall()
        print(f"SPs in Anakapalli: {len(sps)}")
        
        if sps:
            sp_id = sps[0][0]
            # Test the edit query
            cursor.execute('''
                SELECT ds.id, ds.name, ds.contact_number, ds.email, ds.district_id, d.district_name 
                FROM district_sps ds 
                JOIN districts d ON ds.district_id = d.id 
                WHERE ds.id = ?
            ''', (sp_id,))
            result = cursor.fetchone()
            
            if result:
                print(f"Edit query successful!")
                print(f"SP Name: {result[1]}")
                print(f"District Name: {result[5]}")
            else:
                print("Edit query returned no results")
    else:
        print("Anakapalli not found in database")
        
        # Show what districts we do have
        cursor.execute('SELECT district_name FROM districts WHERE is_active = 1 ORDER BY district_name LIMIT 10')
        districts = cursor.fetchall()
        print("Available districts:")
        for d in districts:
            print(f"  - {d[0]}")
    
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
