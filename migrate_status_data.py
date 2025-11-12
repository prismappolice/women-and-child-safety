from db_config import get_db_connection, adapt_query

def migrate_status_to_scores():
    """Migrate data from volunteer_status to volunteer_scores"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    try:
        # Get all status from old table
        cursor.execute("SELECT volunteer_id, status FROM volunteer_status WHERE volunteer_id IS NOT NULL")
        old_statuses = cursor.fetchall()
        
        print(f"Found {len(old_statuses)} status records to migrate")
        
        for vol_id, status in old_statuses:
            # Map old status names to new ones
            status_map = {'accepted': 'approved', 'hold': 'high_priority', 'pending': 'pending', 'rejected': 'rejected'}
            new_status = status_map.get(status, status)
            
            # Check if already exists in volunteer_scores
            query = adapt_query("SELECT id FROM volunteer_scores WHERE volunteer_id = ?")
            cursor.execute(query, (vol_id,))
            existing = cursor.fetchone()
            
            if existing:
                # Update
                query = adapt_query("UPDATE volunteer_scores SET status = ? WHERE volunteer_id = ?")
                cursor.execute(query, (new_status, vol_id))
                print(f"  ✅ Updated volunteer {vol_id}: {status} → {new_status}")
            else:
                # Insert
                query = adapt_query("""
                    INSERT INTO volunteer_scores (volunteer_id, status, admin_notes)
                    VALUES (?, ?, ?)
                """)
                cursor.execute(query, (vol_id, new_status, f'Migrated from old status: {status}'))
                print(f"  ✅ Inserted volunteer {vol_id}: {status} → {new_status}")
        
        conn.commit()
        
        # Verify
        cursor.execute("SELECT volunteer_id, status FROM volunteer_scores ORDER BY volunteer_id")
        all_scores = cursor.fetchall()
        print("\nFinal volunteer_scores table:")
        for s in all_scores:
            print(f"  Volunteer {s[0]}: {s[1]}")
        
        print("\n✅ Migration complete!")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

if __name__ == '__main__':
    migrate_status_to_scores()
