from db_config import get_db_connection

def check_initiatives():
    """Check initiatives table for NULL IDs or data issues"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Check for NULL IDs
    cursor.execute("SELECT COUNT(*) FROM initiatives WHERE id IS NULL")
    null_count = cursor.fetchone()[0]
    print(f"Records with NULL id: {null_count}")
    
    # Get all initiatives
    cursor.execute('SELECT id, title, description, image_url, is_featured, is_active FROM initiatives ORDER BY id')
    initiatives = cursor.fetchall()
    
    print(f"\nTotal initiatives: {len(initiatives)}\n")
    
    for init in initiatives:
        print(f"ID: {init[0]} (Type: {type(init[0])})")
        print(f"Title: {init[1]}")
        print(f"Description: {init[2][:50] if init[2] else 'None'}...")
        print(f"Image URL: {init[3]}")
        print(f"Featured: {init[4]}")
        print(f"Active: {init[5]}")
        print("-" * 70)
    
    conn.close()

if __name__ == '__main__':
    check_initiatives()
