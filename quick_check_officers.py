import sqlite3

# Connect to database
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check if officers table exists and its structure
try:
    cursor.execute("PRAGMA table_info(officers)")
    columns = cursor.fetchall()
    print("Current officers table structure:")
    for col in columns:
        print(f"  {col[1]} - {col[2]}")
    
    # Count current officers
    cursor.execute("SELECT COUNT(*) FROM officers")
    count = cursor.fetchone()[0]
    print(f"\nCurrent officers count: {count}")
    
    if count == 0:
        print("\n✅ Adding sample officers...")
        
        # Add sample officers
        officers_data = [
            ("Sri Harish Kumar Guptha, IPS", "Director General of Police", "Andhra Pradesh Police", "0863-1213456", "dgp@appolice.gov.in", None, "AP DGP with extensive experience in law enforcement.", 1, 1),
            ("P. Sithamahalakshmi", "Additional Director General", "Women Safety Wing", "+91-863-2340024", "adg.women@appolice.gov.in", None, "Dedicated to ensuring safety and security of women across Andhra Pradesh.", 2, 1),
            ("K. Raghuveer", "Superintendent of Police", "Cyber Crime (Women & Children)", "+91-863-2340025", "sp.cyber@appolice.gov.in", None, "Specialist in cyber crimes against women and children protection.", 3, 1)
        ]
        
        for officer in officers_data:
            cursor.execute('''
                INSERT INTO officers (name, designation, department, phone, email, image_url, bio, position_order, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', officer)
        
        conn.commit()
        print("✅ Sample officers added!")
    
    # Show final results
    cursor.execute("SELECT id, name, designation, image_url FROM officers WHERE is_active = 1 ORDER BY position_order")
    officers = cursor.fetchall()
    
    print("\n=== Current Officers ===")
    for officer in officers:
        image_status = "📷 Has Image" if officer[3] else "❌ No Image"
        print(f"ID: {officer[0]} | {officer[1]} | {officer[2]} | {image_status}")
    
    print(f"\n🌐 Website running at: http://127.0.0.1:5000/about")
    print(f"🔧 Admin panel at: http://127.0.0.1:5000/admin/login")
    print(f"👤 Login: admin / admin123")

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    conn.close()
