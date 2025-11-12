from db_config import get_db_connection

def fix_all_district_tables():
    """Fix NULL IDs and create sequences for all district-related tables"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    tables = [
        'district_sps',
        'shakthi_teams',
        'women_police_stations',
        'one_stop_centers'
    ]
    
    print("Fixing all district-related tables...\n")
    
    for table in tables:
        print(f"Processing {table}...")
        
        # Check for NULL IDs
        cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE id IS NULL")
        null_count = cursor.fetchone()[0]
        
        if null_count > 0:
            print(f"  Found {null_count} NULL IDs")
            
            # Get max ID
            cursor.execute(f"SELECT MAX(id) FROM {table} WHERE id IS NOT NULL")
            result = cursor.fetchone()
            max_id = result[0] if result and result[0] else 0
            
            # Fix NULL IDs
            cursor.execute(f"SELECT ctid FROM {table} WHERE id IS NULL")
            null_records = cursor.fetchall()
            
            for i, record in enumerate(null_records):
                new_id = max_id + i + 1
                cursor.execute(f"""
                    UPDATE {table} 
                    SET id = %s, is_active = COALESCE(is_active, '1')
                    WHERE ctid = %s
                """, (new_id, record[0]))
                print(f"    Fixed record with ID: {new_id}")
            
            conn.commit()
        else:
            print(f"  No NULL IDs")
        
        # Get current max ID after fixes
        cursor.execute(f"SELECT MAX(id) FROM {table}")
        result = cursor.fetchone()
        max_id = result[0] if result and result[0] else 0
        next_id = max_id + 1
        
        # Create or update sequence
        sequence_name = f"{table}_id_seq"
        
        try:
            cursor.execute(f"CREATE SEQUENCE {sequence_name} START WITH {next_id}")
            print(f"  Created sequence: {sequence_name}")
        except:
            conn.rollback()
            cursor.execute(f"SELECT setval('{sequence_name}', %s, false)", (next_id,))
            print(f"  Updated sequence: {sequence_name}")
        
        # Set default for id column
        cursor.execute(f"""
            ALTER TABLE {table} 
            ALTER COLUMN id SET DEFAULT nextval('{sequence_name}')
        """)
        
        # Set sequence ownership
        cursor.execute(f"ALTER SEQUENCE {sequence_name} OWNED BY {table}.id")
        
        conn.commit()
        print(f"✓ {table}: max_id={max_id}, next_id={next_id}\n")
    
    conn.close()
    
    print("="*70)
    print("All district tables fixed!")
    print("Now you can add unlimited records without NULL ID problems:")
    print("  - District SPs")
    print("  - Shakthi Teams")
    print("  - Women Police Stations")
    print("  - One Stop Centers")
    print("="*70)

if __name__ == '__main__':
    fix_all_district_tables()
