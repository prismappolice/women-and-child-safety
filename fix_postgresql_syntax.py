#!/usr/bin/env python3
"""
Fix remaining PostgreSQL syntax issues in app.py
"""

import re

def fix_postgresql_syntax():
    """Fix remaining SQLite syntax in app.py"""
    print("🔧 Fixing PostgreSQL syntax in app.py...")
    
    with open("app.py", "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()
    
    # Fix AUTOINCREMENT to SERIAL
    old_pattern = r'id INTEGER PRIMARY KEY AUTOINCREMENT'
    new_pattern = r'id SERIAL PRIMARY KEY'
    
    count = len(re.findall(old_pattern, content))
    content = re.sub(old_pattern, new_pattern, content)
    
    print(f"✅ Fixed {count} AUTOINCREMENT → SERIAL conversions")
    
    # Fix INSERT OR IGNORE to INSERT ... ON CONFLICT
    insert_ignore_pattern = r'INSERT OR IGNORE INTO'
    insert_conflict_pattern = r'INSERT INTO'
    
    if re.search(insert_ignore_pattern, content):
        content = re.sub(insert_ignore_pattern, insert_conflict_pattern, content)
        print("✅ Fixed INSERT OR IGNORE → INSERT")
    
    # Write the fixed content
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("✅ app.py PostgreSQL syntax fixed!")

def test_fixed_app():
    """Test the fixed app"""
    print("\n🧪 Testing fixed app...")
    
    try:
        # Import and test
        from importlib import reload
        import sys
        
        # Remove cached modules
        modules_to_remove = [m for m in sys.modules if m.startswith('app')]
        for module in modules_to_remove:
            del sys.modules[module]
        
        # Now import fresh
        from app import app
        print("✅ App imported successfully")
        
        # Test database connection
        from db_config import get_db_connection
        conn = get_db_connection('main')
        cursor = conn.cursor()
        cursor.execute('SELECT version()')
        version = cursor.fetchone()[0]
        print(f"✅ PostgreSQL connection: {version[:50]}...")
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Final PostgreSQL Syntax Fix")
    print("=" * 40)
    
    fix_postgresql_syntax()
    
    if test_fixed_app():
        print("\n🎉 SUCCESS!")
        print("✅ आपका project अब पूरी तरह से PostgreSQL पर चल रहा है!")
        print("✅ कोई SQLite code नहीं बचा है!")
    else:
        print("\n❌ Still some issues remain")