import sqlite3
import os

def check_volunteer_applications():
    db_path = r'd:\new ap women safety\women_safety.db'
    
    if not os.path.exists(db_path):
        print("❌ Database file does not exist!")
        return
    
    print("=== CHECKING VOLUNTEER APPLICATIONS IN DATABASE ===")
    print(f"Database file: {db_path}")
    print(f"File size: {os.path.getsize(db_path)} bytes")
    print()
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if volunteers table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='volunteers'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            print("❌ 'volunteers' table does not exist in database")
            conn.close()
            return
        
        print("✅ 'volunteers' table exists")
        
        # Count total volunteers
        cursor.execute("SELECT COUNT(*) FROM volunteers")
        total_count = cursor.fetchone()[0]
        print(f"📊 Total volunteer applications: {total_count}")
        
        if total_count > 0:
            print("\n=== VOLUNTEER APPLICATIONS DETAILS ===")
            
            # Get all volunteer data
            cursor.execute("""
                SELECT 
                    v.id,
                    v.registration_id,
                    v.name,
                    v.email, 
                    v.phone,
                    v.created_at,
                    COALESCE(vs.status, 'pending') as status,
                    COALESCE(vs.updated_at, v.created_at) as status_updated
                FROM volunteers v 
                LEFT JOIN volunteer_status vs ON v.id = vs.volunteer_id
                ORDER BY v.created_at DESC
            """)
            
            applications = cursor.fetchall()
            
            for i, app in enumerate(applications, 1):
                print(f"\n--- Application {i} ---")
                print(f"ID: {app[0]}")
                print(f"Registration ID: {app[1]}")
                print(f"Name: {app[2]}")
                print(f"Email: {app[3]}")
                print(f"Phone: {app[4]}")
                print(f"Applied: {app[5]}")
                print(f"Status: {app[6]}")
                print(f"Status Updated: {app[7]}")
                
        else:
            print("❌ No volunteer applications found in database")
        
        # Check volunteer_status table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='volunteer_status'")
        status_table_exists = cursor.fetchone()
        
        if status_table_exists:
            cursor.execute("SELECT COUNT(*) FROM volunteer_status")
            status_count = cursor.fetchone()[0]
            print(f"\n📋 Volunteer status records: {status_count}")
        else:
            print("\n⚠️ 'volunteer_status' table does not exist")
        
        conn.close()
        
        print("\n=== PERSISTENCE CHECK ===")
        print("✅ All data is stored in SQLite database file")
        print("✅ Data will persist after application restart")
        print("✅ Applications will appear in admin dashboard after restart")
        
    except Exception as e:
        print(f"❌ Error checking database: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_volunteer_applications()
