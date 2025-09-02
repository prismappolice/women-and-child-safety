import sqlite3

def check_gallery_items():
    """Check gallery items in database"""
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    try:
        # Check if gallery_items table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_items'")
        table_exists = cursor.fetchone()
        
        if table_exists:
            print("✓ Gallery Items Table exists")
            
            # Get all gallery items
            cursor.execute('SELECT id, title, category, image_url, video_url, is_active FROM gallery_items ORDER BY id DESC')
            all_items = cursor.fetchall()
            
            print(f"\nTotal gallery items in database: {len(all_items)}")
            
            if all_items:
                print("\nGallery Items:")
                for item in all_items:
                    print(f"- ID: {item[0]}, Title: {item[1]}, Category: {item[2]}, Image: {item[3][:50] if item[3] else 'None'}..., Active: {item[5]}")
                
                # Count by category
                cursor.execute('SELECT category, COUNT(*) FROM gallery_items GROUP BY category')
                category_counts = cursor.fetchall()
                
                print(f"\nItems by category:")
                for cat, count in category_counts:
                    print(f"- {cat}: {count} items")
                    
                # Check active items
                cursor.execute('SELECT category, COUNT(*) FROM gallery_items WHERE is_active = 1 GROUP BY category')
                active_counts = cursor.fetchall()
                
                print(f"\nActive items by category:")
                for cat, count in active_counts:
                    print(f"- {cat}: {count} items")
            else:
                print("No gallery items found in database")
                
        else:
            print("❌ Gallery Items Table does not exist")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    check_gallery_items()
