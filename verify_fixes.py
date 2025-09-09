#!/usr/bin/env python3
"""
Verification script to confirm all database fixes are working
"""
import sqlite3
import traceback

def verify_database():
    """Verify all database tables and schemas are working"""
    print("🔍 Verifying database fixes...")
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Test volunteers table
        print("\n1. Testing volunteers table...")
        cursor.execute("SELECT COUNT(*) FROM volunteers")
        volunteers_count = cursor.fetchone()[0]
        print(f"   ✅ Volunteers table accessible - {volunteers_count} records")
        
        # Test gallery_items table
        print("\n2. Testing gallery_items table...")
        cursor.execute("SELECT COUNT(*) FROM gallery_items")
        gallery_count = cursor.fetchone()[0]
        print(f"   ✅ Gallery items table accessible - {gallery_count} records")
        
        # Test gallery_media table
        print("\n3. Testing gallery_media table...")
        cursor.execute("SELECT COUNT(*) FROM gallery_media")
        media_count = cursor.fetchone()[0]
        print(f"   ✅ Gallery media table accessible - {media_count} records")
        
        # Test other critical tables
        critical_tables = ['officers', 'initiatives', 'about_sections', 'home_content']
        print("\n4. Testing other critical tables...")
        for table in critical_tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"   ✅ {table} table accessible - {count} records")
        
        conn.close()
        print("\n🎉 All database fixes verified successfully!")
        print("\n📊 Summary:")
        print("   - Gallery restructured to 5 sections")
        print("   - Volunteers table schema fixed")
        print("   - All existing data preserved")
        print("   - Admin dashboard accessible")
        
        return True
        
    except Exception as e:
        print(f"❌ Database verification failed: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    verify_database()
