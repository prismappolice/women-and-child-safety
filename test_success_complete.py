#!/usr/bin/env python3
"""
Quick test to verify success stories functionality
"""
import sqlite3
import os

def test_success_stories():
    print("=== SUCCESS STORIES TEST ===")
    
    # Test database connection
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Get all success stories
        cursor.execute('SELECT id, title, description, image_url, is_active FROM success_stories ORDER BY id')
        stories = cursor.fetchall()
        
        print(f"Found {len(stories)} success stories:")
        for story in stories:
            print(f"  ID: {story[0]}")
            print(f"  Title: {story[1]}")
            print(f"  Description: {story[2][:50]}...")
            print(f"  Image: {story[3]}")
            print(f"  Active: {story[4]}")
            print()
        
        conn.close()
        
        # Check uploaded images
        uploads_dir = "static/uploads"
        if os.path.exists(uploads_dir):
            success_images = [f for f in os.listdir(uploads_dir) if f.startswith('success_story')]
            print(f"Success story images in uploads: {len(success_images)}")
            for img in success_images:
                print(f"  {img}")
        else:
            print("Uploads directory not found")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_success_stories()
