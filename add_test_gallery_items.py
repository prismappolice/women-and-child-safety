import sqlite3

def add_test_gallery_item():
    """Add a test gallery item to verify the system is working"""
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    try:
        # Add a test image to Images category
        cursor.execute('''
            INSERT INTO gallery_items (title, description, image_url, video_url, category, event_date, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            'Test Image Upload',
            'This is a test image to verify gallery functionality is working correctly.',
            '/static/images/ap_police_logo.png',  # Using existing image
            None,
            'Images',
            '2024-12-20',
            1,  # is_featured
            1   # is_active
        ))
        
        # Add a test video to Videos category
        cursor.execute('''
            INSERT INTO gallery_items (title, description, image_url, video_url, category, event_date, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            'Test Video Upload',
            'This is a test video to verify video section functionality.',
            '/static/images/ap_police_logo.png',  # Thumbnail
            'https://www.youtube.com/watch?v=test',
            'Videos',
            '2024-12-20',
            1,  # is_featured
            1   # is_active
        ))
        
        # Add a test event to Upcoming Events category
        cursor.execute('''
            INSERT INTO gallery_items (title, description, image_url, video_url, category, event_date, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            'Test Upcoming Event',
            'This is a test event to verify upcoming events section functionality.',
            '/static/images/shakthi_logo.png',  # Using existing image
            None,
            'Upcoming Events',
            '2025-01-15',
            1,  # is_featured
            1   # is_active
        ))
        
        conn.commit()
        print("✓ Test gallery items added successfully!")
        
        # Verify the items were added
        cursor.execute('SELECT id, title, category, is_active FROM gallery_items ORDER BY id DESC LIMIT 3')
        items = cursor.fetchall()
        
        print("\nAdded items:")
        for item in items:
            print(f"- ID: {item[0]}, Title: {item[1]}, Category: {item[2]}, Active: {item[3]}")
            
    except Exception as e:
        print(f"Error adding test items: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    add_test_gallery_item()
