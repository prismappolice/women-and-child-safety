#!/usr/bin/env python3
"""
Setup script to populate gallery items in the women safety database.
This script adds default gallery content for Self Defense and Media sections.
"""

import sqlite3

def setup_gallery_content():
    # Connect to database
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # First, check if gallery_items table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gallery_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            image_url TEXT,
            event_date TEXT,
            category TEXT,
            is_featured INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Clear existing gallery items to start fresh
    cursor.execute("DELETE FROM gallery_items")
    
    # Self Defense Training Items
    self_defense_items = [
        (
            'Basic Self Defense Workshop',
            'Comprehensive self-defense training program covering basic techniques, situational awareness, and emergency response for women of all ages.',
            '/static/images/slide1.jpg',
            '2024-12-15',
            'self_defense',
            1,
            1
        ),
        (
            'Advanced Self Defense Techniques',
            'Advanced training sessions including martial arts basics, defensive strategies, and confidence building exercises conducted by certified instructors.',
            '/static/images/slide2.jpg',
            '2025-01-10',
            'self_defense',
            1,
            1
        ),
        (
            'Self Defense for Students',
            'Special training programs designed for school and college students focusing on campus safety, personal protection, and emergency response.',
            '/static/images/slide3.jpg',
            '2025-02-05',
            'self_defense',
            0,
            1
        ),
        (
            'Women\'s Empowerment Through Self Defense',
            'Comprehensive program combining physical training with psychological empowerment, building confidence and self-reliance among women.',
            '/static/images/slide4.jpg',
            '2025-03-08',
            'self_defense',
            0,
            1
        ),
        (
            'Community Self Defense Initiative',
            'Neighborhood-based self defense training programs bringing safety education directly to local communities across Andhra Pradesh.',
            '/static/images/slide5.jpg',
            '2025-03-15',
            'self_defense',
            0,
            1
        )
    ]
    
    # Media Gallery Items
    media_items = [
        (
            'Training Session Photos',
            'Photo gallery featuring highlights from our self defense training sessions, workshops, and community programs.',
            '/static/images/slide1.jpg',
            '2025-01-01',
            'media',
            1,
            1
        ),
        (
            'Training Videos',
            'Video tutorials and demonstrations of self defense techniques, safety tips, and emergency response procedures.',
            '/static/images/slide2.jpg',
            '2025-01-01',
            'media',
            1,
            1
        ),
        (
            'Success Stories',
            'Visual stories and testimonials from women who have successfully used self defense techniques to protect themselves.',
            '/static/images/slide3.jpg',
            '2025-01-01',
            'media',
            0,
            1
        ),
        (
            'News & Events',
            'Latest news, upcoming events, and media coverage of our women safety initiatives and training programs.',
            '/static/images/slide4.jpg',
            '2025-01-01',
            'media',
            0,
            1
        ),
        (
            'Safety Awareness Campaigns',
            'Documentation of our public awareness campaigns, workshops, and community outreach programs for women\'s safety.',
            '/static/images/slide5.jpg',
            '2025-01-01',
            'media',
            0,
            1
        )
    ]
    
    # Insert self defense items
    for item in self_defense_items:
        cursor.execute("""
            INSERT INTO gallery_items (title, description, image_url, event_date, category, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, item)
    
    # Insert media items
    for item in media_items:
        cursor.execute("""
            INSERT INTO gallery_items (title, description, image_url, event_date, category, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, item)
    
    # Commit changes
    conn.commit()
    
    # Verify the setup
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'self_defense'")
    self_defense_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'media'")
    media_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE is_active = 1")
    total_active = cursor.fetchone()[0]
    
    print(f"Gallery setup completed successfully!")
    print(f"- Self Defense items: {self_defense_count}")
    print(f"- Media items: {media_count}")
    print(f"- Total active items: {total_active}")
    
    # Show sample data
    print("\nSample gallery items:")
    cursor.execute("SELECT title, category, event_date FROM gallery_items LIMIT 5")
    samples = cursor.fetchall()
    for title, category, date in samples:
        print(f"- {title} ({category}) - {date}")
    
    conn.close()

if __name__ == "__main__":
    setup_gallery_content()
