#!/usr/bin/env python3
"""
Auto-Migration Startup Script
This script automatically runs database migration and starts the Flask app
"""

import sqlite3
import subprocess
import sys
import os

def auto_migrate_database():
    """Automatically migrate database structure if needed"""
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Check if main_image column exists
        cursor.execute("PRAGMA table_info(gallery_items)")
        columns = [column[1] for column in cursor.fetchall()]
        
        needs_migration = False
        
        if 'main_image' not in columns:
            print("🔧 Adding main_image column...")
            cursor.execute("ALTER TABLE gallery_items ADD COLUMN main_image TEXT")
            # Copy image_url to main_image
            cursor.execute("UPDATE gallery_items SET main_image = image_url WHERE image_url IS NOT NULL")
            needs_migration = True
        
        if 'updated_at' not in columns:
            print("🔧 Adding updated_at column...")
            cursor.execute("ALTER TABLE gallery_items ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
            needs_migration = True
        
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
        
        # Update categories to new format
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
        
        # Ensure we have at least one item in each category
        required_categories = ['self_defense_programs', 'training_videos', 'community_programs', 'news_events']
        cursor.execute("SELECT DISTINCT category FROM gallery_items")
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
                else:  # news_events
                    title = 'Women Safety Week 2025'
                    description = 'Annual women safety awareness week with multiple events, workshops, and community programs.'
                
                cursor.execute("""
                    INSERT INTO gallery_items 
                    (title, description, main_image, event_date, category, is_featured, is_active)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (title, description, '/static/images/slide1.jpg', '2025-09-15', category, 1, 1))
        
        conn.commit()
        conn.close()
        
        if needs_migration:
            print("✅ Database migration completed successfully!")
        else:
            print("✅ Database structure is up to date!")
        
        return True
        
    except Exception as e:
        print(f"❌ Database migration failed: {e}")
        return False

def start_app():
    """Start the Flask application"""
    try:
        print("🚀 Starting AP Women Safety Website...")
        print("=" * 50)
        
        # Run migration first
        if auto_migrate_database():
            print("📊 Gallery system ready with 4 sections:")
            print("   • Self Defence Programs")
            print("   • Training Videos") 
            print("   • Community Programs")
            print("   • News and Events")
            print("")
            print("🌐 Website will be available at: http://127.0.0.1:5000")
            print("🔧 Admin Dashboard: http://127.0.0.1:5000/admin/gallery")
            print("   Login: admin / admin123")
            print("")
            
            # Start Flask app
            subprocess.run([sys.executable, "app.py"], check=True)
        else:
            print("❌ Cannot start app due to database migration failure")
            return False
            
    except KeyboardInterrupt:
        print("\n👋 Shutting down server...")
        return True
    except Exception as e:
        print(f"❌ Failed to start app: {e}")
        return False

if __name__ == "__main__":
    start_app()
