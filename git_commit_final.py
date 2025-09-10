#!/usr/bin/env python3

import subprocess
import os
import sys

def run_git_commit():
    # Change to project directory
    project_dir = r'd:\new ap women safety'
    os.chdir(project_dir)
    
    print(f"Working in directory: {os.getcwd()}")
    
    try:
        # Stage all changes
        print("Staging changes...")
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit with message
        print("Committing changes...")
        commit_message = "Fix volunteer status database connection issue - removed duplicate code after finally block"
        result = subprocess.run(['git', 'commit', '-m', commit_message], 
                              capture_output=True, text=True, check=True)
        
        print("Commit successful!")
        print("Commit output:", result.stdout)
        
        # Get the commit hash
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                              capture_output=True, text=True, check=True)
        
        commit_hash = result.stdout.strip()
        print(f"\n🎯 COMMIT HASH: {commit_hash}")
        
        # Show commit info
        result = subprocess.run(['git', 'show', '--oneline', '-s'], 
                              capture_output=True, text=True, check=True)
        print(f"📝 Commit Info: {result.stdout.strip()}")
        
        return commit_hash
        
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        print(f"Error output: {e.stderr}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    hash_code = run_git_commit()
    if hash_code:
        print(f"\n✅ SUCCESS! Commit Hash: {hash_code}")
    else:
        print("\n❌ Commit failed!")
