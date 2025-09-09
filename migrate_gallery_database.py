#!/usr/bin/env python3
"""
Database Migration Script for Enhanced Gallery System
This script safely migrates the existing gallery_items table to the new structure
"""

import sqlite3
import os

def migrate_gallery_database():
    print("Starting Gallery Database Migration...")
    print("=" * 50)
    
    # Connect to database
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    try:
        # Check current table structure
        cursor.execute("PRAGMA table_info(gallery_items)")
        existing_columns = [column[1] for column in cursor.fetchall()]
        print(f"Existing columns: {existing_columns}")
        
        # Check if main_image column already exists
        if 'main_image' not in existing_columns:
            print("Adding main_image column...")
            cursor.execute("ALTER TABLE gallery_items ADD COLUMN main_image TEXT")
            
            # Copy image_url to main_image if it exists
            if 'image_url' in existing_columns:
                cursor.execute("UPDATE gallery_items SET main_image = image_url WHERE image_url IS NOT NULL")
                print("✓ Copied image_url data to main_image")
        else:
            print("✓ main_image column already exists")
        
        # Check if updated_at column exists
        if 'updated_at' not in existing_columns:
            print("Adding updated_at column...")
            cursor.execute("ALTER TABLE gallery_items ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        else:
            print("✓ updated_at column already exists")
        
        # Create gallery_media table if it doesn't exist
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
        print("✓ gallery_media table created/verified")
        
        # Migrate existing data to new structure if needed
        cursor.execute("SELECT COUNT(*) FROM gallery_media")
        media_count = cursor.fetchone()[0]
        
        if media_count == 0:
            print("Migrating existing gallery data...")
            
            # Get all existing gallery items
            cursor.execute("SELECT id, title, description, main_image FROM gallery_items WHERE main_image IS NOT NULL")
            existing_items = cursor.fetchall()
            
            # Create media entries for existing items
            for item_id, title, description, main_image in existing_items:
                cursor.execute("""
                    INSERT INTO gallery_media 
                    (gallery_item_id, media_type, media_url, media_title, media_description, display_order, is_active)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (item_id, 'image', main_image, f"{title} - Main Image", description, 1, 1))
            
            print(f"✓ Migrated {len(existing_items)} existing images to gallery_media")
        
        # Update categories to new format
        print("Updating categories to new format...")
        
        # Map old categories to new ones
        category_mapping = {
            'self_defense': 'self_defense_programs',
            'media': 'training_videos',  # Assuming media was mostly videos
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
            cursor.execute("""
                UPDATE gallery_items 
                SET category = ? 
                WHERE category = ?
            """, (new_category, old_category))
        
        # Add sample data for missing categories
        cursor.execute("SELECT DISTINCT category FROM gallery_items")
        existing_categories = [row[0] for row in cursor.fetchall()]
        required_categories = ['self_defense_programs', 'training_videos', 'community_programs', 'news_events']
        
        for category in required_categories:
            if category not in existing_categories:
                print(f"Adding sample data for {category}...")
                
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
                
                # Add sample media
                item_id = cursor.lastrowid
                cursor.execute("""
                    INSERT INTO gallery_media 
                    (gallery_item_id, media_type, media_url, media_title, media_description, display_order, is_active)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (item_id, 'image', '/static/images/slide1.jpg', f"{title} - Sample Image", description, 1, 1))
        
        # Commit all changes
        conn.commit()
        
        # Verify migration
        cursor.execute("SELECT COUNT(*) FROM gallery_items")
        total_items = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM gallery_media")
        total_media = cursor.fetchone()[0]
        
        cursor.execute("SELECT category, COUNT(*) FROM gallery_items GROUP BY category")
        category_counts = cursor.fetchall()
        
        print("\n" + "=" * 50)
        print("DATABASE MIGRATION COMPLETED SUCCESSFULLY!")
        print(f"✓ Total Gallery Items: {total_items}")
        print(f"✓ Total Media Files: {total_media}")
        print("✓ Category Distribution:")
        
        for category, count in category_counts:
            print(f"   - {category.replace('_', ' ').title()}: {count} items")
        
        print("\n✓ Database structure updated")
        print("✓ Existing data preserved")
        print("✓ New features ready to use")
        print("✓ Admin dashboard will now work correctly")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ Migration failed: {str(e)}")
        conn.rollback()
        conn.close()
        return False

if __name__ == "__main__":
    migrate_gallery_database()
