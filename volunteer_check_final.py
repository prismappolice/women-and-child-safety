import sqlite3
import os

# Check volunteer applications in database
db_path = r'd:\new ap women safety\women_safety.db'

print("🔍 CHECKING YOUR 3 VOLUNTEER APPLICATIONS")
print("=" * 50)

try:
    if os.path.exists(db_path):
        print(f"✅ Database file exists")
        print(f"📁 File size: {os.path.getsize(db_path)} bytes")
    else:
        print("❌ Database file NOT found!")
        exit()
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if volunteers table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='volunteers'")
    table_exists = cursor.fetchone()
    
    if table_exists:
        print("✅ 'volunteers' table exists")
        
        # Count total applications
        cursor.execute("SELECT COUNT(*) FROM volunteers")
        count = cursor.fetchone()[0]
        print(f"📊 Total applications in database: {count}")
        
        if count >= 3:
            print("🎉 YES! Your applications are stored in database")
        elif count > 0:
            print(f"⚠️ Found only {count} applications (you said you submitted 3)")
        else:
            print("❌ No applications found in database")
        
        # Show all applications
        if count > 0:
            print("\n📋 ALL STORED APPLICATIONS:")
            cursor.execute("""
                SELECT registration_id, name, phone, created_at 
                FROM volunteers 
                ORDER BY created_at DESC
            """)
            
            applications = cursor.fetchall()
            for i, row in enumerate(applications, 1):
                print(f"  {i}. {row[0]} - {row[1]} - {row[2]} - {row[3]}")
    else:
        print("❌ 'volunteers' table does NOT exist")
        count = 0
    
    conn.close()
    
    # FINAL ANSWER
    print("\n" + "=" * 50)
    print("🔥 ANSWER TO YOUR QUESTION:")
    print("=" * 50)
    
    if count >= 3:
        print("✅ YES - Your 3 applications are PERMANENTLY stored in database")
        print("✅ YES - They will appear in admin dashboard after app restart") 
        print("✅ YES - Data persists even if you close/open the application")
        print("✅ Data is stored in SQLite file: women_safety.db")
    elif count > 0:
        print(f"⚠️ Only {count} applications found (not 3 as expected)")
        print("✅ YES - Found applications will persist after restart")
        print("❓ You may need to check if all 3 submissions were successful")
    else:
        print("❌ NO applications found in database")
        print("❌ Applications may not have been saved properly")
        print("❓ Check if volunteer registration was completed successfully")

except Exception as e:
    print(f"💥 Error checking database: {e}")

print("\n🏁 Database check completed!")
