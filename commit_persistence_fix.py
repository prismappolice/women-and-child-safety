import subprocess
import os

os.chdir(r'd:\new ap women safety')

try:
    # Add the app.py file
    subprocess.run(['git', 'add', 'app.py'], check=True)
    print("✅ Added app.py")
    
    # Commit with message
    commit_msg = "CRITICAL FIX: Stop dropping volunteer tables on restart - preserve data permanently"
    result = subprocess.run(['git', 'commit', '-m', commit_msg], 
                          capture_output=True, text=True, check=True)
    print("✅ Committed successfully")
    
    # Get hash
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                          capture_output=True, text=True, check=True)
    
    hash_code = result.stdout.strip()
    print(f"🎯 COMMIT HASH: {hash_code}")
    
    # Save to file
    with open('persistence_fix_hash.txt', 'w') as f:
        f.write(f"COMMIT HASH: {hash_code}\n")
        f.write(f"MESSAGE: {commit_msg}\n")
        f.write("DESCRIPTION: Fixed volunteer table initialization to preserve data on app restart\n")
        
except Exception as e:
    print(f"Error: {e}")
