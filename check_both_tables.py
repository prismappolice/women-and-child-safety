from db_config import get_db_connection

def check_all_status_tables():
    """Check all status-related tables"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Check volunteer_status table
    try:
        cursor.execute("SELECT volunteer_id, status FROM volunteer_status ORDER BY volunteer_id")
        old_status = cursor.fetchall()
        print("volunteer_status table:")
        for s in old_status:
            print(f"  Volunteer {s[0]}: {s[1]}")
    except Exception as e:
        print(f"volunteer_status table error: {e}")
    
    print()
    
    # Check volunteer_scores table
    try:
        cursor.execute("SELECT volunteer_id, status FROM volunteer_scores ORDER BY volunteer_id")
        new_status = cursor.fetchall()
        print("volunteer_scores table:")
        for s in new_status:
            print(f"  Volunteer {s[0]}: {s[1]}")
    except Exception as e:
        print(f"volunteer_scores table error: {e}")
    
    conn.close()

if __name__ == '__main__':
    check_all_status_tables()
