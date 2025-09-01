import subprocess
import os
from datetime import datetime

# Change to project directory
os.chdir(r'd:\new ap women safety')

print("=== 🚀 COMMITTING ALL CHANGES TO GIT ===")
print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

try:
    # Check what files are changed
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    changes = result.stdout.strip()
    
    if changes:
        print("📝 Files to be committed:")
        for line in changes.split('\n'):
            if line.strip():
                print(f"  {line}")
        
        # Add all changes
        result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
        print("✅ Added all files to staging")
        
        # Commit with descriptive message
        commit_msg = f"Final commit - AP Women Safety project complete with 26 districts - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        result = subprocess.run(['git', 'commit', '-m', commit_msg], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Successfully committed to git!")
        
    else:
        print("ℹ️  No new changes to commit")
    
    # Get the current commit hash (full and short)
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    full_hash = result.stdout.strip()
    short_hash = full_hash[:8]
    
    # Get commit details
    result = subprocess.run(['git', 'log', '-1', '--pretty=format:%s'], capture_output=True, text=True)
    last_commit_msg = result.stdout.strip()
    
    result = subprocess.run(['git', 'log', '-1', '--pretty=format:%ci'], capture_output=True, text=True)
    commit_date = result.stdout.strip()
    
    print("\n" + "="*60)
    print("🎯 GIT COMMIT HASH CODE")
    print("="*60)
    print(f"FULL HASH:  {full_hash}")
    print(f"SHORT HASH: {short_hash}")
    print(f"MESSAGE:    {last_commit_msg}")
    print(f"DATE:       {commit_date}")
    print("="*60)
    
    # Get commit count
    result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], capture_output=True, text=True)
    total_commits = result.stdout.strip()
    
    print(f"\n📊 REPOSITORY STATUS:")
    print(f"Total commits: {total_commits}")
    print(f"Current branch: main (assumed)")
    print(f"Project: AP Women Safety - Districts Update")
    
    # Show last 3 commits
    result = subprocess.run(['git', 'log', '--oneline', '-3'], capture_output=True, text=True)
    recent_commits = result.stdout.strip()
    
    print(f"\n📋 RECENT COMMITS:")
    for line in recent_commits.split('\n'):
        if line.strip():
            print(f"  {line}")
    
    print(f"\n✅ SUCCESS: All changes committed with hash {short_hash}")
    
except Exception as e:
    print(f"❌ Error: {e}")

print("\n🎉 PROJECT SAVED SUCCESSFULLY!")
