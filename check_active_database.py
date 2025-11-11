"""
Check which database your application is currently using
"""
from db_config import DB_MODE, get_db_connection, check_db_connection

print("="*60)
print("DATABASE STATUS CHECK")
print("="*60)

print(f"\n📊 Current Database Mode: {DB_MODE}")

if DB_MODE == 'postgresql':
    print("\n✅ Application is using: POSTGRESQL")
    print("   Server: localhost:5432")
    print("   Database: women_safety_db")
    print("   User: postgres")
    print("\n   SQLite files exist but are NOT being used")
    
elif DB_MODE == 'sqlite':
    print("\n✅ Application is using: SQLITE")
    print("   Files: women_safety.db, database.db")
    print("\n   PostgreSQL exists but is NOT being used")

print("\n" + "="*60)
print("CONNECTION TEST")
print("="*60)

# Test connection
if check_db_connection():
    print(f"\n✅ Successfully connected to {DB_MODE.upper()}")
    
    # Get some data to verify
    try:
        conn = get_db_connection('main')
        cursor = conn.cursor()
        
        # Count volunteers
        cursor.execute("SELECT COUNT(*) FROM volunteers")
        vol_count = cursor.fetchone()[0]
        
        # Count gallery items
        cursor.execute("SELECT COUNT(*) FROM gallery_items")
        gallery_count = cursor.fetchone()[0]
        
        print(f"\n📊 Data from {DB_MODE.upper()}:")
        print(f"   - Volunteers: {vol_count}")
        print(f"   - Gallery Items: {gallery_count}")
        
        conn.close()
        
    except Exception as e:
        print(f"\n⚠️  Error reading data: {e}")
else:
    print(f"\n❌ Could not connect to {DB_MODE.upper()}")

print("\n" + "="*60)
print("FILE STATUS")
print("="*60)

import os

sqlite_files = ['women_safety.db', 'database.db', 'volunteer_system.db']
print("\nSQLite Files:")
for file in sqlite_files:
    if os.path.exists(file):
        size = os.path.getsize(file) / 1024  # KB
        print(f"   ✅ {file} ({size:.2f} KB) - EXISTS (backup)")
    else:
        print(f"   ❌ {file} - NOT FOUND")

print("\n" + "="*60)
print("RECOMMENDATION")
print("="*60)
print("\n✅ KEEP SQLite files as backup")
print("✅ Use PostgreSQL for application")
print("\nBenefits:")
print("  - PostgreSQL: Production-ready, scalable")
print("  - SQLite backup: Safety net for rollback")
print("\n💡 You can delete SQLite files after 2 weeks of testing")
print("="*60)
