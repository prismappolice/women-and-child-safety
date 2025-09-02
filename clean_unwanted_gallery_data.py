import sqlite3

def clean_unwanted_gallery_data():
    """Remove any gallery items that are not in the 3 allowed categories"""
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    try:
        # Check current gallery items
        cursor.execute('SELECT id, title, category FROM gallery_items')
        all_items = cursor.fetchall()
        
        print(f"Total gallery items before cleaning: {len(all_items)}")
        
        if all_items:
            print("\nCurrent items:")
            for item in all_items:
                print(f"- ID: {item[0]}, Title: {item[1]}, Category: {item[2]}")
        
        # Define allowed categories
        allowed_categories = ['Images', 'Videos', 'Upcoming Events']
        
        # Find items with unwanted categories
        cursor.execute('SELECT id, title, category FROM gallery_items WHERE category NOT IN (?, ?, ?)', 
                      tuple(allowed_categories))
        unwanted_items = cursor.fetchall()
        
        if unwanted_items:
            print(f"\nFound {len(unwanted_items)} items with unwanted categories:")
            for item in unwanted_items:
                print(f"- ID: {item[0]}, Title: {item[1]}, Category: {item[2]}")
            
            # Ask if user wants to delete them (in this case, just remove automatically)
            print("\nRemoving unwanted category items...")
            cursor.execute('DELETE FROM gallery_items WHERE category NOT IN (?, ?, ?)', 
                          tuple(allowed_categories))
            
            print(f"✓ Removed {cursor.rowcount} items with unwanted categories")
            
        else:
            print("\n✓ No unwanted category items found")
        
        # Show final count
        cursor.execute('SELECT category, COUNT(*) FROM gallery_items GROUP BY category')
        final_counts = cursor.fetchall()
        
        print(f"\nFinal gallery items by category:")
        for cat, count in final_counts:
            print(f"- {cat}: {count} items")
        
        conn.commit()
        print("\n✓ Database cleaned successfully!")
        
    except Exception as e:
        print(f"Error cleaning database: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    clean_unwanted_gallery_data()
