import sqlite3
import os

def check_database_configuration():
    print("=== DATABASE CONFIGURATION ANALYSIS ===")
    print()
    
    # Check current directory
    current_dir = os.getcwd()
    print(f"📁 Current Working Directory: {current_dir}")
    
    # Check for database file
    db_file = "women_safety.db"
    db_path = os.path.join(current_dir, db_file)
    
    print(f"🗃️  Database File: {db_file}")
    print(f"📍 Full Database Path: {db_path}")
    print(f"✅ Database Exists: {os.path.exists(db_path)}")
    
    if os.path.exists(db_path):
        file_size = os.path.getsize(db_path)
        print(f"📊 Database Size: {file_size} bytes ({file_size/1024:.1f} KB)")
    
    print()
    print("🔧 DATABASE CONNECTION CONFIGURATION:")
    print("   - Type: SQLite (File-based)")
    print("   - Connection String: sqlite3.connect('women_safety.db')")
    print("   - Location: Same directory as app.py")
    print("   - URL Format: No URL needed (local file)")
    
    print()
    print("📋 WHAT THIS MEANS:")
    print("   ✅ No database URL configuration needed")
    print("   ✅ Database is a local file (women_safety.db)")
    print("   ✅ Portable - moves with your application")
    print("   ✅ No external database server required")
    
    # Test connection
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()
        
        print()
        print(f"🗂️  DATABASE TABLES ({len(tables)} found):")
        for table in tables:
            print(f"   - {table[0]}")
            
    except Exception as e:
        print(f"❌ Database connection error: {e}")
    
    print()
    print("🚀 FOR HOSTING:")
    print("   - Just upload women_safety.db with your application")
    print("   - No database URL configuration required")
    print("   - SQLite works out of the box on most hosting platforms")

if __name__ == "__main__":
    check_database_configuration()
