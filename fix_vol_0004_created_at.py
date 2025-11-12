from db_config import get_db_connection, adapt_query
from datetime import datetime

def fix_vol_0004_created_at():
    """Fix NULL created_at for VOL-0004"""
    conn = get_db_connection('main')
    cursor = conn.cursor()
    
    try:
        # Use current timestamp for VOL-0004
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        query = adapt_query("UPDATE volunteers SET created_at = ? WHERE id = 4")
        cursor.execute(query, (current_time,))
        
        conn.commit()
        
        print(f"✅ Updated VOL-0004 created_at to: {current_time}")
        
        # Verify
        cursor.execute("SELECT id, name, registration_id, created_at FROM volunteers ORDER BY id")
        all_vols = cursor.fetchall()
        
        print("\nAll volunteers after fix:")
        for v in all_vols:
            print(f"  {v[2]}: {v[1]} - Applied: {v[3]}")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

if __name__ == '__main__':
    fix_vol_0004_created_at()
