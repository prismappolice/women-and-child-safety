#!/usr/bin/env python3
"""
Complete Gallery System Update
This script performs all necessary updates for the enhanced gallery system
"""

import sqlite3

def complete_gallery_update():
    print("COMPLETE GALLERY SYSTEM UPDATE")
    print("=" * 50)
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Step 1: Update database structure
        print("Step 1: Updating database structure...")
        
        # Check and add main_image column
        cursor.execute("PRAGMA table_info(gallery_items)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'main_image' not in columns:
            cursor.execute("ALTER TABLE gallery_items ADD COLUMN main_image TEXT")
            cursor.execute("UPDATE gallery_items SET main_image = image_url WHERE image_url IS NOT NULL")
            print("✓ Added main_image column")
        
        if 'updated_at' not in columns:
            cursor.execute("ALTER TABLE gallery_items ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
            print("✓ Added updated_at column")
        
        # Create gallery_media table
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
        print("✓ gallery_media table ready")
        
        # Step 2: Update categories
        print("\nStep 2: Updating categories...")
        
        category_mapping = {
            'self_defense': 'self_defense_programs',
            'media': 'training_videos',
            'photos': 'community_programs',
            'videos': 'training_videos',
            'events': 'news_events',
            'achievements': 'news_events',
            'General': 'community_programs',
            'Events': 'news_events',
            'Training': 'self_defense_programs',
            'Awareness': 'community_programs',
            'Success Stories': 'news_events'
        }
        
        for old_category, new_category in category_mapping.items():
            cursor.execute("UPDATE gallery_items SET category = ? WHERE category = ?", (new_category, old_category))
        
        print("✓ Categories updated to new format")
        
        # Step 3: Add upcoming events
        print("\nStep 3: Adding upcoming events...")
        
        cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'upcoming_events'")
        existing_upcoming = cursor.fetchone()[0]
        
        if existing_upcoming == 0:
            upcoming_events = [
                ('Women Safety Awareness Week 2025', 'Annual comprehensive women safety awareness week featuring workshops, training sessions, self-defense programs, and community outreach activities.', '/static/images/slide1.jpg', '2025-10-15', 1),
                ('Monthly Self Defense Workshop', 'Regular monthly self-defense workshop covering basic techniques, situational awareness, and emergency response strategies for all age groups.', '/static/images/slide2.jpg', '2025-09-15', 1),
                ('Digital Safety Seminar', 'Educational seminar on digital safety, cyber security, online privacy protection, and prevention of digital harassment.', '/static/images/slide3.jpg', '2025-09-25', 0),
                ('Community Safety Drive', 'Community-wide safety awareness drive focusing on neighborhood watch programs, emergency preparedness, and safety protocols.', '/static/images/slide4.jpg', '2025-10-05', 0),
                ('International Women\'s Day Celebration', 'Special celebration honoring women\'s achievements, featuring inspiring speakers, cultural programs, and recognition ceremonies.', '/static/images/slide5.jpg', '2026-03-08', 1)
            ]
            
            for event in upcoming_events:
                cursor.execute('''
                    INSERT INTO gallery_items (title, description, main_image, event_date, category, is_featured, is_active)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', event + ('upcoming_events', 1))
            
            print(f"✓ Added {len(upcoming_events)} upcoming events")
        else:
            print(f"✓ {existing_upcoming} upcoming events already exist")
        
        # Step 4: Ensure all required categories have content
        print("\nStep 4: Ensuring all categories have content...")
        
        required_categories = ['self_defense_programs', 'training_videos', 'community_programs', 'news_events', 'upcoming_events']
        cursor.execute("SELECT DISTINCT category FROM gallery_items WHERE is_active = 1")
        existing_categories = [row[0] for row in cursor.fetchall()]
        
        for category in required_categories:
            if category not in existing_categories:
                if category == 'self_defense_programs':
                    title = 'Basic Self Defense Training'
                    description = 'Comprehensive self-defense training program covering basic techniques and situational awareness.'
                elif category == 'training_videos':
                    title = 'Self Defense Tutorial Videos'
                    description = 'Step-by-step video tutorials demonstrating various self-defense techniques and safety procedures.'
                elif category == 'community_programs':
                    title = 'Community Safety Outreach'
                    description = 'Reaching out to communities across Andhra Pradesh to spread safety awareness and support.'
                elif category == 'news_events':
                    title = 'Latest Safety News'
                    description = 'Latest news, updates, and developments in women safety initiatives and training programs.'
                else:  # upcoming_events
                    title = 'Safety Awareness Workshop'
                    description = 'Upcoming safety awareness workshop covering essential topics for women\'s safety and empowerment.'
                
                cursor.execute("""
                    INSERT INTO gallery_items 
                    (title, description, main_image, event_date, category, is_featured, is_active)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (title, description, '/static/images/slide1.jpg', '2025-09-15', category, 1, 1))
                
                print(f"✓ Added sample content for {category}")
        
        conn.commit()
        
        # Step 5: Verify the setup
        print("\nStep 5: Verifying setup...")
        
        cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE is_active = 1")
        total_items = cursor.fetchone()[0]
        
        cursor.execute("SELECT category, COUNT(*) FROM gallery_items WHERE is_active = 1 GROUP BY category")
        category_counts = cursor.fetchall()
        
        cursor.execute("SELECT COUNT(*) FROM gallery_media WHERE is_active = 1")
        total_media = cursor.fetchone()[0]
        
        conn.close()
        
        print(f"✓ Total Gallery Items: {total_items}")
        print(f"✓ Total Media Files: {total_media}")
        print("✓ Category Distribution:")
        
        for category, count in category_counts:
            print(f"   • {category.replace('_', ' ').title()}: {count} items")
        
        print("\n" + "=" * 50)
        print("GALLERY SYSTEM UPDATE COMPLETED SUCCESSFULLY!")
        print("✅ 5 sections now available:")
        print("   • Self Defence Programs")
        print("   • Training Videos")
        print("   • Community Programs") 
        print("   • News and Events")
        print("   • Upcoming Events")
        print("")
        print("✅ Admin Dashboard Features:")
        print("   • Updated category filters")
        print("   • Multiple image/video upload")
        print("   • Category-based management")
        print("   • Edit upcoming events")
        print("")
        print("✅ Main Website Features:")
        print("   • 5 distinct sections")
        print("   • Dynamic content from database")
        print("   • Admin edits reflect immediately")
        print("   • All existing data preserved")
        
        return True
        
    except Exception as e:
        print(f"❌ Update failed: {e}")
        return False

if __name__ == "__main__":
    complete_gallery_update()
