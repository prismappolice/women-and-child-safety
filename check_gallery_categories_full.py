from db_config import get_db_connection

def check_all_categories():
    """Check all categories in gallery_items"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT DISTINCT category, COUNT(*) as count
        FROM gallery_items
        GROUP BY category
        ORDER BY category
    """)
    categories = cursor.fetchall()
    
    print(f"Gallery categories:\n")
    for cat, count in categories:
        print(f"{cat}: {count} items")
    
    print("\n" + "="*70 + "\n")
    
    # Check for date-related columns
    cursor.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'gallery_items'
        ORDER BY ordinal_position
    """)
    columns = cursor.fetchall()
    
    print("Gallery_items columns:")
    for col, dtype in columns:
        print(f"  {col}: {dtype}")
    
    conn.close()

if __name__ == '__main__':
    check_all_categories()
