import subprocess
import sys
import os

# Change to the project directory
os.chdir(r'd:\new ap women safety')

print("Current directory:", os.getcwd())

try:
    # Check git status first
    print("\n=== Git Status ===")
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    print("Status output:", result.stdout)
    
    # Add all changes
    print("\n=== Adding Changes ===")
    result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
    print("Add result code:", result.returncode)
    if result.stderr:
        print("Add stderr:", result.stderr)
    
    # Commit changes
    print("\n=== Committing Changes ===")
    result = subprocess.run(['git', 'commit', '-m', 'Fix volunteer status database connection issue - removed duplicate code after finally block'], 
                          capture_output=True, text=True)
    print("Commit result code:", result.returncode)
    print("Commit stdout:", result.stdout)
    if result.stderr:
        print("Commit stderr:", result.stderr)
    
    # Get the latest commit hash
    print("\n=== Getting Commit Hash ===")
    result = subprocess.run(['git', 'log', '-1', '--format=%H'], capture_output=True, text=True)
    hash_code = result.stdout.strip()
    print(f"COMMIT HASH: {hash_code}")
    
    # Also get commit info
    result = subprocess.run(['git', 'log', '-1', '--oneline'], capture_output=True, text=True)
    print(f"Commit info: {result.stdout.strip()}")
    
except Exception as e:
    print("Error occurred:", str(e))
    import traceback
    traceback.print_exc()
