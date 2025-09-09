#!/usr/bin/env python3
"""
Add Upcoming Events Data
This script adds sample upcoming events to demonstrate the new section
"""

import sqlite3
from datetime import datetime, timedelta

def add_upcoming_events():
    print("Adding Upcoming Events Data...")
    print("=" * 50)
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Check if we already have upcoming events
        cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'upcoming_events'")
        existing_count = cursor.fetchone()[0]
        
        if existing_count > 0:
            print(f"✓ {existing_count} upcoming events already exist")
            conn.close()
            return
        
        # Add sample upcoming events
        upcoming_events = [
            {
                'title': 'Women Safety Awareness Week 2025',
                'description': 'Annual comprehensive women safety awareness week featuring workshops, training sessions, self-defense programs, and community outreach activities.',
                'main_image': '/static/images/slide1.jpg',
                'event_date': '2025-10-15',
                'is_featured': 1
            },
            {
                'title': 'Monthly Self Defense Workshop',
                'description': 'Regular monthly self-defense workshop covering basic techniques, situational awareness, and emergency response strategies for all age groups.',
                'main_image': '/static/images/slide2.jpg',
                'event_date': '2025-09-15',
                'is_featured': 1
            },
            {
                'title': 'Digital Safety Seminar',
                'description': 'Educational seminar on digital safety, cyber security, online privacy protection, and prevention of digital harassment.',
                'main_image': '/static/images/slide3.jpg',
                'event_date': '2025-09-25',
                'is_featured': 0
            },
            {
                'title': 'Community Safety Drive',
                'description': 'Community-wide safety awareness drive focusing on neighborhood watch programs, emergency preparedness, and safety protocols.',
                'main_image': '/static/images/slide4.jpg',
                'event_date': '2025-10-05',
                'is_featured': 0
            },
            {
                'title': 'International Women\'s Day Celebration',
                'description': 'Special celebration honoring women\'s achievements, featuring inspiring speakers, cultural programs, and recognition ceremonies.',
                'main_image': '/static/images/slide5.jpg',
                'event_date': '2026-03-08',
                'is_featured': 1
            }
        ]
        
        # Insert upcoming events
        event_ids = []
        for event in upcoming_events:
            cursor.execute('''
                INSERT INTO gallery_items (title, description, main_image, event_date, category, is_featured, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (event['title'], event['description'], event['main_image'], 
                  event['event_date'], 'upcoming_events', event['is_featured'], 1))
            
            event_ids.append(cursor.lastrowid)
        
        # Add sample media for upcoming events
        sample_media = [
            # Women Safety Week
            {'event_id': event_ids[0], 'media_type': 'image', 'url': '/static/images/slide1.jpg', 'title': 'Safety Week Banner', 'order': 1},
            {'event_id': event_ids[0], 'media_type': 'image', 'url': '/static/images/slide2.jpg', 'title': 'Workshop Schedule', 'order': 2},
            
            # Monthly Workshop
            {'event_id': event_ids[1], 'media_type': 'image', 'url': '/static/images/slide3.jpg', 'title': 'Workshop Venue', 'order': 1},
            {'event_id': event_ids[1], 'media_type': 'image', 'url': '/static/images/slide4.jpg', 'title': 'Training Equipment', 'order': 2},
            
            # Digital Safety
            {'event_id': event_ids[2], 'media_type': 'image', 'url': '/static/images/slide5.jpg', 'title': 'Digital Safety Tips', 'order': 1},
        ]
        
        # Check if gallery_media table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_media'")
        media_table_exists = cursor.fetchone()
        
        if media_table_exists:
            for media in sample_media:
                cursor.execute('''
                    INSERT INTO gallery_media 
                    (gallery_item_id, media_type, media_url, media_title, media_description, display_order, is_active)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (media['event_id'], media['media_type'], media['url'], 
                      media['title'], f"Media for {media['title']}", media['order'], 1))
        
        conn.commit()
        
        # Verify the data
        cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'upcoming_events'")
        total_events = cursor.fetchone()[0]
        
        cursor.execute("SELECT title, event_date FROM gallery_items WHERE category = 'upcoming_events' ORDER BY event_date")
        events_list = cursor.fetchall()
        
        print(f"✓ Added {total_events} upcoming events")
        print("\nUpcoming Events Added:")
        for title, date in events_list:
            print(f"  - {title} ({date})")
        
        if media_table_exists:
            cursor.execute("SELECT COUNT(*) FROM gallery_media WHERE gallery_item_id IN (SELECT id FROM gallery_items WHERE category = 'upcoming_events')")
            media_count = cursor.fetchone()[0]
            print(f"✓ Added {media_count} media files for upcoming events")
        
        conn.close()
        
        print("\n" + "=" * 50)
        print("UPCOMING EVENTS SETUP COMPLETED!")
        print("✓ Admin can now edit upcoming events")
        print("✓ Main website shows upcoming events section")
        print("✓ All data preserved and new section added")
        
        return True
        
    except Exception as e:
        print(f"✗ Error adding upcoming events: {e}")
        return False

if __name__ == "__main__":
    add_upcoming_events()
