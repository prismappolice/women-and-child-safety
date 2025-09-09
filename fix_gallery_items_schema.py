#!/usr/bin/env python3
"""
Fix gallery_items table schema - check columns and add missing ones
"""
import sqlite3
import traceback

def fix_gallery_items_schema():
    """Fix gallery_items table schema by adding missing columns"""
    print("🔧 Checking and fixing gallery_items table schema...")
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Check current columns
        cursor.execute("PRAGMA table_info(gallery_items)")
        columns_info = cursor.fetchall()
        existing_columns = [col[1] for col in columns_info]
        
        print(f"📋 Current columns in gallery_items: {existing_columns}")
        
        # Define required columns
        required_columns = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'title': 'TEXT NOT NULL',
            'description': 'TEXT',
            'main_image': 'TEXT',
            'image_url': 'TEXT',  # Backup column for compatibility
            'event_date': 'DATE',
            'category': 'TEXT',
            'is_featured': 'BOOLEAN DEFAULT 0',
            'is_active': 'BOOLEAN DEFAULT 1',
            'created_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
        }
        
        # Add missing columns
        columns_added = []
        for column_name, column_type in required_columns.items():
            if column_name not in existing_columns:
                try:
                    # For adding columns, we use simplified types
                    if column_name == 'id':
                        continue  # Skip ID as it should already exist
                    elif 'DEFAULT' in column_type:
                        cursor.execute(f'ALTER TABLE gallery_items ADD COLUMN {column_name} {column_type}')
                    else:
                        cursor.execute(f'ALTER TABLE gallery_items ADD COLUMN {column_name} {column_type}')
                    columns_added.append(column_name)
                    print(f"   ✅ Added column: {column_name}")
                except Exception as e:
                    print(f"   ⚠️ Could not add {column_name}: {e}")
        
        if columns_added:
            conn.commit()
            print(f"\n🎉 Successfully added {len(columns_added)} columns to gallery_items table")
        else:
            print("\n✅ Gallery_items table already has all required columns")
        
        # Verify final schema
        cursor.execute("PRAGMA table_info(gallery_items)")
        final_columns = cursor.fetchall()
        print(f"\n📋 Final columns in gallery_items: {[col[1] for col in final_columns]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error fixing gallery_items schema: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    fix_gallery_items_schema()
