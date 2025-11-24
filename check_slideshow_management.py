import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='women_safety_db',
    user='postgres',
    password='postgres123',
    port='5432'
)
cursor = conn.cursor()

print("=" * 90)
print("HOMEPAGE SLIDESHOW IMAGE MANAGEMENT - CURRENT STATUS")
print("=" * 90)

# Check home_content table
cursor.execute("SELECT section_name, title, image_url FROM home_content ORDER BY section_name, sort_order")
rows = cursor.fetchall()

print("\n📋 Current home_content sections:")
print("-" * 90)
for section, title, image_url in rows:
    print(f"Section: {section:15} | Title: {title:30} | Image: {image_url if image_url else 'None'}")

# Check if there's a specific slideshow section
cursor.execute("SELECT * FROM home_content WHERE section_name LIKE '%slide%' OR section_name LIKE '%hero%' OR section_name LIKE '%banner%'")
slideshow_sections = cursor.fetchall()

print(f"\n🔍 Slideshow/Hero/Banner sections in database: {len(slideshow_sections)}")
if slideshow_sections:
    for row in slideshow_sections:
        print(f"   Found: {row}")
else:
    print("   ❌ No dedicated slideshow management found in home_content table")

conn.close()

print("\n" + "=" * 90)
print("ANALYSIS:")
print("=" * 90)

# Read index.html to see hardcoded images
print("\n📄 Checking index.html for hardcoded slideshow images...")
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
import re
slide_images = re.findall(r'<img src="/static/images/(slide\d+\.jpg)"', content)

if slide_images:
    print(f"\n✅ Found {len(slide_images)} hardcoded slideshow images:")
    for idx, img in enumerate(slide_images, 1):
        print(f"   {idx}. /static/images/{img}")
    
    print("\n📊 CURRENT STATUS:")
    print("   ❌ Slideshow images are HARDCODED in index.html")
    print("   ❌ Admin CANNOT change slideshow images dynamically")
    print("   ❌ Need to manually edit index.html to change images")
    
    print("\n💡 SOLUTION NEEDED:")
    print("   ✅ Create slideshow_images table in database")
    print("   ✅ Add admin route /admin/slideshow to manage images")
    print("   ✅ Update index.html to load images from database")
    print("   ✅ Admin can then add/edit/delete slideshow images dynamically")
else:
    print("   ⚠️  No slideshow images found")

print("\n" + "=" * 90)
