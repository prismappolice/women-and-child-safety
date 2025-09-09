#!/usr/bin/env python3
"""
Quick Database Fix for Gallery System
"""

import sqlite3

try:
    print("Fixing database structure...")
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Add main_image column if it doesn't exist
    try:
        cursor.execute("ALTER TABLE gallery_items ADD COLUMN main_image TEXT")
        print("✓ Added main_image column")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("✓ main_image column already exists")
        else:
            print(f"Error adding main_image: {e}")
    
    # Copy image_url to main_image
    try:
        cursor.execute("UPDATE gallery_items SET main_image = image_url WHERE image_url IS NOT NULL AND main_image IS NULL")
        print("✓ Copied image_url to main_image")
    except:
        pass
    
    # Add updated_at column if it doesn't exist
    try:
        cursor.execute("ALTER TABLE gallery_items ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        print("✓ Added updated_at column")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("✓ updated_at column already exists")
    
    # Create gallery_media table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gallery_media (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gallery_item_id INTEGER,
            media_type TEXT CHECK(media_type IN ('image', 'video')),
            media_url TEXT NOT NULL,
            media_title TEXT,
            media_description TEXT,
            display_order INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (gallery_item_id) REFERENCES gallery_items(id) ON DELETE CASCADE
        )
    """)
    print("✓ gallery_media table created")
    
    conn.commit()
    conn.close()
    print("✓ Database structure fixed successfully!")
    
except Exception as e:
    print(f"Error: {e}")
