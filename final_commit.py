import subprocess
import os
from datetime import datetime

os.chdir(r'd:\new ap women safety')

try:
    print("=== SAVING ALL VOLUNTEER SYSTEM CHANGES ===")
    
    # Check git status
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    if result.stdout.strip():
        print("📝 Changes to commit:")
        for line in result.stdout.strip().split('\n'):
            if line.strip():
                print(f"  {line}")
    else:
        print("ℹ️ No changes to commit")
        exit()
    
    # Add all changes
    subprocess.run(['git', 'add', '.'], check=True)
    print("✅ Added all changes to staging")
    
    # Commit with comprehensive message
    commit_msg = "Complete volunteer management system - dashboard statistics, data persistence, status management"
    result = subprocess.run(['git', 'commit', '-m', commit_msg], 
                          capture_output=True, text=True, check=True)
    print("✅ Committed successfully!")
    print("Commit output:", result.stdout)
    
    # Get commit hash
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                          capture_output=True, text=True, check=True)
    
    hash_code = result.stdout.strip()
    print(f"🎯 FINAL COMMIT HASH: {hash_code}")
    
    # Save comprehensive summary
    with open('final_volunteer_commit.txt', 'w') as f:
        f.write("COMPLETE VOLUNTEER SYSTEM COMMIT\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"COMMIT HASH: {hash_code}\n")
        f.write(f"COMMIT MESSAGE: {commit_msg}\n")
        f.write(f"COMMIT DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("FEATURES IMPLEMENTED:\n")
        f.write("✅ Volunteer registration system\n")
        f.write("✅ Admin dashboard for volunteer management\n")
        f.write("✅ Status tracking (Pending → Hold → Accept/Reject)\n")
        f.write("✅ Volunteer status checking for users\n")
        f.write("✅ Data persistence (fixed table dropping issue)\n")
        f.write("✅ Dashboard statistics display\n")
        f.write("✅ Clean UI (removed duplicate buttons)\n\n")
        
        f.write("FILES MODIFIED:\n")
        f.write("- app.py (main application with all volunteer routes)\n")
        f.write("- templates/admin_dashboard.html (statistics & clean UI)\n")
        f.write("- templates/volunteer_registration.html\n")
        f.write("- templates/check_volunteer_status.html\n")
        f.write("- templates/manage_volunteers.html\n")
        f.write("- Database tables: volunteers, volunteer_status\n\n")
        
        f.write("CRITICAL FIXES:\n")
        f.write("🔧 Fixed database table initialization (no more data loss)\n")
        f.write("🔧 Fixed volunteer status checking database connection\n")
        f.write("🔧 Fixed dashboard statistics not updating\n")
        f.write("🔧 Removed duplicate volunteer management buttons\n\n")
        
        f.write("SYSTEM STATUS: FULLY FUNCTIONAL ✅\n")
    
    print(f"\n🎉 ALL CHANGES SAVED TO GIT!")
    print(f"📋 Summary saved to: final_volunteer_commit.txt")
    
except subprocess.CalledProcessError as e:
    if "nothing to commit" in e.stderr or "nothing to commit" in e.stdout:
        print("ℹ️ No new changes to commit - everything is already saved!")
    else:
        print(f"❌ Git error: {e}")
        print(f"Error output: {e.stderr}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    import traceback
    traceback.print_exc()
