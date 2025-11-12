from db_config import get_db_connection

def check_officers():
    """Check officers table for NULL IDs or data issues"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Check for NULL IDs
    cursor.execute("SELECT COUNT(*) FROM officers WHERE id IS NULL")
    null_count = cursor.fetchone()[0]
    print(f"Records with NULL id: {null_count}")
    
    # Get all officers
    cursor.execute('SELECT id, name, designation, phone, email, image_url, is_active FROM officers ORDER BY id')
    officers = cursor.fetchall()
    
    print(f"\nTotal officers: {len(officers)}\n")
    
    for officer in officers:
        print(f"ID: {officer[0]} (Type: {type(officer[0])})")
        print(f"Name: {officer[1]}")
        print(f"Designation: {officer[2]}")
        print(f"Phone: {officer[3]}")
        print(f"Email: {officer[4]}")
        print(f"Image URL: {officer[5]}")
        print(f"Active: {officer[6]}")
        print("-" * 70)
    
    conn.close()

if __name__ == '__main__':
    check_officers()
