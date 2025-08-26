import sqlite3
import os

# Connect to database
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

print("=== Current Officers in Database ===")
cursor.execute('SELECT id, name, designation, image_url FROM officers')
current_officers = cursor.fetchall()

if current_officers:
    for officer in current_officers:
        print(f"ID: {officer[0]}, Name: {officer[1]}, Designation: {officer[2]}, Image: {officer[3]}")
    
    # Delete existing officers to start fresh
    cursor.execute('DELETE FROM officers')
    print("\n✅ Deleted existing officers")

# Insert sample officers (you can replace these with real data)
sample_officers = [
    (
        "Sri Harish Kumar Guptha, IPS",
        "Director General of Police",
        "Andhra Pradesh Police",
        "+91-863-1213456",
        "dgp@appolice.gov.in",
        None,  # Will update this when you upload actual images
        "AP DGP with extensive experience in law enforcement and women safety initiatives.",
        1
    ),
    (
        "P. Sithamahalakshmi",
        "Additional Director General",
        "Women Safety Wing",
        "+91-863-2340024",
        "adg.women@appolice.gov.in",
        None,  # Will update this when you upload actual images
        "Dedicated to ensuring safety and security of women across Andhra Pradesh.",
        2
    ),
    (
        "K. Raghuveer",
        "Superintendent of Police",
        "Cyber Crime (Women & Children)",
        "+91-863-2340025",
        "sp.cyber@appolice.gov.in",
        None,  # Will update this when you upload actual images
        "Specialist in cyber crimes against women and children protection.",
        3
    )
]

for officer in sample_officers:
    cursor.execute('''
        INSERT INTO officers (name, designation, department, phone, email, image_url, bio, position_order)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', officer)

conn.commit()

print("\n✅ Added sample officers to database")

# Verify the data
cursor.execute('SELECT id, name, designation, department, image_url FROM officers ORDER BY position_order')
new_officers = cursor.fetchall()

print("\n=== New Officers in Database ===")
for officer in new_officers:
    print(f"ID: {officer[0]}, Name: {officer[1]}, Designation: {officer[2]}, Department: {officer[3]}, Image: {officer[4]}")

# Check if uploads directory exists
uploads_path = 'static/uploads'
if not os.path.exists(uploads_path):
    os.makedirs(uploads_path)
    print(f"\n✅ Created uploads directory: {uploads_path}")
else:
    print(f"\n✅ Uploads directory exists: {uploads_path}")

conn.close()
print("\n🎉 Database setup complete! Now you can:")
print("1. Go to admin panel: http://127.0.0.1:5000/admin/login")
print("2. Login with admin credentials")
print("3. Go to Officers management")
print("4. Edit each officer and upload their photo")
