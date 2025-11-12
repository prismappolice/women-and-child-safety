from db_config import get_db_connection

def fix_safety_tips_sequence():
    """Fix NULL IDs in safety_tips table and create proper sequence"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    try:
        # Check for NULL IDs
        cursor.execute('SELECT COUNT(*) FROM safety_tips WHERE id IS NULL')
        null_count = cursor.fetchone()[0]
        print(f"Found {null_count} safety tips with NULL ID")
        
        if null_count > 0:
            # Get the maximum existing ID
            cursor.execute('SELECT COALESCE(MAX(id), 0) FROM safety_tips WHERE id IS NOT NULL')
            max_id = cursor.fetchone()[0]
            next_id = max_id + 1
            print(f"Maximum existing ID: {max_id}")
            print(f"Will assign IDs starting from: {next_id}")
            
            # Get all NULL ID records
            cursor.execute('SELECT category, title FROM safety_tips WHERE id IS NULL')
            null_records = cursor.fetchall()
            
            # Assign IDs to NULL records
            for i, record in enumerate(null_records):
                new_id = next_id + i
                cursor.execute(
                    'UPDATE safety_tips SET id = %s WHERE id IS NULL AND category = %s AND title = %s',
                    (new_id, record[0], record[1])
                )
                print(f"Assigned ID {new_id} to tip: {record[1][:50]}")
            
            # Create sequence if it doesn't exist
            cursor.execute("""
                SELECT EXISTS (
                    SELECT 1 FROM pg_class WHERE relname = 'safety_tips_id_seq'
                )
            """)
            seq_exists = cursor.fetchone()[0]
            
            if not seq_exists:
                print("\nCreating safety_tips_id_seq sequence...")
                # Get new max ID after updates
                cursor.execute('SELECT MAX(id) FROM safety_tips')
                new_max_id = cursor.fetchone()[0]
                next_seq_val = new_max_id + 1
                
                cursor.execute(f"CREATE SEQUENCE safety_tips_id_seq START WITH {next_seq_val}")
                cursor.execute("ALTER TABLE safety_tips ALTER COLUMN id SET DEFAULT nextval('safety_tips_id_seq')")
                cursor.execute("ALTER SEQUENCE safety_tips_id_seq OWNED BY safety_tips.id")
                print(f"✅ Sequence created starting at {next_seq_val}")
            else:
                # Update existing sequence
                cursor.execute('SELECT MAX(id) FROM safety_tips')
                new_max_id = cursor.fetchone()[0]
                next_seq_val = new_max_id + 1
                cursor.execute(f"ALTER SEQUENCE safety_tips_id_seq RESTART WITH {next_seq_val}")
                print(f"✅ Sequence updated to start at {next_seq_val}")
            
            conn.commit()
            print("\n✅ All safety tips now have valid IDs!")
        else:
            print("✅ No NULL IDs found. All safety tips have valid IDs.")
            
        # Show all tips
        cursor.execute('SELECT id, category, title FROM safety_tips ORDER BY id')
        all_tips = cursor.fetchall()
        print(f"\nTotal safety tips: {len(all_tips)}")
        for tip in all_tips:
            print(f"  ID {tip[0]}: [{tip[1]}] {tip[2][:50]}")
            
    except Exception as e:
        conn.rollback()
        print(f"❌ Error: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    fix_safety_tips_sequence()
