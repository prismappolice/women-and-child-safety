#!/usr/bin/env python3
"""
Update all database connections in app.py to use the new connection helper
This prevents database lock issues across the entire application
"""

def update_database_connections():
    """Replace all sqlite3.connect calls with get_db_connection()"""
    
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count current instances
    old_pattern = "sqlite3.connect('women_safety.db')"
    count = content.count(old_pattern)
    print(f"Found {count} instances of old database connections")
    
    # Replace with new connection helper
    new_pattern = "get_db_connection()"
    updated_content = content.replace(old_pattern, new_pattern)
    
    # Write back to file
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    # Verify replacement
    with open('app.py', 'r', encoding='utf-8') as f:
        new_content = f.read()
    
    remaining = new_content.count(old_pattern)
    replaced = new_content.count(new_pattern)
    
    print(f"✅ Replaced {count} database connections")
    print(f"✅ Now using {replaced} instances of get_db_connection()")
    print(f"✅ Remaining old connections: {remaining}")
    
    if remaining == 0:
        print("🎉 All database connections updated successfully!")
        print("🔒 No more database lock issues!")
    else:
        print("⚠️ Some connections may still need manual updating")

if __name__ == "__main__":
    update_database_connections()
