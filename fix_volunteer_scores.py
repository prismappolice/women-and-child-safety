#!/usr/bin/env python3

from db_config import get_db_connection

def fix_volunteer_scores_table():
    """Fix volunteer_scores table to have proper SERIAL ID"""
    
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    print("=== FIXING VOLUNTEER_SCORES TABLE STRUCTURE ===")
    
    try:
        # Check if sequence exists
        cursor.execute("SELECT pg_get_serial_sequence('volunteer_scores', 'id')")
        sequence = cursor.fetchone()[0]
        
        if not sequence:
            print("Adding SERIAL ID to volunteer_scores table...")
            
            # Create sequence
            cursor.execute("CREATE SEQUENCE IF NOT EXISTS volunteer_scores_id_seq")
            
            # First fix NULL IDs
            cursor.execute("""
                UPDATE volunteer_scores 
                SET id = nextval('volunteer_scores_id_seq') 
                WHERE id IS NULL
            """)
            
            # Set column default to use sequence
            cursor.execute("""
                ALTER TABLE volunteer_scores 
                ALTER COLUMN id SET DEFAULT nextval('volunteer_scores_id_seq')
            """)
            
            # Make ID NOT NULL
            cursor.execute("""
                ALTER TABLE volunteer_scores 
                ALTER COLUMN id SET NOT NULL
            """)
            
            # Set sequence to max existing ID + 1
            cursor.execute("""
                SELECT setval('volunteer_scores_id_seq', 
                             COALESCE((SELECT MAX(id) FROM volunteer_scores WHERE id IS NOT NULL), 0) + 1)
            """)
            
            conn.commit()
            print("✅ SERIAL ID added successfully")
        else:
            print("✅ SERIAL ID already exists")
            
        # Fix NULL IDs
        cursor.execute("SELECT COUNT(*) FROM volunteer_scores WHERE id IS NULL")
        null_count = cursor.fetchone()[0]
        
        if null_count > 0:
            print(f"Fixing {null_count} records with NULL IDs...")
            
            # Update NULL IDs with sequence values
            cursor.execute("""
                UPDATE volunteer_scores 
                SET id = nextval('volunteer_scores_id_seq') 
                WHERE id IS NULL
            """)
            
            conn.commit()
            print(f"✅ Fixed {null_count} NULL ID records")
        else:
            print("✅ No NULL IDs to fix")
            
        # Final verification
        cursor.execute("SELECT COUNT(*) FROM volunteer_scores WHERE id IS NULL")
        remaining_nulls = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM volunteer_scores")
        total_records = cursor.fetchone()[0]
        
        print(f"\nFinal Status:")
        print(f"  Total records: {total_records}")
        print(f"  NULL IDs remaining: {remaining_nulls}")
        
        if remaining_nulls == 0:
            print("✅ volunteer_scores table is now properly configured")
        else:
            print("❌ Some issues remain")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
        
    conn.close()

if __name__ == "__main__":
    fix_volunteer_scores_table()