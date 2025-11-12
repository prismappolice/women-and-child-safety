from db_config import get_db_connection

def check_volunteer_scores():
    """Check volunteer_scores table after accept"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT v.id, v.name, v.registration_id, vs.status, vs.admin_notes
        FROM volunteers v
        LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
        ORDER BY v.id
    ''')
    volunteers = cursor.fetchall()
    
    print("Volunteers with status:")
    for v in volunteers:
        print(f"  ID: {v[0]} - {v[1]} - {v[2]}")
        print(f"    Status: {v[3] if v[3] else 'No status (pending)'}")
        print(f"    Notes: {v[4] if v[4] else 'No notes'}")
        print()
    
    conn.close()

if __name__ == '__main__':
    check_volunteer_scores()
