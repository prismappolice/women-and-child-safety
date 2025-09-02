#!/usr/bin/env python3
"""
Add multiple Self Defence Programme images and videos
"""

import sqlite3
from datetime import datetime, timedelta

def add_self_defence_content():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Check current count of Self Defence items
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'Self Defence Programme'")
    current_count = cursor.fetchone()[0]
    print(f"Current Self Defence Programme items: {current_count}")
    
    # Add multiple self defence content
    self_defence_items = [
        {
            'title': 'Basic Self Defence Training - Session 1',
            'description': 'Introduction to personal safety awareness and basic defensive postures. Learn how to stay alert and recognize potential threats in various situations.',
            'image_url': '/static/images/slide1.jpg',
            'video_url': '',
            'event_date': '2024-12-15',
            'category': 'Self Defence Programme',
            'is_featured': 1,
            'is_active': 1
        },
        {
            'title': 'Advanced Self Defence Techniques',
            'description': 'Advanced defensive moves including escape techniques, pressure points, and effective strikes. Practical training for real-world scenarios.',
            'image_url': '/static/images/slide2.jpg',
            'video_url': '',
            'event_date': '2024-12-12',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Self Defence with Everyday Objects',
            'description': 'Learn how to use common items like keys, bags, and mobile phones as defensive tools. Practical techniques for urban environments.',
            'image_url': '/static/images/slide3.jpg',
            'video_url': '',
            'event_date': '2024-12-10',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Martial Arts Basics for Women',
            'description': 'Introduction to martial arts moves specifically adapted for women. Focus on leverage and technique over strength.',
            'image_url': '/static/images/slide4.jpg',
            'video_url': '',
            'event_date': '2024-12-08',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Self Defence Training Video - Complete Guide',
            'description': 'Comprehensive video tutorial covering all aspects of personal safety and self-defence techniques. Step-by-step instructions for beginners.',
            'image_url': '/static/images/slide5.jpg',
            'video_url': '/static/videos/self_defence_tutorial.mp4',
            'event_date': '2024-12-05',
            'category': 'Self Defence Programme',
            'is_featured': 1,
            'is_active': 1
        },
        {
            'title': 'Group Self Defence Workshop',
            'description': 'Community workshop where multiple participants practice together. Learn team-based safety strategies and support systems.',
            'image_url': '/static/images/slide1.jpg',
            'video_url': '',
            'event_date': '2024-12-03',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Self Defence for Students',
            'description': 'Special program designed for college and school students. Focus on campus safety and public transport security.',
            'image_url': '/static/images/slide2.jpg',
            'video_url': '',
            'event_date': '2024-12-01',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Emergency Response Training',
            'description': 'Learn how to respond in emergency situations. Includes calling for help, escape routes, and first aid basics.',
            'image_url': '/static/images/slide3.jpg',
            'video_url': '',
            'event_date': '2024-11-28',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        }
    ]
    
    # Clear existing Self Defence items first to avoid duplicates
    cursor.execute("DELETE FROM gallery_items WHERE category = 'Self Defence Programme'")
    
    # Insert new items
    for item in self_defence_items:
        cursor.execute('''
            INSERT INTO gallery_items (title, description, image_url, video_url, event_date, category, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            item['title'],
            item['description'],
            item['image_url'],
            item['video_url'],
            item['event_date'],
            item['category'],
            item['is_featured'],
            item['is_active']
        ))
    
    conn.commit()
    
    # Verify the additions
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'Self Defence Programme'")
    new_count = cursor.fetchone()[0]
    print(f"✅ Added {new_count} Self Defence Programme items")
    
    # Show sample items
    cursor.execute("SELECT title, description FROM gallery_items WHERE category = 'Self Defence Programme' LIMIT 3")
    samples = cursor.fetchall()
    print("\nSample items added:")
    for i, (title, desc) in enumerate(samples, 1):
        print(f"{i}. {title}")
        print(f"   {desc[:80]}...")
    
    conn.close()
    print("\n🎯 Self Defence Programme content updated successfully!")

if __name__ == "__main__":
    add_self_defence_content()
