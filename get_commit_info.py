import subprocess
import os

# Change to project directory
os.chdir(r'd:\new ap women safety')

try:
    # Get current commit hash
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    commit_hash = result.stdout.strip()
    
    # Get commit message  
    result = subprocess.run(['git', 'log', '-1', '--pretty=format:%s'], capture_output=True, text=True)
    commit_message = result.stdout.strip()
    
    # Get commit date
    result = subprocess.run(['git', 'log', '-1', '--pretty=format:%ci'], capture_output=True, text=True)
    commit_date = result.stdout.strip()
    
    # Get changed files count
    result = subprocess.run(['git', 'show', '--stat', '--pretty=format:', 'HEAD'], capture_output=True, text=True)
    stats = result.stdout.strip()
    
    print("=== GIT COMMIT INFORMATION ===")
    print(f"Commit Hash: {commit_hash}")
    print(f"Commit Message: {commit_message}")
    print(f"Commit Date: {commit_date}")
    print(f"Short Hash: {commit_hash[:8]}")
    print()
    print("=== FILES CHANGED ===")
    print(stats)
    
except Exception as e:
    print(f"Error: {e}")
