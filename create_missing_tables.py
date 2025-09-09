#!/usr/bin/env python3
"""
Check and create missing content tables
"""
import sqlite3

def check_and_create_tables():
    """Check if content tables exist and create if missing"""
    print("🔍 Checking Content Tables...")
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Get list of existing tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        existing_tables = [table[0] for table in cursor.fetchall()]
        print(f"📋 Existing tables: {existing_tables}")
        
        required_tables = {
            'about_content': 'About page sections',
            'safety_tips': 'Safety tips',
            'pdf_resources': 'PDF resources',
            'home_content': 'Home page content'
        }
        
        missing_tables = []
        for table, description in required_tables.items():
            if table in existing_tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                print(f"✅ {description}: {count} records")
            else:
                missing_tables.append((table, description))
                print(f"❌ {description}: TABLE MISSING")
        
        # Create missing tables
        if missing_tables:
            print(f"\n🔧 Creating {len(missing_tables)} missing tables...")
            
            # Create about_content table
            if 'about_content' in [t[0] for t in missing_tables]:
                cursor.execute('''
                    CREATE TABLE about_content (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        section_name TEXT NOT NULL,
                        title TEXT,
                        content TEXT NOT NULL,
                        image_url TEXT,
                        sort_order INTEGER DEFAULT 0,
                        is_active INTEGER DEFAULT 1,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                print("✅ Created about_content table")
            
            # Create safety_tips table  
            if 'safety_tips' in [t[0] for t in missing_tables]:
                cursor.execute('''
                    CREATE TABLE safety_tips (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        category TEXT,
                        icon_class TEXT,
                        is_featured BOOLEAN DEFAULT 0,
                        is_active BOOLEAN DEFAULT 1,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                print("✅ Created safety_tips table")
            
            # Create pdf_resources table
            if 'pdf_resources' in [t[0] for t in missing_tables]:
                cursor.execute('''
                    CREATE TABLE pdf_resources (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        file_path TEXT NOT NULL,
                        file_size INTEGER,
                        download_count INTEGER DEFAULT 0,
                        is_active BOOLEAN DEFAULT 1,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                print("✅ Created pdf_resources table")
            
            # Create home_content table
            if 'home_content' in [t[0] for t in missing_tables]:
                cursor.execute('''
                    CREATE TABLE home_content (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        section_name TEXT NOT NULL,
                        title TEXT,
                        content TEXT NOT NULL,
                        image_url TEXT,
                        link_url TEXT,
                        icon_class TEXT,
                        display_order INTEGER DEFAULT 0,
                        is_active INTEGER DEFAULT 1,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                print("✅ Created home_content table")
            
            conn.commit()
            print("🎉 All missing tables created!")
        else:
            print("✅ All required tables exist")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_and_create_tables()
