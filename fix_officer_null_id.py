from db_config import get_db_connection

def fix_officer_null_id():
    """Fix NULL ID in officers table"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Find the NULL ID record
    cursor.execute("SELECT name, designation FROM officers WHERE id IS NULL")
    null_record = cursor.fetchone()
    
    if null_record:
        print(f"Found NULL ID record: {null_record[0]}")
        
        # Get the max ID
        cursor.execute("SELECT MAX(id) FROM officers WHERE id IS NOT NULL")
        max_id = cursor.fetchone()[0]
        next_id = max_id + 1 if max_id else 1
        
        print(f"Max ID: {max_id}, will assign ID: {next_id}")
        
        # Update the NULL ID record
        cursor.execute("""
            UPDATE officers 
            SET id = %s, is_active = COALESCE(is_active::integer, 1)
            WHERE id IS NULL
        """, (next_id,))
        
        conn.commit()
        
        # Verify
        cursor.execute("SELECT id, name FROM officers WHERE id = %s", (next_id,))
        fixed_record = cursor.fetchone()
        print(f"\nFixed! ID: {fixed_record[0]}, Name: {fixed_record[1]}")
        
        # Check if any NULL IDs remain
        cursor.execute("SELECT COUNT(*) FROM officers WHERE id IS NULL")
        remaining_nulls = cursor.fetchone()[0]
        print(f"\nRemaining NULL IDs: {remaining_nulls}")
        
    else:
        print("No NULL IDs found!")
    
    conn.close()

if __name__ == '__main__':
    fix_officer_null_id()
