from db_config import get_db_connection

def check_and_fix_all_null_ids():
    """Check and fix ALL NULL IDs in all tables"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    tables = [
        'volunteers', 'gallery_items', 'pdf_resources', 'safety_tips',
        'initiatives', 'officers', 'success_stories', 'contact_info',
        'events', 'home_content'
    ]
    
    print("Checking and fixing NULL IDs in all tables...\n")
    
    total_fixed = 0
    
    for table in tables:
        try:
            # Check for NULL IDs
            cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE id IS NULL")
            null_count = cursor.fetchone()[0]
            
            if null_count > 0:
                print(f"⚠ {table}: Found {null_count} NULL IDs")
                
                # Get max ID
                cursor.execute(f"SELECT MAX(id) FROM {table} WHERE id IS NOT NULL")
                result = cursor.fetchone()
                max_id = result[0] if result and result[0] else 0
                
                # Get all NULL ID records
                cursor.execute(f"SELECT ctid FROM {table} WHERE id IS NULL")
                null_records = cursor.fetchall()
                
                for i, record in enumerate(null_records):
                    new_id = max_id + i + 1
                    cursor.execute(f"""
                        UPDATE {table} 
                        SET id = %s 
                        WHERE ctid = %s
                    """, (new_id, record[0]))
                    print(f"  Fixed record with new ID: {new_id}")
                
                conn.commit()
                total_fixed += null_count
                print(f"✓ {table}: Fixed {null_count} records\n")
            else:
                print(f"✓ {table}: No NULL IDs\n")
                
        except Exception as e:
            conn.rollback()
            print(f"✗ {table}: {e}\n")
    
    conn.close()
    
    print("="*70)
    if total_fixed > 0:
        print(f"Fixed {total_fixed} NULL IDs across all tables!")
    else:
        print("No NULL IDs found - all tables are clean!")
    print("="*70)

if __name__ == '__main__':
    check_and_fix_all_null_ids()
