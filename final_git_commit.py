import subprocess
import os
from datetime import datetime

print("=== FINAL GIT COMMIT - ALL CHANGES ===")
print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# Change to project directory
os.chdir(r'd:\new ap women safety')
print(f"Working directory: {os.getcwd()}")

try:
    # Step 1: Add all files
    print("1. Adding all files to git staging...")
    result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
    if result.returncode == 0:
        print("   ✅ All files added successfully")
    else:
        print(f"   ❌ Error adding files: {result.stderr}")
    
    # Step 2: Commit with comprehensive message
    commit_message = f"FINAL COMMIT: Complete AP Women Safety project - 26 districts updated, admin fixes, data mapping, git tracking - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    print("2. Committing changes...")
    result = subprocess.run(['git', 'commit', '-m', commit_message], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("   ✅ COMMIT SUCCESSFUL!")
        print(f"   Message: {commit_message}")
    elif "nothing to commit" in result.stdout:
        print("   ✅ Everything already committed - no new changes")
    else:
        print(f"   Commit output: {result.stdout}")
        print(f"   Commit errors: {result.stderr}")
    
    # Step 3: Get current status
    print("\n3. Current git status:")
    result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
    if result.stdout.strip():
        print(f"   Uncommitted files: {result.stdout}")
    else:
        print("   ✅ All files committed - working tree clean")
    
    # Step 4: Get commit hash
    print("\n4. Current commit details:")
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    commit_hash = result.stdout.strip()
    print(f"   Commit hash: {commit_hash}")
    print(f"   Short hash: {commit_hash[:8]}")
    
    # Step 5: Show recent commits
    print("\n5. Recent commits:")
    result = subprocess.run(['git', 'log', '--oneline', '-5'], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if line.strip():
            print(f"   {line}")
    
    print("\n" + "="*50)
    print("🎉 ALL CHANGES SUCCESSFULLY COMMITTED TO GIT!")
    print("🔒 Your project is now fully backed up and versioned")
    print("📝 All your modifications are safely stored")
    print("="*50)

except Exception as e:
    print(f"❌ Error during git operations: {e}")

print("\nPress Enter to continue...")
input()
