#!/usr/bin/env python3
"""
Fix Database Lock Issues
This script fixes SQLite database lock problems and ensures proper connection handling
"""

import sqlite3
import os
import time

def fix_database_lock():
    """Fix database lock issues and ensure proper connection handling"""
    
    db_path = 'women_safety.db'
    
    print("🔧 FIXING DATABASE LOCK ISSUES...")
    
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return
    
    # Try multiple approaches to fix the lock
    approaches = [
        ("Direct connection with timeout", lambda: sqlite3.connect(db_path, timeout=30.0)),
        ("WAL mode connection", lambda: sqlite3.connect(f"file:{db_path}?mode=rwc", uri=True, timeout=30.0)),
        ("Force unlock connection", lambda: sqlite3.connect(db_path, timeout=1.0))
    ]
    
    for approach_name, connect_func in approaches:
        try:
            print(f"\n🔄 Trying: {approach_name}")
            
            conn = connect_func()
            conn.execute('PRAGMA busy_timeout = 30000')  # 30 second timeout
            conn.execute('PRAGMA journal_mode = WAL')     # Enable WAL mode for better concurrency
            conn.execute('PRAGMA synchronous = NORMAL')   # Optimize for performance
            
            # Test the connection
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM gallery_items')
            count = cursor.fetchone()[0]
            
            # Commit and close properly
            conn.commit()
            conn.close()
            
            print(f"✅ SUCCESS: {approach_name} worked!")
            print(f"✅ Gallery items: {count}")
            print("✅ Database is now accessible")
            return True
            
        except Exception as e:
            print(f"❌ {approach_name} failed: {e}")
            try:
                if 'conn' in locals():
                    conn.close()
            except:
                pass
            continue
    
    print("\n⚠️ All approaches failed. Database may need manual intervention.")
    return False

def create_connection_helper():
    """Create a helper function for safe database connections"""
    
    helper_code = '''
def get_db_connection():
    """Get a safe database connection with proper timeout and WAL mode"""
    import sqlite3
    import time
    
    db_path = 'women_safety.db'
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            conn = sqlite3.connect(db_path, timeout=30.0)
            conn.execute('PRAGMA busy_timeout = 30000')
            conn.execute('PRAGMA journal_mode = WAL')
            conn.execute('PRAGMA synchronous = NORMAL')
            return conn
        except sqlite3.OperationalError as e:
            if "locked" in str(e) and attempt < max_retries - 1:
                time.sleep(1)  # Wait 1 second before retry
                continue
            else:
                raise
    
    raise sqlite3.OperationalError("Could not connect to database after retries")
'''
    
    with open('db_connection_helper.py', 'w') as f:
        f.write(helper_code)
    
    print("✅ Created db_connection_helper.py for safe database connections")

if __name__ == "__main__":
    success = fix_database_lock()
    if success:
        create_connection_helper()
        print("\n🎉 Database lock issues fixed!")
        print("💡 Use the connection helper for future database operations")
    else:
        print("\n❌ Could not fix database lock automatically")
        print("💡 You may need to restart the Flask app or system")
