#!/usr/bin/env python3
"""
Clean Only Gallery Script - No Sample Data
This script only cleans the gallery database without adding any sample content
Admin dashboard will show completely empty sections ready for fresh content
"""

import sqlite3
import os

def clean_gallery_only():
    """Clean gallery database completely - no sample data"""
    
    db_path = 'women_safety.db'
    
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("🧹 Cleaning gallery database (no sample data will be added)...")
        
        # Delete all gallery items
        cursor.execute('DELETE FROM gallery_items')
        deleted_items = cursor.rowcount
        print(f"🗑️ Deleted {deleted_items} gallery items")
        
        # Delete all gallery media
        try:
            cursor.execute('DELETE FROM gallery_media')
            deleted_media = cursor.rowcount
            print(f"🗑️ Deleted {deleted_media} media files")
        except:
            print("ℹ️ No gallery_media table found")
        
        # Reset auto-increment counters
        cursor.execute('DELETE FROM sqlite_sequence WHERE name IN ("gallery_items", "gallery_media")')
        
        # Ensure proper table structure exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gallery_items (
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
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gallery_media (
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
        
        conn.commit()
        
        # Verify clean state
        cursor.execute('SELECT COUNT(*) FROM gallery_items')
        count = cursor.fetchone()[0]
        
        if count == 0:
            print("✅ Gallery completely cleaned!")
            print("✅ Admin dashboard will show empty 5 sections:")
            print("   - 🛡️ Self Defence Programs")
            print("   - 📹 Training Videos")
            print("   - ❤️ Community Programs")
            print("   - 📰 News & Events")
            print("   - 📅 Upcoming Events")
            print("\n🎯 Ready for admin to add fresh content!")
        else:
            print(f"⚠️ Warning: {count} items still remain")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    clean_gallery_only()
