#!/usr/bin/env python3
"""
Fix gallery_items table - add missing image columns safely
"""
import sqlite3

def fix_gallery_items_columns():
    """Add missing image columns to gallery_items table without affecting data"""
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        print("🔧 Fixing gallery_items table image columns...")
        
        # Check current columns
        cursor.execute("PRAGMA table_info(gallery_items)")
        existing_columns = [col[1] for col in cursor.fetchall()]
        print(f"📋 Current columns: {existing_columns}")
        
        # Add missing image columns
        columns_to_add = [
            ('main_image', 'TEXT'),
            ('image_url', 'TEXT'),
            ('event_date', 'DATE'),
            ('category', 'TEXT'),
            ('is_featured', 'BOOLEAN DEFAULT 0'),
            ('is_active', 'BOOLEAN DEFAULT 1')
        ]
        
        added_columns = []
        for col_name, col_type in columns_to_add:
            if col_name not in existing_columns:
                try:
                    cursor.execute(f'ALTER TABLE gallery_items ADD COLUMN {col_name} {col_type}')
                    added_columns.append(col_name)
                    print(f"✅ Added column: {col_name}")
                except Exception as e:
                    print(f"⚠️ Could not add {col_name}: {e}")
        
        if added_columns:
            conn.commit()
            print(f"🎉 Successfully added {len(added_columns)} columns")
        else:
            print("✅ All required columns already exist")
        
        # Check data count to ensure no data loss
        cursor.execute("SELECT COUNT(*) FROM gallery_items")
        count = cursor.fetchone()[0]
        print(f"📊 Gallery items preserved: {count} records")
        
        # Verify final schema
        cursor.execute("PRAGMA table_info(gallery_items)")
        final_columns = [col[1] for col in cursor.fetchall()]
        print(f"📋 Final columns: {final_columns}")
        
        conn.close()
        print("🎉 Gallery items table fixed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    fix_gallery_items_columns()
