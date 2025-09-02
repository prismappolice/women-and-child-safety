import sqlite3

def add_new_gallery_item():
    """Add one more Self Defence Programme image safely"""
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Check current count for Self Defence Programme
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'Self Defence Programme'")
    current_count = cursor.fetchone()[0]
    print(f"Current Self Defence items: {current_count}")
    
    # New item data
    new_item = {
        'title': 'Women Self Defence Workshop - Advanced Techniques',
        'description': 'Advanced self-defence workshop covering escape techniques, pressure points, and situational awareness for women safety.',
        'image_url': '/static/images/slide2.jpg',  # Using existing safe image
        'video_url': '',
        'event_date': '2024-12-25',
        'category': 'Self Defence Programme',
        'is_featured': 0,
        'is_active': 1
    }
    
    # Add the new item
    cursor.execute('''
        INSERT INTO gallery_items (title, description, image_url, video_url, event_date, category, is_featured, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        new_item['title'],
        new_item['description'], 
        new_item['image_url'],
        new_item['video_url'],
        new_item['event_date'],
        new_item['category'],
        new_item['is_featured'],
        new_item['is_active']
    ))
    
    conn.commit()
    
    # Verify addition
    cursor.execute("SELECT COUNT(*) FROM gallery_items WHERE category = 'Self Defence Programme'")
    new_count = cursor.fetchone()[0]
    print(f"New Self Defence items count: {new_count}")
    print(f"✅ Added {new_count - current_count} new item")
    
    # Get the newly added item
    cursor.execute("SELECT title, description FROM gallery_items WHERE title = ?", (new_item['title'],))
    added_item = cursor.fetchone()
    if added_item:
        print(f"✅ Successfully added: {added_item[0]}")
        print(f"   Description: {added_item[1][:50]}...")
    
    conn.close()
    print("🎉 New gallery item added safely!")
    print("💡 No existing project data was affected!")

if __name__ == "__main__":
    add_new_gallery_item()
