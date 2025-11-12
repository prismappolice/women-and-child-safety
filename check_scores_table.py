from db_config import get_db_connection

def check_volunteer_scores_structure():
    """Check volunteer_scores table structure"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'volunteer_scores'
            ORDER BY ordinal_position
        """)
        columns = cursor.fetchall()
        
        print("volunteer_scores table columns:")
        for col in columns:
            print(f"  - {col[0]}: {col[1]}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    check_volunteer_scores_structure()
