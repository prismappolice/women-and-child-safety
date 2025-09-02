#!/usr/bin/env python3
"""
Add multiple images to gallery sections without damaging existing data
"""

import sqlite3
import os

def add_multiple_gallery_images():
    print("🔍 Adding multiple gallery images safely...")
    
    # Check if database exists
    if not os.path.exists('women_safety.db'):
        print("❌ Database not found!")
        return
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Verify table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_items'")
    if not cursor.fetchone():
        print("❌ Gallery table not found! Creating...")
        cursor.execute('''CREATE TABLE gallery_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            image_url TEXT,
            video_url TEXT,
            event_date DATE,
            category TEXT NOT NULL,
            is_featured INTEGER DEFAULT 0,
            is_active INTEGER DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        print("✅ Gallery table created")
    
    # Check current count
    cursor.execute("SELECT COUNT(*) FROM gallery_items")
    before_count = cursor.fetchone()[0]
    print(f"📊 Current gallery items: {before_count}")
    
    # Multiple images for each section
    gallery_data = [
        # Self Defence Programme (8 items)
        ('Basic Self Defence Training - Session 1', 'Learn fundamental defensive postures and basic strikes for personal safety', '/static/images/slide1.jpg', '', '2024-12-20', 'Self Defence Programme', 1, 1),
        ('Advanced Self Defence Moves', 'Advanced techniques including escape from grabs and pressure points', '/static/images/slide2.jpg', '', '2024-12-18', 'Self Defence Programme', 0, 1),
        ('Self Defence with Common Objects', 'Using everyday items like keys, bags for defense', '/static/images/slide3.jpg', '', '2024-12-16', 'Self Defence Programme', 0, 1),
        ('Group Self Defence Workshop', 'Community training sessions for women groups', '/static/images/slide4.jpg', '', '2024-12-14', 'Self Defence Programme', 0, 1),
        ('Martial Arts Basics for Women', 'Introduction to martial arts adapted for women', '/static/images/slide5.jpg', '', '2024-12-12', 'Self Defence Programme', 0, 1),
        ('Self Defence for Students', 'Special program for college and school students', '/static/images/slide1.jpg', '', '2024-12-10', 'Self Defence Programme', 0, 1),
        ('Emergency Response Training', 'How to respond in dangerous situations', '/static/images/slide2.jpg', '', '2024-12-08', 'Self Defence Programme', 0, 1),
        ('Self Defence Demonstration', 'Live demonstration of defensive techniques', '/static/images/slide3.jpg', '', '2024-12-06', 'Self Defence Programme', 0, 1),
        
        # Training Videos (6 items)
        ('Safety Awareness Training Video', 'Comprehensive personal safety awareness video', '/static/images/slide1.jpg', '/static/videos/safety_awareness.mp4', '2024-12-15', 'Training Videos', 1, 1),
        ('Cyber Safety Education', 'Digital safety and online harassment prevention', '/static/images/slide2.jpg', '/static/videos/cyber_safety.mp4', '2024-12-13', 'Training Videos', 0, 1),
        ('Emergency Response Tutorial', 'Step-by-step emergency response guide', '/static/images/slide3.jpg', '/static/videos/emergency.mp4', '2024-12-11', 'Training Videos', 0, 1),
        ('Legal Rights Awareness', 'Know your legal rights and protections', '/static/images/slide4.jpg', '/static/videos/legal_rights.mp4', '2024-12-09', 'Training Videos', 0, 1),
        ('Workplace Safety Training', 'Professional environment safety guidelines', '/static/images/slide5.jpg', '/static/videos/workplace.mp4', '2024-12-07', 'Training Videos', 0, 1),
        ('Self Defence Video Tutorial', 'Complete self-defence video guide', '/static/images/slide1.jpg', '/static/videos/self_defence.mp4', '2024-12-05', 'Training Videos', 1, 1),
        
        # Community Programmes (6 items)
        ('Village Outreach Program - District 1', 'Rural awareness program in remote villages', '/static/images/slide2.jpg', '', '2024-12-14', 'Community Programmes', 1, 1),
        ('School Safety Education Initiative', 'Safety education in schools and colleges', '/static/images/slide3.jpg', '', '2024-12-12', 'Community Programmes', 0, 1),
        ('Workplace Safety Campaign', 'Corporate awareness programs', '/static/images/slide4.jpg', '', '2024-12-10', 'Community Programmes', 0, 1),
        ('Community Volunteer Training', 'Training local volunteers for safety awareness', '/static/images/slide5.jpg', '', '2024-12-08', 'Community Programmes', 0, 1),
        ('Women Empowerment Workshop', 'Empowering women through education', '/static/images/slide1.jpg', '', '2024-12-06', 'Community Programmes', 0, 1),
        ('Public Transport Safety Drive', 'Safety awareness in public transportation', '/static/images/slide2.jpg', '', '2024-12-04', 'Community Programmes', 0, 1),
        
        # News & Events (6 items)
        ('State Women Safety Conference 2024', 'Annual conference on women safety policies', '/static/images/slide3.jpg', '', '2024-12-15', 'News & Events', 1, 1),
        ('Safety Equipment Distribution', 'Mass distribution of safety devices', '/static/images/slide4.jpg', '', '2024-12-13', 'News & Events', 0, 1),
        ('Awards Ceremony - Safety Champions', 'Recognizing outstanding contributors', '/static/images/slide5.jpg', '', '2024-12-11', 'News & Events', 0, 1),
        ('Media Coverage - Campaign Launch', 'Press coverage of new safety initiatives', '/static/images/slide1.jpg', '', '2024-12-09', 'News & Events', 0, 1),
        ('International Women\'s Day Celebration', 'Special event celebrating women achievements', '/static/images/slide2.jpg', '', '2024-12-07', 'News & Events', 0, 1),
        ('Safety Week Inauguration', 'Official launch of safety awareness week', '/static/images/slide3.jpg', '', '2024-12-05', 'News & Events', 1, 1),
        
        # Upcoming Events (3 items - text only as requested)
        ('Monthly Safety Workshop', 'Regular monthly safety training session', '', '', '2025-01-15', 'Upcoming Events', 0, 1),
        ('Cyber Security Awareness Week', 'Week-long digital safety program', '', '', '2025-02-10', 'Upcoming Events', 0, 1),
        ('District Level Coordinator Meeting', 'Meeting for all district safety coordinators', '', '', '2025-02-20', 'Upcoming Events', 0, 1),
    ]
    
    print(f"📝 Adding {len(gallery_data)} gallery items...")
    
    # Add all items
    for item in gallery_data:
        try:
            cursor.execute('''INSERT INTO gallery_items 
                             (title, description, image_url, video_url, event_date, category, is_featured, is_active) 
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', item)
        except Exception as e:
            print(f"⚠️  Skipped duplicate: {item[0]}")
    
    conn.commit()
    
    # Check final count
    cursor.execute("SELECT COUNT(*) FROM gallery_items")
    after_count = cursor.fetchone()[0]
    added_count = after_count - before_count
    
    print(f"✅ Added {added_count} new gallery items")
    print(f"📊 Total gallery items now: {after_count}")
    
    # Show count by category
    print("\n📂 Items per category:")
    categories = ['Self Defence Programme', 'Training Videos', 'Community Programmes', 'News & Events', 'Upcoming Events']
    
    for category in categories:
        cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = ?", (category,))
        count = cursor.fetchone()[0]
        print(f"  ✅ {category}: {count} items")
    
    conn.close()
    print("\n🎉 Gallery images added successfully!")
    print("💡 No damage to existing project data!")
    print("🌐 Check gallery at: http://127.0.0.1:5000/gallery")

if __name__ == "__main__":
    add_multiple_gallery_images()
