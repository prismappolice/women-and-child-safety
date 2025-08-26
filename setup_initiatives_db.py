import sqlite3

# Connect to database
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("=== Current Initiatives in Database ===")
cursor.execute('SELECT id, title, description, image_url, is_featured, is_active FROM initiatives')
initiatives = cursor.fetchall()

if initiatives:
    for initiative in initiatives:
        print(f"\nID: {initiative[0]}")
        print(f"Title: {initiative[1]}")
        print(f"Description: {initiative[2][:100]}...")  # First 100 chars
        print(f"Image URL: {initiative[3]}")
        print(f"Featured: {'Yes' if initiative[4] else 'No'}")
        print(f"Active: {'Yes' if initiative[5] else 'No'}")
        print("-" * 50)
else:
    print("❌ No initiatives found in database")
    
    # Add sample initiatives for testing
    sample_initiatives = [
        (
            "Self Defense Training Program",
            "Comprehensive self-defense training program designed to empower women with practical skills and confidence to protect themselves in various situations. The program includes physical techniques, mental preparedness, and awareness strategies.",
            None,
            1,  # Featured
            1   # Active
        ),
        (
            "Women Safety Mobile App",
            "Advanced mobile application featuring GPS tracking, emergency contacts, safe zone mapping, and instant alert systems. The app connects users with nearby police stations and provides real-time safety updates.",
            None,
            1,  # Featured
            1   # Active
        ),
        (
            "Community Awareness Workshops",
            "Educational workshops conducted across districts to raise awareness about women's rights, legal procedures, and available support systems. These workshops engage families and communities in creating safer environments.",
            None,
            0,  # Not featured
            1   # Active
        )
    ]
    
    for initiative in sample_initiatives:
        cursor.execute('''
            INSERT INTO initiatives (title, description, image_url, is_featured, is_active)
            VALUES (?, ?, ?, ?, ?)
        ''', initiative)
    
    conn.commit()
    print("✅ Added sample initiatives to database")
    
    # Show updated initiatives
    cursor.execute('SELECT id, title, image_url FROM initiatives')
    new_initiatives = cursor.fetchall()
    
    print("\n=== Sample Initiatives Added ===")
    for initiative in new_initiatives:
        print(f"ID: {initiative[0]}, Title: {initiative[1]}, Image: {initiative[2]}")

conn.close()
print("\n🎉 Initiatives setup complete!")
print("Now you can:")
print("1. Go to: http://127.0.0.1:5000/admin/initiatives")
print("2. Edit any initiative and upload images")
print("3. Check the website at: http://127.0.0.1:5000/initiatives")
