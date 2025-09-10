import sqlite3
import os
from datetime import datetime

def check_volunteer_data():
    print("=" * 60)
    print("🔍 VOLUNTEER DATA CHECK - " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 60)
    
    # Main database path
    main_db = r'd:\new ap women safety\women_safety.db'
    
    print(f"\n📁 Database Location: {main_db}")
    print(f"📁 Database Exists: {os.path.exists(main_db)}")
    
    if not os.path.exists(main_db):
        print("❌ Main database not found!")
        return
    
    try:
        print(f"📁 Database Size: {os.path.getsize(main_db)} bytes")
        
        conn = sqlite3.connect(main_db)
        cursor = conn.cursor()
        
        # Check if volunteers table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='volunteers';")
        volunteers_table = cursor.fetchone()
        print(f"\n📊 Volunteers Table Exists: {volunteers_table is not None}")
        
        if volunteers_table:
            # Get total count
            cursor.execute("SELECT COUNT(*) FROM volunteers")
            total = cursor.fetchone()[0]
            print(f"📊 Total Volunteer Applications: {total}")
            
            if total > 0:
                print(f"\n{'='*50}")
                print("📝 VOLUNTEER APPLICATIONS FOUND:")
                print(f"{'='*50}")
                
                cursor.execute("""
                    SELECT v.id, v.registration_id, v.name, v.phone, v.email, 
                           COALESCE(vs.status, 'pending') as status, 
                           v.created_at
                    FROM volunteers v 
                    LEFT JOIN volunteer_status vs ON v.id = vs.volunteer_id 
                    ORDER BY v.created_at DESC
                """)
                
                applications = cursor.fetchall()
                for i, app in enumerate(applications, 1):
                    print(f"\n🔹 Application {i}:")
                    print(f"   📋 Registration ID: {app[1]}")
                    print(f"   👤 Name: {app[2]}")
                    print(f"   📞 Phone: {app[3]}")
                    print(f"   📧 Email: {app[4]}")
                    print(f"   📊 Status: {app[5]}")
                    print(f"   📅 Applied: {app[6]}")
            else:
                print("\n❌ NO VOLUNTEER APPLICATIONS FOUND")
        
        # Check volunteer_status table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='volunteer_status';")
        status_table = cursor.fetchone()
        print(f"\n📊 Volunteer Status Table Exists: {status_table is not None}")
        
        if status_table:
            cursor.execute("SELECT COUNT(*) FROM volunteer_status")
            status_count = cursor.fetchone()[0]
            print(f"📊 Status Records: {status_count}")
        
        conn.close()
        
        # Database persistence check
        print(f"\n{'='*50}")
        print("🗄️ DATABASE PERSISTENCE INFO:")
        print(f"{'='*50}")
        print("✅ Database Type: SQLite (Permanent)")
        print("✅ Storage: File-based (women_safety.db)")
        print("✅ Persistence: Data survives app restart")
        print("✅ Location: Same folder as your Flask app")
        print("❌ NOT Temporary - Data is permanently stored")
        
        # Check other potential databases
        print(f"\n📂 OTHER DATABASE FILES:")
        other_dbs = ['volunteer_system.db']
        for db_name in other_dbs:
            db_path = f'd:\\new ap women safety\\{db_name}'
            if os.path.exists(db_path):
                print(f"📁 Found: {db_name}")
                try:
                    conn2 = sqlite3.connect(db_path)
                    cursor2 = conn2.cursor()
                    cursor2.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
                    table_count = cursor2.fetchone()[0]
                    print(f"   📊 Tables: {table_count}")
                    conn2.close()
                except:
                    print(f"   ❌ Could not read {db_name}")
            else:
                print(f"❌ Not found: {db_name}")
        
    except Exception as e:
        print(f"❌ Error checking database: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_volunteer_data()
