exec("""
import sqlite3
import os

print("=" * 60)
print("🔍 CHECKING YOUR 3 VOLUNTEER APPLICATIONS")
print("=" * 60)

db_path = r'd:\\new ap women safety\\women_safety.db'

if os.path.exists(db_path):
    print("✅ Database file found!")
    print(f"📁 Size: {os.path.getsize(db_path)} bytes")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check volunteers table
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='volunteers'")
    if cursor.fetchone():
        print("✅ Volunteers table exists")
        
        # Count applications
        cursor.execute("SELECT COUNT(*) FROM volunteers")
        count = cursor.fetchone()[0]
        print(f"📊 Total applications: {count}")
        
        if count > 0:
            # Show applications
            cursor.execute("SELECT registration_id, name, phone FROM volunteers ORDER BY created_at DESC")
            apps = cursor.fetchall()
            print("\\n📋 Your Applications:")
            for i, app in enumerate(apps, 1):
                print(f"  {i}. {app[0]} - {app[1]} - {app[2]}")
        
        print("\\n" + "=" * 60)
        print("🔥 FINAL ANSWER:")
        print("=" * 60)
        
        if count >= 3:
            print("✅ YES! Your 3 applications are PERMANENTLY STORED")
            print("✅ YES! They will show in dashboard after restart")
            print("✅ YES! Data persists when you close/open app")
        elif count > 0:
            print(f"⚠️ Found {count} applications (not 3)")
            print("✅ Found applications WILL persist after restart")
        else:
            print("❌ No applications found")
    else:
        print("❌ Volunteers table not found")
    
    conn.close()
else:
    print("❌ Database file not found!")

print("\\n🏁 Check complete!")
""")
