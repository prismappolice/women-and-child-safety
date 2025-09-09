#!/usr/bin/env python3
"""
Fix gallery_media table schema - add missing media_type column safely
"""
import sqlite3

def fix_gallery_media_schema():
    """Add missing media_type column to gallery_media table without affecting other data"""
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        print("🔧 Fixing gallery_media table schema...")
        
        # Check if gallery_media table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_media'")
        if not cursor.fetchone():
            print("📋 Creating gallery_media table...")
            cursor.execute('''
                CREATE TABLE gallery_media (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    gallery_item_id INTEGER,
                    media_url TEXT,
                    media_type TEXT DEFAULT 'image',
                    caption TEXT,
                    is_active BOOLEAN DEFAULT 1,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (gallery_item_id) REFERENCES gallery_items (id)
                )
            ''')
            print("✅ Created gallery_media table with all required columns")
        else:
            # Check current columns
            cursor.execute("PRAGMA table_info(gallery_media)")
            existing_columns = [col[1] for col in cursor.fetchall()]
            print(f"📋 Current gallery_media columns: {existing_columns}")
            
            # Add missing columns
            required_columns = [
                ('media_type', 'TEXT DEFAULT \'image\''),
                ('caption', 'TEXT'),
                ('is_active', 'BOOLEAN DEFAULT 1'),
                ('created_at', 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP')
            ]
            
            for col_name, col_type in required_columns:
                if col_name not in existing_columns:
                    try:
                        cursor.execute(f'ALTER TABLE gallery_media ADD COLUMN {col_name} {col_type}')
                        print(f"✅ Added column: {col_name}")
                    except Exception as e:
                        print(f"⚠️ Could not add {col_name}: {e}")
        
        conn.commit()
        
        # Verify final schema
        cursor.execute("PRAGMA table_info(gallery_media)")
        final_columns = [col[1] for col in cursor.fetchall()]
        print(f"📋 Final gallery_media columns: {final_columns}")
        
        # Check data count to ensure no data loss
        cursor.execute("SELECT COUNT(*) FROM gallery_media")
        media_count = cursor.fetchone()[0]
        print(f"📊 Gallery media records preserved: {media_count}")
        
        conn.close()
        print("🎉 Gallery media table schema fixed successfully!")
        
    except Exception as e:
        print(f"❌ Error fixing gallery_media schema: {e}")
        return False
    
    return True

if __name__ == "__main__":
    fix_gallery_media_schema()
