from db_config import get_db_connection, adapt_query

def test_status_check():
    """Test volunteer status check query"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Test with Registration ID
    identifier = 'VOL-2025-0001'
    print(f"Testing with identifier: {identifier}")
    
    try:
        if identifier.startswith('VOL-'):
            full_query = adapt_query("""
                SELECT 
                    v.id, v.registration_id, v.name, v.email, v.phone, 
                    v.age, v.address, v.occupation, v.education, 
                    v.experience, v.motivation, v.availability, v.skills,
                    v.created_at, COALESCE(vs.status, 'pending') as status,
                    COALESCE(vs.updated_at, v.created_at) as updated_at,
                    vs.admin_notes
                FROM volunteers v 
                LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id 
                WHERE v.registration_id = ?
            """)
        else:
            full_query = adapt_query("""
                SELECT 
                    v.id, v.registration_id, v.name, v.email, v.phone, 
                    v.age, v.address, v.occupation, v.education, 
                    v.experience, v.motivation, v.availability, v.skills,
                    v.created_at, COALESCE(vs.status, 'pending') as status,
                    COALESCE(vs.updated_at, v.created_at) as updated_at,
                    vs.admin_notes
                FROM volunteers v 
                LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id 
                WHERE v.phone = ?
            """)
        
        print(f"\nQuery: {full_query}\n")
        cursor.execute(full_query, (identifier,))
        
        result = cursor.fetchone()
        if result:
            print(f"✅ Found volunteer!")
            print(f"ID: {result[0]}")
            print(f"Registration ID: {result[1]}")
            print(f"Name: {result[2]}")
            print(f"Email: {result[3]}")
            print(f"Phone: {result[4]}")
            print(f"Status: {result[14]}")
            print(f"Admin Notes: {result[16] if len(result) > 16 and result[16] else 'None'}")
        else:
            print("❌ No volunteer found")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

if __name__ == '__main__':
    test_status_check()
