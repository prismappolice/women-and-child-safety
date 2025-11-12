from db_config import get_db_connection

def fix_initiative_null_id():
    """Fix NULL ID in initiatives table"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # Find the NULL ID record
    cursor.execute("SELECT title, description FROM initiatives WHERE id IS NULL")
    null_record = cursor.fetchone()
    
    if null_record:
        print(f"Found NULL ID record: {null_record[0]}")
        
        # Get the max ID
        cursor.execute("SELECT MAX(id) FROM initiatives WHERE id IS NOT NULL")
        max_id = cursor.fetchone()[0]
        next_id = max_id + 1 if max_id else 1
        
        print(f"Max ID: {max_id}, will assign ID: {next_id}")
        
        # Update the NULL ID record
        cursor.execute("""
            UPDATE initiatives 
            SET id = %s, is_active = COALESCE(is_active, 1)
            WHERE id IS NULL
        """, (next_id,))
        
        conn.commit()
        
        # Verify
        cursor.execute("SELECT id, title FROM initiatives WHERE id = %s", (next_id,))
        fixed_record = cursor.fetchone()
        print(f"\nFixed! ID: {fixed_record[0]}, Title: {fixed_record[1]}")
        
        # Check if any NULL IDs remain
        cursor.execute("SELECT COUNT(*) FROM initiatives WHERE id IS NULL")
        remaining_nulls = cursor.fetchone()[0]
        print(f"\nRemaining NULL IDs: {remaining_nulls}")
        
    else:
        print("No NULL IDs found!")
    
    conn.close()

if __name__ == '__main__':
    fix_initiative_null_id()
