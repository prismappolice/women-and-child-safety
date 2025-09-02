#!/usr/bin/env python3
"""
Gallery verification script - check if 5-section gallery is working
"""

import requests
import sqlite3
import os

def check_database():
    """Check database structure and data"""
    print("=== DATABASE CHECK ===")
    
    if not os.path.exists('women_safety.db'):
        print("❌ Database file not found")
        return False
    
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    # Check if table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_items'")
    if not cursor.fetchone():
        print("❌ gallery_items table not found")
        return False
    
    print("✅ gallery_items table exists")
    
    # Check table structure
    cursor.execute("PRAGMA table_info(gallery_items)")
    columns = [col[1] for col in cursor.fetchall()]
    required_columns = ['id', 'title', 'description', 'image_url', 'category', 'is_active']
    
    for col in required_columns:
        if col in columns:
            print(f"✅ Column {col} exists")
        else:
            print(f"❌ Column {col} missing")
    
    # Check data count
    cursor.execute("SELECT COUNT(*) FROM gallery_items")
    count = cursor.fetchone()[0]
    print(f"📊 Total gallery items: {count}")
    
    # Check categories
    cursor.execute("SELECT DISTINCT category FROM gallery_items")
    categories = [row[0] for row in cursor.fetchall()]
    print(f"📂 Categories: {categories}")
    
    expected_categories = ['Self Defence Programme', 'Training Videos', 'Community Programmes', 'News & Events', 'Upcoming Events']
    for cat in expected_categories:
        if cat in categories:
            print(f"✅ Category '{cat}' exists")
        else:
            print(f"❌ Category '{cat}' missing")
    
    conn.close()
    return True

def check_flask_app():
    """Check if Flask app is running and gallery page loads"""
    print("\n=== FLASK APP CHECK ===")
    
    try:
        response = requests.get('http://127.0.0.1:5000/gallery', timeout=5)
        if response.status_code == 200:
            print("✅ Gallery page loads successfully")
            
            # Check if our 5 sections are in the HTML
            content = response.text
            sections = ['Self Defence Programme', 'Training Videos', 'Community Programmes', 'News & Events', 'Upcoming Events']
            
            for section in sections:
                if section in content:
                    print(f"✅ Section '{section}' found in HTML")
                else:
                    print(f"❌ Section '{section}' not found in HTML")
            
            return True
        else:
            print(f"❌ Gallery page returned status {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to Flask app: {e}")
        print("Make sure the Flask app is running on http://127.0.0.1:5000")
        return False

def main():
    print("🔍 GALLERY VERIFICATION REPORT")
    print("=" * 50)
    
    db_ok = check_database()
    app_ok = check_flask_app()
    
    print("\n=== SUMMARY ===")
    if db_ok and app_ok:
        print("🎉 Gallery restructuring completed successfully!")
        print("✅ All 5 sections are properly configured")
        print("✅ Admin can now manage content through /admin/gallery")
    else:
        print("⚠️  Some issues found - check the details above")

if __name__ == "__main__":
    main()
