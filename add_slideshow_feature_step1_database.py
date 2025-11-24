"""
SAFE APPROACH: Add slideshow_images table
- Creates NEW table only
- Does NOT modify existing tables
- Adds current slide1-5 images to table
- 100% backward compatible
"""
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host='localhost',
    database='women_safety_db',
    user='postgres',
    password='postgres123',
    port='5432'
)
cursor = conn.cursor()

print("=" * 80)
print("SAFE SLIDESHOW MANAGEMENT FEATURE - STEP 1: DATABASE")
print("=" * 80)

# Step 1: Create new table (does NOT touch existing tables)
print("\n📊 Creating slideshow_images table...")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS slideshow_images (
        id SERIAL PRIMARY KEY,
        image_url VARCHAR(500) NOT NULL,
        title VARCHAR(255),
        caption TEXT,
        sort_order INTEGER DEFAULT 0,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()
print("✅ Table created successfully (or already exists)")

# Step 2: Check if data already exists
cursor.execute("SELECT COUNT(*) FROM slideshow_images")
count = cursor.fetchone()[0]

if count > 0:
    print(f"\n✅ Slideshow images already exist ({count} records)")
    print("   Skipping sample data insertion")
else:
    print(f"\n📝 Adding existing slide images to database...")
    
    # Add current hardcoded images to database
    existing_slides = [
        ('/static/images/slide1.jpg', 'Women Safety Awareness', 'Empowering women through education and awareness programs', 1),
        ('/static/images/slide2.jpg', 'Community Support', 'Building strong community networks for women safety', 2),
        ('/static/images/slide3.jpg', 'Self Defense Training', 'Professional self-defense workshops and training sessions', 3),
        ('/static/images/slide4.jpg', 'Legal Assistance', '24/7 legal aid and counseling services', 4),
        ('/static/images/slide5.jpg', 'Emergency Response', 'Quick response teams and helpline services', 5)
    ]
    
    for image_url, title, caption, sort_order in existing_slides:
        cursor.execute("""
            INSERT INTO slideshow_images (image_url, title, caption, sort_order, is_active)
            VALUES (%s, %s, %s, %s, %s)
        """, (image_url, title, caption, sort_order, True))
        print(f"   ✅ Added: {image_url}")
    
    conn.commit()
    print(f"\n✅ Added {len(existing_slides)} slideshow images")

# Step 3: Verify data
cursor.execute("SELECT id, image_url, title, sort_order, is_active FROM slideshow_images ORDER BY sort_order")
slides = cursor.fetchall()

print(f"\n📋 Current slideshow images in database:")
print("-" * 80)
for slide_id, image_url, title, sort_order, is_active in slides:
    status = "✅ Active" if is_active else "❌ Inactive"
    print(f"[{slide_id}] {status} Order: {sort_order} | {title}")
    print(f"    Image: {image_url}")

conn.close()

print("\n" + "=" * 80)
print("✅ DATABASE SETUP COMPLETE")
print("=" * 80)
print("\n✅ Safety Check:")
print("   - New table created: slideshow_images")
print("   - Existing tables: NOT TOUCHED")
print("   - Current images: Preserved in database")
print("   - Website: Still works with hardcoded fallback")
print("\n🎯 Next: Add admin interface to manage these images")
print("=" * 80)
