#!/usr/bin/env python3
"""
Check all content tables to see what data exists
"""
import sqlite3

def check_all_content():
    """Check what content exists in all tables"""
    print("🔍 Checking All Content Tables")
    print("=" * 60)
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # Check about_sections
        print("\n1. 📋 ABOUT SECTIONS:")
        try:
            cursor.execute("SELECT title, content FROM about_sections ORDER BY display_order")
            about_data = cursor.fetchall()
            if about_data:
                for i, (title, content) in enumerate(about_data, 1):
                    print(f"   {i}. {title}")
                    print(f"      Content: {content[:100]}...")
            else:
                print("   📭 No about sections found")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        # Check safety tips
        print("\n2. 🛡️ SAFETY TIPS:")
        try:
            cursor.execute("SELECT title, content FROM safety_tips WHERE is_active = 1 ORDER BY created_at DESC")
            safety_data = cursor.fetchall()
            if safety_data:
                for i, (title, content) in enumerate(safety_data, 1):
                    print(f"   {i}. {title}")
                    print(f"      Content: {content[:100]}...")
            else:
                print("   📭 No safety tips found")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        # Check PDF resources
        print("\n3. 📄 PDF RESOURCES:")
        try:
            cursor.execute("SELECT title, description, file_path FROM pdf_resources WHERE is_active = 1 ORDER BY created_at DESC")
            pdf_data = cursor.fetchall()
            if pdf_data:
                for i, (title, desc, path) in enumerate(pdf_data, 1):
                    print(f"   {i}. {title}")
                    print(f"      Description: {desc[:100] if desc else 'No description'}...")
                    print(f"      File: {path}")
            else:
                print("   📭 No PDF resources found")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        # Check home content
        print("\n4. 🏠 HOME CONTENT:")
        try:
            cursor.execute("SELECT section_name, content FROM home_content ORDER BY display_order")
            home_data = cursor.fetchall()
            if home_data:
                for i, (section, content) in enumerate(home_data, 1):
                    print(f"   {i}. {section}")
                    print(f"      Content: {content[:100]}...")
            else:
                print("   📭 No home content found")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        # Check officers
        print("\n5. 👮 OFFICERS:")
        try:
            cursor.execute("SELECT name, designation, district FROM officers LIMIT 5")
            officer_data = cursor.fetchall()
            if officer_data:
                for i, (name, designation, district) in enumerate(officer_data, 1):
                    print(f"   {i}. {name} - {designation} ({district})")
            else:
                print("   📭 No officers found")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        # Check initiatives
        print("\n6. 🚀 INITIATIVES:")
        try:
            cursor.execute("SELECT title, description FROM initiatives WHERE is_active = 1 LIMIT 3")
            init_data = cursor.fetchall()
            if init_data:
                for i, (title, desc) in enumerate(init_data, 1):
                    print(f"   {i}. {title}")
                    print(f"      Description: {desc[:100]}...")
            else:
                print("   📭 No initiatives found")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 SUMMARY:")
        
        tables_to_check = [
            ('about_sections', 'About Us content'),
            ('safety_tips', 'Safety Tips'),
            ('pdf_resources', 'PDF Resources'),
            ('home_content', 'Home Page content'),
            ('officers', 'Police Officers'),
            ('initiatives', 'Initiatives/Programs')
        ]
        
        for table, description in tables_to_check:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                status = "✅" if count > 0 else "📭"
                print(f"   {status} {description}: {count} records")
            except Exception as e:
                print(f"   ❌ {description}: Error - {e}")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

if __name__ == "__main__":
    check_all_content()
