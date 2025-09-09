#!/usr/bin/env python3
"""
Fix Volunteers Table Schema - Add Missing Columns Only
This fixes only the volunteers table without affecting any other data
"""

import sqlite3
import os

def fix_volunteers_table_only():
    """Fix only volunteers table schema issues"""
    
    db_path = 'women_safety.db'
    
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        return
    
    try:
        conn = sqlite3.connect(db_path, timeout=30.0)
        cursor = conn.cursor()
        
        print("🔧 Fixing ONLY volunteers table schema...")
        
        # Check current volunteers table structure
        cursor.execute("PRAGMA table_info(volunteers)")
        columns = [col[1] for col in cursor.fetchall()]
        print(f"Current volunteers columns: {columns}")
        
        fixed = []
        
        # Add missing columns if they don't exist
        if 'full_name' not in columns and 'name' in columns:
            # Copy data from name to full_name
            cursor.execute('ALTER TABLE volunteers ADD COLUMN full_name TEXT')
            cursor.execute('UPDATE volunteers SET full_name = name WHERE full_name IS NULL')
            fixed.append('full_name (copied from name)')
            print("✅ Added full_name column")
        elif 'full_name' not in columns:
            cursor.execute('ALTER TABLE volunteers ADD COLUMN full_name TEXT')
            fixed.append('full_name')
            print("✅ Added full_name column")
        
        if 'registration_date' not in columns:
            cursor.execute('ALTER TABLE volunteers ADD COLUMN registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP')
            cursor.execute('UPDATE volunteers SET registration_date = created_at WHERE registration_date IS NULL AND created_at IS NOT NULL')
            fixed.append('registration_date')
            print("✅ Added registration_date column")
        
        conn.commit()
        
        # Verify the fix
        cursor.execute("PRAGMA table_info(volunteers)")
        new_columns = [col[1] for col in cursor.fetchall()]
        print(f"New volunteers columns: {new_columns}")
        
        if 'full_name' in new_columns and 'registration_date' in new_columns:
            print("✅ SUCCESS: Volunteers table fixed")
            print("✅ Admin dashboard will work without errors")
        else:
            print("❌ Some columns still missing")
        
        # Check other tables are untouched
        print(f"\n🔒 CHECKING OTHER DATA IS SAFE:")
        safe_tables = ['officers', 'initiatives', 'home_content', 'about_content', 'gallery_items']
        for table in safe_tables:
            try:
                cursor.execute(f'SELECT COUNT(*) FROM {table}')
                count = cursor.fetchone()[0]
                print(f"✅ {table}: {count} items (safe)")
            except:
                print(f"ℹ️ {table}: doesn't exist or empty")
        
        if fixed:
            print(f"\n🎉 Fixed columns: {', '.join(fixed)}")
            print("🔒 All other data completely safe")
        else:
            print("\n✅ No fixes needed - table already correct")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    fix_volunteers_table_only()
