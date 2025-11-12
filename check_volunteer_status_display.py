from db_config import get_db_connection

def check_volunteer_status():
    """Check volunteer status from volunteer_scores table"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    try:
        # Get volunteers with their scores and status
        cursor.execute('''
            SELECT v.id, v.name, v.email, vs.status, vs.admin_notes, vs.total_score
            FROM volunteers v
            LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
            ORDER BY v.id
        ''')
        volunteers = cursor.fetchall()
        
        print(f"Total volunteers: {len(volunteers)}\n")
        
        for vol in volunteers:
            vol_id = vol[0] if vol[0] else 0
            print(f"ID: VOL-2025-{vol_id:04d}")
            print(f"Name: {vol[1] if vol[1] else 'N/A'}")
            print(f"Email: {vol[2] if vol[2] else 'N/A'}")
            print(f"Status: {vol[3] if vol[3] else 'No status (pending)'}")
            print(f"Score: {vol[5] if vol[5] else 'Not scored'}")
            print(f"Notes: {vol[4] if vol[4] else 'No notes'}")
            print("-" * 50)
        
        # Check if volunteer_scores table exists and has data
        cursor.execute("SELECT COUNT(*) FROM volunteer_scores")
        score_count = cursor.fetchone()[0]
        print(f"\nTotal records in volunteer_scores: {score_count}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    check_volunteer_status()
