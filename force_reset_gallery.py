#!/usr/bin/env python3
"""
Force Reset Gallery Database - Complete Clean Slate
This will ensure the admin dashboard shows only the 5 new sections with no old content
"""

import sqlite3
import os

def force_reset_gallery():
    """Completely reset gallery database to clean state"""
    
    db_path = 'women_safety.db'
    
    if not os.path.exists(db_path):
        print("Database not found!")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("🔄 Force resetting gallery database...")
        
        # Check current state
        cursor.execute('SELECT COUNT(*) FROM gallery_items')
        count = cursor.fetchone()[0]
        print(f"Found {count} existing items")
        
        # Drop and recreate gallery tables for complete reset
        print("🗑️ Dropping existing tables...")
        cursor.execute('DROP TABLE IF EXISTS gallery_media')
        cursor.execute('DROP TABLE IF EXISTS gallery_items')
        
        # Recreate gallery_items table with proper structure
        print("🏗️ Creating fresh gallery_items table...")
        cursor.execute('''
            CREATE TABLE gallery_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                main_image TEXT,
                event_date TEXT,
                category TEXT NOT NULL,
                is_featured BOOLEAN DEFAULT 0,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Recreate gallery_media table
        print("🏗️ Creating fresh gallery_media table...")
        cursor.execute('''
            CREATE TABLE gallery_media (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gallery_item_id INTEGER,
                file_path TEXT NOT NULL,
                file_type TEXT,
                title TEXT,
                description TEXT,
                display_order INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (gallery_item_id) REFERENCES gallery_items (id) ON DELETE CASCADE
            )
        ''')
        
        # Clean up sequence tables
        cursor.execute('DELETE FROM sqlite_sequence WHERE name IN ("gallery_items", "gallery_media")')
        
        conn.commit()
        print("✅ Gallery database completely reset!")
        print("✅ Admin dashboard will now show clean 5 sections:")
        print("   1. 🛡️ Self Defence Programs")
        print("   2. 📹 Training Videos")
        print("   3. ❤️ Community Programs") 
        print("   4. 📰 News & Events")
        print("   5. 📅 Upcoming Events")
        print("\n🎉 Ready for fresh content!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    force_reset_gallery()
