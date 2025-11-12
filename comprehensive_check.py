from db_config import get_db_connection

def comprehensive_check():
    """Comprehensive check of volunteers data"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    print("="*70)
    print("1. CHECKING VOLUNTEERS TABLE")
    print("="*70)
    cursor.execute('''
        SELECT id, name, registration_id, email, phone, created_at
        FROM volunteers
        ORDER BY id
    ''')
    volunteers = cursor.fetchall()
    
    print(f"\nTotal volunteers: {len(volunteers)}")
    for v in volunteers:
        print(f"\n  ID: {v[0]} (NULL: {v[0] is None})")
        print(f"  Name: {v[1]}")
        print(f"  Reg ID: {v[2]}")
        print(f"  Email: {v[3]}")
        print(f"  Phone: {v[4]}")
        print(f"  Created: {v[5]} (NULL: {v[5] is None})")
    
    print("\n" + "="*70)
    print("2. CHECKING VOLUNTEER_SCORES TABLE")
    print("="*70)
    cursor.execute('''
        SELECT volunteer_id, status, admin_notes, created_at
        FROM volunteer_scores
        ORDER BY volunteer_id
    ''')
    scores = cursor.fetchall()
    
    print(f"\nTotal records: {len(scores)}")
    for s in scores:
        print(f"\n  Volunteer ID: {s[0]}")
        print(f"  Status: {s[1]}")
        print(f"  Notes: {s[2]}")
        print(f"  Created: {s[3]}")
    
    print("\n" + "="*70)
    print("3. CHECKING VOLUNTEER_STATUS TABLE (OLD)")
    print("="*70)
    try:
        cursor.execute('''
            SELECT volunteer_id, status, updated_at
            FROM volunteer_status
            ORDER BY volunteer_id
        ''')
        old_status = cursor.fetchall()
        
        print(f"\nTotal records: {len(old_status)}")
        for s in old_status:
            print(f"\n  Volunteer ID: {s[0]} (NULL: {s[0] is None})")
            print(f"  Status: {s[1]}")
            print(f"  Updated: {s[2]}")
    except Exception as e:
        print(f"  Error or table doesn't exist: {e}")
    
    print("\n" + "="*70)
    print("4. CHECKING ADMIN_VOLUNTEERS QUERY RESULT")
    print("="*70)
    cursor.execute('''
        SELECT v.id, v.name, v.email, v.phone, v.age, v.address, v.education, v.occupation, 
               v.motivation, v.skills, v.created_at,
               vs.age_score, vs.education_score, vs.motivation_score, vs.skills_score, 
               vs.total_score, vs.status, vs.admin_notes
        FROM volunteers v
        LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
        ORDER BY v.created_at DESC
    ''')
    admin_data = cursor.fetchall()
    
    print(f"\nTotal rows: {len(admin_data)}")
    for i, row in enumerate(admin_data):
        print(f"\nRow {i+1}:")
        print(f"  [0] ID: {row[0]}")
        print(f"  [1] Name: {row[1]}")
        print(f"  [10] Created: {row[10]}")
        print(f"  [16] Status: {row[16]}")
        print(f"  [17] Notes: {row[17]}")
    
    print("\n" + "="*70)
    print("5. CHECKING FOR DUPLICATE IDs")
    print("="*70)
    cursor.execute('''
        SELECT id, COUNT(*) as count
        FROM volunteers
        GROUP BY id
        HAVING COUNT(*) > 1
    ''')
    duplicates = cursor.fetchall()
    
    if duplicates:
        print("⚠️ DUPLICATES FOUND:")
        for d in duplicates:
            print(f"  ID {d[0]}: {d[1]} occurrences")
    else:
        print("✅ No duplicate IDs found")
    
    print("\n" + "="*70)
    print("6. CHECKING REGISTRATION_ID UNIQUENESS")
    print("="*70)
    cursor.execute('''
        SELECT registration_id, COUNT(*) as count
        FROM volunteers
        GROUP BY registration_id
        HAVING COUNT(*) > 1
    ''')
    dup_regs = cursor.fetchall()
    
    if dup_regs:
        print("⚠️ DUPLICATE REGISTRATION IDs:")
        for d in dup_regs:
            print(f"  {d[0]}: {d[1]} occurrences")
    else:
        print("✅ No duplicate registration IDs")
    
    conn.close()
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Total volunteers: {len(volunteers)}")
    print(f"Volunteers with NULL ID: {sum(1 for v in volunteers if v[0] is None)}")
    print(f"Volunteers with NULL created_at: {sum(1 for v in volunteers if v[5] is None)}")
    print(f"Volunteers with status in scores table: {len(scores)}")
    print("="*70)

if __name__ == '__main__':
    comprehensive_check()
