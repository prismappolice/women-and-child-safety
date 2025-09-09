#!/usr/bin/env python3
"""
Enhanced Gallery System Setup
This script creates an advanced gallery system that supports multiple images and videos per gallery item.
"""

import sqlite3
import os

def setup_enhanced_gallery():
    print("Setting up Enhanced Gallery System...")
    print("=" * 50)
    
    # Connect to database
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Create enhanced gallery_items table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gallery_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            main_image TEXT,
            event_date TEXT,
            category TEXT,
            is_featured INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create gallery_media table for multiple images/videos
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
    
    # Clear existing data and set up fresh content
    cursor.execute("DELETE FROM gallery_items")
    cursor.execute("DELETE FROM gallery_media")
    
    # Self Defense Programs
    self_defense_items = [
        {
            'title': 'Basic Self Defense Training',
            'description': 'Comprehensive basic self-defense training covering fundamental techniques, awareness, and safety protocols.',
            'main_image': '/static/images/slide1.jpg',
            'event_date': '2025-09-15',
            'category': 'self_defense_programs',
            'is_featured': 1
        },
        {
            'title': 'Advanced Combat Techniques',
            'description': 'Advanced self-defense training including martial arts, tactical awareness, and emergency response.',
            'main_image': '/static/images/slide2.jpg',
            'event_date': '2025-10-01',
            'category': 'self_defense_programs',
            'is_featured': 1
        },
        {
            'title': 'Women\'s Empowerment Workshop',
            'description': 'Combining physical training with psychological empowerment and confidence building.',
            'main_image': '/static/images/slide3.jpg',
            'event_date': '2025-10-15',
            'category': 'self_defense_programs',
            'is_featured': 0
        }
    ]
    
    # Training Videos
    training_videos = [
        {
            'title': 'Self Defense Tutorial Series',
            'description': 'Step-by-step video tutorials covering various self-defense techniques and safety procedures.',
            'main_image': '/static/images/slide4.jpg',
            'event_date': '2025-09-01',
            'category': 'training_videos',
            'is_featured': 1
        },
        {
            'title': 'Emergency Response Training',
            'description': 'Video guides for emergency situations, first aid, and crisis management.',
            'main_image': '/static/images/slide5.jpg',
            'event_date': '2025-09-10',
            'category': 'training_videos',
            'is_featured': 1
        }
    ]
    
    # Community Programs
    community_programs = [
        {
            'title': 'Community Safety Outreach',
            'description': 'Reaching out to communities across Andhra Pradesh to spread safety awareness.',
            'main_image': '/static/images/slide1.jpg',
            'event_date': '2025-09-20',
            'category': 'community_programs',
            'is_featured': 1
        },
        {
            'title': 'School Safety Programs',
            'description': 'Safety awareness and training programs conducted in schools and colleges.',
            'main_image': '/static/images/slide2.jpg',
            'event_date': '2025-09-25',
            'category': 'community_programs',
            'is_featured': 0
        }
    ]
    
    # News and Events
    news_events = [
        {
            'title': 'Women Safety Week 2025',
            'description': 'Annual women safety awareness week with multiple events and workshops.',
            'main_image': '/static/images/slide3.jpg',
            'event_date': '2025-10-05',
            'category': 'news_events',
            'is_featured': 1
        },
        {
            'title': 'State Safety Conference',
            'description': 'State-level conference on women safety initiatives and policy updates.',
            'main_image': '/static/images/slide4.jpg',
            'event_date': '2025-10-20',
            'category': 'news_events',
            'is_featured': 0
        }
    ]
    
    # Insert all items
    all_items = self_defense_items + training_videos + community_programs + news_events
    gallery_item_ids = []
    
    for item in all_items:
        cursor.execute("""
            INSERT INTO gallery_items (title, description, main_image, event_date, category, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (item['title'], item['description'], item['main_image'], item['event_date'], 
              item['category'], item['is_featured'], 1))
        
        gallery_item_ids.append(cursor.lastrowid)
    
    # Add sample media files for each gallery item
    sample_media = [
        # For each gallery item, add multiple sample images and videos
        {'gallery_item_id': gallery_item_ids[0], 'media_type': 'image', 'media_url': '/static/images/slide1.jpg', 'media_title': 'Training Session 1', 'display_order': 1},
        {'gallery_item_id': gallery_item_ids[0], 'media_type': 'image', 'media_url': '/static/images/slide2.jpg', 'media_title': 'Training Session 2', 'display_order': 2},
        {'gallery_item_id': gallery_item_ids[0], 'media_type': 'image', 'media_url': '/static/images/slide3.jpg', 'media_title': 'Training Session 3', 'display_order': 3},
        
        {'gallery_item_id': gallery_item_ids[1], 'media_type': 'image', 'media_url': '/static/images/slide4.jpg', 'media_title': 'Advanced Training 1', 'display_order': 1},
        {'gallery_item_id': gallery_item_ids[1], 'media_type': 'image', 'media_url': '/static/images/slide5.jpg', 'media_title': 'Advanced Training 2', 'display_order': 2},
        
        {'gallery_item_id': gallery_item_ids[3], 'media_type': 'video', 'media_url': '/static/videos/sample_video.mp4', 'media_title': 'Tutorial Video 1', 'display_order': 1},
        {'gallery_item_id': gallery_item_ids[3], 'media_type': 'video', 'media_url': '/static/videos/sample_video2.mp4', 'media_title': 'Tutorial Video 2', 'display_order': 2},
    ]
    
    for media in sample_media:
        cursor.execute("""
            INSERT INTO gallery_media (gallery_item_id, media_type, media_url, media_title, media_description, display_order, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (media['gallery_item_id'], media['media_type'], media['media_url'], 
              media['media_title'], media.get('media_description', ''), media['display_order'], 1))
    
    # Commit changes
    conn.commit()
    
    # Verify setup
    cursor.execute("SELECT COUNT(*) FROM gallery_items")
    total_items = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM gallery_media")
    total_media = cursor.fetchone()[0]
    
    cursor.execute("SELECT category, COUNT(*) FROM gallery_items GROUP BY category")
    category_counts = cursor.fetchall()
    
    print(f"✓ Enhanced Gallery System Setup Complete!")
    print(f"  - Total Gallery Items: {total_items}")
    print(f"  - Total Media Files: {total_media}")
    print("\nCategory Distribution:")
    
    for category, count in category_counts:
        print(f"  - {category.replace('_', ' ').title()}: {count} items")
    
    print("\nFeatures Available:")
    print("  ✓ Multiple images per gallery item")
    print("  ✓ Multiple videos per gallery item") 
    print("  ✓ Admin can add unlimited media files")
    print("  ✓ Media files have titles and descriptions")
    print("  ✓ Display order control")
    print("  ✓ Individual media file management")
    
    conn.close()
    return True

if __name__ == "__main__":
    setup_enhanced_gallery()
