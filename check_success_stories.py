import sqlite3
import os

def check_success_stories():
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Check table structure
        cursor.execute("PRAGMA table_info(success_stories)")
        columns = cursor.fetchall()
        print("Success Stories Table Structure:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        print()
        
        # Check current data
        cursor.execute("SELECT * FROM success_stories ORDER BY sort_order")
        stories = cursor.fetchall()
        
        print(f"Found {len(stories)} success stories:")
        for story in stories:
            print(f"ID: {story[0]}")
            print(f"Title: {story[1]}")
            print(f"Description: {story[2][:100]}...")
            print(f"Image URL: {story[5] if len(story) > 5 else 'No image'}")
            print(f"Active: {story[7] if len(story) > 7 else 'Unknown'}")
            print("-" * 50)
        
        conn.close()
        
        # Check uploaded images
        uploads_dir = "static/uploads"
        if os.path.exists(uploads_dir):
            success_images = [f for f in os.listdir(uploads_dir) if f.startswith('success_story')]
            print(f"\nSuccess story images in uploads folder:")
            for img in success_images:
                print(f"  {img}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_success_stories()
