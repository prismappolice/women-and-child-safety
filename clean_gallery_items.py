#!/usr/bin/env python3
"""
Clean Gallery Items - Remove old items, keep structure for new 5 sections
This will remove existing gallery items but preserve the database structure
so admin can add fresh content to the 5 new sections.
"""

import sqlite3
import os

def clean_gallery_items():
    """Remove existing gallery items but keep database structure"""
    
    db_path = 'women_safety.db'
    
    if not os.path.exists(db_path):
        print(f"Database {db_path} not found!")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Show current items before deletion
        cursor.execute('SELECT COUNT(*) FROM gallery_items')
        count = cursor.fetchone()[0]
        print(f"Found {count} existing gallery items")
        
        if count > 0:
            cursor.execute('SELECT id, title, category FROM gallery_items LIMIT 5')
            items = cursor.fetchall()
            print("\nSample existing items:")
            for item in items:
                print(f"  - ID: {item[0]}, Title: {item[1]}, Category: {item[2]}")
            
            # Delete all existing gallery items
            cursor.execute('DELETE FROM gallery_items')
            deleted_items = cursor.rowcount
            print(f"\n✅ Deleted {deleted_items} existing gallery items")
            
            # Also clean gallery_media if it exists
            try:
                cursor.execute('DELETE FROM gallery_media')
                deleted_media = cursor.rowcount
                print(f"✅ Deleted {deleted_media} media files")
            except:
                pass
            
            # Reset auto-increment
            cursor.execute('DELETE FROM sqlite_sequence WHERE name="gallery_items"')
            cursor.execute('DELETE FROM sqlite_sequence WHERE name="gallery_media"')
            
            conn.commit()
            print("✅ Gallery cleaned successfully!")
            print("\nNow admin can add fresh content to the 5 new sections:")
            print("  1. Self Defence Programs")
            print("  2. Training Videos") 
            print("  3. Community Programs")
            print("  4. News & Events")
            print("  5. Upcoming Events")
            
        else:
            print("No existing items found - gallery is already clean!")
            
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    clean_gallery_items()
