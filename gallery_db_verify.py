#!/usr/bin/env python3
"""
Simple gallery database verification
"""

import sqlite3
import os

def verify_gallery_setup():
    print("🔍 GALLERY DATABASE VERIFICATION")
    print("=" * 40)
    
    if not os.path.exists('women_safety.db'):
        print("❌ Database file not found - creating new database")
        create_gallery_table()
        return
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Check if table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_items'")
    if not cursor.fetchone():
        print("❌ gallery_items table not found - creating table")
        create_gallery_table()
        return
    
    print("✅ gallery_items table exists")
    
    # Check data count
    cursor.execute("SELECT COUNT(*) FROM gallery_items")
    count = cursor.fetchone()[0]
    print(f"📊 Total gallery items: {count}")
    
    # Check categories
    cursor.execute("SELECT DISTINCT category FROM gallery_items")
    categories = [row[0] for row in cursor.fetchall()]
    print(f"📂 Current categories: {categories}")
    
    expected_categories = ['Self Defence Programme', 'Training Videos', 'Community Programmes', 'News & Events', 'Upcoming Events']
    
    missing_categories = []
    for cat in expected_categories:
        cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = ?", (cat,))
        cat_count = cursor.fetchone()[0]
        if cat_count > 0:
            print(f"✅ Category '{cat}' has {cat_count} items")
        else:
            print(f"❌ Category '{cat}' has no items")
            missing_categories.append(cat)
    
    # Add sample data for missing categories
    if missing_categories and count == 0:
        print("\n📝 Adding sample data for all categories...")
        add_sample_data(cursor)
        conn.commit()
        print("✅ Sample data added successfully")
    
    conn.close()
    print("\n🎉 Gallery setup verification completed!")

def create_gallery_table():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gallery_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            image_url TEXT,
            video_url TEXT,
            event_date DATE,
            category TEXT NOT NULL,
            is_featured INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print("✅ gallery_items table created")
    add_sample_data(cursor)
    conn.commit()
    conn.close()

def add_sample_data(cursor):
    sample_data = [
        ('Basic Self Defence Training', 'Comprehensive self-defence training session for women covering basic techniques and safety awareness.', '/static/images/slide1.jpg', '2024-12-15', 'Self Defence Programme', 1),
        ('Safety Awareness Video', 'Educational video demonstrating personal safety tips and emergency response procedures.', '/static/images/slide2.jpg', '2024-12-10', 'Training Videos', 1),
        ('Community Outreach Program', 'Village-level awareness program focusing on women\'s rights and safety measures.', '/static/images/slide3.jpg', '2024-12-05', 'Community Programmes', 1),
        ('Women Safety Week Inauguration', 'Official launch of the state-wide women safety awareness week with participation from dignitaries.', '/static/images/slide4.jpg', '2024-12-01', 'News & Events', 1),
        ('District Level Safety Workshop', 'Upcoming workshop scheduled for all district coordinators to discuss safety initiatives.', '/static/images/slide5.jpg', '2025-01-15', 'Upcoming Events', 1)
    ]
    
    for item in sample_data:
        cursor.execute('''
            INSERT INTO gallery_items (title, description, image_url, event_date, category, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', item)

if __name__ == "__main__":
    verify_gallery_setup()
