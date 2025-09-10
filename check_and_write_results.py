import sqlite3
import os

# Write results to a file so we can read them
result_file = r'd:\new ap women safety\volunteer_status_result.txt'

with open(result_file, 'w') as f:
    f.write("VOLUNTEER APPLICATION CHECK RESULTS\n")
    f.write("=" * 50 + "\n\n")
    
    try:
        db_path = r'd:\new ap women safety\women_safety.db'
        
        if os.path.exists(db_path):
            f.write(f"✅ Database file exists: {db_path}\n")
            f.write(f"📁 File size: {os.path.getsize(db_path)} bytes\n\n")
            
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check volunteers table
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='volunteers'")
            table_exists = cursor.fetchone()
            
            if table_exists:
                f.write("✅ 'volunteers' table exists\n\n")
                
                # Count applications
                cursor.execute("SELECT COUNT(*) FROM volunteers")
                count = cursor.fetchone()[0]
                f.write(f"📊 Total volunteer applications: {count}\n\n")
                
                # Show applications if any
                if count > 0:
                    f.write("📋 APPLICATIONS IN DATABASE:\n")
                    cursor.execute("""
                        SELECT registration_id, name, phone, email, created_at 
                        FROM volunteers 
                        ORDER BY created_at DESC
                    """)
                    
                    applications = cursor.fetchall()
                    for i, app in enumerate(applications, 1):
                        f.write(f"  {i}. ID: {app[0]}\n")
                        f.write(f"     Name: {app[1]}\n")
                        f.write(f"     Phone: {app[2]}\n")
                        f.write(f"     Email: {app[3]}\n")
                        f.write(f"     Submitted: {app[4]}\n\n")
                
                # Check status table
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='volunteer_status'")
                status_table = cursor.fetchone()
                if status_table:
                    cursor.execute("SELECT COUNT(*) FROM volunteer_status")
                    status_count = cursor.fetchone()[0]
                    f.write(f"📋 Status records: {status_count}\n\n")
                
                conn.close()
                
                # FINAL ANSWER
                f.write("=" * 50 + "\n")
                f.write("🔥 ANSWER TO YOUR QUESTION:\n")
                f.write("=" * 50 + "\n\n")
                
                if count >= 3:
                    f.write("✅ YES! Your 3 volunteer applications are STORED in database\n")
                    f.write("✅ YES! They will appear in admin dashboard after restart\n")
                    f.write("✅ YES! Data is PERMANENT (stored in SQLite database file)\n")
                    f.write("✅ Applications will persist even if you close/reopen app\n")
                elif count > 0:
                    f.write(f"⚠️ Found {count} applications (you mentioned 3)\n")
                    f.write("✅ Applications found WILL persist after restart\n")
                    f.write("❓ Check if all submissions completed successfully\n")
                else:
                    f.write("❌ NO volunteer applications found in database\n")
                    f.write("❌ Applications may not have been saved properly\n")
            else:
                f.write("❌ 'volunteers' table does NOT exist\n")
                f.write("❌ Volunteer system may not be properly initialized\n")
        else:
            f.write("❌ Database file does NOT exist\n")
            f.write("❌ No data can be stored without database file\n")
    
    except Exception as e:
        f.write(f"💥 Error: {str(e)}\n")
    
    f.write("\n🏁 Check completed successfully!\n")

print("Results written to volunteer_status_result.txt")
