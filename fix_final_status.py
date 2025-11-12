from db_config import get_db_connection, adapt_query

def fix_volunteer_0004_status():
    """Set VOL-0004 status to approved"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    try:
        # Update VOL-0004 to approved with clean notes
        query = adapt_query('''
            UPDATE volunteer_scores 
            SET status = ?, admin_notes = ?
            WHERE volunteer_id = 4
        ''')
        cursor.execute(query, ('approved', 'Application approved by admin'))
        
        # Also update VOL-2 and VOL-3 back to pending with clean notes
        query = adapt_query('''
            UPDATE volunteer_scores 
            SET status = ?, admin_notes = ?
            WHERE volunteer_id IN (2, 3)
        ''')
        cursor.execute(query, ('pending', 'Application under review'))
        
        conn.commit()
        
        print("✅ Status updated:")
        
        # Verify
        cursor.execute('''
            SELECT volunteer_id, status, admin_notes
            FROM volunteer_scores
            ORDER BY volunteer_id
        ''')
        all_status = cursor.fetchall()
        
        for s in all_status:
            print(f"\n  Volunteer {s[0]}: {s[1]}")
            print(f"    Notes: {s[2][:50]}...")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    fix_volunteer_0004_status()
