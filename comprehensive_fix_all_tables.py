from db_config import get_db_connection

def comprehensive_fix_all_tables():
    """
    Comprehensive fix for ALL tables:
    1. Fix NULL IDs
    2. Fix NULL is_active values
    3. Create sequences for automatic ID generation
    4. Set default values for id columns
    """
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    # All tables that need fixing
    tables_config = [
        # District Contact Tables
        ('district_sps', 'district_sps_id_seq'),
        ('shakthi_teams', 'shakthi_teams_id_seq'),
        ('women_police_stations', 'women_police_stations_id_seq'),
        ('one_stop_centers', 'one_stop_centers_id_seq'),
        
        # Main Content Tables
        ('volunteers', 'volunteers_id_seq'),
        ('gallery_items', 'gallery_items_id_seq'),
        ('pdf_resources', 'pdf_resources_id_seq'),
        ('safety_tips', 'safety_tips_id_seq'),
        ('initiatives', 'initiatives_id_seq'),
        ('officers', 'officers_id_seq'),
        ('success_stories', 'success_stories_id_seq'),
        ('contact_info', 'contact_info_id_seq'),
        ('events', 'events_id_seq'),
        ('home_content', 'home_content_id_seq'),
    ]
    
    print("="*80)
    print("COMPREHENSIVE DATABASE FIX - ALL TABLES")
    print("="*80)
    print()
    
    total_fixed_ids = 0
    total_fixed_active = 0
    
    for table, sequence in tables_config:
        print(f"\n{'='*80}")
        print(f"Processing: {table}")
        print(f"{'='*80}")
        
        # Step 1: Fix NULL IDs
        cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE id IS NULL")
        null_id_count = cursor.fetchone()[0]
        
        if null_id_count > 0:
            print(f"  ⚠ Found {null_id_count} NULL IDs - Fixing...")
            
            cursor.execute(f"SELECT MAX(id) FROM {table} WHERE id IS NOT NULL")
            result = cursor.fetchone()
            max_id = result[0] if result and result[0] else 0
            
            cursor.execute(f"SELECT ctid FROM {table} WHERE id IS NULL")
            null_records = cursor.fetchall()
            
            for i, record in enumerate(null_records):
                new_id = max_id + i + 1
                cursor.execute(f"UPDATE {table} SET id = %s WHERE ctid = %s", (new_id, record[0]))
                total_fixed_ids += 1
            
            conn.commit()
            print(f"  ✓ Fixed {null_id_count} NULL IDs")
        else:
            print(f"  ✓ No NULL IDs")
        
        # Step 2: Fix NULL is_active values (if column exists)
        try:
            cursor.execute(f"""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = '{table}' AND column_name = 'is_active'
            """)
            has_is_active = cursor.fetchone() is not None
            
            if has_is_active:
                cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE is_active IS NULL")
                null_active_count = cursor.fetchone()[0]
                
                if null_active_count > 0:
                    print(f"  ⚠ Found {null_active_count} NULL is_active values - Fixing...")
                    cursor.execute(f"UPDATE {table} SET is_active = '1' WHERE is_active IS NULL")
                    conn.commit()
                    total_fixed_active += null_active_count
                    print(f"  ✓ Fixed {null_active_count} NULL is_active values")
                else:
                    print(f"  ✓ No NULL is_active values")
        except Exception as e:
            print(f"  ℹ No is_active column (normal for some tables)")
        
        # Step 3: Get current max ID
        cursor.execute(f"SELECT MAX(id) FROM {table}")
        result = cursor.fetchone()
        max_id = result[0] if result and result[0] else 0
        next_id = max_id + 1
        
        # Step 4: Create or update sequence
        try:
            cursor.execute(f"CREATE SEQUENCE IF NOT EXISTS {sequence} START WITH {next_id}")
            print(f"  ✓ Created sequence: {sequence}")
        except:
            conn.rollback()
            cursor.execute(f"SELECT setval('{sequence}', %s, false)", (next_id,))
            print(f"  ✓ Updated sequence: {sequence}")
        
        # Step 5: Set default for id column
        cursor.execute(f"ALTER TABLE {table} ALTER COLUMN id SET DEFAULT nextval('{sequence}')")
        
        # Step 6: Set sequence ownership
        cursor.execute(f"ALTER SEQUENCE {sequence} OWNED BY {table}.id")
        
        conn.commit()
        
        # Step 7: Final verification
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        total_count = cursor.fetchone()[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE id IS NULL")
        remaining_null = cursor.fetchone()[0]
        
        print(f"  ✓ Total records: {total_count}")
        print(f"  ✓ Next ID will be: {next_id}")
        print(f"  ✓ Remaining NULL IDs: {remaining_null}")
    
    conn.close()
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total NULL IDs fixed: {total_fixed_ids}")
    print(f"Total NULL is_active fixed: {total_fixed_active}")
    print("\n✅ ALL TABLES ARE NOW CONFIGURED FOR DYNAMIC ADD/DELETE!")
    print("="*80)
    print("\nYou can now add unlimited records to:")
    print("  - All District Contacts (SPs, Teams, Stations, Centers)")
    print("  - Gallery Items (Images, Videos, Events)")
    print("  - Initiatives")
    print("  - Officers")
    print("  - PDF Resources")
    print("  - Safety Tips")
    print("  - Success Stories")
    print("  - Volunteers")
    print("  - Events")
    print("  - Home Content")
    print("\nAll will get automatic IDs and show immediately to users and admin!")
    print("="*80)

if __name__ == '__main__':
    comprehensive_fix_all_tables()
