#!/usr/bin/env python3
import subprocess
import os

os.chdir(r'd:\new ap women safety')

try:
    # Add changes
    result = subprocess.run(['git', 'add', 'app.py'], capture_output=True, text=True)
    print("Git add result:", result.returncode)
    
    # Commit changes
    result = subprocess.run(['git', 'commit', '-m', 'Fix volunteer status checking database connection issue'], 
                          capture_output=True, text=True)
    print("Commit result:", result.returncode)
    print("Commit output:", result.stdout)
    
    # Get hash
    result = subprocess.run(['git', 'log', '-1', '--format=%H'], capture_output=True, text=True)
    print("Latest commit hash:", result.stdout.strip())
    
except Exception as e:
    print("Error:", e)
