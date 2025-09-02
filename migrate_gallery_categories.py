import sqlite3

def migrate_gallery_categories():
    """
    Migrate existing gallery categories to the new 3-category system:
    - Images, Videos, Upcoming Events
    """
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    try:
        # Check current categories
        cursor.execute('SELECT DISTINCT category FROM gallery_items WHERE category IS NOT NULL')
        existing_categories = [row[0] for row in cursor.fetchall()]
        
        print("Current categories:", existing_categories)
        
        # Category mapping - map old categories to new ones
        category_mapping = {
            'General': 'Images',
            'Events': 'Upcoming Events', 
            'Training': 'Images',
            'Awareness': 'Images',
            'Success Stories': 'Images',
            'Legal Awareness Campaign': 'Images',
            'Legal Awareness': 'Images',
            'Campaigns': 'Images',
            'Campaign': 'Images',
            'photos': 'Images',
            'videos': 'Videos',
            'image': 'Images',
            'video': 'Videos',
            'event': 'Upcoming Events',
            'upcoming': 'Upcoming Events'
        }
        
        # Update categories
        for old_category in existing_categories:
            if old_category in category_mapping:
                new_category = category_mapping[old_category]
                cursor.execute('UPDATE gallery_items SET category = ? WHERE category = ?', 
                             (new_category, old_category))
                print(f"Updated '{old_category}' -> '{new_category}'")
            elif old_category not in ['Images', 'Videos', 'Upcoming Events']:
                # Any category not in our mapping gets moved to Images by default
                cursor.execute('UPDATE gallery_items SET category = ? WHERE category = ?', 
                             ('Images', old_category))
                print(f"Updated '{old_category}' -> 'Images' (default)")
        
        conn.commit()
        
        # Verify the migration
        cursor.execute('SELECT DISTINCT category FROM gallery_items WHERE category IS NOT NULL')
        final_categories = [row[0] for row in cursor.fetchall()]
        
        print("\nFinal categories:", final_categories)
        
        # Show count per category
        cursor.execute('SELECT category, COUNT(*) FROM gallery_items GROUP BY category')
        category_counts = cursor.fetchall()
        
        print("\nItems per category:")
        for cat, count in category_counts:
            print(f"- {cat}: {count} items")
            
        print("\nMigration completed successfully!")
        
    except Exception as e:
        print(f"Error during migration: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_gallery_categories()
