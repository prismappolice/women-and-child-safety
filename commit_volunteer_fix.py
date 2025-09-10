#!/usr/bin/env python3

import subprocess
import os
import sys

def run_git_command(command):
    """Run a git command and return the output"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=r'd:\new ap women safety')
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), 1

def main():
    print("=== Git Commit Process ===")
    
    # Check git status
    print("\n1. Checking git status...")
    stdout, stderr, code = run_git_command("git status --porcelain")
    if code == 0:
        if stdout:
            print("Modified files found:")
            print(stdout)
        else:
            print("No changes to commit")
            return
    else:
        print(f"Error checking status: {stderr}")
        return
    
    # Add all changes
    print("\n2. Adding changes to staging...")
    stdout, stderr, code = run_git_command("git add .")
    if code != 0:
        print(f"Error adding files: {stderr}")
        return
    print("Files added to staging area")
    
    # Commit changes
    print("\n3. Committing changes...")
    commit_message = "Fix volunteer status checking database connection issue\n\n- Remove duplicate code after finally block in check_volunteer_status function\n- Fix sqlite3.ProgrammingError when checking volunteer status\n- Maintain proper database connection management\n- No disruption to existing project structure"
    
    stdout, stderr, code = run_git_command(f'git commit -m "{commit_message}"')
    if code != 0:
        print(f"Error committing: {stderr}")
        return
    print("Changes committed successfully")
    
    # Get commit hash
    print("\n4. Getting commit hash...")
    stdout, stderr, code = run_git_command("git rev-parse HEAD")
    if code == 0:
        commit_hash = stdout
        print(f"\n✅ COMMIT SUCCESSFUL!")
        print(f"📝 Commit Hash: {commit_hash}")
        
        # Get short hash too
        stdout_short, _, _ = run_git_command("git rev-parse --short HEAD")
        if stdout_short:
            print(f"📝 Short Hash: {stdout_short}")
        
        # Show commit details
        print(f"\n📄 Commit Details:")
        stdout, stderr, code = run_git_command("git log -1 --oneline")
        if code == 0:
            print(f"   {stdout}")
            
        return commit_hash
    else:
        print(f"Error getting commit hash: {stderr}")
        return None

if __name__ == "__main__":
    main()
