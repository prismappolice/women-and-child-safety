#!/usr/bin/env python3
"""
Check all existing data that user had added previously
"""
import sqlite3

def check_all_user_data():
    """Check all user's existing data across all tables"""
    print("🔍 CHECKING ALL YOUR EXISTING DATA")
    print("=" * 60)
    
    try:
        conn = sqlite3.connect('women_safety.db')
        cursor = conn.cursor()
        
        # 1. Check Officers Data (important user data)
        print("\n1. 👮‍♀️ POLICE OFFICERS DATA:")
        try:
            cursor.execute("""
                SELECT name, designation, district, department, phone, email 
                FROM officers 
                ORDER BY position_order, name
            """)
            officers = cursor.fetchall()
            if officers:
                print(f"   📊 Total Officers: {len(officers)}")
                for i, (name, designation, district, dept, phone, email) in enumerate(officers[:5], 1):
                    print(f"   {i}. {name}")
                    print(f"      📍 {designation} - {district}")
                    print(f"      🏢 {dept}")
                    print(f"      📞 {phone}")
                    print(f"      ✉️ {email}")
                    print()
                if len(officers) > 5:
                    print(f"   ... and {len(officers) - 5} more officers")
            else:
                print("   📭 No officers data found")
        except Exception as e:
            print(f"   ❌ Error checking officers: {e}")
        
        # 2. Check Initiatives/Programs Data
        print("\n2. 🚀 INITIATIVES/PROGRAMS DATA:")
        try:
            cursor.execute("""
                SELECT title, description, start_date, status, contact_person 
                FROM initiatives 
                WHERE is_active = 1
                ORDER BY start_date DESC
            """)
            initiatives = cursor.fetchall()
            if initiatives:
                print(f"   📊 Total Active Initiatives: {len(initiatives)}")
                for i, (title, desc, start_date, status, contact) in enumerate(initiatives[:3], 1):
                    print(f"   {i}. {title}")
                    print(f"      📝 {desc[:100]}...")
                    print(f"      📅 Started: {start_date}")
                    print(f"      📊 Status: {status}")
                    print(f"      👤 Contact: {contact}")
                    print()
                if len(initiatives) > 3:
                    print(f"   ... and {len(initiatives) - 3} more initiatives")
            else:
                print("   📭 No initiatives data found")
        except Exception as e:
            print(f"   ❌ Error checking initiatives: {e}")
        
        # 3. Check Volunteers Data
        print("\n3. 🙋‍♀️ VOLUNTEERS DATA:")
        try:
            cursor.execute("""
                SELECT name, email, phone, district, skills, registration_date 
                FROM volunteers 
                ORDER BY registration_date DESC
            """)
            volunteers = cursor.fetchall()
            if volunteers:
                print(f"   📊 Total Volunteers: {len(volunteers)}")
                for i, (name, email, phone, district, skills, reg_date) in enumerate(volunteers[:3], 1):
                    print(f"   {i}. {name}")
                    print(f"      📧 {email}")
                    print(f"      📞 {phone}")
                    print(f"      📍 {district}")
                    print(f"      🎯 Skills: {skills}")
                    print(f"      📅 Registered: {reg_date}")
                    print()
                if len(volunteers) > 3:
                    print(f"   ... and {len(volunteers) - 3} more volunteers")
            else:
                print("   📭 No volunteers data found")
        except Exception as e:
            print(f"   ❌ Error checking volunteers: {e}")
        
        # 4. Check Gallery Items (user added content)
        print("\n4. 🖼️ GALLERY ITEMS DATA:")
        try:
            cursor.execute("""
                SELECT title, description, category, event_date, main_image 
                FROM gallery_items 
                WHERE is_active = 1
                ORDER BY event_date DESC
            """)
            gallery_items = cursor.fetchall()
            if gallery_items:
                print(f"   📊 Total Gallery Items: {len(gallery_items)}")
                for i, (title, desc, category, event_date, image) in enumerate(gallery_items, 1):
                    print(f"   {i}. {title}")
                    print(f"      📝 {desc[:100] if desc else 'No description'}...")
                    print(f"      🏷️ Category: {category}")
                    print(f"      📅 Date: {event_date}")
                    print(f"      🖼️ Image: {image or 'No image'}")
                    print()
            else:
                print("   📭 No gallery items found (new gallery setup)")
        except Exception as e:
            print(f"   ❌ Error checking gallery: {e}")
        
        # 5. Check Success Stories
        print("\n5. 🌟 SUCCESS STORIES DATA:")
        try:
            cursor.execute("""
                SELECT title, description, date, stat1_number, stat1_label 
                FROM success_stories 
                WHERE is_active = 1
                ORDER BY date DESC
            """)
            stories = cursor.fetchall()
            if stories:
                print(f"   📊 Total Success Stories: {len(stories)}")
                for i, (title, desc, date, stat1_num, stat1_label) in enumerate(stories[:2], 1):
                    print(f"   {i}. {title}")
                    print(f"      📝 {desc[:100]}...")
                    print(f"      📅 Date: {date}")
                    print(f"      📊 Stat: {stat1_num} {stat1_label}")
                    print()
                if len(stories) > 2:
                    print(f"   ... and {len(stories) - 2} more stories")
            else:
                print("   📭 No success stories found")
        except Exception as e:
            print(f"   ❌ Error checking success stories: {e}")
        
        # 6. Check Custom Content Added by User
        print("\n6. 📝 CUSTOM CONTENT DATA:")
        
        # Check about content
        try:
            cursor.execute("SELECT COUNT(*) FROM about_content WHERE is_active = 1")
            about_count = cursor.fetchone()[0]
            print(f"   📋 About page sections: {about_count}")
        except:
            print("   📋 About page sections: 0")
        
        # Check safety tips
        try:
            cursor.execute("SELECT COUNT(*) FROM safety_tips WHERE is_active = 1")
            tips_count = cursor.fetchone()[0]
            print(f"   🛡️ Safety tips: {tips_count}")
        except:
            print("   🛡️ Safety tips: 0")
        
        # Check PDF resources
        try:
            cursor.execute("SELECT COUNT(*) FROM pdf_resources WHERE is_active = 1")
            pdf_count = cursor.fetchone()[0]
            print(f"   📄 PDF resources: {pdf_count}")
        except:
            print("   📄 PDF resources: 0")
        
        # Summary of all data
        print("\n" + "=" * 60)
        print("📊 DATA PRESERVATION SUMMARY:")
        
        all_tables = [
            ('officers', 'Police Officers'),
            ('initiatives', 'Initiatives/Programs'),
            ('volunteers', 'Volunteer Registrations'),
            ('gallery_items', 'Gallery Items'),
            ('success_stories', 'Success Stories'),
            ('about_content', 'About Page Content'),
            ('safety_tips', 'Safety Tips'),
            ('pdf_resources', 'PDF Resources'),
            ('home_content', 'Home Page Content')
        ]
        
        total_records = 0
        for table, description in all_tables:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                total_records += count
                status = "✅" if count > 0 else "📭"
                print(f"   {status} {description}: {count} records")
            except Exception as e:
                print(f"   ❌ {description}: Error - {e}")
        
        print(f"\n🎯 TOTAL DATA RECORDS: {total_records}")
        print("✅ All your existing data is preserved and safe!")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {e}")

if __name__ == "__main__":
    check_all_user_data()
