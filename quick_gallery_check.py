import sqlite3

conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Check if tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cursor.fetchall()]
print("Available tables:", tables)

# Check if gallery_items table exists
if 'gallery_items' in tables:
    print("\n✓ gallery_items table exists")
    
    # Get table structure
    cursor.execute("PRAGMA table_info(gallery_items)")
    columns = cursor.fetchall()
    print("Columns:")
    for col in columns:
        print(f"  {col[1]} ({col[2]})")
    
    # Get sample data
    cursor.execute("SELECT * FROM gallery_items LIMIT 3")
    samples = cursor.fetchall()
    print(f"\nSample data ({len(samples)} items):")
    for item in samples:
        print(f"  {item}")
        
else:
    print("\n✗ gallery_items table does NOT exist")
    print("Need to create gallery_items table")

conn.close()
