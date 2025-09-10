import subprocess
import os
from datetime import datetime

def commit_changes():
    # Change to project directory
    os.chdir(r'd:\new ap women safety')
    
    print("=== COMMITTING VOLUNTEER STATUS FIX ===")
    
    try:
        # Add all changes
        subprocess.run(['git', 'add', '.'], check=True)
        print("✅ Added all files to staging")
        
        # Commit with message
        commit_msg = "Commit all changes including volunteer system fixes and new commit scripts"
        result = subprocess.run(['git', 'commit', '-m', commit_msg], 
                              capture_output=True, text=True, check=True)
        
        print("✅ Commit successful!")
        
        # Get commit hash
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                              capture_output=True, text=True, check=True)
        
        commit_hash = result.stdout.strip()
        
        # Save hash to file for reading
        with open('latest_commit_hash.txt', 'w') as f:
            f.write(f"COMMIT HASH: {commit_hash}\n")
            f.write(f"COMMIT MESSAGE: {commit_msg}\n")
            f.write(f"COMMIT TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"🎯 COMMIT HASH: {commit_hash}")
        return commit_hash
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

# Execute the commit
if __name__ == "__main__":
    commit_changes()
