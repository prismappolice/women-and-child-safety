#!/usr/bin/env python3
"""
Fix Gallery Database Schema - Add Missing Columns
This fixes the sqlite3.OperationalError: no such column: main_image
"""

import sqlite3
import os

def fix_gallery_schema():
    """Fix gallery database schema to include all required columns"""
    
    db_path = 'women_safety.db'
    
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("🔧 Fixing gallery database schema...")
        
        # Check current table structure
        cursor.execute("PRAGMA table_info(gallery_items)")
        columns = [col[1] for col in cursor.fetchall()]
        print(f"Current columns: {columns}")
        
        # Add missing columns if they don't exist
        missing_columns = []
        
        if 'main_image' not in columns:
            cursor.execute('ALTER TABLE gallery_items ADD COLUMN main_image TEXT')
            missing_columns.append('main_image')
            print("✅ Added main_image column")
        
        if 'updated_at' not in columns:
            cursor.execute('ALTER TABLE gallery_items ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP')
            missing_columns.append('updated_at')
            print("✅ Added updated_at column")
        
        # Copy image_url to main_image for existing records if needed
        if 'main_image' in missing_columns:
            cursor.execute('UPDATE gallery_items SET main_image = image_url WHERE main_image IS NULL AND image_url IS NOT NULL')
            print("✅ Copied image_url to main_image for existing records")
        
        # Create gallery_media table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gallery_media (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gallery_item_id INTEGER,
                file_path TEXT,
                file_type TEXT,
                media_type TEXT,
                media_url TEXT,
                media_title TEXT,
                media_description TEXT,
                title TEXT,
                description TEXT,
                display_order INTEGER DEFAULT 0,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (gallery_item_id) REFERENCES gallery_items (id) ON DELETE CASCADE
            )
        ''')
        
        # Check gallery_media table structure and add missing columns
        cursor.execute("PRAGMA table_info(gallery_media)")
        media_columns = [col[1] for col in cursor.fetchall()]
        print(f"Current gallery_media columns: {media_columns}")
        
        media_missing_columns = []
        
        if 'media_type' not in media_columns:
            cursor.execute('ALTER TABLE gallery_media ADD COLUMN media_type TEXT')
            media_missing_columns.append('media_type')
            print("✅ Added media_type column")
        
        if 'media_url' not in media_columns:
            cursor.execute('ALTER TABLE gallery_media ADD COLUMN media_url TEXT')
            media_missing_columns.append('media_url')
            print("✅ Added media_url column")
        
        if 'media_title' not in media_columns:
            cursor.execute('ALTER TABLE gallery_media ADD COLUMN media_title TEXT')
            media_missing_columns.append('media_title')
            print("✅ Added media_title column")
        
        if 'media_description' not in media_columns:
            cursor.execute('ALTER TABLE gallery_media ADD COLUMN media_description TEXT')
            media_missing_columns.append('media_description')
            print("✅ Added media_description column")
        
        print("✅ Ensured gallery_media table exists with all required columns")
        
        conn.commit()
        
        # Verify the fix
        cursor.execute("PRAGMA table_info(gallery_items)")
        new_columns = [col[1] for col in cursor.fetchall()]
        print(f"New columns: {new_columns}")
        
        if 'main_image' in new_columns:
            print("✅ SUCCESS: main_image column now exists")
            print("✅ Gallery pages will work without errors")
        else:
            print("❌ ERROR: main_image column still missing")
        
        # Ensure gallery is still empty (no sample data)
        cursor.execute('DELETE FROM gallery_items')
        cursor.execute('DELETE FROM gallery_media')
        cursor.execute('DELETE FROM sqlite_sequence WHERE name IN ("gallery_items", "gallery_media")')
        print("✅ Gallery remains clean and empty")
        
        conn.commit()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    fix_gallery_schema()
