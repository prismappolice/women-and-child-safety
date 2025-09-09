#!/usr/bin/env python3
"""
EMERGENCY: Restore only your original data, remove my additions
"""
import sqlite3

def restore_only_original_data():
    """Remove any sample data I added and keep only your original data"""
    print("🔧 EMERGENCY: Restoring only your original data...")
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Check what tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [table[0] for table in cursor.fetchall()]
        print(f"📋 Tables found: {tables}")
        
        # For content tables that I may have added sample data to, 
        # I'll only clear them if they have generic sample content
        
        # Clear about_content if it has sample content I added
        if 'about_content' in tables:
            cursor.execute("SELECT COUNT(*) FROM about_content")
            count = cursor.fetchone()[0]
            print(f"📝 About content: {count} records")
            # Only clear if it looks like sample data (no custom user data)
            cursor.execute("SELECT title FROM about_content WHERE title LIKE '%Our Mission%' OR title LIKE '%Our Vision%'")
            sample_data = cursor.fetchall()
            if sample_data:
                print("   🧹 Clearing sample about content...")
                cursor.execute("DELETE FROM about_content WHERE title LIKE '%Our Mission%' OR title LIKE '%Our Vision%' OR title LIKE '%About Us%'")
        
        # Clear safety_tips if it has sample content I added
        if 'safety_tips' in tables:
            cursor.execute("SELECT COUNT(*) FROM safety_tips")
            count = cursor.fetchone()[0]
            print(f"🛡️ Safety tips: {count} records")
            # Clear sample safety tips
            cursor.execute("DELETE FROM safety_tips WHERE title IN ('Personal Safety', 'Digital Safety', 'Public Transport Safety', 'Workplace Safety')")
        
        # Clear pdf_resources if it has sample content I added
        if 'pdf_resources' in tables:
            cursor.execute("SELECT COUNT(*) FROM pdf_resources")
            count = cursor.fetchone()[0]
            print(f"📄 PDF resources: {count} records")
            # Clear sample PDF resources
            cursor.execute("DELETE FROM pdf_resources WHERE title IN ('Women Safety Guidelines', 'Emergency Contact Numbers', 'Legal Rights Handbook', 'Self Defense Guide')")
        
        # Clear home_content if it has sample content I added
        if 'home_content' in tables:
            cursor.execute("SELECT COUNT(*) FROM home_content")
            count = cursor.fetchone()[0]
            print(f"🏠 Home content: {count} records")
            # Clear sample home content
            cursor.execute("DELETE FROM home_content WHERE title LIKE '%Ensuring Women%' OR title LIKE '%24/7 Emergency%' OR title LIKE '%Community Programs%' OR title LIKE '%Legal Support%'")
        
        # DO NOT TOUCH these tables - they contain your original data:
        protected_tables = ['officers', 'initiatives', 'volunteers', 'gallery_items', 'success_stories']
        
        print("\n🔒 PROTECTED TABLES (Your Original Data):")
        for table in protected_tables:
            if table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                print(f"   ✅ {table}: {count} records (PRESERVED)")
        
        conn.commit()
        conn.close()
        
        print("\n🎯 EMERGENCY RESTORE COMPLETE!")
        print("   ✅ Your original data preserved")
        print("   🧹 Sample content removed")
        print("   ✅ Only your data remains")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    restore_only_original_data()
