#!/usr/bin/env python3
"""
Ensure gallery_items table has all required columns
"""
import sqlite3

def ensure_gallery_columns():
    """Add any missing columns to gallery_items table"""
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Check current columns
        cursor.execute("PRAGMA table_info(gallery_items)")
        existing_columns = [col[1] for col in cursor.fetchall()]
        print(f"Current gallery_items columns: {existing_columns}")
        
        # Add missing columns one by one
        required_columns = [
            ('main_image', 'TEXT'),
            ('image_url', 'TEXT'),
            ('event_date', 'DATE'),
            ('category', 'TEXT'),
            ('is_featured', 'BOOLEAN DEFAULT 0'),
            ('is_active', 'BOOLEAN DEFAULT 1')
        ]
        
        for col_name, col_type in required_columns:
            if col_name not in existing_columns:
                try:
                    cursor.execute(f'ALTER TABLE gallery_items ADD COLUMN {col_name} {col_type}')
                    print(f"Added column: {col_name}")
                except Exception as e:
                    print(f"Could not add {col_name}: {e}")
        
        conn.commit()
        conn.close()
        print("Gallery table columns updated successfully!")
        
    except Exception as e:
        print(f"Error updating gallery table: {e}")

if __name__ == "__main__":
    ensure_gallery_columns()
