import sqlite3

def check_gallery_categories():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Check if gallery_items table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_items'")
    table_exists = cursor.fetchone()
    
    if table_exists:
        print("Gallery Items Table exists")
        
        # Get all categories
        cursor.execute('SELECT DISTINCT category FROM gallery_items WHERE category IS NOT NULL')
        categories = cursor.fetchall()
        
        print(f"\nCurrent categories in database:")
        if categories:
            for cat in categories:
                print(f"- {cat[0]}")
        else:
            print("No categories found")
            
        # Get count of items in each category
        cursor.execute('SELECT category, COUNT(*) FROM gallery_items GROUP BY category')
        category_counts = cursor.fetchall()
        
        print(f"\nItems count by category:")
        for cat, count in category_counts:
            print(f"- {cat}: {count} items")
            
        # Show all items
        cursor.execute('SELECT id, title, category FROM gallery_items ORDER BY category')
        all_items = cursor.fetchall()
        
        print(f"\nAll gallery items:")
        for item_id, title, category in all_items:
            print(f"- ID {item_id}: {title} ({category})")
    else:
        print("Gallery Items Table does not exist")
    
    conn.close()

if __name__ == "__main__":
    check_gallery_categories()
