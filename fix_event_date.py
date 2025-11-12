from db_config import get_db_connection

def fix_event_date():
    """Fix wrong date in event ID 81"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Check current date
    cursor.execute("SELECT event_date FROM gallery_items WHERE id = 81")
    old_date = cursor.fetchone()[0]
    print(f"Current date: {old_date}")
    
    # Fix the date - remove extra "1" prefix
    cursor.execute("""
        UPDATE gallery_items 
        SET event_date = '2026-02-10'
        WHERE id = 81
    """)
    
    conn.commit()
    
    # Verify
    cursor.execute("SELECT event_date FROM gallery_items WHERE id = 81")
    new_date = cursor.fetchone()[0]
    print(f"Updated date: {new_date}")
    
    conn.close()
    print("\nDate fixed successfully!")

if __name__ == '__main__':
    fix_event_date()
