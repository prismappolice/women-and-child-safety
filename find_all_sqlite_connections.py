"""
Comprehensive Check - Find all SQLite connections in admin routes
"""

import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔍 Searching for SQLite connections in admin routes...\n")
print("=" * 80)

# Find all sqlite3.connect calls with line numbers
lines = content.split('\n')
sqlite_connections = []

for i, line in enumerate(lines, 1):
    if 'sqlite3.connect(' in line:
        # Get context - function name
        for j in range(max(0, i-30), i):
            if 'def ' in lines[j]:
                func_name = lines[j].strip()
                break
        else:
            func_name = "Unknown function"
        
        sqlite_connections.append({
            'line': i,
            'code': line.strip(),
            'function': func_name
        })

print(f"📊 Found {len(sqlite_connections)} SQLite connections\n")

# Group by database file
by_db = {}
for conn in sqlite_connections:
    if 'women_safety.db' in conn['code']:
        db = 'women_safety.db'
    elif 'database.db' in conn['code']:
        db = 'database.db'
    elif 'volunteer_system.db' in conn['code']:
        db = 'volunteer_system.db'
    else:
        db = 'unknown'
    
    if db not in by_db:
        by_db[db] = []
    by_db[db].append(conn)

# Print categorized results
for db, connections in by_db.items():
    print(f"\n📁 Database: {db}")
    print(f"   Connections found: {len(connections)}")
    print("-" * 80)
    
    # Check if in admin routes
    admin_routes = [c for c in connections if 'admin' in c['function'].lower()]
    other_routes = [c for c in connections if 'admin' not in c['function'].lower()]
    
    if admin_routes:
        print(f"\n   ⚠️  ADMIN ROUTES (Need PostgreSQL fix):")
        for conn in admin_routes:
            print(f"      Line {conn['line']}: {conn['function']}")
    
    if other_routes:
        print(f"\n   ℹ️  Other routes:")
        for conn in other_routes[:10]:  # Show first 10
            print(f"      Line {conn['line']}: {conn['function']}")
        if len(other_routes) > 10:
            print(f"      ... and {len(other_routes) - 10} more")

print("\n" + "=" * 80)
print("\n🎯 PRIORITY FIX NEEDED:")
print("   All admin routes MUST use get_db_connection('main') for PostgreSQL")
print("\n✅ Correct pattern:")
print("   conn = get_db_connection('main')")
print("   query = adapt_query('SELECT ...')")
print("\n❌ Wrong pattern:")
print("   conn = sqlite3.connect('women_safety.db')")
print("   cursor.execute('SELECT ...')")
