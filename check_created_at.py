from db_config import get_db_connection

def check_created_at():
    """Check created_at for all volunteers"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, name, registration_id, created_at
        FROM volunteers
        ORDER BY id
    ''')
    volunteers = cursor.fetchall()
    
    print("Volunteers created_at data:")
    for v in volunteers:
        print(f"  ID: {v[0]} - {v[1]} - {v[2]}")
        print(f"    Created At: {v[3]} (Type: {type(v[3])})")
        print()
    
    conn.close()

if __name__ == '__main__':
    check_created_at()
