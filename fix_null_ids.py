#!/usr/bin/env python3

from db_config import get_db_connection

def fix_null_ids():
    """Fix NULL ID issues in volunteer_scores table"""
    
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    print("=== FIXING NULL ID ISSUES ===")
    
    # Check volunteer_scores table structure
    cursor.execute("""
        SELECT column_name, column_default, is_nullable
        FROM information_schema.columns 
        WHERE table_name = 'volunteer_scores' 
        ORDER BY ordinal_position
    """)
    columns = cursor.fetchall()
    print("volunteer_scores table structure:")
    for col in columns:
        print(f"  - {col[0]} (default: {col[1]}, nullable: {col[2]})")
    
    # Check for NULL IDs
    cursor.execute("SELECT COUNT(*) FROM volunteer_scores WHERE id IS NULL")
    null_count = cursor.fetchone()[0]
    print(f"\nRecords with NULL IDs: {null_count}")
    
    if null_count > 0:
        print("Fixing NULL IDs...")
        
        # Get records with NULL IDs
        cursor.execute("SELECT volunteer_id, status FROM volunteer_scores WHERE id IS NULL")
        null_records = cursor.fetchall()
        
        # Delete NULL ID records
        cursor.execute("DELETE FROM volunteer_scores WHERE id IS NULL")
        
        # Re-insert with proper sequence
        for volunteer_id, status in null_records:
            cursor.execute("""
                INSERT INTO volunteer_scores (volunteer_id, status, admin_notes)
                VALUES (%s, %s, %s)
            """, (volunteer_id, status or 'pending', 'Fixed NULL ID record'))
        
        conn.commit()
        print(f"✅ Fixed {len(null_records)} records with NULL IDs")
    else:
        print("✅ No NULL IDs found")
    
    # Verify fix
    cursor.execute("SELECT COUNT(*) FROM volunteer_scores WHERE id IS NULL")
    remaining_nulls = cursor.fetchone()[0]
    
    if remaining_nulls == 0:
        print("✅ All NULL IDs have been fixed")
    else:
        print(f"❌ Still {remaining_nulls} NULL IDs remaining")
    
    conn.close()

if __name__ == "__main__":
    fix_null_ids()