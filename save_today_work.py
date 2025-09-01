import subprocess
import os
from datetime import datetime

# Change to project directory
os.chdir(r'd:\new ap women safety')

print("=== SAVING TODAY'S WORK TO GIT ===")
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

try:
    # Add all changes
    result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
    print("✅ Added all files to git staging")
    
    # Commit with today's date
    commit_msg = f"Final save of today's work - {datetime.now().strftime('%Y-%m-%d')} - AP Districts update completed"
    result = subprocess.run(['git', 'commit', '-m', commit_msg], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Successfully committed to git!")
        print(f"Commit message: {commit_msg}")
    else:
        if "nothing to commit" in result.stdout:
            print("✅ Everything already saved - no new changes to commit")
        else:
            print(f"Commit output: {result.stdout}")
    
    # Get current commit hash
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    commit_hash = result.stdout.strip()
    
    # Get commit count
    result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], capture_output=True, text=True)
    commit_count = result.stdout.strip()
    
    print(f"\n📝 CURRENT STATUS:")
    print(f"Current commit hash: {commit_hash[:8]}...")
    print(f"Total commits: {commit_count}")
    
    # Get today's commits
    today = datetime.now().strftime('%Y-%m-%d')
    result = subprocess.run(['git', 'log', '--oneline', f'--since="{today} 00:00:00"'], capture_output=True, text=True)
    today_commits = result.stdout.strip()
    
    if today_commits:
        print(f"\n📅 TODAY'S COMMITS:")
        for line in today_commits.split('\n'):
            if line.strip():
                print(f"  {line}")
    else:
        print(f"\n📅 No commits found for today ({today})")
    
except Exception as e:
    print(f"❌ Error: {e}")

print("\n=== SAVE COMPLETE ===")
