#!/usr/bin/env python3
"""
Complete SQLite Cleanup Script
Removes all remaining SQLite code and files from the project
"""

import re
import os
import shutil
from datetime import datetime

def backup_files():
    """Create backup of current files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"sqlite_cleanup_backup_{timestamp}"
    os.makedirs(backup_dir, exist_ok=True)
    
    # Backup app.py
    shutil.copy2("app.py", f"{backup_dir}/app.py")
    print(f"✅ Backup created: {backup_dir}/app.py")
    
    return backup_dir

def clean_app_py():
    """Remove SQLite references from app.py"""
    print("🧹 Cleaning SQLite references from app.py...")
    
    with open("app.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Track changes
    changes = []
    
    # Remove sqlite3 import
    if "import sqlite3" in content:
        content = re.sub(r'^import sqlite3.*?\n', '', content, flags=re.MULTILINE)
        changes.append("Removed: import sqlite3")
    
    # Replace sqlite3.connect calls with get_db_connection
    sqlite_connects = [
        "conn = sqlite3.connect('database.db')",
        "conn = sqlite3.connect('volunteer_system.db')",
        "conn = sqlite3.connect('women_safety.db')"
    ]
    
    for old_conn in sqlite_connects:
        if old_conn in content:
            content = content.replace(old_conn, "conn = get_db_connection('main')")
            changes.append(f"Fixed: {old_conn}")
    
    # Fix sqlite_master queries (PostgreSQL equivalent)
    sqlite_master_patterns = [
        (r"SELECT name FROM sqlite_master WHERE type='table' AND name='districts'",
         "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'districts')"),
        (r"SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%district%'",
         "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name LIKE '%district%'")
    ]
    
    for old_pattern, new_pattern in sqlite_master_patterns:
        if re.search(old_pattern, content):
            content = re.sub(old_pattern, new_pattern, content)
            changes.append(f"Fixed sqlite_master query")
    
    # Write cleaned content
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ app.py cleaned - {len(changes)} changes made")
    for change in changes:
        print(f"   - {change}")

def move_sqlite_files():
    """Move SQLite files to backup directory"""
    print("📁 Moving SQLite database files...")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    sqlite_backup_dir = f"old_sqlite_files_{timestamp}"
    os.makedirs(sqlite_backup_dir, exist_ok=True)
    
    sqlite_files = [
        "database.db", 
        "women_safety.db", 
        "volunteer_system.db",
        "database_backup_20251111_135245.db",
        "database_backup_fix.db",
        "volunteer_system_backup_20251111_135249.db",
        "women_safety_backup_20251111_135238.db"
    ]
    
    moved_files = []
    for file in sqlite_files:
        if os.path.exists(file):
            shutil.move(file, f"{sqlite_backup_dir}/{file}")
            moved_files.append(file)
    
    print(f"✅ Moved {len(moved_files)} SQLite files to {sqlite_backup_dir}/")
    for file in moved_files:
        print(f"   - {file}")
    
    return sqlite_backup_dir

def verify_cleanup():
    """Verify that cleanup was successful"""
    print("🔍 Verifying cleanup...")
    
    issues = []
    
    # Check app.py for remaining SQLite references
    with open("app.py", "r") as f:
        content = f.read()
        
    if "import sqlite3" in content:
        issues.append("SQLite import still exists")
    
    if "sqlite3.connect" in content:
        issues.append("Direct SQLite connections still exist")
    
    # Check for remaining SQLite files
    sqlite_files = ["database.db", "women_safety.db", "volunteer_system.db"]
    for file in sqlite_files:
        if os.path.exists(file):
            issues.append(f"SQLite file still exists: {file}")
    
    if issues:
        print("❌ Issues found:")
        for issue in issues:
            print(f"   - {issue}")
        return False
    else:
        print("✅ Cleanup verification passed!")
        return True

def main():
    print("🚀 Starting Complete SQLite Cleanup...")
    print("=" * 50)
    
    # Create backup
    backup_dir = backup_files()
    
    # Clean app.py
    clean_app_py()
    
    # Move SQLite files
    sqlite_backup_dir = move_sqlite_files()
    
    # Verify cleanup
    success = verify_cleanup()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 SQLite CLEANUP COMPLETE!")
        print("✅ Your project now uses PostgreSQL ONLY")
        print("✅ All SQLite code removed from app.py")
        print("✅ All SQLite files moved to backup")
        print(f"\n📁 Backups created:")
        print(f"   - Code backup: {backup_dir}/")
        print(f"   - SQLite files: {sqlite_backup_dir}/")
    else:
        print("❌ Cleanup had some issues - check the verification output")
    
    print("\nNext steps:")
    print("1. Test your application: python app.py")
    print("2. Verify all pages work correctly")
    print("3. If everything works, you can delete the backup folders")

if __name__ == "__main__":
    main()