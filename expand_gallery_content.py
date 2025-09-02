#!/usr/bin/env python3
"""
Safely add more images and videos to gallery sections
Excluding Upcoming Events as requested
"""

import sqlite3

def add_gallery_content():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    print("🔍 Current gallery content check...")
    
    # Check current counts
    categories = ['Self Defence Programme', 'Training Videos', 'Community Programmes', 'News & Events']
    
    for category in categories:
        cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = ?", (category,))
        count = cursor.fetchone()[0]
        print(f"📊 {category}: {count} items")
    
    # Additional content for each section
    new_gallery_items = [
        # Self Defence Programme - 5 more items
        {
            'title': 'Basic Self Defence Moves - Part 1',
            'description': 'Learn fundamental defensive techniques including proper stance, blocking, and basic strikes. Essential skills for personal safety.',
            'image_url': '/static/images/slide1.jpg',
            'video_url': '',
            'event_date': '2024-12-20',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Advanced Self Defence Techniques',
            'description': 'Advanced defensive moves including escape from grabs, pressure points, and multiple attacker scenarios.',
            'image_url': '/static/images/slide2.jpg',
            'video_url': '',
            'event_date': '2024-12-18',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Self Defence with Objects',
            'description': 'Using everyday items for defense - keys, bags, mobile phones, and other common objects as defensive tools.',
            'image_url': '/static/images/slide3.jpg',
            'video_url': '',
            'event_date': '2024-12-16',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Group Self Defence Training',
            'description': 'Community-based training sessions where women learn together and practice defensive techniques in groups.',
            'image_url': '/static/images/slide4.jpg',
            'video_url': '',
            'event_date': '2024-12-14',
            'category': 'Self Defence Programme',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Self Defence Demonstration Video',
            'description': 'Complete video demonstration of all basic self-defence moves with step-by-step instructions.',
            'image_url': '/static/images/slide5.jpg',
            'video_url': '/static/videos/self_defence_demo.mp4',
            'event_date': '2024-12-12',
            'category': 'Self Defence Programme',
            'is_featured': 1,
            'is_active': 1
        },
        
        # Training Videos - 4 more items
        {
            'title': 'Safety Awareness Training Video',
            'description': 'Comprehensive safety awareness video covering personal safety tips, emergency contacts, and prevention strategies.',
            'image_url': '/static/images/slide1.jpg',
            'video_url': '/static/videos/safety_awareness.mp4',
            'event_date': '2024-12-15',
            'category': 'Training Videos',
            'is_featured': 1,
            'is_active': 1
        },
        {
            'title': 'Cyber Safety Education Video',
            'description': 'Digital safety training covering online harassment prevention, safe social media practices, and cyber crime awareness.',
            'image_url': '/static/images/slide2.jpg',
            'video_url': '/static/videos/cyber_safety.mp4',
            'event_date': '2024-12-13',
            'category': 'Training Videos',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Emergency Response Training',
            'description': 'Training video on how to respond in emergency situations, including calling for help and first aid basics.',
            'image_url': '/static/images/slide3.jpg',
            'video_url': '/static/videos/emergency_response.mp4',
            'event_date': '2024-12-11',
            'category': 'Training Videos',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Legal Awareness Training',
            'description': 'Educational video about women\'s legal rights, how to file complaints, and available legal support systems.',
            'image_url': '/static/images/slide4.jpg',
            'video_url': '/static/videos/legal_awareness.mp4',
            'event_date': '2024-12-09',
            'category': 'Training Videos',
            'is_featured': 0,
            'is_active': 1
        },
        
        # Community Programmes - 4 more items
        {
            'title': 'Village Awareness Program - District 1',
            'description': 'Rural outreach program focusing on women\'s safety awareness in remote villages and agricultural communities.',
            'image_url': '/static/images/slide1.jpg',
            'video_url': '',
            'event_date': '2024-12-08',
            'category': 'Community Programmes',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'School Safety Education Program',
            'description': 'Educational program conducted in schools to teach students about personal safety and anti-bullying measures.',
            'image_url': '/static/images/slide2.jpg',
            'video_url': '',
            'event_date': '2024-12-06',
            'category': 'Community Programmes',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Workplace Safety Initiative',
            'description': 'Corporate program addressing workplace harassment prevention and creating safe work environments for women.',
            'image_url': '/static/images/slide3.jpg',
            'video_url': '',
            'event_date': '2024-12-04',
            'category': 'Community Programmes',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Community Safety Volunteers Training',
            'description': 'Training program for community volunteers who help in spreading safety awareness and supporting local women.',
            'image_url': '/static/images/slide4.jpg',
            'video_url': '',
            'event_date': '2024-12-02',
            'category': 'Community Programmes',
            'is_featured': 0,
            'is_active': 1
        },
        
        # News & Events - 4 more items  
        {
            'title': 'State Women Safety Conference 2024',
            'description': 'Annual state-level conference discussing new policies, achievements, and future plans for women safety initiatives.',
            'image_url': '/static/images/slide1.jpg',
            'video_url': '',
            'event_date': '2024-12-07',
            'category': 'News & Events',
            'is_featured': 1,
            'is_active': 1
        },
        {
            'title': 'Safety Equipment Distribution Drive',
            'description': 'Large-scale distribution of safety equipment including emergency whistles, pepper sprays, and safety apps.',
            'image_url': '/static/images/slide2.jpg',
            'video_url': '',
            'event_date': '2024-12-05',
            'category': 'News & Events',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Awards Ceremony for Safety Champions',
            'description': 'Recognition ceremony honoring individuals and organizations contributing significantly to women safety initiatives.',
            'image_url': '/static/images/slide3.jpg',
            'video_url': '',
            'event_date': '2024-12-03',
            'category': 'News & Events',
            'is_featured': 0,
            'is_active': 1
        },
        {
            'title': 'Media Coverage - Safety Campaign Launch',
            'description': 'Media coverage of the new safety campaign launch with participation from government officials and celebrities.',
            'image_url': '/static/images/slide4.jpg',
            'video_url': '',
            'event_date': '2024-12-01',
            'category': 'News & Events',
            'is_featured': 0,
            'is_active': 1
        }
    ]
    
    print(f"\n📝 Adding {len(new_gallery_items)} new gallery items...")
    
    # Add all new items
    for item in new_gallery_items:
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
    
    print("✅ Gallery content added successfully!")
    
    # Show final counts
    print("\n📊 Updated gallery content:")
    for category in categories:
        cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = ?", (category,))
        count = cursor.fetchone()[0]
        print(f"✅ {category}: {count} items")
    
    # Check Upcoming Events (should remain unchanged)
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'Upcoming Events'")
    upcoming_count = cursor.fetchone()[0]
    print(f"📅 Upcoming Events: {upcoming_count} items (unchanged as requested)")
    
    conn.close()
    print("\n🎉 Gallery expansion completed successfully!")
    print("💡 All existing project data preserved!")

if __name__ == "__main__":
    try:
        add_gallery_content()
        print("✅ Gallery content expansion completed successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check if the database file exists and is accessible.")
