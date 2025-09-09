#!/usr/bin/env python3
"""
Fix Volunteers Table Schema Consistency
This fixes the column name inconsistencies in the volunteers table
"""

import sqlite3
import os

def fix_volunteers_schema():
    """Fix volunteers table schema to be consistent throughout the application"""
    
    db_path = 'women_safety.db'
    
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        return
    
    try:
        conn = sqlite3.connect(db_path, timeout=30.0)
        cursor = conn.cursor()
        
        print("🔧 Fixing volunteers table schema...")
        
        # Check current table structure
        cursor.execute("PRAGMA table_info(volunteers)")
        columns = cursor.fetchall()
        current_columns = [col[1] for col in columns]
        print(f"Current columns: {current_columns}")
        
        # Check what columns we need
        required_columns = {
            'full_name': 'TEXT',
            'registration_date': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP', 
            'district': 'TEXT',
            'status': 'TEXT DEFAULT "pending"'
        }
        
        missing_columns = []
        
        # Add missing columns
        for col_name, col_type in required_columns.items():
            if col_name not in current_columns:
                print(f"Adding missing column: {col_name}")
                cursor.execute(f'ALTER TABLE volunteers ADD COLUMN {col_name} {col_type}')
                missing_columns.append(col_name)
        
        # If we have 'name' but not 'full_name', copy the data
        if 'name' in current_columns and 'full_name' in missing_columns:
            cursor.execute('UPDATE volunteers SET full_name = name WHERE full_name IS NULL')
            print("✅ Copied 'name' to 'full_name'")
        
        # If we have 'created_at' but not 'registration_date', copy the data  
        if 'created_at' in current_columns and 'registration_date' in missing_columns:
            cursor.execute('UPDATE volunteers SET registration_date = created_at WHERE registration_date IS NULL')
            print("✅ Copied 'created_at' to 'registration_date'")
        
        conn.commit()
        
        # Verify the fix
        cursor.execute("PRAGMA table_info(volunteers)")
        new_columns = [col[1] for col in cursor.fetchall()]
        print(f"Updated columns: {new_columns}")
        
        # Check if required columns exist
        success = all(col in new_columns for col in required_columns.keys())
        
        if success:
            print("✅ SUCCESS: All required columns now exist")
            print("✅ Admin dashboard and volunteer registration will work")
        else:
            missing = [col for col in required_columns.keys() if col not in new_columns]
            print(f"❌ Still missing columns: {missing}")
        
        # Check data count
        cursor.execute('SELECT COUNT(*) FROM volunteers')
        count = cursor.fetchone()[0]
        print(f"✅ Volunteer records: {count}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    fix_volunteers_schema()
