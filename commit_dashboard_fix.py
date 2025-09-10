import subprocess
import os
from datetime import datetime

os.chdir(r'd:\new ap women safety')

try:
    # Add changes
    subprocess.run(['git', 'add', '.'], check=True)
    print("✅ Added all changes")
    
    # Commit
    commit_msg = "Fix admin dashboard: volunteer statistics display + remove duplicate buttons"
    result = subprocess.run(['git', 'commit', '-m', commit_msg], 
                          capture_output=True, text=True, check=True)
    print("✅ Committed successfully")
    
    # Get hash
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                          capture_output=True, text=True, check=True)
    
    hash_code = result.stdout.strip()
    print(f"🎯 COMMIT HASH: {hash_code}")
    
    # Save info
    with open('dashboard_fix_hash.txt', 'w') as f:
        f.write(f"COMMIT HASH: {hash_code}\n")
        f.write(f"MESSAGE: {commit_msg}\n")
        f.write(f"DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("FIXES:\n")
        f.write("1. Dashboard statistics now update automatically\n")
        f.write("2. Removed duplicate volunteer management buttons\n")
        f.write("3. Fixed volunteer count calculation\n")
    
except Exception as e:
    print(f"Error: {e}")
