"""
Simple diagnostic to show what database is being used
"""
from db_config import DB_MODE, get_db_connection
import psycopg2
import sqlite3

print("=" * 80)
print("DATABASE DIAGNOSTIC")
print("=" * 80)

print(f"\nDB_MODE: {DB_MODE}")

# Try to connect and check
conn = get_db_connection('main')
print(f"Connection type: {type(conn)}")

if isinstance(conn, psycopg2.extensions.connection):
    print("✅ Using PostgreSQL!")
    
    cursor = conn.cursor()
    
    # Get PostgreSQL version
    cursor.execute('SELECT version()')
    version = cursor.fetchone()[0]
    print(f"PostgreSQL Version: {version.split(',')[0]}")
    
    # Check volunteers table
    cursor.execute('''
        SELECT v.id, v.name, vs.status
        FROM volunteers v
        LEFT JOIN volunteer_scores vs ON v.id = vs.volunteer_id
        ORDER BY v.id
    ''')
    
    print("\n" + "=" * 80)
    print("CURRENT VOLUNTEER STATUSES IN POSTGRESQL")
    print("=" * 80)
    
    volunteers = cursor.fetchall()
    for vol in volunteers:
        print(f"ID {vol[0]}: {vol[1]} - Status: {vol[2] if vol[2] else 'NULL'}")
    
    print("\n" + "=" * 80)
    print("BUTTON VISIBILITY FOR EACH VOLUNTEER")
    print("=" * 80)
    
    for vol in volunteers:
        vol_id, name, status = vol
        print(f"\nVolunteer: {name} (ID: {vol_id})")
        print(f"  Status: {status if status else 'NULL'}")
        
        if status == 'pending' or status == 'high_priority' or status is None:
            print("  Buttons: Hold, Accept, Reject, View")
        elif status == 'approved':
            print("  Buttons: View ONLY (Hold/Accept/Reject HIDDEN)")
        elif status == 'rejected':
            print("  Buttons: View ONLY (Hold/Accept/Reject HIDDEN)")
    
elif isinstance(conn, sqlite3.Connection):
    print("❌ Still using SQLite!")
    print("This might explain why changes don't show up")
else:
    print(f"❓ Unknown connection type: {type(conn)}")

conn.close()

print("\n" + "=" * 80)
print("RECOMMENDATION")
print("=" * 80)

if isinstance(conn, psycopg2.extensions.connection):
    print("✅ Database is correctly using PostgreSQL")
    print("If admin panel still shows old data:")
    print("  1. Clear browser cache: Ctrl+Shift+Delete")
    print("  2. Hard refresh: Ctrl+F5")
    print("  3. Close browser completely and reopen")
    print("  4. Try incognito/private window")
else:
    print("❌ Need to switch to PostgreSQL")
    print("Check .env file or db_config.py")

print("=" * 80)
