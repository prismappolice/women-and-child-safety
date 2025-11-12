from db_config import get_db_connection, adapt_query

def fix_vol_0004_id():
    """Fix NULL ID for VOL-2025-0004"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    try:
        # Check for NULL ID volunteers
        cursor.execute("SELECT COUNT(*) FROM volunteers WHERE id IS NULL")
        null_count = cursor.fetchone()[0]
        print(f"Found {null_count} volunteers with NULL ID")
        
        if null_count > 0:
            # Get max ID
            cursor.execute("SELECT COALESCE(MAX(id), 0) FROM volunteers WHERE id IS NOT NULL")
            max_id = cursor.fetchone()[0]
            next_id = max_id + 1
            print(f"Next ID will be: {next_id}")
            
            # Update NULL IDs
            query = adapt_query("UPDATE volunteers SET id = ? WHERE id IS NULL AND registration_id = 'VOL-2025-0004'")
            cursor.execute(query, (next_id,))
            
            print(f"✅ Updated VOL-2025-0004 with ID {next_id}")
            
            # Check if sequence exists
            cursor.execute("SELECT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'volunteers_id_seq')")
            seq_exists = cursor.fetchone()[0]
            
            if seq_exists:
                cursor.execute(f"ALTER SEQUENCE volunteers_id_seq RESTART WITH {next_id + 1}")
                print(f"✅ Updated sequence to start at {next_id + 1}")
            else:
                cursor.execute(f"CREATE SEQUENCE volunteers_id_seq START WITH {next_id + 1}")
                cursor.execute("ALTER TABLE volunteers ALTER COLUMN id SET DEFAULT nextval('volunteers_id_seq')")
                cursor.execute("ALTER SEQUENCE volunteers_id_seq OWNED BY volunteers.id")
                print(f"✅ Created sequence starting at {next_id + 1}")
            
            conn.commit()
            
            # Verify
            cursor.execute("SELECT id, name, registration_id FROM volunteers ORDER BY id")
            all_vols = cursor.fetchall()
            print("\nAll volunteers after fix:")
            for v in all_vols:
                print(f"  ID: {v[0]} - {v[1]} - {v[2]}")
        else:
            print("✅ No NULL IDs found")
            
    except Exception as e:
        conn.rollback()
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

if __name__ == '__main__':
    fix_vol_0004_id()
