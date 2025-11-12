from db_config import get_db_connection

def check_volunteers():
    """Check volunteer IDs"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, name, registration_id FROM volunteers ORDER BY id')
    volunteers = cursor.fetchall()
    
    print("Volunteers in database:")
    for v in volunteers:
        print(f"  ID: {v[0]} (type: {type(v[0])}) - Name: {v[1]} - Reg ID: {v[2]}")
    
    conn.close()

if __name__ == '__main__':
    check_volunteers()
