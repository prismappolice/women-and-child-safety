import sqlite3

def fix_success_stories_images():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Check current stories
    cursor.execute('SELECT id, title, image_url FROM success_stories')
    stories = cursor.fetchall()
    
    print("Current Success Stories:")
    for story in stories:
        print(f"ID: {story[0]}, Title: {story[1][:40]}..., Image: {story[2]}")
    
    # Update with actual available images
    updates = [
        (1, '/static/images/slide1.jpg'),
        (2, '/static/images/slide2.jpg'), 
        (3, '/static/images/slide3.jpg')
    ]
    
    print("\nUpdating image URLs...")
    for story_id, image_url in updates:
        cursor.execute('UPDATE success_stories SET image_url = ? WHERE id = ?', (image_url, story_id))
        print(f"Updated story {story_id} with image: {image_url}")
    
    conn.commit()
    
    # Verify updates
    cursor.execute('SELECT id, title, image_url FROM success_stories')
    updated_stories = cursor.fetchall()
    
    print("\nUpdated Success Stories:")
    for story in updated_stories:
        print(f"ID: {story[0]}, Title: {story[1][:40]}..., Image: {story[2]}")
    
    conn.close()
    print("\nImage URLs updated!")

if __name__ == "__main__":
    fix_success_stories_images()
