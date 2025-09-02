#!/usr/bin/env python3
"""
Gallery table setup script for 5-section gallery structure
"""

import sqlite3
import os

def setup_gallery_table():
    """Setup gallery_items table with required columns"""
    
    # Check if database exists
    db_path = 'women_safety.db'
    if not os.path.exists(db_path):
        print("Database file doesn't exist. Creating new database...")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create gallery_items table if it doesn't exist
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
    
    print("✓ Gallery items table created/verified")
    
    # Check if there are any existing items
    cursor.execute("SELECT COUNT(*) FROM gallery_items")
    count = cursor.fetchone()[0]
    print(f"Current gallery items count: {count}")
    
    # Add sample data for each of the 5 categories if table is empty
    if count == 0:
        print("Adding sample data for all 5 categories...")
        
        sample_data = [
            {
                'title': 'Basic Self Defence Training',
                'description': 'Comprehensive self-defence training session for women covering basic techniques and safety awareness.',
                'image_url': '/static/images/slide1.jpg',
                'event_date': '2024-12-15',
                'category': 'Self Defence Programme',
                'is_featured': 1,
                'is_active': 1
            },
            {
                'title': 'Safety Awareness Video',
                'description': 'Educational video demonstrating personal safety tips and emergency response procedures.',
                'image_url': '/static/images/slide2.jpg',
                'event_date': '2024-12-10',
                'category': 'Training Videos',
                'is_featured': 1,
                'is_active': 1
            },
            {
                'title': 'Community Outreach Program',
                'description': 'Village-level awareness program focusing on women\'s rights and safety measures.',
                'image_url': '/static/images/slide3.jpg',
                'event_date': '2024-12-05',
                'category': 'Community Programmes',
                'is_featured': 1,
                'is_active': 1
            },
            {
                'title': 'Women Safety Week Inauguration',
                'description': 'Official launch of the state-wide women safety awareness week with participation from dignitaries.',
                'image_url': '/static/images/slide4.jpg',
                'event_date': '2024-12-01',
                'category': 'News & Events',
                'is_featured': 1,
                'is_active': 1
            },
            {
                'title': 'District Level Safety Workshop',
                'description': 'Upcoming workshop scheduled for all district coordinators to discuss safety initiatives.',
                'image_url': '/static/images/slide5.jpg',
                'event_date': '2025-01-15',
                'category': 'Upcoming Events',
                'is_featured': 1,
                'is_active': 1
            }
        ]
        
        for item in sample_data:
            cursor.execute('''
                INSERT INTO gallery_items (title, description, image_url, event_date, category, is_featured, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                item['title'],
                item['description'],
                item['image_url'],
                item['event_date'],
                item['category'],
                item['is_featured'],
                item['is_active']
            ))
        
        print(f"✓ Added {len(sample_data)} sample gallery items")
    
    # Display current categories
    cursor.execute("SELECT DISTINCT category FROM gallery_items")
    categories = [row[0] for row in cursor.fetchall()]
    print(f"Available categories: {categories}")
    
    conn.commit()
    conn.close()
    
    print("✓ Gallery table setup completed successfully!")

if __name__ == "__main__":
    setup_gallery_table()
