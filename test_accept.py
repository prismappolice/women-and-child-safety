from db_config import get_db_connection, adapt_query

def test_accept_workflow():
    """Test accept volunteer workflow"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    volunteer_id = 4  # VOL-2025-0004
    
    try:
        print(f"Testing Accept workflow for volunteer {volunteer_id}")
        
        # Simulate what admin_approve_volunteer does
        query = adapt_query('''
            UPDATE volunteer_scores 
            SET status = ?
            WHERE volunteer_id = ?
        ''')
        cursor.execute(query, ('approved', volunteer_id))
        
        if cursor.rowcount == 0:
            print("No existing record, inserting new one...")
            query = adapt_query('''
                INSERT INTO volunteer_scores (volunteer_id, status, admin_notes)
                VALUES (?, ?, ?)
            ''')
            cursor.execute(query, (volunteer_id, 'approved', 'Application approved by admin'))
        else:
            print(f"✅ Updated {cursor.rowcount} record(s)")
        
        conn.commit()
        
        # Verify
        query = adapt_query('''
            SELECT v.id, v.name, v.registration_id, vs.status
            FROM volunteers v
            LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
            WHERE v.id = ?
        ''')
        cursor.execute(query, (volunteer_id,))
        
        result = cursor.fetchone()
        print(f"\nVerification:")
        print(f"  ID: {result[0]}")
        print(f"  Name: {result[1]}")
        print(f"  Reg ID: {result[2]}")
        print(f"  Status: {result[3]}")
        
        if result[3] == 'approved':
            print("\n✅ Accept workflow working correctly!")
        else:
            print(f"\n❌ Expected 'approved' but got '{result[3]}'")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

if __name__ == '__main__':
    test_accept_workflow()
